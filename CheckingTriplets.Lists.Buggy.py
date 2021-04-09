#Task: print any elements that occur 3 consecutive times in a list.

arr = [1,1,1,64,22,33,33,33,70]

size = len(arr) 
  
for i in range(size - 2):
        if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
                print(arr[i])


#There are 4 bugs in this code! I've found: 1,2,3

