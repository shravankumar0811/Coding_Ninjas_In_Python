##Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.



# Read input as sepcified in the question
# Print output as specified in the question

## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
##      print(val1, " ", val2)
import math
s=int(input())
e=int(input())
w=int(input())
for i in range(s,e+1,w):
    c=((i-32)*5)/9
    if c>0:
        x=math.floor(c)
    else:
        x=math.ceil(c)
    print(i,x,sep='\t')
