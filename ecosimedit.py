file = open('EcoSim.eco','r')
x = 0
count = 0

for o in file:
    count = count+1    
ecosimlist = [0]*count

file.close()
file = open('EcoSim.eco','r')

for i in file:
    ecosimlist[x] = i
    x = x+1
    
file.close()


#Program to iterate through the file
#print("Please enter a line to read")

num = input("Please enter a line from 1 to "+str(count)+" to read\n")

try:
    int(num)
except ValueError:
    print("Please enter a number")
print("line "+num+" In the file is: \n")

print(ecosimlist[int(num)])
