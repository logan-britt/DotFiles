-- This file sets up the main entry point for lazy lua. It has the
--   list of plugins that are in use and also enables lazy loading.

-- Boot strap the lua if it is not installed
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- Now we configure the plugins to be installed onto the system
local plugins = {
    -- colorschemes
    "folke/tokyonight.nvim",
    "EdenEast/nightfox.nvim",
    "AlexvZyl/nordic.nvim",
    "bluz71/vim-moonfly-colors",
    "scottmckendry/cyberdream.nvim",

    -- filetree engine
    { 
        'nvim-tree/nvim-tree.lua',
        lazy=false,
        dependencies = {
            'nvim-tree/nvim-web-devicons'
        },
    },

    -- telescope search 
    {
        'nvim-telescope/telescope.nvim', 
        tag = '0.1.8',
        dependencies = { 
            'nvim-lua/plenary.nvim' 
        }
    }
}

local opts = {}

require("lazy").setup(plugins, opts)
