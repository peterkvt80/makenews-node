# @param - Web url link from a BBC RSS feed
# @brief Reads the new story and extracts the story text
# @return Plain story text
import requests
from bs4 import BeautifulSoup

def extract_bbc_story(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('article')
    if not article:
        return None
    paragraphs = article.find_all('p')
    story = '\n'.join(p.get_text() for p in paragraphs)
    return story