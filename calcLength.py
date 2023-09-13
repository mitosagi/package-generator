from util.text_io import read_text, write_text
from util.get_files import get_files_and_folders, ext_filter
from util.sevenzip import extract
import tiktoken
from extractcontent3 import ExtractContent
from urlextract import URLExtract
import re


# extracter
extractor = ExtractContent()
opt = {"threshold": 50}
extractor.set_option(opt)

# tiktoken
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")


def trim_token(text, length):
    return encoding.decode(encoding.encode(text)[:length])


# main
texts_readme = read_text(
    'data/NVEnc_readme.txt')
write_text('workspace/trim-readme.txt', trim_token(texts_readme, 2000))

texts_html = read_text(
    'data/NVEnc.html')
extractor.analyse(texts_html)
plain_text_html, title = extractor.as_text()
print(title)
write_text('workspace/trim-html.txt', trim_token(plain_text_html, 2000))

regex = r"<!-- saved from url=\(\d+\).+? -->"
url = URLExtract().find_urls(re.search(regex, texts_html).group())[0]


extract('data/Aviutl_NVEnc_7.31.zip')
