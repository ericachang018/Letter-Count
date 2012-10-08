from sys import argv
#from os.path import 

script, filename = argv 
#python lettercount.py twain.txt

#opens the .txt file as a file object
txt = open(filename) 
#creates a string of texts by calling read() on txt 
filetext = txt.read()

#create an empty list that will eventually be of length 256
#1st we want to convert all the letters to numbers 0 - 255 (unicode) 
#2nd we want variables for each unicode number and have it increment by one each time it is read. 
# each position in the list corresponds to a unique character
# so in the loop, for each char, we will increment ls[position] that corresponds to the char by 1

#string.lower() returns a lowercase version of string
twain_lower=filetext.lower()

#initialize a list containing 26 zeros
chr_list = [0]*26

for char in twain_lower:
    uni = ord(char) 
    #if the unicode is between 97 and 122, corresponding to 'a' to 'z'
    # and we want to convert the unicode from 97 -122 to a list position of [0-25]
    # given uni that ranges from 97 to 122, we want to convert 97 to 0 and 122 to 25, by 
    # subtracting 97 from each uni
    #then we want to update the value in the list char_list by 1 for the corresponding position
    if ((uni >=97) and (uni <= 122)): 
        chr_list[uni-97] = chr_list[uni-97] + 1

#print chr_list


for letter in chr_list: 
    print letter 
