#! usr/bin/env python3
import numpy as np
def main():
	i=0 #integers can be declared with a number
	n=10 # also an int
	x=119.0 #floating point nums are declared with a "."
	
	#we can use numpy to declare arrays quickly
	y=np.zeros(n,dtype=float) #declares 10 zeros as floats using np
	#can use for loops to iterate with a variable.
	for i in range(n):
		y[i]=2.0 * float(i) + 1.0 #set y=2i+1 as floats
	#or we can also simply iterate through a variable.
	#print(y)
	for y_element in y:
		print(y_element)
#execute the main function
if __name__=="__main__":
	main()