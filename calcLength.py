from util.text_io import read_text, write_text
import tiktoken
from extractcontent3 import ExtractContent

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
