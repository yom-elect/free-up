'''time = [1,4,5,6,7,8,8,5]
time1 = [(tom*3) for tom in time]
print (time1)
name  = "house"
live = [noun.upper() for noun in name]
print ()

boxes = [1,2,4,0,5,5,0,45,]
nnew = [str(box)for box in boxes]
print(nnew)

numbers = [2,3,4,5]
pie = [num *2 if num % 2 == 0  else num/2 for num in numbers]
bic = pie[2:]
print(bic)

hot = "am tired but going to push through!!!!"
cold = ' '.join(char for char in hot if char not in "aslum")
print (cold)

for nums in nested:
    for ind in nums:
        print (ind)..
nested = [[1,2,3],[2,4,6],[3,6,9]]
bic = [[print val for val in l] for l in nested]
print (bic

board = [[num for num in range(1,4)]for val in range(1,4)]
print (board)'''

words = [["x" if num % 2 !=0 else "o" for num in range(1,4)] for val in range (1,4)]

your = [["gg" for vir in [1,2,3,4]] for vin in range(1,5)]
print (your)
