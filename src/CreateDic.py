'''
Created on Feb 14, 2014

@author: The Queen
'''
import re;
from Util import read_file, FILE_ADDRESSES

def create_dic():
    all_names = open((FILE_ADDRESSES + 'all_names.txt'), 'a')
    # clear the file if it is has values from previous tests
    all_names.truncate()
    
    # for each year read names and write them to a file
    for num in range(2000, 2013):
        file_name = FILE_ADDRESSES + 'Popular Baby Names ' + str(num) + '.htm'
        text = read_file(file_name, 'rU')
        
        # no number and a word: name
        names = re.findall('<td>[^\d*]\w*</td>', text)
        # just a number: rank
        ranks = re.findall('<td>\d*</td>', text)
        
        # create a dictionary object from values
        names_with_ranks = {}
        
        # there are both girls and boys names in one file, so for every two name we increase the rank number
        i = 0
        for index in range(len(names)):
            names_with_ranks[re.search('[^<td>]\w+', names[index]).group()] = re.search('[^<td>]\d*', ranks[i]).group()
            if (index % 2 == 1):
                i+=1
        fill_dic(names_with_ranks, all_names)
    all_names.close()

def fill_dic(names_with_ranks, file_object):
    # write names and their ranks to file
    for name in names_with_ranks:
        file_object.write(name + '\t' + names_with_ranks[name] + '\n')
    