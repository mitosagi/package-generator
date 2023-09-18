from bs4 import BeautifulSoup
from extractcontent3 import ExtractContent


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

    return plain_text, headers, title
