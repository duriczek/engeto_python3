# Election Scraper

This script creates a CSV file, that contains election results form a website: wwww.volby.cz

## Installation

First, install needed libraries using pip:

```
pip install -r requirements.txt
```

Running the script
To run, 2 arguments are needed in this order:
1. URL
2. filename.csv

Example:
python election-scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106" "Ostrava-mesto.csv"
