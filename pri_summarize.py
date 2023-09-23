import os
from util.html2text import url2text
from util.text_io import read_text, text2yaml, write_text
from util.get_files import calc_sha384, get_files_and_folders, search_file
from util.extract_zip import extract
from util.gpt_token import trim_token, count_token
import re


def pri_summarize():
    input_folder = 'input'

    zipfilename = search_file(input_folder, ['\.(zip|lzh|7z|rar)'])
    extracted_folder = extract(zipfilename)
    texts_html = read_text(search_file(input_folder, ['\.html']))

    plain_text_html, headers, title = url2text(
        # 'https://qiita.com/m-m-n/items/9e5f601ed7c4997b66f8')
        # 'https://www.nicovideo.jp/watch/sm16915418')
        'https://github.com/team-apm/apm-data/issues/675')

    metadata = {
        'title': title,
        'headers': headers,
        'archiveName': os.path.basename(zipfilename)
    } | get_files_and_folders(extracted_folder)
    metadata_yaml = text2yaml(metadata)
    write_text('workspace/metadata.yaml', metadata_yaml)
    write_text('workspace/hidden_metadata.json',
               {'pageURL': [(result.groups()[0] if result else '') for result in [re.search(r"<!-- saved from url=\(\d+\)(.+?) -->", texts_html)]][0],
                'archive': calc_sha384(zipfilename),
                'files': [{'rawfilename': file,
                           'hash': calc_sha384(os.path.join(extracted_folder, file))}
                          for file in metadata['files']]})

    readme_path = search_file(
        extracted_folder, ['(readme|説明|使)', '\.(md|txt)'])
    readme_text = read_text(readme_path) if readme_path else ''

    separater = '-'*16
    return '\n'.join([
        '今回インストールするパッケージの圧縮ファイルから読み取ったメタデータです。',
        metadata_yaml,
        separater,
        '公式サイトの説明です。',
        trim_token(plain_text_html, 2000),
        separater,
        '圧縮ファイルに含まれるReadmeファイルの説明です。',
        trim_token(readme_text, 2000),
        separater,
        read_text('pri_summarize.txt'),])


if __name__ == '__main__':
    prompt = pri_summarize()
    write_text('workspace/gpt3_input.txt', prompt)
    print(count_token(prompt))
