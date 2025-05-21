import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text,'html.parser')
        title = soup.title.string if soup.title else "No title found"
        print(f"Title : {title}")

        meta_desc = soup.find("Meta", attrs={"name" : "description"})
        if meta_desc:
            print(f"Meta Description : {meta_desc['content']}")
        else:
            print("No meta descrioption found") 

        links = soup.find_all('a')
        print(f"Number of links found : {len(links)}")
        for link in links[:5]:
            print(f" {link.get('href')}")
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")

def main():
    url_name = input("Enter url to gather data : ")
    scrape_website(url_name)

if __name__ == "__main__":
    main()