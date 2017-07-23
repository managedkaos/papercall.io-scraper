import requests
from bs4 import BeautifulSoup

# set the main URL
base_url = "https://www.papercall.io"
cfps_url = "/cfps?page=1"

# loop over the pages
while cfps_url is not None:
    # make a request to the main menu URL
    r = requests.get(str(base_url)+str(cfps_url))

    # convert the response text to soup
    soup = BeautifulSoup(r.text, "lxml")

    # scraping goes here

    # get the next url
    next_url = soup.find("a", {"rel":"next"})
    
    # 
    try:
        cfps_url = next_url['href']
    except:
        cfps_url = None
    print cfps_url
