MESSAGE = [
    'The acceptable command line arguments and there values follow:',
    '\targument: --help -H values: NONE',
]

def print_help() -> None:
    for line in MESSAGE:
        print(line)
