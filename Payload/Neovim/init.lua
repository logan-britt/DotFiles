--- disable the built in file browser so nvim-tree will work ---
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

--- the basic config files for overall stuff ---
require('local.option')
require('local.keymap')

--- the plugin manager lua files ---
require('expansion.lazy')
require('expansion.colorscheme')
require('expansion.nvim-tree')
require('expansion.telescope')
--require('expansion.')

--- the language server and auto complete ---

--- the graphics configuration ---
require('graphics.neovide')
