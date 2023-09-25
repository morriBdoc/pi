from mpmath import mp

decimals = input('How many decimal places: ')

if decimals.isdigit() == False:
    print('The input is not a valid digit.')
    input()
else:
    mp.dps = int(decimals) + 1
    if mp.dps - 1 > 100000:
        print('Only 100000 decimal digits can be printed.')
        input()
    else:
        print(mp.pi)
        input()