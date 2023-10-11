import random

w = ['rock','paper','scissors']
print('welcome to rock paper scissors 1.0')
print('''available choices are
1 = rock 
2 = paper 
3 = scissors      ''')
customer = input("enter your choice = ")
cpu = random.choice(w)
print('CPU CHOOSE ',cpu)
if customer == cpu :
    print('draw')
else :
    if customer == 'rock' and cpu == 'scissors':
        print('you win')
    if customer == 'scissors' and cpu == 'rock':
        print('you loose')
    if customer == 'scissors' and cpu == 'paper':
        print('you win')
    if customer == 'paper' and cpu == 'scissors':
        print('you loose')
    if customer == 'paper' and cpu == 'rock':
        print('you win')
    if customer == 'rock' and cpu == 'paper':
        print('you loose') 

  