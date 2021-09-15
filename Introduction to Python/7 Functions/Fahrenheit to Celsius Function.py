##Fahrenheit to Celsius Function
##Send Feedback
##Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
##Input Format :
##3 integers - S, E and W respectively
##Output Format :
##Fahrenheit to Celsius conversion table. One line for every Fahrenheit and Celsius Fahrenheit value. Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")



import math
def printTable(s,e,w):
    for i in range(s,e+1,w):
        c=((i-32)*5)/9
        if c>0:
            x=math.floor(c)
        else:
            x=math.ceil(c)
        print(i,x,sep='\t')
	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)





