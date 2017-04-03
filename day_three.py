#following line is to get the input
import sys
N = int(input().strip()) #since this is supposed to be number, I need to change it to integer
if N%2 == 1:
    print("Weird")
elif 2<= N <=5:
    print("Not Weird")
elif 6<= N <=20:
    print("Weird")
else:
    print("Not Weird")
