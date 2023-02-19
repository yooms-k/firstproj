import time as t

kickstarter = input("Wanna start my super duper awesome speech? ")
speech = '''Heyyy, 
it's been a while since i last coded... well this is my restart coding project!! 
There's plenty of coding concepts that I had already forgotten but I'll try my best to relearn it! 
Don't worry everyone I'll be back to tip-top condition in a few days! 
Keep calm and await my comeback. 

signing off, 
yooms '''

for i in speech:
    print(i, end="")
    t.sleep(0.09)