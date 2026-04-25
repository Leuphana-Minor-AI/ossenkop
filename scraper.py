import requests # for making HTTP requests
from bs4 import BeautifulSoup # for parsing HTML
import csv # for writing to CSV
import time # for adding delay between requests
import re # for cleaning price text

# Approx conversion rate (you can update this anytime)
GBP_TO_EUR = 1.17

# Convert rating text to number
def get_rating(star_class):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(star_class, 0)

# Base URL for pagination
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Create CSV file
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price (£)", "Price (€)", "Rating"])

    # Loop through pages
    for page in range(1, 6):  # adjust as needed
        url = base_url.format(page)
        print(f"Scraping page {page}...")

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books: # Extract data for each book
            # Title
            title = book.h3.a["title"]

            # Price (FIXED encoding-safe version)
            price_text = book.find("p", class_="price_color").text
            price_clean = re.sub(r"[^\d.]", "", price_text)  # keeps only numbers + dot
            price_gbp = float(price_clean)

            # Convert to EUR
            price_eur = round(price_gbp * GBP_TO_EUR, 2)

            # Rating
            rating_class = book.find("p", class_="star-rating")["class"][1]
            rating = get_rating(rating_class)

            # Save to CSV
            writer.writerow([title, price_gbp, price_eur, rating]) 

        time.sleep(1)  # avoid overwhelming the server

print("Complete")