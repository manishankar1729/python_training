import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os

url = "https://www.bing.com/search?q=what+is+meaning+of+comphersion+in+python&qs=n&form=QBRE&sp=-1&lq=0&pq=what+is+meaning+of+comphersion+in+pytho&sc=11-39&sk=&cvid=A1535272C5A9428D8BE43FFAABCEDA7D&ghsh=0&ghacc=0&ghpl="

def fetch_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return [a['href'] for a in soup.find_all('a', href=True)]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching links from {url}: {e}")
        return []

def download_file(link, folder="downloads"):
    try:
        os.makedirs(folder, exist_ok=True)
        response = requests.get(link, stream=True)
        response.raise_for_status()
        filename = os.path.join(folder, os.path.basename(link))
        if not filename.strip():
            return
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed  {link}: {e}")

def main():
    links = fetch_links(url)
    print("Extracted Links:")
    for link in links:
        print(link)
    full_links = [link for link in links if link.startswith("http")]
    with open("links.txt", "w") as f:
        for link in full_links:
            f.write(link + "\n")
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_file, full_links)

if __name__ == "__main__":
    main()
