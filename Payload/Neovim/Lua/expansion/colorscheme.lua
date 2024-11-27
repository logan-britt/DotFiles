-- This file configures all of the color schemes and configures the 
--   commands switch between them!

-- Tokyo Night
require('tokyonight').setup({
    sytle = "night",
    light_style = "day",
    transparent = true
})

-- Night Fox
require('nightfox').setup({
    transparent = true
})

-- Nordic 
require('nordic').setup({
    transparent = {
        bg = true,
        float = true
    }
})

-- Moonfly Colors
-- there is goning to be some fuckery goning on here TO DO!

-- Cyberdream
require('cyberdream').setup({
    transparent = true
})

-- Here we register the functions that switch between the color schemes
--   so that it can be done quickly.
function change_color( input_table ) 
    if input_table.nargs == 1 then -- handels just a single color swap
        if input_table.fargs[1] == 'tokyonight' then
            vim.cmd.colorscheme('tokyonight')
        elseif input_table.fargs[1] == 'nightfox' then
            vim.cmd.colorscheme('nightfox')
        elseif input_table.fargs[1] == 'moonfly' then
            vim.cmd.colorscheme('moonfly')
        elseif input_table.fargs[1] == 'nordic' then
            vim.cmd.colorscheme('cyberdream')
        end
    else -- handels swaping to a colorscheme with varents
    end
end
vim.api.nvim_create_user_command('Color', change_color, {})

-- Lastly we load the color scheme so that it will have been configured
--   before we load it.
vim.cmd.colorscheme('nightfox')
