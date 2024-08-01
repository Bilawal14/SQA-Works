import bs4
import requests as req


base_url = f"https://books.toscrape.com/catalogue/page-1.html"

res = req.get(base_url)
print(res.status_code)

#print(res.text)

soup = bs4.BeautifulSoup(res.text,"html")
#print(soup)
#print(soup.select(".product_pod"))
#print(soup.select("./product_pod"))
books = soup.find_all("h3")
for i in books:
    # Title
    print(i.find("a")["title"])