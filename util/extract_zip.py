from pyunpack import Archive
import os
import zipfile
import chardet


def extract(filepath):
    folderpath = os.path.join(
        'workspace', os.path.splitext(os.path.basename(filepath))[0])
    ext = os.path.splitext(filepath)[1]

    if ext == '.zip':
        with zipfile.ZipFile(filepath) as z:
            raw_data = bytearray()
            for info in z.infolist():
                raw_data += info.filename.encode('cp437')

            encoding_info = chardet.detect(raw_data)
            encoding = encoding_info['encoding']

            if encoding == 'Windows-1252':
                encoding = 'cp932'
            if encoding is None:
                print("Unable to determine the file's encoding.")
                encoding = "utf-8"

            for info in z.infolist():
                info.filename = info.filename.encode('cp437').decode(encoding)
                z.extract(info, path=folderpath)
    else:
        Archive(filepath).extractall(folderpath, True)

    return folderpath
