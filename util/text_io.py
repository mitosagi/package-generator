import json
import yaml
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
        if (type(text) is str):
            f.write(text)
        else:
            json.dump(text, f, indent=2, ensure_ascii=False)


def text2yaml(data):
    return str(yaml.dump(data, encoding='utf-8', allow_unicode=True))
