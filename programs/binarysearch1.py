# first find the first letter..
# open any page and see the letter on it. ("google") - > start with "g"
#   if the open page has a letter greater than "g"
#         then we check the pages before that
#         else we check the pages after that

# Algorithm
# -----------
# Input:
#    (Ordered) List of something - aList
#    Something you are trying to find - item
# Output:
#   The position of the item we are looking for.
#    or -1 (not there)

# left = 0
# right = len(list) - 1
# mid = (left + right) // 2
# if aList[mid] == item -> then print mid
# if not
#    if aList[mid] > item -> then right = mid - 1
#    else left = mid + 1


aList = []
for _ in range(10):
    aList.append( input("enter a string: ") )
    
aList = sorted(aList)


item = input("enter a string to search: ")

print(aList)

    
### Binary search algorithm starts here
left = 0
right = len(aList) - 1

while left < right:
    
    mid = (left + right) // 2
    
    if aList[mid] == item:
        print("Found the string. It is at position " + str(mid))
        break
    
    if aList[mid] > item:
        right = mid - 1
    else:
        left = mid + 1
        
        
if aList[mid] != item:
    print("Not found")
        
        

        
        








