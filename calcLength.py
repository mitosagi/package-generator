from util.read_text import read_text_file_with_auto_encoding
import tiktoken
from bs4 import BeautifulSoup
from extractcontent3 import ExtractContent
extractor = ExtractContent()
opt = {"threshold": 50}
extractor.set_option(opt)


encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
texts = read_text_file_with_auto_encoding(
    'data/NVEnc_readme.txt')
with open('out.txt', 'w', encoding='UTF-8') as f:
    f.write(encoding.decode(encoding.encode(texts)[:2000]))

texts_html = read_text_file_with_auto_encoding(
    'data/NVEnc.html')
soup = BeautifulSoup(texts_html, "html.parser")
with open('out_html.txt', 'w', encoding='UTF-8') as f:
    f.write(soup.get_text())
    print(len(encoding.encode(soup.get_text())))

extractor.analyse(texts_html)
text, title = extractor.as_text()
with open('out_html_extract.txt', 'w', encoding='UTF-8') as f:
    f.write(text)
    print(len(encoding.encode(text)))
    print(title)
