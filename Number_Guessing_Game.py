###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random

# a = ['2', '4', '6']
# b = ['4', '5', '6']
# print(a[2])
# print(b[1])

# for x in b:
#     if x == a[2]:
#         print('YAY')
#     else:
#         print('NAY')

# Generating a random number #
digits = list(range(10))
random.shuffle(digits)
new_digits = digits[:3]
print(new_digits)

match_count = 0
close_count = 0

guess_str = input("What is your guess?\n")
# print(guess)
guess_lst = list(guess_str)
for a in range(0,len(guess_lst)):
    guess_lst[a] = int(guess_lst[a])
print(guess_lst)

for x in range(0,len(guess_lst)):
    if guess_lst[x] == new_digits[x]:
        #print ('Match')
        match_count +=1
    elif guess_lst[x] == new_digits[(x-1)%3] or guess_lst[x] == new_digits[(x+1)%3]:
        #print('Close')
        close_count +=1

if match_count == 3:
    print('Congratulations!')
else:
    print(f'You have {match_count} match(es) and {close_count} close guess(es)')



# for x in range(0,len(guess_lst)):
#     if guess_lst[x] == new_digits[x]:
#         print ('Match')
#     elif guess_lst[x] == new_digits[(x-1)%3] or guess_lst[x] == new_digits[(x+1)%3]:
#         print('Close')
#     else:
#         print('Nope')

    
# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
