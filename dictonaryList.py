# 1
# from pickle import APPEND


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

z[0]['x'] = 15
print(z)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory['soccer'].append('Andres')
print(sports_directory)

print("__________________________________")

# 2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(lists):
    for i in lists:
        for key in i:
            print(key, i[key])
iterateDictionary(students)


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

print("__________________________________")

# 3
players = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name':'Tonel'}
]

def iterateDictionary2(key, players):
    for listitem in players:
        print(listitem[key])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# First Names
# Michael
# John
# Mark
# KB
# Last Names
# Jordan
# Rosales
# Guillen
# Tonel

print("__________________________________")

# 4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
} 

#  def printInfo (some_dict):
#     for key,a in some_dict.items():
#         print(key.upper(),len(a))
#         for var in some_dict[key]:
#              print(f"{var} " )

# printInfo(dojo)

def printInfo(dic):
    for items,a in dic.items():
        print(items.upper(),len(a))
        for loctaions in dic[items]:
            print(f"{loctaions}")

printInfo(dojo)

# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

