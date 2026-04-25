import requests # to make HTTP requests
from bs4 import BeautifulSoup # to parse HTML content
import csv # to write data to CSV
import time # to add delay between requests

GBP_TO_EUR = 1.17  #approximate conversion rate

def get_rating(star_class):    #convert star rating from class name to int
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(star_class, 0)

base_url = "http://books.toscrape.com/catalogue/page-{}.html" #base url with placeholder for different pages

# Open CSV file
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price (£)", "Price (€)", "Rating"]) #defines header fow for csv

    # Loop through pages
    for page in range(1, 51):  #range of pages to scrape
        url = base_url.format(page) #format the base url with the current page number
        print(f"Scraping page {page}...") #shows progress in terminal

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod") #finds all book entries on the page

        for book in books: #extracts data for each book
            # Title
            title = book.h3.a["title"]

            # Price in pounds (remove £ symbol)
            price_text = book.find("p", class_="price_color").text
            price_gbp = float(price_text.replace("£", ""))

            # Convert to euros
            price_eur = round(price_gbp * GBP_TO_EUR, 2)

            # Rating (stored as class like "star-rating Three")
            rating_class = book.find("p", class_="star-rating")["class"][1]
            rating = get_rating(rating_class)

            # Write to CSV
            writer.writerow([title, price_gbp, price_eur, rating])

        time.sleep(1)  # add delay to avoid overwhelming the server

print("Complete")