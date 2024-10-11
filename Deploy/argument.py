'''
    This part of the script has the global variables needed to parse
      the command line arguments into a usable form.
'''
POSSIBLE_ARGUMENTS: dict[str, list[str]] = {
    'help': None,
    'H': None,
    
    '': [],
    '': []
}

'''
    Here we define the methods needed to process the raw list of command
      line arguments into a dictonary of arguments and values.
'''
def find_given_arguments(arguments: list[str]) -> dict[str, int]:
    given_arguments: dict[str, int] = {} 
    for index in range(len(arguments)):
        if '--' == arguments[index][0:2]:
            given_arguments[arguments[index][2:]] = index 
        elif '-' == arguments[index][0]:
            given_arguments[arguments[index][1]] = index
    return given_arguments

def extract_argument_value(index: int, arguments: list[str]) -> str:
    value: str = ''
    argument = arguments[index]
    if argument[0:2] == '--' and POSSIBLE_ARGUMENTS[argument[2:]] != None:
        value = arguments[index + 1]
    elif argument[0:2] == '--':
        value = None
    elif argument[0] == '-':
        value = argument[2:]
    return value

def check_argument_values(arguments: dict[str, str]) -> bool:
    arg_check = True
    for argument in arguments:
        value = arguments[argument]
        acceped_check = argument in POSSIBLE_ARGUMENTS
        if acceped_check and POSSIBLE_ARGUMENTS[argument] != None:
            value_check = value in POSSIBLE_ARGUMENTS[argument]
        elif acceped_check:
            value_check = True
        else:
            value_check = False

        if not (acceped_check and value_check):
            arg_check = False
    return arg_check
