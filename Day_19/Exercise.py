## Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melina_trump_speech.txt file and count number of lines and words
def read_text(directory):
    with open(directory,'r') as f:
        line = f.readlines()
        no_lines = len(line)
        print('Number of lines are:',no_lines)
        words = f.split()
        no_words = len(words)
        print(f'There are {no_words} words in this text')
        
read_text('obama_speech.txt')

read_text('michelle_obama_speech.txt')

read_text('donald_speech.txt')

read_text('melina_trump_speech.txt')


# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def read_json(directory,n):
    with open(directory, 'r', encoding='utf-8') as f:
        countries_dict = json.loads(f)
        for key in countries_dict:
            if key == 'languages':
                spoken_languages = countries_dict[key]
                most_spoken = sorted(spoken_languages.items(),key = lambda x:x[1],reverse=True)[:n]
                print('The most spoken languages are:',most_spoken)

read_json('countries_data.json','language')


# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated 
# countries

def most_populated_countries (filename,n):
    with open(filename) as f:
        data = json.load(f)


    countries = []

    for countries_data in data:
        name = country_data['name']
        population = country_data['population']
        countries.append((name,population))

    sorted_countries = sorted(countries, key=lambda x: x[1], reverse = True)
    top_countries = [country[0] for country in sorted_countries[:n]]

    return top_countries


print(most_populated_countries(filename='./data/countries_data.json', n=10))
    

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.

with open('email_exchange_big.txt','r') as f:
    lines = f.readlines()
    email =  mails.split()
    email_addresses = []
    for line in lines:
    email_addresses.extend(re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line))
    email_addresses[:]