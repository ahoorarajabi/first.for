'''
for i in range(10, 0, -1):
    print(i)
    if i == 1:
        print('partab')
'''
'''
n=40
for i in range(n):
    print((n-i) * " "+i*" * ")
'''
'''
  *         #2 fasele 1 setare n=3
 * *        #1 fasele 2 setare n=3
* * *       #0 fasele 3 setare n=3
 '''
'''
number=int(input("adade khod ra vared konid:"))
for i in range(11):
    print(f'{number}x{i}={number*i}')
'''
'''
sum=0
number=0
for i in range (101):
    if i % 2==0:
        sum=sum+i
        number=number+1
print(sum)
print(number)
'''
ghabool=0
mardood=0
for i in range(5):
    score=int(input("nomre khod ra vared konid:"))
    if score >=10:
        print(f"shoma ba nomre{score} ghaboold shodid.")
        ghabool=ghabool+1
    else:
        print(f"shoma ba nomre {score}, mardood shodid.")
        mardood=mardood+1
print(f"tedad ghabooli ha{ghabool}, tedad mardoodi ha{mardood}.")