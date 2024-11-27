---! import the modules needed to make the keymaps work !---
local ok, regex = pcall(require, 'local.regex')
if not ok then
    print('The regex module has a syntax error preventing importing!')
end

---!  !---
