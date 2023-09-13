from util.text_io import read_text, write_text
from util.get_files import get_files_and_folders, ext_filter
from util.extract_zip import extract
from util.token import trim_token
from extractcontent3 import ExtractContent
from urlextract import URLExtract
import re

# extracter
extractor = ExtractContent()
opt = {"threshold": 50}
extractor.set_option(opt)

# main
package_info = {}

texts_readme = read_text(
    'data/NVEnc_readme.txt')
write_text('workspace/trim-readme.txt', trim_token(texts_readme, 2000))

texts_html = read_text(
    'data/NVEnc.html')
extractor.analyse(texts_html)
plain_text_html, title = extractor.as_text()
package_info.update({'title': title})
write_text('workspace/trim-html.txt', trim_token(plain_text_html, 2000))

regex = r"<!-- saved from url=\(\d+\).+? -->"
url = URLExtract().find_urls(re.search(regex, texts_html).group())[0]
package_info.update({'pageURL': url})

files_and_folders = get_files_and_folders(
    extract('data/Aviutl_NVEnc_7.31.zip'))
package_info.update({'files':  ext_filter(
    files_and_folders['files']), 'folders': files_and_folders['folders']})

write_text('workspace/package-info.txt', package_info)
