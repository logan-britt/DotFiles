#!/usr/bin/env python3

from sys import argv, platform
from os.path import expanduser
from shutil import copytree, copy, rmtree
from os import listdir, mkdir

def parse_args(sys_args: list[str]) -> dict[str, bool]:
    args = {
        'neovim': False,
        'alacritty': False,
        'zsh': False,
        'fastfetch': False
    }

    for index in range(len(sys_args)):
        if sys_args[index][0:2] == '--' and sys_args[index][2:] in args:
            args[sys_args[index][2:]] = True
        else:
            print('The argument that was given was not a supported program.')
            print(f'You inputed: {sys_args[index][2:]}')
            print('\n')
            exit()

    return args

def find_deploy_path() -> str:
    if 'win' in platform:
        path = f'~\\AppData\\Local'
        path = expanduser(path)
    else:
        path = f'~/.config'
        path = expanduser(path)
    return path

def neovim(deploy_path: str) -> bool:
    if 'win' in platform:
        neovim_path = f'{deploy_path}\\nvim'
        source_init_path = 'Payload\\Neovim\\init.lua'
        deploy_init_path = f'{neovim_path}\\init.lua'
        source_lua_path = 'Payload\\Neovim\\Lua'
        deploy_lua_path = f'{neovim_path}\\lua'
    else:
        neovim_path = f'{deploy_path}/nvim'
        source_init_path = 'Payload/Neovim/init.lua'
        deploy_init_path = f'{neovim_path}/init.lua'
        source_lua_path = 'Payload/Neovim/Lua'
        deploy_lua_path = f'{neovim_path}/lua'
    
    check = True

    if 'nvim' not in listdir(deploy_path):
        mkdir(neovim_path)
    else:
        rmtree(neovim_path)
        mkdir(neovim_path)
    
    copy(source_init_path, deploy_init_path)
    copytree(source_lua_path, deploy_lua_path)
    
    return check

def alacritty(deploy_path: str) -> bool:
    check = True
    return check

def zsh() -> bool:
    if 'win' in platform:
        print('zsh is only avalible for non windows systems!')
        return False

    check = True
    if '.zsh_helpers' in listdir(expanduser('~')):
        rmtree(f'{expanduser("~")}/.zsh_helpers')

    copy('Payload/Zsh/zshrc', f'{expanduser("~")}/.zshrc')
    copytree('Payload/Zsh/Scripts', f'{expanduser("~")}/.zsh_helpers')

    return check

def fastfetch(deploy_path: str) -> bool:
    if 'win' in platform:
        fastfetch_path = f'{deploy_path}\\fastfetch'
        source_path = 'Payload\\Fastfetch\\config.jsonc'
        payload_path = f'{fastfetch_path}\\config.jsonc'
    else:
        fastfetch_path = f'{deploy_path}/fastfetch'
        source_path = 'Payload/Fastfetch/config.jsonc'
        payload_path = f'{fastfetch_path}/config.jsonc'

    check = True

    if 'fastfetch' not in listdir(deploy_path):
        mkdir(fastfetch_path)
    else:
        rmtree(fastfetch_path)
        mkdir(fastfetch_path)

    copy(source_path, payload_path)

    return check

def main(sys_args: list[str]) -> None:
    args = parse_args(sys_args)
    deploy_path = find_deploy_path()
    for key in args:
        check = True
        if args[key] and key == 'neovim':
            check = neovim(deploy_path)
            if not check:
                print('Neovim config deployment faild.')
        elif args[key] and key == 'alacritty':
            check = alacritty(deploy_path)
            if not check:
                print('Alacritty config deployment faild.')
        elif args[key] and key == 'zsh':
            check = zsh()
            if not check:
                print('Zsh config deployment faild.')
        elif args[key] and key == 'fastfetch':
            check = fastfetch(deploy_path)
            if not check:
                print('Fastfetch config deployment faild.')
    print('\n')

if __name__ == '__main__':
    main( argv[1:] )
