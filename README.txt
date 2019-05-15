This is a little project I worked on that was inspired by the social media posts going around saying serial killers belong to only a few astrological signs.
I thought that had to be inaccurate.
I worked on this project to get used to web scraping, regex, pandas, and matplotlib.

I separated each step into a .py file:

Step 1: SKSoup.py scrapes data from the web that contains serial killers and their birthdays.
Step 2: SKtoCSV.py turns the scraped data into a .csv.
Step 3: SKPandas.py iterates over the .csv to determine astrological signs and adds them to a column.
Step 4: SKAnalysis.py uses pandas and matplotlib to create a bar chart showing the number of serial killers per astrological sign.

All iterations of the data files are contained in the DataFiles folder.
Figure_1 is a copy of the bar chart after SKAnalysis has been run.

Britt