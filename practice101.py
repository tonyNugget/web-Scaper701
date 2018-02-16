import os
import inspect
import requests
import re
from bs4 import BeautifulSoup


def foldercreation(foldername):
    current_path = os.path.dirname(inspect.getfile(inspect.currentframe())) + "/" + foldername

    if os.path.exists(current_path):
        pass
    else:
        os.mkdir(current_path)


def find_a_tag():
    pass


req = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
re_comp = re.compile(r"\w{3}\.\w+\.\w{3}")
re_search = re.search(re_comp, req.url)
print(re_search.group())
foldercreation(re_search.group())
soup = BeautifulSoup(req.text, 'lxml')
print(soup)
