"""

elections_scraper.py: third project in Engeto Online Python Akademy

author: Vojtěch Duraj

email: engeto.0i4o5@passinbox.com

discord: vojtech_duraj

"""

import csv
import sys
import requests
from bs4 import BeautifulSoup

# Scrape data from website.
def scrape_html(url: str) -> BeautifulSoup:
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Failed to load the website: {url}')
        sys.exit()
    return BeautifulSoup(response.text, 'html.parser')

# List party names from html.
def get_parties(url: str) -> list:
    soup = scrape_html(url).find_all('td', 'overflow_name')
    data = []
    for row in soup:
        party = row.get_text()
        data.append(party)
    return data

# List total values from html.
def get_totals(url: str) -> list:
    soup = scrape_html(url).find_all('td')
    registered = ''.join((soup[3].get_text()).split())
    envelopes = ''.join((soup[4].get_text()).split())
    valid = ''.join((soup[7].get_text()).split())
    return [registered, envelopes, valid]

# List party votes from html.
def get_votes(url: str) -> list:
    soup = scrape_html(url).find_all('td', 'cislo', headers=['t1sb3', 't2sb3'])
    data = get_totals(url)
    for row in soup:
        votes = row.get_text().replace('\xa0', '')
        data.append(votes)
    return data

# List data from all subpages.
def get_data(url: str) -> list:
    soup = scrape_html(url).find_all('tr')
    data = []
    print('Processing data...')
    for row in soup:
        cell = row.find_all('td')
        try:
            link = 'https://www.volby.cz/pls/ps2017nss/' + cell[0].find('a')['href']
        except (IndexError, TypeError):
            continue
        else:
            code, name = cell[0].get_text(), cell[1].get_text()
            location = [code, name] + get_votes(link)
            data.append(location)

    # Set up the final list.
    header = ['code', 'location', 'registered', 'envelopes', 'valid'] + get_parties(link)
    data.insert(0 ,header)
    return data

# Save data to a new CSV file.
def write_csv(file, data):
    with open(file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    print(f"File {file} was successfully created.")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.exit('Invalid arguments. Please enter <URL> <filename.csv>.')
    
    website = sys.argv[1]
    filename = sys.argv[2]

    if 'https://www.volby.cz/pls/ps2017nss/' not in website:
        sys.exit('Invalid URL address.')
    elif '.csv' not in filename:
        sys.exit('Invalid filename.')
    
    dataset = get_data(website)
    write_csv(filename, dataset)