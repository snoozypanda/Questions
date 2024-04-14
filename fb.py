a_z = 'abcdefghijklmnopqrstuvwxyz'
pasw = 'dog'
tests = 0
guess = ''
azlen = len(a_z)

for i in range(azlen):
    for j in range(azlen):
        for k in range(azlen):
            guess = a_z[i] + a_z[j] + a_z[k]
            tests += 1
            if guess == pasw:
                print('Got "{}" after {} tests'.format(guess, str(tests)))
                break

input()
import string
import itertools

for possible_password in itertools.permutations(string.ascii_letters, 3): 
    print(possible_password)
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def brute_force_guesser(target, guess = '', counter = 0):
    if len(guess) == len(target):
        counter += 1
        if guess == target:
            print('Got "{}" after {} tests'.format(guess, str(counter)))
            return True, counter
        return False, counter
    else:
        for c in ALPHABET:
            target_found, counter = brute_force_guesser(target, guess + c, counter)
            if target_found:
                return True, counter
        return False, counter    
    import math
    global guess

pasw = str(input('Input password: '))
chars = 'abcdefghijklmnopqrstuvwxyz' #only limeted myself to lowercase for simplllicity.
base = len(chars)+1

def cracker(pasw):
    guess = ''
    tests = 1
    c = 0
    m = 0

    while True:
        y = tests
        while True:
            c = y % base
            m = math.floor((y - c) / base)
            y = m
            guess = chars[(c - 1)] + guess
            print(guess)
            if m == 0:
                break

        if guess == pasw:
            print('Got "{}" after {} tests'.format(guess, str(tests)))
            break
        else:
            tests += 1
            guess = ''


cracker(pasw)
input()    