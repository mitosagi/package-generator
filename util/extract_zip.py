from datetime import datetime
from pyunpack import Archive
import os
import zipfile
import chardet


def extract(filepath):
    folderpath = os.path.join(
        'workspace', os.path.splitext(os.path.basename(filepath))[0])
    ext = os.path.splitext(filepath)[1]

    latest_modification_time = datetime(1980, 1, 1)

    if ext == '.zip':
        with zipfile.ZipFile(filepath) as z:
            raw_data = bytearray()
            for info in z.infolist():
                raw_data += info.filename.encode(
                    'utf-8' if info.flag_bits & 0x800 else 'cp437')

            encoding_info = chardet.detect(raw_data)
            encoding = encoding_info['encoding']

            if encoding == 'Windows-1252':
                encoding = 'cp932'
            if encoding is None:
                print("Unable to determine the file's encoding.")
                encoding = "utf-8"

            for info in z.infolist():
                info.filename = info.filename.encode(
                    'utf-8' if info.flag_bits & 0x800 else 'cp437').decode(encoding)
                z.extract(info, path=folderpath)

            # get modification time
            files_in_zip = z.infolist()
            for file_info in files_in_zip:
                file_modification_time = datetime(*file_info.date_time)
                if file_modification_time > latest_modification_time:
                    latest_modification_time = file_modification_time
    else:
        Archive(filepath).extractall(folderpath, True)

    if hasattr(latest_modification_time, 'strftime'):
        latest_modification_time = latest_modification_time.strftime(
            '%Y/%m/%d')
    if latest_modification_time == datetime(1980, 1, 1):
        latest_modification_time == ''

    return folderpath, latest_modification_time
