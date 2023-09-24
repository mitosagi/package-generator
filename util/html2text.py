import re
from bs4 import BeautifulSoup
from extractcontent3 import ExtractContent
import asyncio
from pyppeteer import launch
import requests


async def get_html(url):
    def decode_unicode_escapes(s):
        escapes = re.findall(r'(?:\\u[0-9a-fA-F]{4})+', s)
        copy_str = str(s)

        for escape in escapes:
            copy_str = copy_str.replace(escape, bytes(
                escape, encoding='utf-8').decode('unicode-escape'))

        return copy_str

    browser = await launch(args=['--no-sandbox'])
    page = await browser.newPage()
    await page.setUserAgent(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")
    await page.goto(url, waitUntil=['load', 'networkidle0'])
    contents = decode_unicode_escapes(decode_unicode_escapes(decode_unicode_escapes(await page.content())))
    return contents


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
    return html2text(asyncio.get_event_loop().run_until_complete(get_html(url)))
