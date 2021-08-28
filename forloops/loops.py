for num in range(1000):
    if num %2 == 0: #this will give me numbers that are even only. %2 is modulus 2. 0 represents that there is no remainder, thus telling me it's an even number
        if num %33 == 0: # first we want an even number, then we want that number to only be divisible by X
            print(num)
