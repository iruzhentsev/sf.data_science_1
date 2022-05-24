"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) #guess the number

#count of attempts
count = 0
while True:
    count+=1
    predict_number = int(input ("Guess number from 1 to 100: "))
    
    if predict_number > number:
        print("The number must be less!")
    elif predict_number < number:
        print("The number must be higher")
    
    else:
        print(f"You are guessed right! This is = {number}, in {count} attempts")
        break # end of the game