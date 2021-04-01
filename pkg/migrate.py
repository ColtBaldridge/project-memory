import os
from pathlib import Path
import shutil


def verify_migration(dir1, dir2):
    return os.walk(dir1) == os.walk(dir2)


def main():
    cwd = Path('E:/Pictures')
    src = Path('F:/')
    dst = Path('E:/Pictures/staging')
    os.chdir(cwd)
    if not os.path.exists(dst):
        os.mkdir(dst)
    shutil.copytree(src, dst)

    verify_migration(src, dst)


if __name__ == '__main__':
    main()