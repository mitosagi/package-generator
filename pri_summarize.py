import os
from util.text_io import read_text, text2yaml, write_text
from util.get_files import calc_sha384, get_files_and_folders, search_file
from util.extract_zip import extract
from util.token import trim_token, count_token
from extractcontent3 import ExtractContent
import re

input_folder = 'input'

zipfilename = search_file(input_folder, ['\.(zip|lzh|7z|rar)'])
extracted_folder = extract(zipfilename)
texts_html = read_text(search_file(input_folder, ['\.html']))

extractor = ExtractContent({"threshold": 50})
extractor.analyse(texts_html)
plain_text_html, title = extractor.as_text()

metadata = {
    'pageURL': [(result.groups()[0] if result else '') for result in [re.search(r"<!-- saved from url=\(\d+\)(.+?) -->", texts_html)]][0],
    'title': title,
} | get_files_and_folders(extracted_folder)
metadata_yaml = text2yaml(metadata)
write_text('workspace/metadata.yaml', metadata_yaml)

separater = '-'*16
prompt = '\n'.join([
    '今回インストールするパッケージの圧縮ファイルから読み取ったメタデータです。',
    metadata_yaml,
    separater,
    '圧縮ファイルのファイル名です',
    zipfilename,
    separater,
    '圧縮ファイルに含まれるReadmeファイルの説明です。',
    trim_token(plain_text_html, 2000),
    separater,
    '公式サイトの説明です。',
    trim_token(read_text(search_file(extracted_folder,
               ['(readme|説明|使)', '\.(md|txt)'])), 2000),
    separater,
    read_text('pri_summarize.txt'),])
write_text('workspace/gpt3_input.txt', prompt)
print(count_token(prompt))

write_text('workspace/sha368.json',
           {'archive': calc_sha384(zipfilename),
            'files': [{'rawfilename': file,
                       'hash': calc_sha384(os.path.join(extracted_folder, file))}
                      for file in metadata['files']]})
