from bs4 import BeautifulSoup         #essential
import requests                         #essential
url = "https://quotes.toscrape.com"     #variable for url your going to scrape data from, cleaner

response = requests.get(url)
status = response.status_code
print(response)                     #this will check the websites status, 200 means working as intended

content = response.content
soup = BeautifulSoup(content, 'html.parser')    #will scrape the date from the website, set as a variable for cleaner code format
print(soup.title)                                       #will print website title
print(soup.title.get_text())                            #will print only website title text
print(soup.body)                                        #will print the entire website including classes, objects and labels for each item
print(response.status_code)                             #will print status code (remember 200 is good)

quotes = soup.find_all("div", class_="quote")
for quote in quotes:
    print(quote.text)                                   #this will print everything labelled as a quote from the website, in this case the tags on the quote and
                                                        # the author name are included as they are also part of the quote label

#you can use inspect element on the website to view the labels and find exactly what it is you need to parse specific data

#below is another way to do what the above does

to_scrape = requests.get(url)
soup2 = BeautifulSoup(to_scrape.text, 'html.parser')        #will specifically scrape text
quotes2 = soup2.find_all("span", attrs={"class": "text"})           #using inspect element to call labels for specific text
authors = soup2.find_all("small", attrs={"class": "author"})        #same here

for quote, author in zip(quotes2, authors):                             #a nested for loop to print the text of the quote, then the author name next to it
    print(f"\n{quote.text} - {author.text}")
