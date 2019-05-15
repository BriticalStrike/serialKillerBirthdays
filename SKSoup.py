from bs4 import BeautifulSoup
import requests

page_quote = "https://www.murdermiletours.com/blog/serial-killers-and-their-birthdays-date-of-birth"

page = requests.get(page_quote).text
soup = BeautifulSoup(page, 'lxml')


for num in range(2):
    match = soup.find_all('td', class_='wsite-multicol-col')[num]
    newdiv = match.div.text
    newfile = open("DataFiles\SKBdays.txt", "a", encoding="utf8")
    newfile.write(newdiv)
    newfile.close()
