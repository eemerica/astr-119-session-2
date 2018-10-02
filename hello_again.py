#! usr/bin/env python3
import numpy as np #Includes the numpy library

def main():#Defines a function named main that does not currently take arguments
	i=0 #declare i, initialize to integer 0
	x=119.0
	for i in range(120): #iterates from 0 to 119 (0 to n-1)
		if((i%2)==0):#if i is even.
			x+=3.0#add 3 to x
		else:# if i is odd
			x-=5.0 #subtract 5 from x
	s="%3.2e"%x #makes a string s containing the value of x in scientific notation
	print(s) #print s to the screen

#now the rest of the program continues.
if __name__=="__main__": #call main
	main() #run the main function