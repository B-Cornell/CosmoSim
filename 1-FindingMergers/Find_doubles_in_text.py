#This gets all of the doubles of the descId in the imported text and then prints them and writes them into a text file called Doubles_1e14.txt

import numpy;

#This is a list of all the descIds
descId = numpy.genfromtxt('1e14_as_the_desc_mass_limit.csv', delimiter =',', usecols = (5,));

target = open('Doubles_1e14.txt', 'w')

def repeats():
    fl = 0;
    while fl < 447414 :  #this is the amount of rows in the text to loop through
        tested = fl + 1
    	looped = descId[fl] 
    
    	while tested < 447414:
            if looped == descId[tested]:
                print looped
		target.write(str(looped))
            tested = tested + 1
    
        fl = fl + 1;
    return(1);

repeats()
target.close();



