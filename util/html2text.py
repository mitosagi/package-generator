import re
from bs4 import BeautifulSoup
from extractcontent3 import ExtractContent
import requests


def html2text(html_string):
    extractor = ExtractContent({"threshold": 50})
    extractor.analyse(html_string)
    plain_text, title = extractor.as_text()
    html, _ = extractor.as_html()

    soup = BeautifulSoup(html, "html.parser")
    headers = []
    for tag in soup.find_all(True):
        if tag.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            hashes = "#" * int(tag.name[1])
            headers.append(f"{hashes} {tag.get_text()}")

    return '\n'.join([title] + headers + [plain_text])


def url2text(url):
    nico_regex = r'nicovideo.+(sm\d+)'
    if re.search(nico_regex, url):
        nico_url = 'https://ext.nicovideo.jp/api/getthumbinfo/' + \
            re.search(nico_regex, url).group(1)
        return requests.post(nico_url).text
    text = requests.post(url).text
    print(text)
    return html2text(text)
