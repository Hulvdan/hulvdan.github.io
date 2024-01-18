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
    vim.fn.jobstart(command, {on_exit = callback})
end

function save_file_if_needed()
    if vim.bo.buftype == "" and vim.bo.modified == true then
        vim.fn.execute(":w")
    end
end

function build(silent)
    local command = [[.venv\Scripts\python.exe build.py]]
    if silent then
        launch_background(command, function() end)
    else
        launch_side(command, true)
    end
end

-- Keyboard Shortcuts --
-- ================== --
local opts = { remap = false, silent = true }

vim.keymap.set("n", "<A-b>", function()
    save_file_if_needed()
    build(false)
end, opts)

vim.keymap.set("n", "<leader>w", function()
    save_file_if_needed()
    if vim.bo.filetype == "markdown" then
        build(true)
        print("Built!")
    end
end, opts)
