from util.text_io import read_text, write_text
from util.get_files import folder_filter, get_files_and_folders, ext_filter
from util.extract_zip import extract
from util.token import trim_token, count_token
from extractcontent3 import ExtractContent
from urlextract import URLExtract
import re
import glob

# extractcontent3
extractor = ExtractContent()
opt = {"threshold": 50}
extractor.set_option(opt)

# main
package_info = {}
zipfilename = 'data/Aviutl_NVEnc_7.31.zip'

texts_html = read_text(
    'data/NVEnc.html')
extractor.analyse(texts_html)
plain_text_html, title = extractor.as_text()
package_info.update({'title': title})
write_text('workspace/trim-html.txt', trim_token(plain_text_html, 2000))

regex = r"<!-- saved from url=\(\d+\).+? -->"
url = URLExtract().find_urls(re.search(regex, texts_html).group())[0]
package_info.update({'pageURL': url})

extracted_folder = extract(zipfilename)
files_and_folders = get_files_and_folders(extracted_folder)
package_info.update({'files': ext_filter(files_and_folders['files']),
                     'folders': folder_filter(files_and_folders['folders'])})

texts_readme = read_text(
    [p for p in glob.glob(extracted_folder + "/**", recursive=True)
     if re.search('(?i)readme', p)][0])
write_text('workspace/trim-readme.txt', trim_token(texts_readme, 2000))

write_text('workspace/package-info.txt', package_info)

separater = '-'*16
prompt = '\n'.join([
    '今回インストールするパッケージの圧縮ファイルから読み取ったメタデータです。',
    read_text('workspace/package-info.txt'),
    separater,
    '圧縮ファイルのファイル名です',
    zipfilename,
    separater,
    '圧縮ファイルに含まれるReadmeファイルの説明です。',
    read_text('workspace/trim-html.txt'),
    separater,
    '公式サイトの説明です。',
    read_text('workspace/trim-readme.txt'),
    separater,
    read_text('main_prompt.txt'),])
write_text('workspace/prompt.txt', prompt)
print(count_token(prompt))
