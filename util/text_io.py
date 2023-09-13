import chardet


def read_text(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()

    encoding_info = chardet.detect(raw_data)
    encoding = encoding_info['encoding']

    if encoding is None:
        raise ValueError("Unable to determine the file's encoding.")

    return raw_data.decode(encoding)


def write_text(file_path, text):
    with open(file_path, 'w', encoding='UTF-8') as f:
        f.write(text)
