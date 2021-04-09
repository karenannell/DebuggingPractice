#Task: print any elements that occur 3 consecutive times in a list.

arr = [1, 1, 1, 64, 23, 64, 22, 22, 22] #missing arr variable
  
size = len(arr) #should be len not length
  
for i in range(size - 2): 
    if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]: #if statement should be here, not before size; should be "and" not &
        print(arr[i])
