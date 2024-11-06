import pipeline as pipe
import sys

def main(sys_args: list[str]) -> None:
    pipeline = pipe.Pipeline( sys_args )

    pipeline.read_command_line()
    pipeline.read_config_file()
    while pipeline.still_running():
        pipeline.deploy_dot_file()
        pipeline.deploy_script()
        pipeline.install_program()
        pipeline.github_repo()

if __name__ == '__main__':
    main( sys.argv[1:] )
