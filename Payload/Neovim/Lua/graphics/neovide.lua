-- This file configures the setup for the neovide neovim graphics
--   front end. It will only interact with the global variables 
--   that configure it.

-- a header guard so that this only fires if neovide is the running editor
if vim.g.neovide then
    vim.g.neovide_remember_window_size = false
    vim.g.neovide_profiler = false
    vim.g.neovide_transparency = 0.8
    vim.g.neovide_fullscreen = false
    vim.g.neovide_cursor_animate_command_line = true
    vim.g.neovide_scale_factor = 1.0 
else
    print('You are using a graphics front end that is not supported.')
end
