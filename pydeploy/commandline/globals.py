''' Just a list of global variables for use in other places. '''

# the arguments and there possible values
valid_pairs = {
    'neovim': ['full', 'lua-only', 'debug'],
    'alacritty': ['full', 'toml-only'],
    'lua': None,
    'rust': None,
    'javascript': ['nodejs', 'deno'],
    'c/c++': ['gcc', 'llvm', 'cl'],

    'file': None
}

# a list of flags for the state of different things
package_manager = False
lua_interpreter_present = False
c++_compiler_present = False
nodejs_present = False
rust_compiler_present = False
neovim_present = False
alacritty_present = False
