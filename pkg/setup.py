from pathlib import Path
from os import mkdir
from os import scandir
from os.path import exists


class Folder:

    def __init__(self, label):
        '''Create a Folder object.'''
        self.name = str(label)
        self.path = Path(str(label))

        mkdir(self.name)


def main():
    for year in range(1990, 2022):
        folder = str(year)
        if not exists(folder):
            mkdir(folder)
            print(f'Created folder {year}')
        else:
            print(f'Folder {year} already exists')


if __name__ == '__main__':
    main()