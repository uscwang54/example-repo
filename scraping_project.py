# scrape all the information from http://quotes.toscrape.com
import requests
import bs4
import random

url = "http://quotes.toscrape.com"

authors = []
quotes = []
abouts = []

while True:

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    author_class = soup.select(".author")
    author = [author_class[i].get_text() for i in range(len(author_class))]
    authors.extend(author)

    quote_class = soup.select(".text")
    quote = [quote_class[i].get_text() for i in range(len(quote_class))]
    quotes.extend(quote)

    about_href = soup.select("span a")
    about = ["http://quotes.toscrape.com"+about_href[i]['href'] for i in range(len(author_class))]
    abouts.extend(about)

    next = soup.select(".next a")

    if next==[]:
        break

    url = "http://quotes.toscrape.com"+next[0]['href']

all_quotes = []
for i in range(len(quotes)):
    quote_dict = {"author":authors[i], "quote":quotes[i], "about":abouts[i]}
    all_quotes.append(quote_dict)

##################################################################################

while True:

    print("Welcome to the quote guessing game!")
    print("\n")

    random_quote = random.choice(all_quotes)
    quote_text = random_quote['quote']
    print(quote_text)

    count = 0
    while count<3:

        user_guess = input("Guess who said this? ")

        if user_guess == random_quote["author"]: # user gets correct guess
            print("congrats! Your guess is correct.")
            break

        else: # user gets wrong guess
            count+=1 # every time user gets wrong guess, count +1

            if count==1: # initial guess wrong, first time hint
                print("Wrong. Try again.")
                res = requests.get(random_quote["about"])
                soup = bs4.BeautifulSoup(res.text, 'lxml')
                born_date = soup.select(".author-born-date")[0].get_text()
                born_location = soup.select(".author-born-location")[0].get_text()
                print("Here is a hint: The author was born on "+born_date+" "+born_location)

            elif count==2: # initial and 2nd guesses wrong, 2nd time hint
                print("Wrong. Try again.")
                res = requests.get(random_quote["about"])
                soup = bs4.BeautifulSoup(res.text, "lxml")
                first_name = soup.select(".author-title")[0].get_text().split()[0]
                print("Here is another hint: The author's first name is "+first_name)

            else : # initial, 1st and 2nd guesses wrong. Game over!
                print("Wrong.")
                res = requests.get(random_quote["about"])
                soup = bs4.BeautifulSoup(res.text, "lxml")
                description = soup.select(".author-description")[0].get_text()
                print("The author's description is: \n"+description)
                print('\n')
                user_input = input('Do you want to play again (y or n)? ')

    if user_input.lower()[0] == 'y':
        continue

    else:
        break
