# 1 
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filters = [num for num in numbers if num <= 0]
print(filters)

# 2 
# Flatten the following list of lists of lists to a one dimensional list 
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list=[ mat for row in list_of_lists for num in row for mat in num ]
print(flatten_list)



# 3 Using list comprehension create the following list of tuples
list_of_tuples=[(i, i**0, i, i*i,i*i*i, i*i*i*i, i*i*i*i*i) for i in range(11)]
for tup in list_of_tuples:
    print(tup)


## 4 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened = [[y[0].upper(), y[0][:3].upper(), y[1].upper()] for x in countries for y in x ]
print(flattened)


# 5
# Change the following list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict=[{"country":y[0].upper(), "city":y[1].upper()}for x in countries for y in x]
print(countries_dict)

## 6
## Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_con=[" ".join(y) for x in names for y in x]
print(names_con)

# 8
# Write a lambda function which can solve a slope or y-intercept of linear functions
slope= lambda x_1,x_2,y_1,y_2: (y_2-y_1)/(x_2-x_1)