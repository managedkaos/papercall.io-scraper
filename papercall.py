import re
import requests
from bs4 import BeautifulSoup

# set the main URL
base_url = "https://www.papercall.io"
cfps_url = "/cfps?page=1"

# loop over the pages
while cfps_url is not None:
    # create the target URL by concatenating the base and cpfs URLs
    target_url = str(base_url) + str(cfps_url)
    
    # make a request to the target  URL
    r = requests.get(target_url)

    # convert the response text to soup
    soup = BeautifulSoup(r.text, "lxml")

    # get all the divs with the "box" class
    for box in soup.find_all("div", {"class":"box"}):
       for justifize in box("div", {"class":"justifize__box"}):
           for event_titles in justifize.find_all("h3", {"class":"event__title"}):
               for event in event_titles.find_all("a", {"class":""}):
                   print event.string
                   
                   # get the event name and location
                   match = event.string.split(" - ")

                   # expect no location if only one item in match
                   if len(match) == 1:
                       match.append("")

                   # expect a dash in the name if three items in match
                   elif len(match) == 3:
                       match[0] = match[0] + " - " + match[1]
                       match[1] = match[2]

                   # otherwise match should be good(?)
                   else:
                       pass

                   print "name:     ", match[0]
                   print "location: ", match[1]
                   print "url:      ", event['href']
                   print
           #for meta_data in justifize.find_all("h4"):
           #    print meta_data

    # get the next url
    next_url = soup.find("a", {"rel":"next"})
    
    # get the next URL or set to None if not found
    try:
        cfps_url = next_url['href']
    except:
        cfps_url = None
