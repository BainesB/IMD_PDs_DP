# Write some code that open all the in the directors directory and dump the production titles and the company name in a dict.

# list of the text files that contain production titles. 

titles = [
        '../directors/AtlanticProductionsDirrectors.txt', 
        '../directors/PioneerDirectors.txt',
        '../directors/DSP_Dirrectors.txt',
        '../directors/SmallCompanyDirrectors.txt',
        ]

Just_titles = []

def printlines(filename):
    f = open(filename, 'r')

    contents = f.readlines()

    count = 0
    for i in contents:
        if 'Title' in i:

            # Get the dirrectors name. 

            string = i
            parts = string.split('Title:')
            name_thing = parts[1].split('Director')
            name = name_thing[1].split(':')
            name_thingy = name_thing[1].split(':')
            name = name_thingy[1].split('ProdDate')
            #print(name[0],name_thing[0])

            # Get the Production name. ## This is what we need. 
            # stick them in a list. 
            if name_thing[0] not in Just_titles:
                Just_titles.append(name_thing[0])

            count += 1

    f.close()


for i in titles:
    printlines(i)




print('List_of_titles = [')

for i in Just_titles:
    print('\t"'+i+'",')

print(']')





'''
# this has the steps for extracting the names. 




string = '2 Title:  Apollo 11: The Untold Story  Director:  Tom Whitter  ProdDate: 2006 TV Movie'
>>> print(string)
2 Title:  Apollo 11: The Untold Story  Director:  Tom Whitter  ProdDate: 2006 TV Movie
>>> string.split('Title')
['2 ', ':  Apollo 11: The Untold Story  Director:  Tom Whitter  ProdDate: 2006 TV Movie']
>>> parts = string.split('Title')
>>> parts
['2 ', ':  Apollo 11: The Untold Story  Director:  Tom Whitter  ProdDate: 2006 TV Movie']
>>> name_thing = parts[1].split('Director')
>>> name_thing
[':  Apollo 11: The Untold Story  ', ':  Tom Whitter  ProdDate: 2006 TV Movie']
>>> name = name_thing.split(':')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'split'
>>> name = name_thing[1].split(':')
>>> name
['', '  Tom Whitter  ProdDate', ' 2006 TV Movie']
>>> name_thingy = name_thing[1].split(':')
>>> name_thingy
['', '  Tom Whitter  ProdDate', ' 2006 TV Movie']
>>> name = name_thingy[1].split('ProdDate')
>>> name
['  Tom Whitter  ', '']
>>> name[0]
'  Tom Whitter  '


'''

