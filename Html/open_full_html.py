from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
url = 'http://www.waterwaysguide.org.au/waterwaysguide/access-point/4980/partial'
 
req = Request(url, headers={'User-Agent': 'Chrome/46.0.2490.80'})
webpage = urlopen(req).read()
