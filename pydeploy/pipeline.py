import commandline.args

class Pipeline:
    '''
    '''
    def __init__(self, sys_args: list[str]): #just sets up variables
        self.raw_arguments: list[str] = sys_args
        
        self.dotfile_names: list[tuple[str, str]] = []
        self.script_names: list[tuple[str, str]] = []
        self.github_names: list[tuple[str, str]] = []
        self.install_names: list[tuple[str, str]] = []

        self.dotfile_jobs: int = 0
        self.script_jobs: int = 0
        self.github_jobs: int = 0
        self.install_jobs: int = 0

        self.configuration_path: str = 'does not exsist'

    def read_command_line(self) -> None:
        # check the setup of the command line to see if it is valid
        if not commandline.args.check_valid( self.raw_arguments ):
            commandline.args.print_validity_error( self.raw_arguments )
            exit()

        #get the number and names of the dotfile setup
        jobs, names = commandline.args.parse_dotfile_jobs()
        self.dotfile_jobs = jobs
        self.dotfile_names = names

        #get the number and names of the script jobs
        jobs, names = commandline.args.parse_script_jobs()
        self.script_jobs = jobs
        self.script_names = names

        #you know the drill but with github stuff this time
        jobs, names = commandline.args.parse_github_jobs()
        self.github_jobs = jobs
        self.github_names = names

        #ditto but with system and internet installs
        jobs, names = commandline.args.parse_install_jobs()
        self.install_jobs = jobs
        self.install_names = names

    def read_config_file(self) -> None:
        if self.configuration_path == None:
            return

    def deploy_script(self) -> None:
        if self.script_jobs == 0:
            return

    def deploy_dot_file(self) -> None:
        if self.dotfile_jobs == 0:
            return

    def install_program(self) -> None:
        if self.install_jobs == 0:
            return

    def deploy_github_repo(self) -> None:
        if self.github_jobs == 0:
            return

    def still_running(self) -> bool:
        dotfile_check: bool = self.dotfile_jobs != 0
        script_check: bool = self.script_jobs != 0
        github_check: bool = self.github_jobs != 0
        install_check: bool = self.install_jobs != 0
        if dotfile_check or script_check or github_check or install_check:
            return True
        return False
