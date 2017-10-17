"""
The CVS file Missouri_Beer_Wine.cvsPreview the documentView in a new window lists suppliers to the state of Missouri.  Find the 5-digit zip code that holds the most suppliers.  When you see a 9-digit zip code, truncate the last 4 digits.  You can use Google to track down the winning zip code to validate your program.  

Your program should print the number of suppliers in that zip code, and the zip code itself.  
"""

import collections
import sys

def getRightZipCode(zipCode):
    if len(zipCode)>5:
        return zipCode[:5]
    else:
        return zipCode

file="Missouri_Beer__Wine.csv"

if len(sys.argv)==2:
    file=sys.argv[1]

try:
    dict=collections.Counter()
    with open(file,"r")as f:
        f.readline()#read the first line

        for line in f:
            if(line[0]!='"'):
                zipCode=line.split(",")[1]#whole zip code

                zipCode_right=getRightZipCode(zipCode)

                dict[zipCode_right]+=1

            else:
                #get the name ignoring the first comma
                endPos=line.find('"',1)
                name=line[0:endPos]
                line=line.replace(name,"")
                zipCode=line.split(",")[1]# whole zip code

                zipCode_right=getRightZipCode(zipCode)

                dict[zipCode_right] += 1

    for i,key in enumerate(sorted(dict,key=dict.get,reverse=True)):
        if(i!=5):
            print("{0}: {1} {2}".format(i+1,dict[key],key))
        else:
            break
except FileNotFoundError:
    print("File not found")

except:# hopefully it wont get here
    print("Something went wrong, Please call the development team")
