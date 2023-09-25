from mpmath import mp

decimals = input('How many decimal places: ')

# You can change this if you have a good processor
MAX_decimals = 100000 # DEFAULT: 100000

if decimals.isdigit() == False:
    print('The input is not a valid digit.')
    input()
else:
    mp.dps = int(decimals) + 1
    if mp.dps - 1 > MAX_decimals:
        print('Only 100000 decimal digits can be printed.')
        input()
    else:
        print(mp.pi)
        input()
