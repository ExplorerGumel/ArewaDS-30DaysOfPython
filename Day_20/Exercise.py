#Read this url and find the 10 most frequent words.
#romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

import requests
import re
from collections import Counter

response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
text = response.text

words = re.findall('\b\w+\b', text, re.I)
word_counts = Counter(words)

for word, count in word_counts.most_common(10):
    print(word, count)



#Read the countries API and find
#    the 10 largest countries
#    the 10 most spoken languages
#    the total number of languages in the countries API
import requests

response = requests.get("https://restcountries.eu/rest/v2/all")
data = response.json()

largest_countries = sorted(data, key=lambda x: x['area'], reverse=True)[:10]

for country in largest_countries:
    print(country['name'])

languages = {}

for country in data:
    for language in country['languages']:
        if language['name'] in languages:
            languages[language['name']] += 1
        else:
            languages[language['name']] = 1

most_spoken_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10]

for language, count in most_spoken_languages:
    print(language)

languages = set()

for country in data:
    for language in country['languages']:
        languages.add(language['name'])

print(len(languages))




#UCI is one of the most common places to get data sets for data science and machine learning. 
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional 
# libraries it will be difficult, so you may try it with BeautifulSoup4
import requests
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/ml/datasets.php"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

datasets_table = soup.find_all('table')[5]

for row in datasets_table.find_all('tr')[1:]:
    columns = row.find_all('td')
    dataset_name = columns[0].text.strip()
    dataset_url = "https://archive.ics.uci.edu/ml/" + columns[0].find('a')['href']
    print(dataset_name, dataset_url)
