import json
import smtplib
import time

import requests
from bs4 import BeautifulSoup

logged_in = False

with open("config.json", "r") as file:
    config = json.load(file)

def send_email(new_property_url):
    server = smtplib.SMTP(config["smtp_server"], config["smtp_port"])
    server.starttls()
    server.login(config["login_email"], config["login_password"])
    subject = "New Property Alert!"
    body = f"Check out the new property: {new_property_url}"
    msg = f"Subject: {subject}\n\n{body}"
    for recipient in config["email_to"]:
        server.sendmail(config["email_from"], recipient, msg)
    server.quit()

def scrape_properties():

    if not logged_in:
        login()

    url = "https://www.pararius.com/apartments/nederland/0-2500/3-bedrooms/75m2"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find property listings
    listings = soup.find_all('section', class_='listing-search-item')

    new_properties = []
    for listing in listings:
        title = listing.find('a', class_='listing-search-item__link--title').text.strip()
        link = listing.find('a', class_='listing-search-item__link--title')['href']
        full_link = f"https://www.pararius.com{link}"
        new_properties.append(full_link)

    return new_properties


def login():
    global logged_in
    session = requests.Session()

    login_url = config["pararius_login_url"]
    login_payload = config["pararius_login_payload"]

    login_response = session.post(login_url, data=login_payload)
    if login_response.status_code == 200:
        logged_in = True
        print("Logged in successfully!")
    else:
        logged_in = False
        print("Login failed!")

def main():
    tracked_properties = set()

    new_properties = scrape_properties()
    for property_url in new_properties:
        if property_url not in tracked_properties:
            tracked_properties.add(property_url)

    print(f"Initial properties loaded: {len(tracked_properties)}")

    while True:
        new_properties = scrape_properties()
        for property_url in new_properties:
            if property_url not in tracked_properties:
                print(f"New property found: {property_url}")
                send_email(property_url)
                tracked_properties.add(property_url)

        # Sleep some before checking again
        time.sleep(26)

if __name__ == "__main__":
    main()