#!/usr/bin/env python3

from os import walk
from shutil import rmtree
from sys import platform

def main() -> None:
    if 'win' in platform:
        seperator = '\\'
    else:
        seperator = '/'

    for root, folders, files in walk('.'):
        if '__pycache__' in folders:
            rmtree(f'{root}{seperator}__pycache__')


if __name__ == '__main__':
    main()
