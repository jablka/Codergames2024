# Output contains:
# number n, which is minimum number of insertions needed to make array consecutive; 
# following with missing elements in ascending order. 

with open("4 Task Input File.txt") as f:
    arr = f.read()

arr = arr.split(' ')

arr = [int(i) for i in arr if i!='']

minimum = min(arr)
maximum = max(arr)

bag = []
for i in range(minimum,maximum+1):
    if i in arr:
        continue
    else:
        bag.append(i)

print(str(len(bag))+': '+str(bag)[1:-1])
