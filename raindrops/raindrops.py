RAINDROPS = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

def raindrops(number):
    output = "".join([string for factor, string in RAINDROPS.items() if number % factor == 0])
    return output or str(number)