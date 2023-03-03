### 1
import re
paragraph = 'I love teaching . If you do not love teaching what else can you love . I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love .'
splits = re.split(' ',paragraph)
print(splits)
curr_frequency=[]
for i in splits:
    curr_frequency.append(splits.count(i))
for x,y in zip(splits,curr_frequency):
    word_s = (x,y)
    print(tuple(word_s))


### 2

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

num = re.findall("-*\d+", text,re.I)
num = [int(x) for x in num]
print(num)



### 1

import re

pattern = "^[a-zA-Z_][a-zA-Z0-9_]*$"

def is_valid_variable(name):
    return re.match(pattern, name, re.I) is not None

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

sentence = '%I $am@%. a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'

def clean_text(text):
    texts = re.sub('[^a-zA-Z0-9\s]','',text)
    return texts
print(clean_text(sentence))
