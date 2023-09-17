import json
import os
import yaml
import chardet


def read_text(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()

    encoding_info = chardet.detect(raw_data)
    encoding = encoding_info['encoding']

    if encoding is None:
        print("Unable to determine the file's encoding.")
        encoding = "utf-8"

    return raw_data.decode(encoding)


def write_text(file_path, text):
    dirname = os.path.dirname(file_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(file_path, 'w', encoding='UTF-8') as f:
        if (type(text) is str):
            f.write(text)
        else:
            json.dump(text, f, indent=2, ensure_ascii=False)


def text2yaml(data):
    return yaml.safe_dump(data, allow_unicode=True)
