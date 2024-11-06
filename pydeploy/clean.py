from os import walk, listdir
from os.path import join

from sys import platform

from shutil import rmtree

def main() -> None:
    for (root, dirs, files) in walk('.', topdown=True):
        if '__pycache__' in dirs:
            rmtree(join(root, '__pycache__'))

if __name__ == '__main__':
    main()
