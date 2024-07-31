function run_command()
    return vim.g.hulvdan_run_command
end

-- Форматтер.
require("conform").setup({
    formatters = {
        black = { command = [[.venv\Scripts\black.exe]] },
        isort = { command = [[.venv\Scripts\isort.exe]] },
    },
})

-- Helper Functions --
-- ================ --
function save_files()
    vim.fn.execute(":wa")
end

function build()
    run_command()([[.venv\Scripts\python.exe build.py]])
end

-- Keyboard Shortcuts --
-- ================== --
local opts = { remap = false, silent = true }

vim.keymap.set("n", "<A-b>", function()
    save_files()
    build()
end, opts)

function reload_file()
    vim.fn.execute(":e")
end

vim.keymap.set("n", "<leader>w", function()
    save_files()

    if vim.bo.filetype == "markdown" or vim.bo.filetype == "css" then
        build()
        print("Built!")
    end
end, opts)
