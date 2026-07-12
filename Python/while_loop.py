x = 0
y = "spiderman"

while x < len(y):
    if y[x] == "i":
        x += 1
        continue

    print(y[x])
    x += 1
#----------------------------------------------------------------
x = 0
y = "ironman"

while x < len(y):
    if y[x] == "o":
        x += 1
        break
    print("value of x:", y[x])
    x += 1

#-----------------------------------------------------------------
x = 0
y = "Thor"

while x < len(y):
    if y[x] == "o":
        x += 1
        pass
    print("value of x:", y[x])
    x += 1

#-----------------------------------------------------------------
x=0
y=["spiderman","ironman","halk","Thor","captainamerica"]

while x < len(y):
    if y[x]== "tushar" :
       x+=1
       continue
    print("value of x:",y[x])
    x+=1
