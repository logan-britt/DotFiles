# the only global main lib import
from sys import argv

# the helper imports for the user input from command line
from Deploy.argument import find_given_arguments
from Deploy.argument import extract_argument_value
from Deploy.argument import check_argument_values

# the helper imports for printing the help message
from Deploy.help import print_help

# the helper imports for building and configuring neovim
from Deploy.neovim import build_neovim, install_neovim_dependencies
from Deploy.neovim import move_dotfiles_to_location

def main(system_args: list[str]) -> None:
    # the storage for the command line arguments and there values
    args: dict[str, str] = {}

    # read the command line and parse the arguments
    argument_locations: dict[str, int] = find_given_arguments( system_args )
    for argument in argument_locations:
        index = argument_locations[argument]
        args[argument] = extract_argument_value(index, system_args)
    if not check_argument_values(args):
        print('At least one of the arguments and it\'s value is not supported')
        print('\tso check your arguments and values.')
        return

    # print the help message and return
    if 'help' in args or 'H' in args:
        print_help()
        return

    # begin the setting up of the development environment

if __name__ == '__main__':
    main( argv[1:] )
