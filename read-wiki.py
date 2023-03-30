from time import sleep
from bs4 import BeautifulSoup, Tag
import requests
import re

HYPERION_CANTOS_WIKI = "https://hyperioncantos.fandom.com"


wiki_pages = []
resp = requests.get(HYPERION_CANTOS_WIKI + "/wiki/Special:AllPages")
if resp.status_code == 200:
    print(f"Reading /wiki/Special:AllPages")
    soup = BeautifulSoup(resp.content, "html.parser")
    all_pages = soup.find("ul", class_="mw-allpages-chunk")
    for page in all_pages.children:
        if isinstance(page, Tag):
            # Get links for all the pages in the hyperion cantos wiki
            wiki_pages.append(page.find("a")["href"])
else:
    raise Exception("Hyperion Cantos Wiki request failed")


for page in wiki_pages:
    resp = requests.get(HYPERION_CANTOS_WIKI + page)
    if resp.status_code == 200:
        print(f"Reading {page}")
        soup = BeautifulSoup(resp.content, "html.parser")
        header_text = soup.find("h1", id="firstHeading").string
        content_section = soup.find("div", class_="mw-parser-output")

        # Remove the figure tag, since it is not text based
        [tag.decompose() for tag in content_section.find_all("figure")]
        content_section_text = content_section.get_text()
        content_section_text = re.sub("\[\d+\]", "", content_section_text)
        with open(f"data/{page.split('/')[-1]}.txt", "w") as f:
            f.write(header_text.strip())
            f.write("\n")
            f.write(content_section_text.strip())
