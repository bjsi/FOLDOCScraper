import requests
from typing import Dict
from bs4 import BeautifulSoup
from time import sleep
import json


baseurl = "https://foldoc.org"

pages = [
        "/contents/A.html",
        "/contents/B.html",
        "/contents/C.html",
        "/contents/D.html",
        "/contents/E.html",
        "/contents/F.html",
        "/contents/G.html",
        "/contents/H.html",
        "/contents/I.html",
        "/contents/J.html",
        "/contents/K.html",
        "/contents/L.html",
        "/contents/M.html",
        "/contents/N.html",
        "/contents/O.html",
        "/contents/P.html",
        "/contents/Q.html",
        "/contents/R.html",
        "/contents/S.html",
        "/contents/T.html",
        "/contents/U.html",
        "/contents/V.html",
        "/contents/W.html",
        "/contents/X.html",
        "/contents/Y.html",
        "/contents/Z.html"
        ]


def download_html(rel_url: str) -> str:
    """
    Download the html of the relative url
    """

    abs_url = baseurl + rel_url
    response = requests.get(abs_url)
    return response.text


def extract_keyword_url_map(html: str) -> Dict[str, str]:
    """
    Create a keyword -> url dictionary from the html.
    """

    soup = BeautifulSoup(html, 'html.parser')
    ret = {}
    d = soup.find('div', {'class': 'word-list'})
    for a in d.find_all('a'):
        ret[a.string] = baseurl + a["href"]
    return ret


def save_as_json(dic: Dict[str, str]) -> None:
    with open('keyword_url_map', 'w') as fp:
        json.dump(dic, fp)


if __name__ == "__main__":
    ret: Dict[str, str] = {}
    for page in pages:
        html = download_html(page)
        dic = extract_keyword_url_map(html)
        ret = {**ret, **dic}
        sleep(0.5)
    save_as_json(ret)
