'''
Created on Feb 15, 2014

@author: The Queen
'''
from CreateDic import create_dic
from CountNames import count_names

# create preliminary file containing names and their ranks 
create_dic()

# get a name from user
name = raw_input('Enter a name: ')

# find how many time this name has been selected by parents
names_count = count_names(name)
print name + ' occurred ' + names_count[0] + ' times with ranks\n' + str(names_count[1]) + ' \nautomatically sorted by year'