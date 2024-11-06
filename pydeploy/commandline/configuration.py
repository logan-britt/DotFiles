from shutil import which

'''
    The helper functions. Like elsewhere we have the method names preceded
      by and underscore. They should be thaught of as private.
'''

'''
    This part of the file includes the methods used to set the global variables
      to there proper setup configuration. They will be exported to be used in
      the __init__ script of the module.
'''
def is_there_a_package_manager() -> bool:
    if which('pacman') != None or which('apt-get') != None:
        return True
    else:
        return False

def is_there_a_cpp_compiler() -> bool:
    if which('gcc') != None or which('clang') != None or which('cl') != None:
        return True
    else:
        return False

def is_there_a_rust_compiler() -> bool:
    if which('rustc') != None:
        return True
    else:
        return False

def is_there_a_nodejs_interpreter() -> bool:
    if which('node') != None:
        return True
    else:
        return False

def is_there_a_lua_interpreter() -> bool:
    if which('lua') != None:
        return True
    else:
        return False

def is_there_a_neovim_installation() -> bool:
    if which('nvim') != None:
        return True
    else:
        return False

def is_there_a_alacritty_installation() -> bool:
    if which('alacritty') != None:
        return True
    else:
        return False
