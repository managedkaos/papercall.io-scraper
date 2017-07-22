import requests
from bs4 import BeautifulSoup

# set the main URL
base_url = "https://www.papercall.io"
cfps_url = "/cfps?page=1"

# make a request to the main menu URL
r = requests.get(base_url+cfps_url)

# convert the response text to soup
soup = BeautifulSoup(r.text, "lxml")

next_url = soup.find("a", {"rel":"next"})
print next_url
