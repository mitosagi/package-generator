import shutil
from pyunpack import Archive
import os


def extract(filepath):
    folderpath = os.path.join(
        'workspace', os.path.splitext(os.path.basename(filepath))[0])
    Archive(filepath).extractall(folderpath, True)
    return folderpath
