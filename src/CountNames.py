'''
Created on Feb 16, 2014

@author: The Queen
'''
from Util import read_file, FILE_ADDRESSES
# from string import split
import re;

def count_names(name):
    text = read_file(FILE_ADDRESSES + 'all_names.txt', 'rU')
    
    ranks = []
    
    m = re.findall('(' + name + ')\t(\d+)', text, re.IGNORECASE)
#     print m
    for name in m:
        ranks.append(name[1])
#     print ranks
    
    names_with_count = (str(len(m)), ranks)
        
#         counted_names.append(name)
        
    return names_with_count