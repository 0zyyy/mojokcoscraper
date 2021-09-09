from bs4 import BeautifulSoup as bs
import requests
from csv import DictWriter
print("Import sukses")
def scrapeWeb():
    halaman = int(input("Berapa halaman? "))
    jenis_halam = input("Scrape halaman mana? ").lower()
    all_news = []
    for x in range(1,halaman + 1):
        cap = requests.get(f"https://mojok.co/{jenis_halam}/page/{x}")
        soup = bs(cap.text, "html.parser")
        contain = soup.find(class_="jeg_postblock")
        posts = contain.find_all(class_="jeg_post")
        for post in posts:
            uhuys = post.find(class_="jeg_post_title")
            author = post.find(class_="jeg_meta_author")
            all_news.append({
                "Jungdul": uhuys.find("a").get_text(),
                "Link": uhuys.find("a")["href"],
                "Author": author.find("a").get_text()
            })
        # btn = soup.find(class_="next")
    # print(str(len(all_news)) + " artikel ditemukan")
    return all_news

news = scrapeWeb()
with open("news.csv","w") as file:
    headers = ["Jungdul","Link","Author"]
    csv_writer = DictWriter(file,fieldnames=headers)
    csv_writer.writeheader()
    for new in news:
        csv_writer.writerow(new)
print("scrape success")