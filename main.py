
from bs4 import BeautifulSoup
import csv

# Load HTML file
with open("input.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find the search results table
table = soup.find("table", class_="search-result-table")

rows = []
for tr in table.find_all("tr"):
    cells = tr.find_all(["td", "th"])
    row = [c.get_text(" ", strip=True) for c in cells]
    rows.append(row)

# Write CSV
with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Done → output.csv created")
