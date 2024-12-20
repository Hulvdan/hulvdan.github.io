-- Workspace Settings --
-- ================== --
vim.fn.execute(":set nornu")
vim.fn.execute(":set nonumber")
vim.fn.execute(":set signcolumn=no")
vim.fn.execute(":set colorcolumn=")
vim.fn.execute(":set nobackup")
vim.fn.execute(":set nowritebackup")

-- Helper Functions --
-- ================ --
function launch_tab(command)
    vim.fn.execute([[term ]] .. command)
end

function launch_side(command, switch)
    local esc_command = command:gsub([[%\]], [[\\]]):gsub([[% ]], [[\ ]])
    vim.fn.execute([[vs +term\ ]] .. esc_command)

    if switch == true then
        vim.fn.execute("wincmd x")
        vim.fn.execute("wincmd l")
    end
end

function launch_background(command, callback)
    vim.fn.jobstart(command, { on_exit = callback })
end

function save_file_if_needed()
    if vim.bo.buftype == "" and vim.bo.modified == true then
        vim.fn.execute(":w")
    end
end

function build(silent)
    local command = [[.venv\Scripts\python.exe build.py]]
    vim.g.hulvdan_run_command(command)
end

-- Keyboard Shortcuts --
-- ================== --
local opts = { remap = false, silent = true }

vim.keymap.set("n", "<A-b>", function()
    save_file_if_needed()
    build(false)
end, opts)

function save_files()
    vim.fn.execute(":wa")
end

function reload_file()
    vim.fn.execute(":e")
end

vim.keymap.set("n", "<leader>w", function()
    save_files()

    if vim.bo.filetype == "markdown" then
        build(true)
        print("Built!")
    end

    if vim.bo.filetype == "python" then
        local view = vim.fn.winsaveview()

        -- local buf_path = vim.api.nvim_buf_get_name(vim.api.nvim_get_current_buf())
        -- launch_background([[.venv\Scripts\black.exe -q "]] .. buf_path .. '"', function()
        launch_background([[.venv\Scripts\black.exe -q . && .venv\Scripts\isort.exe .]], function()
            reload_file()

            vim.fn.winrestview(view)

            vim.api.nvim_input("mzhllhjkkj`z") -- NOTE: for nvim-treesitter-context
            build(true)
        end)
    end
end, opts)
