#*******************************************
#Hole Counter
#Caleb Bell
#Version 1.0
#This script is designed to count the number of holes from 0 -100,000
#1/28/2017
#
#*******************************************



def hasHole():
    num =""
    if num.find(num,'0') or num.find(num,'4') or num.find(num,'6') or num.find(num,'8') or num.find(num,'9'):
        return True
    else:
        return False

test = '1'   
print(test.hasHole())