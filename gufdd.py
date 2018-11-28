from collections import Counter
import statistics
'''d = {'a':2, 'b':4, 'c':10} 
def fun(a, b, c): 
    
    print(a, b, c) 
  
# A call with unpacking of dictionary 

fun(**d)

string1 = input ("insert string1 :")
string2 = input ("insert string2 :")

dict1, dict2 =  Counter(string1), Counter(string2)

keys1, keys2 =  dict1.keys(), dict2.keys()

len1, len2 =  len(keys1) , len(keys2)

set1 = set(keys1)

commmon_keys = len (set1.intersection(keys2))

if commmon_keys ==0 :
    print (len1 + len2 )

else :
    print (max(len1,len2)- commmon_keys)'''


data =  [1,2,4,5,7,7,8]
n = len (data)
mean = 0
for i in range (0, n):
    mean += data[i]
    print (float(mean/n))

if n% 2!= 0 :
    median =  sorted(data)
    print (median[n//2])

elif n % 2 ==0 :
    med =  sorted(data)
    median = ((med[(n-1)//2])+(med[n//2]))//2
    print (median)

print (statistics.mode(data))

''n=int(input())
x=sorted(list(int(i) for i in input().split(" ")))
t=max(x.count(i) for i in x)
print(sum(x)/n)
print((x[len(x)//2]+x[len(x)//2-1])/2)
print(min(i for i in x if x.count(i)==t))



n = int (input())
data =  s'''

import statistics
data =  map(int,input().split())
n =  (input())
mean = 0
for i in range (0, n):
    mean += data[i]
    print ((mean/n))

if n% 2!= 0 :
    median =  sorted(data)
    print (median[n//2])

elif n % 2 ==0 :
    med =  sorted(data)
    median = ((med[(n-1)//2])+(med[n//2]))//2
    print (median)

print (statistics.mode(data))
