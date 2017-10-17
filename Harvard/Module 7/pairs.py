import sys
def reverse(word):
    word_Reversed=""
    for charac in word[::-1]:
        word_Reversed+=charac

    return  word_Reversed

dict_words_rever={}
file="words.txt"
if len(sys.argv)==2:#if there is a console input file will be the path
    file= sys.argv[1]

try:

    with open(file,"r") as f:
        for lin in f:
            key=lin[:-1]# get rid of newLine char
            val=reverse(key)
            dict_words_rever[key]=val# fromat key= word val= word_reversed
    dict_done={}
    for word in dict_words_rever:
        if (dict_words_rever[word] in dict_words_rever) and (dict_words_rever[word] not in dict_done): #get rid of dupli
            dict_done[word]= dict_words_rever[word]

    for i,key in enumerate(sorted(dict_done)):
        if(i==10):
            break
        else:
            print("{0}: {1} {2}".format(i+1,key,dict_done[key]))

except FileNotFoundError:
    print("File not found")
    exit(1)
except:
    print("Something went wrong")
    exit(1)

"""""
#another way
list_pairs=[]
for keys in dict_done:
    list_pairs.append(keys+" "+dict_done[keys])

list_pairs.sort()

for i in range(1,11):
    print(str(i)+" "+list_pairs[i])
"""
