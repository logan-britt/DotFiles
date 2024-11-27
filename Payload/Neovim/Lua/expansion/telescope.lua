-- Here we set up the configuration to the telescope extension
--   so that it works how we want it to when we keymap or make
--   a user command later on in this file.
require('telescope').setup({
    defaults = {
        -- holds the "built" in keymaps
        mappings = {
        },
        -- holds the built in piker settings
        pickers = {
        },
        -- idk what this is really
        extensions = {
        }
    }
})

-- Configure the things that idk right now... sorry this is under heavy
--   development!

-- Set up the keymaps and the user commands for the telescope
--   neovim extension.
local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>ff', builtin.find_files, {desc = 'Telescope find files'})
vim.keymap.set('n', '<leader>fg', builtin.live_grep, {desc = 'Telescope live grep'})
vim.keymap.set('n', '<leader>fb', builtin.buffers, {desc = 'Telescope buffers'})
vim.keymap.set('n', '<leader>fh', builtin.help_tags, {desc = 'Telescope help tags'})
