from requests_html import HTMLSession
import feedparser
from time import sleep

session=HTMLSession()

def get_amd():
    url='https://www.amd.com/en/newsroom.html'
    r=session.get(url)
    #h5.card-title
    title=r.html.find('a.card-full-link',first=True)
    title=title.text
    link=r.html.find('a.card-full-link',first=True)
    link = 'https://www.amd.com' + link.attrs['href'] if 'href' in link.attrs and 'amd.com' not in link.attrs['href'] else link.attrs['href']
    print(title,'\n',link)


def get_cnbc():
    rss='https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100003114'
    #cnbc has multiple rss feeds, so you can utilize this code for all of them
    d = feedparser.parse(rss)
    title = d.entries[0].title
    excerpt=d.entries[0].description
    link=d.entries[0].link
    print(title)
    print(excerpt)
    print(link)


while True:
    sleep(10)
    get_amd()
    sleep(30)
    get_cnbc()
    sleep(20)
