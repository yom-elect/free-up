# classs

'''(n) = int (input ())
(i)= 1
result = 1
for i in range (0,10):
    i += 1
    result = [ n*i  for i in range(0,11)]
   

    print (f"{n} * {i} = {result[i]}") '''
class User:
    def __init__(self,first ,last,age):
        self.first = first
        self.last  = last
        self.age = age


    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]} {self.last[0]}"
    
    def likees(self, thing):
        return f"{self.first} likes {thing}"

user1 = User ("mum","kofo","47")
user2 =  User ("Ayo" ,"Lola", "24")

print (user1.likees("icee"))
print (user2.likees("love"))
