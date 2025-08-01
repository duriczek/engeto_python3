# Elections Scraper

This script creates a CSV file, that contains election results form [volby.cz](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

Choose any region ('X') from the link above.

## Installation

Download needed libraries using pip:

```
pip install -r requirements.txt
```

## Usage

To run, two arguments are needed in order:
1. URL
2. filename.csv

**Example:**

```
python elections_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106" "Ostrava-mesto.csv"
```