import requests
import re
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urlparse
from html.parser import HTMLParser
import os
import pandas as pd

# Regex pattern to match a URL
HTTP_URL_PATTERN = r'^http[s]*://.+'

domain = "openai.com"  
full_url = "https://openai.com/"

# Create a class to parse HTML content and extract hyperlinks (URLs)
class HyperlinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        # Create a list to store the hyperlinks
        self.hyperlinks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.hyperlinks.append(attrs["href"])

# sending an HTTP request to specified URL, retrieving the HTML content of the webpage
def get_hyperlinks(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
        return []
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        return []
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return []
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
        return []
    
    # parsing the HTML to extract hyperlinks
    html = response.text
    parser = HyperlinkParser()
    parser.feed(html)

    return parser.hyperlinks

# Function to get the hyperlinks from a URL that are within the same domain
def get_domain_hyperlinks(local_domain, url):
    clean_links = []
    for link in set(get_hyperlinks(url)):
        clean_link = None

        # If the link is a URL, check if it is within the same domain
        if re.search(HTTP_URL_PATTERN, link):
            # Parse the URL and check if the domain is the same
            url_obj = urlparse(link)
            if url_obj.netloc == local_domain:
                clean_link = link

        # If link not a URL, checking if it is a relative link
        else:
            if link.startswith("/"):
                link = link[1:]
            elif link.startswith("#") or link.startswith("mailto:"):
                continue
            clean_link = "https://" + local_domain + "/" + link

        if clean_link is not None:
            if clean_link.endswith("/"):
                clean_link = clean_link[:-1]
            clean_links.append(clean_link)

    # Returning hyperlinks within same domain
    return list(set(clean_links))

def crawl(url):
    # Parse the URL and get the domain
    local_domain = urlparse(url).netloc

    # Create a queue to store the URLs to crawl
    queue = deque([url])

    # Create a set to store the URLs that have already been seen (no duplicates)
    seen = set([url])

    # Create a directory to store the text files
    if not os.path.exists("text/"):
        os.mkdir("text/")

    if not os.path.exists("text/" + local_domain + "/"):
        os.mkdir("text/" + local_domain + "/")

    # Create a directory to store the csv files
    if not os.path.exists("processed"):
        os.mkdir("processed")

    while queue:
        url = queue.pop()
        print(url)  # for debugging

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
            continue
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            continue
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            continue
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)
            continue

        with open('text/' + local_domain + '/' + url[8:].replace("/", "_") + ".txt", "w", encoding="UTF-8") as f:
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()

            if "You need to enable JavaScript to run this app." in text:
                print("Unable to parse page " + url + " due to JavaScript being required")
            else:
                f.write(text)

        for link in get_domain_hyperlinks(local_domain, url):
            if link not in seen:
                queue.append(link)
                seen.add(link)

def remove_newlines(serie):
    serie = serie.str.replace('\n', ' ')
    serie = serie.str.replace('\\n', ' ')
    serie = serie.str.replace('  ', ' ')
    serie = serie.str.replace('  ', ' ')
    return serie

crawl(full_url)


texts=[]

# Get all the text files in the text directory
for file in os.listdir("text/" + domain + "/"):
    with open("text/" + domain + "/" + file, "r", encoding="UTF-8") as f:
        text = f.read()
        texts.append((file[11:-4].replace('-',' ').replace('_', ' ').replace('#update',''), text))

# Create a dataframe from the list of texts
df = pd.DataFrame(texts, columns = ['fname', 'text'])

# Set the text column to be the raw text with the newlines removed
df['text'] = df.fname + ". " + remove_newlines(df.text)
df.to_csv('processed/scraped.csv')
df.head()