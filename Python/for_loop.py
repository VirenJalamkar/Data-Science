x=0
y="spiderman"

for a in y:
    print(a)
#-----------------------------------
x=0
c="ironman"

for b in c:
    print(b,end="")
print()
#-----------------------------------
names = ["spiderman", "thor", "halk"]

for index, name in enumerate(names):
    print(index, name)
#-------------------------------------
names = ["spiderman","ironman", "thor", "halk"]

for name in names:
    if name == "ironman":
        break

    print(name)