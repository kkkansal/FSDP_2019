

kunal = input("Enter Numbers").split(",")

kunal = []

for i in kunal:
    kunal.append(int(i))


kunal.sort()


final = kunal[1:-1]


average = sum( final ) / len( final )

print ("Average is :", int( average ))
