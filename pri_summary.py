from util.text_io import read_text, text2yaml, write_text
from util.get_files import get_files_and_folders
from util.extract_zip import extract
from util.token import trim_token, count_token
from extractcontent3 import ExtractContent
import re
import glob

package_info = {}
zipfilename = 'data/Aviutl_NVEnc_7.31.zip'
extracted_folder = extract(zipfilename)
texts_html = read_text(
    'data/NVEnc.html')

extractor = ExtractContent({"threshold": 50})
extractor.analyse(texts_html)
plain_text_html, title = extractor.as_text()

metadata = text2yaml({
    'pageURL': [(result.groups()[0] if result else '') for result in [re.search(r"<!-- saved from url=\(\d+\)(.+?) -->", texts_html)]][0],
    'title': title,
} | get_files_and_folders(extracted_folder))
write_text('workspace/metadata.yaml', metadata)

separater = '-'*16
prompt = '\n'.join([
    '今回インストールするパッケージの圧縮ファイルから読み取ったメタデータです。',
    metadata,
    separater,
    '圧縮ファイルのファイル名です',
    zipfilename,
    separater,
    '圧縮ファイルに含まれるReadmeファイルの説明です。',
    trim_token(plain_text_html, 2000),
    separater,
    '公式サイトの説明です。',
    trim_token(read_text([p for p in glob.glob(
        extracted_folder + "/**", recursive=True)if re.search('(?i)readme', p)][0]), 2000),
    separater,
    read_text('pri_summary.prompt.txt'),])
write_text('workspace/gpt3_input.txt', prompt)
print(count_token(prompt))
