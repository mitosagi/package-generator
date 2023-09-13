from pyunpack import Archive


def extract(filepath):
    Archive(filepath).extractall('.')
