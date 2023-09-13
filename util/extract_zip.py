import shutil
from pyunpack import Archive
import os


def extract(filepath):
    folderpath = os.path.splitext(filepath)[0]
    try:
        shutil.rmtree(folderpath)
    except FileNotFoundError:
        pass
    os.mkdir(folderpath)
    Archive(filepath).extractall(folderpath)
    return folderpath
