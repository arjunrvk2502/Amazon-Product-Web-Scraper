# 🛒 Amazon Product Web Scraper

This is a Python-based web scraping project that extracts product information from **Amazon.in**. Given a product name, it fetches data like **title, price, ratings, reviews, discounts, and availability**, and saves the results to a CSV file.

---

## 📌 Features

- 🔍 Scrapes live product data from Amazon.in
- 📦 Extracts key product attributes:
  - **Title**
  - **Price**
  - **Ratings**
  - **Number of Reviews**
  - **MRP (Original Price)**
  - **Discount Percentage**
  - **Availability**
- 🔄 Random User-Agent rotation to avoid blocking
- 🧠 Handles HTTP 503 retry logic
- 📁 Stores output in **CSV format** for easy analysis

---

## 🛠️ Technologies Used

- `requests` — for sending HTTP requests  
- `BeautifulSoup (bs4)` — for parsing HTML content  
- `pandas` — for structuring and saving the data  
- `numpy` — for handling missing data  
- `time`, `random` — for delays and user-agent rotation

---

## 🚀 How to Run

### 1. Install Dependencies
Make sure you have Python 3.x installed. Then run:

```
pip install requests beautifulsoup4 pandas numpy
```

### 2. Run the Script

python web_scrapping.py

### 3. Input the Product
You’ll be prompted to enter a product name:

Enter the product you need to scrap from amazon : headphones

### 4. Output
A CSV file named headphones.csv will be saved on your desktop with the extracted data.

---

## 🧠 How It Works

1. Constructs the Amazon search URL from user input.  
2. Sends a GET request with a **random User-Agent**.  
3. Parses the search results page to extract product links.  
4. Visits each product link to fetch detailed info.  
5. Stores all data in a dictionary.  
6. Converts the dictionary into a Pandas DataFrame.  
7. Cleans the data and saves it to a CSV file.

---

## ⚠️ Important Notes

- ❗ This scraper is intended for **educational purposes only**.
- 🔁 The code targets the HTML structure of **Amazon.in**, which may change over time. If it stops working, update the HTML classes or tag selectors.
- 🛡️ Use delays (`time.sleep`) and rotate User-Agents to reduce the risk of getting blocked or banned.

---

## 👨‍💻 Author

**Arjun R.V.**  
📬 [LinkedIn Profile](https://www.linkedin.com/in/arjun-vijayakumar-a5609932a)

---

## 📜 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
