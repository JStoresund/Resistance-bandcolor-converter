#Resistance-color converter

resistorColors = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Grey", "White"]
allColors = ["Silver", "Gold","Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Grey", "White"]

suffixes = ["m", "Null", "k", "M"]
            #-3    0      3    6 

resistance = input("What's the resistance? ")

if resistance[-1] in suffixes:
    resistance = int(resistance[:-1]) * (10**((suffixes.index(resistance[-1])-1)*3))
else:
    resistance = float(resistance)

def findMultiplier(x, upperLim, lowerLim):
    a=0
    if x>upperLim:
        while x>=upperLim:
            x/=10
            a+=1
    elif x<lowerLim:
        while x<=lowerLim:
            x*=10
            a-=1
    return a

lastColor4 = findMultiplier(resistance, 1000, 1)
lastColor3 = findMultiplier(resistance, 100, 1)

if resistance<0.01:
    colors4=[]
    colors3=[]
    print("Resistance too low")
elif resistance<0.1:
    colors4 = ["Black", "Black", resistorColors[int(str(round(resistance, 2))[-1])]]
    colors3 = ["Black", resistorColors[int(str(round(resistance, 2))[-1])]]
elif resistance<1:
    colors4 = ["Black", "Black", resistorColors[int(str(round(resistance, 1))[-1])]]
    colors3 = ["Black", resistorColors[int(str(round(resistance, 1))[-1])]]
elif round(resistance)<10:
    colors4 = ["Black", "Black", resistorColors[round(resistance)]]
    colors3 = ["Black", resistorColors[round(resistance)]]
elif round(resistance)<100:
    colors4 = ["Black", resistorColors[int(str(round(resistance))[0])], resistorColors[int(str(round(resistance))[1])]]
    colors3 = [resistorColors[int(str(round(resistance))[0])], resistorColors[int(str(round(resistance))[1])]]
else:
    newResistance=resistance/(10**lastColor4)
    colors4 = []
    colors3 = []
    for i in range(3):
        colors4.append(resistorColors[int(str(newResistance)[i])])
    for i in range(2):
        colors3.append(resistorColors[int(str(newResistance)[i])])

colors4.append(allColors[lastColor4 + 2])
colors3.append(allColors[lastColor3 + 2])

print(*colors4) #Color code with 4 bands
print(*colors3) #Color code with 3 bands
