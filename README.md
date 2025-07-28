# Amazon-Product-Web-Scraper
This is a Python-based web scraping project that extracts product information from Amazon.in. Given a product name, it fetches data like title, price, ratings, reviews, discounts, and availability, and saves the results to a CSV file.
📌 Features
Scrapes live product data from Amazon.in

Extracts key product attributes:

Title

Price

Ratings

Number of Reviews

MRP (Original Price)

Discount Percentage

Availability

Random User-Agent rotation to avoid blocking

Handles HTTP 503 retry logic

Stores output in CSV format for easy analysis

🛠️ Technologies Used
requests — for sending HTTP requests

BeautifulSoup (bs4) — for parsing HTML content

pandas — for structuring and saving the data

numpy — for handling missing data

time, random — for delays and user-agent rotation


🚀 How to Run
Install dependencies
Make sure you have Python 3.x installed. Then install the required libraries:
pip install requests beautifulsoup4 pandas numpy

Run the script
python web_scrapping.py

Input the product
You'll be prompted to enter the product name you want to search for. Example:
Enter the product you need to scrap from amazon : headphones

Output
A CSV file named headphones.csv will be saved on your desktop containing the scraped data.

🧠 How It Works
Constructs the Amazon search URL from user input.

Sends a GET request with a randomly chosen User-Agent header.

Parses the search results page to extract links for individual product pages.

Visits each product link to fetch detailed info.

Appends all data to a dictionary.

Converts the dictionary to a Pandas DataFrame.

Cleans and saves the final output as a CSV.

⚠️ Important Notes
This scraper is designed for educational purposes only. Scraping Amazon may violate their Terms of Service.

It targets the structure of Amazon.in, which is subject to change. If it stops working, HTML classes or tags might need updates.

Use delays (time.sleep) and rotate User-Agents to reduce the risk of IP bans.

👨‍💻 Author
Arjun R.V.
📬 www.linkedin.com/in/arjun-vijayakumar-a5609932a

📜 License
This project is licensed under the MIT License.

