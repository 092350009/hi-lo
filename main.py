import random
from random import randint


class game:
	
  def __init__(self, balance):
	  self.balance = balance
	  
  
  def roll(self):
    print('🎲 rolling the dice...')
    result = randint(1,6)
    print(f'rolled number:{result}')
    if self.mode == 'hi':
          if result >= 4:
            print('-----You Won!\n10 coin has been added to yourbalanceyourbalance')
            self.balance += 10
          else:
            print('------You Lost\n 10 coin has been deducted')
            self.balance -= 10
    elif self.mode == 'low':
          if result <= 3:
            print('-----You Won!\n10 coin has been added to yourbalanceyourbalance')
            self.balance += 10
            
          else:
            print('------You Lost\n 10 coin has been deducted')
            self.balance -=10
  def hi(self):
    print(f'Game bet mode changed to high')
    self.mode = 'hi'
  def low(self):
    print(f'Game bet mode changed to Low')
    self.mode = 'low'
  def bal(self):
    print(f'you\'re remaining balance : {self.balance}')

balance = 100
p = game(balance)

print("             W E L C O M E  TO  H I G H - L O W  G A M E.")
print('  ')
print('∆ Enter 1 to see rules of the game ')
while True:
  try:
    x = int(input('Enter your choice number :    '))
    if x == 1:
      print('this is a high or low game the rules are simple\nfirst start the game by setting bet mode(choosing high or low)\nif you bet high and rolled the dice then if your dice outcome is 4,5,6 you will win if other numbers come you will lose \nby losing we will deduct 10 coin from your balance and we will add 10 coins if you win\n     GOOD LUCK $ ')
      print('these are the commands listed below\n-1 for reading rules\n-2 for setting bet mode\n-3 for rolling the dice')
    elif x == 2:
      new = int(input(' H I G H  O R  L O W ? \nEnter 1 for High 2 for Low.'))
      if new == 1:
        p.hi()
      elif new == 2:
        p.low()
    elif x == 3:
       p.roll()
    elif x == 4:
       p.bal()
  except:
      pass
      
  
      
      
      
      
    
    
  


	
