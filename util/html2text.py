from playwright.async_api import async_playwright
import asyncio
import re
from bs4 import BeautifulSoup
from extractcontent3 import ExtractContent
import nest_asyncio
import requests
nest_asyncio.apply()


async def url2html(url):
    async with async_playwright() as p:
        browser = await p.webkit.launch()
        page = await browser.new_page()
        await page.goto(url)
        html = await page.content()
        await browser.close()
    return html


def html2text(html_string):
    soup = BeautifulSoup(html_string, "html.parser")
    github = soup.find(class_="markdown-body")
    html_string = html_string if not github else str(github)

    extractor = ExtractContent({"threshold": 50})
    extractor.analyse(html_string)
    plain_text, title = extractor.as_text()

    soup = BeautifulSoup(html_string, "html.parser")
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
    return html2text(asyncio.run(url2html(url)))
