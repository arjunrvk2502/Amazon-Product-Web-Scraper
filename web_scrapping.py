import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import time
import random


def fetch_product_data(link, headers):
    try:
        new_webpage = requests.get(link, headers=headers)
        if new_webpage.status_code == 503:
            print("Received 503 error. Retrying after delay...")
            time.sleep(random.uniform(5, 15))  # Wait for a random time between 5 to 15 seconds
            return fetch_product_data(link, headers)  # Retry fetching the data
        return new_webpage
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
        

def product_title(soup):
    try:
        title = soup.find("span" , attrs={"id" : "productTitle"})
        title = title.text
        title = title.strip()
    except:
        title = ""
    return title


def product_price(soup):
    try:
        price = soup.find("span" , attrs={"class" : "a-price-whole"})
        price = price.text
        price = price.strip()
    except:
        price = ""
    return price


def product_discount(soup):
    try:
        discount = soup.find("span" , attrs={"class" : "a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage"}).text
    except:
        discount  = ""
    return discount


def product_mrp(soup):
    try:
        mrp = soup.find("span" , attrs={"class" : "a-price a-text-price"}).find("span" , attrs = {"class" : "a-offscreen"}).text.strip()
    except:
        mrp = ""
    return mrp


def product_ratings(soup):
    try:
        ratings = soup.find("span" , attrs={"class" : "a-size-medium a-color-base"}).text.strip()
    except:
        ratings = ""
    return ratings


def product_availability(soup):
    try:
        availability = soup.find("span" , attrs={"class" : "a-size-medium a-color-success"}).text.strip()
    except:
        availability = ""
    return availability


def product_reviews(soup):
    try:
        reviews = soup.find("span" , attrs={"id" : "acrCustomerReviewText"}).text.strip()
    except:
        reviews = ""
    return reviews


if __name__ == "__main__":

    user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.961.38 Safari/537.36 Edg/93.0.961.38',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',]
    
    #get product name from user
    product_name = input("Enter the product you need to scrap from amazon : ").strip()
    product_webname = product_name.replace(" ","+")

    #URL of the webpage
    url = f"https://www.amazon.in/s?k={product_webname}&ref=nb_sb_noss"

    #my user-agent
    header = ({'User-Agent':random.choice(user_agents),
               'Accept-Language': 'en-US, en;q=0.5'})
    
    #HTTP request
    webpage = requests.get(url , headers=header) #print(website.status_code)  #print(type(website.content))  #print(website.content) --> <Bytes> --> <HTML>
    
    
    if webpage.status_code == 200:
        print("Working On ....")

    #chect status
    if webpage.status_code != 200:
        print("Failed to retrieve webpage")
        print(webpage) #--> <response[503,400,429....]>
        exit()

    #fetch all data and convert it into html code(using BueatifulSoup)
    soup = bs(webpage.text , "html.parser")

    #fetch all the product links
    links = soup.find_all("a" , attrs={"class" : "a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal"})

    #store all the product links
    links_list = []

    #loop over all the links in the webpage and add to the list
    for link in links:
        links_list.append(link.get("href"))
    
    d = {"title":[] , "price":[] , "ratings":[] , "reviews":[] , "discount":[] , "mrp":[] , "availability":[]}
    count = 1
    print("Plese wait a minute.")
    for link in links_list:
        full_link = "https://www.amazon.in" + link

        new_webpage = fetch_product_data(full_link , header)

        if new_webpage is None:
            continue
        
        new_soup = bs(new_webpage.content , "html.parser")

        d["title"].append(product_title(new_soup))
        d["price"].append(product_price(new_soup))
        d["ratings"].append(product_ratings(new_soup))
        d["reviews"].append(product_reviews(new_soup))
        d["mrp"].append(product_mrp(new_soup))
        d["discount"].append(product_discount(new_soup))
        d["availability"].append(product_availability(new_soup))

        print(f"Fetching product {count} details..")
        count += 1
        time.sleep(random.uniform(1, 3))

    #create the DataFrame
    df = pd.DataFrame.from_dict(d)
    df["title"] = df["title"].replace("", np.nan)
    df = df.dropna(subset=["title"])
    df.to_csv(f"C:/Users/Administrator/Desktop/{product_name}.csv", header=True , index=False)
    print(f"Data saved to {product_name}.csv")
    