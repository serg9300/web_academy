from beautifulsoup4 import beautifulsoup4
import urllib
import re

html_page = urllib.urlopen("http://arstechnica.com")
soup = beautifulsoup4(html_page)
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print(link.get('href'))