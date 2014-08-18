'''
Created on Feb 16, 2014

@author: The Queen
'''

def read_file(file_name, mode):
    file1 = open(file_name,mode)
    text = file1.read()
    file1.close()
    
    return text


FILE_ADDRESSES = 'files\\'