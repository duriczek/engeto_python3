# Election Scraper

This script creates a CSV file, that contains election results form a website: www.volby.cz

## Installation

First, download needed libraries using pip:

```
pip install -r requirements.txt
```

## Usage

To run, two arguments are needed in order:
1. URL
2. filename.csv

**Example:**

```
python election-scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106" "Ostrava-mesto.csv"
```