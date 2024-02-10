largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
    
print("After", largest_so_far)

#count loop
count = 0
print("Before", count)
for thing in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    print(count, thing)
print("After", count)

#summing loop

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print("After", zork)

#Average in a loop

count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum/count)

#Filtering
print("Before")
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20 :
        print("Large number", value)
print("After")

#Boolean

found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3:
        found = True
    print(found, value)
print("After", found)

#lowest
smallest_so_far = None
print("Before")
for value in [9, 41, 12, 3, 74, 15] :
    if smallest_so_far is None :
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value
    print(smallest_so_far, value)
    
print("After", smallest_so_far)

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try :
        numb = int(num)
    except :
        print("Invalid input")
        continue
    if largest is None :
        largest = numb
    elif numb > largest :
        largest = numb   
    elif smallest is None :
        smallest = numb
    elif numb < smallest :
        smallest = numb       
    
print("Maximum is", largest)
print("Minimum is", smallest)