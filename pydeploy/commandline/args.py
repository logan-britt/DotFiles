from commandline.globals import valid_pairs
from commandline.globals import package_manager, lua_interpreter_present
from commandline.globals import c++_compiler_present, nodejs_present
from commandline.globals import rust_compiler_present, neovim_present
from commandline.globals import alacritty_present

from dataclasses import dataclass

'''
    The helper functions that are not ment to be imported into other files.
      They follow the python convention that "private" methods are to be
      preceded by a underscore. A list of the methods now follows:
        (-) check_argument  returns true if argument is valid false if not
        (-) check_argument_value  same as check_argument execpt for values
        (-) 

    Next we lay out the classes and dataclasses needed to make the script
      work. As allways they will be preceded with and underscore. A list
      of them now follows:
        (-) Error  contains the type argument value and location of the error
        (-) 
'''
@dataclass
class _Error:
    m_type: str
    m_argument: str
    m_value: str
    m_index: int

    def print_message(self) -> None:
        message = f'The given argument value pair were: ({self.m_argument}, {self.m_value})'

        print(f'An error was dected at index: {self.m_index}')
        print(f'The error was of type: {self.m_type}')
        print(message)
        print(2*'\n')

def _check_argument(arg: str, manifest) -> bool:
    if arg in manifest:
        return True
    return False

def _check_argument_value(arg: str, value: str, manifest) -> bool:
    if value in manifest[arg]:
        return True
    return False

'''
    The main exported methods for the pipeline class to simplify the
      expression of the command line reading algorithm. A list of
      the methods now follows:
        (-) check_valid  returns true if valid and false if not
        (-) print_validity_error  prints message when command line not valid
        (-) parse_dotfile_jobs  gets the numbers and the names of the jobs
        (-) print_help_message  prints the help message to command line 
        (-) 
'''
def check_valid(sys_args: list[str]) -> bool:
    validity_check: bool = True
    if len(sys_args) == 0:
        return validity_check

    for i in range(len(sys_args)):
        if sys_args[i][0:2] == '--':
            if not _check_argument(sys_args[i][2:], valid_pairs):
                validity_check = False
                break
            if valid_pairs[sys_args[i][2:]] == None:
                continue
            if sys_args[i+1][0:2] == '--':
                continue
            if not sys_args[i+1] in valid_pairs[sys_args[i][2:]]:
                validity_check = False
                break

    return validity_check

def print_validity_error(sys_args: list[str]) -> None:
    # find all of the argument locations for later use
    argument_indecies: list[int] = []
    for index in range(len(sys_args)):
        if sys_args[index][0:2] == '--':
            argument_indecies.append(index)

    # start a list of errors
    error_list: list[_Error] = []

    # check for the pressence of invalid arguments
    for index in argument_indecies:
        if not sys_args[index][2:] in valid_pairs:
            error = _Error('Type', f'{sys_args[index][2:]}', 'Not Valid', index)
            error_list.append(error)
    
    # check for the pressence of invalid values for an agrument
    for index in argument_indecies:
        if index + 1 == len(sys_args):
            continue
        elif sys_args[index+1][0:2] == '--':
            continue
        elif sys_args[index+1] not in valid_pairs[sys_args[index][2:]]:
            argument = sys_args[index][2:]
            value = sys_args[index+1]
            error = _Error('Value', f'{argument}', f'{value}', index+1)
            error_list.append(error)

    # actualy print the message
    for error in error_list:
        error.print_message()

def parse_dotfile_jobs(sys_args: list[str]) -> (int, list[str]):
    job_count: int = 0
    job_names: list[str] = []

    argument_follows: dict[int, bool] = {}
    for index in range(len(sys_args)):
        if sys_args[index][0:2] == '--' and sys_args[index][0:2] != '--':
            argument_follows[index] = True
        elif sys_args[index][0:2] == '--':
            argument_follows[index] = False

    for index in argument_follows:
        if argument_follows[index]:
            pass
        else:
            pass

    return job_count, job_names

def print_help_message() -> None:
    pass
