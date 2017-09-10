import pymongo
from bs4 import BeautifulSoup
from items import CrawlBbcNewsItem

# Use the SoupBeauti library to clean up the html
# - reformat the html page
# - Remove unnessary content (scrip, error message, ...)
class CleansingPipeline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):
        print ("_________________________________________________________")
        soup = BeautifulSoup(item["content_html"], 'html.parser')
        for script in soup(["script", "style"]):
            script.extract()
        for span in soup.find_all("span", {'class':'off-screen'}): 
            span.decompose()
        item["content_text"] = soup.get_text()
        item["content_html"] = soup.prettify()

        return item