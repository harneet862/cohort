# float and int for numbers 

x = 3 
print(type(x)) #type takes the varible and returns the type 
#Python is dynamically typed language which means no need to declare the type 

print(x)
print(x+1)
print(x-1)
print(x*2)
print(x **2)

x += 1 # adds one to the x equivalent to x= x+1
print(x)
x *= 2
print(x) # automatically adds the new line character
y = 2.5
print(type(y))
print(y, y+1, y*2, y**2) #adds the space by itself 

# booleans : True or False
t = True
f = False
print(type(t))
print(t and f)
print(t or f)
print(not t)
print( t != f) # this is true since they are not equal
print( t == f) # this is false since they are not equal


#Strings  (a class or an object)
hello = "hello0"
world = 'world' # double quote or single quote is the same here
print(hello)
print("hello")
print(len(hello))
hw = "hello" + ' ' + "world" # string concatenation
dw = "hello" + "world"
print(hw)
print(dw) # Nos space added automatically 
hw12 = "%s %s %d" % (hello, world, 12) #sprintf style string formatting 
new_hw12 = f'{hello} {world} {12}' #fprintf stype string formatting 
print(hw12)
print(new_hw12)

# Functions with the strings

s = "hello"
print(s.capitalize()) #captalise the first word of string
print(s.upper()) #capatilise the whole string
print(s.rjust(7)) 
print(s.center(7))
print(s.ljust(7))
print(s.replace('l', '(ell)'))
print('   world'.strip()) #removes the spaces from the right and the left hand side 

# List or array

xs = [3,1,2] # can take different types of datas
print(xs , xs[2])
print(xs[-1]) # prints the last element
xs[2] = "foo"
print(xs)
xs.append('bar') #changes the list directly
x = xs.append('fooo')
print(xs)
print(x)
xs.pop()
print(xs) 
#Check these

nums = list(range(5))
print(nums)
print(nums[2:4]) # the last element is exculusive that means it is not included
print(nums[2:])
print(nums[:2])
print(nums[:]) #whole list
print(nums[:-1]) # last element is not included
nums[2:4] = [8,9]
print(nums)
copy = nums # it creates a shallow copy means any change to the original changes the actual copy as well
copy[0] = 12 #one of the option to get around this is to use nums[:]
print(nums)
# Ask this 
copy2 = nums[:]
copy2 = nums
copy2[0] = 13
print(nums)


# Loops 
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal) # python is based on indentation

for idx, animal in enumerate(animals):
    print('# %d : %s'% (idx+1 , animal))

squares = [x**2 for x in nums]
print(squares)

#square[len(nums)]
#for i in nums:
 #   nums[i] = nums[i] * nums[i]

#dictionaries
d = {'cat':'cute', 'dog':'furry'}
#Dictionaries are more efficient with the list because they use hash algorithms i.e O(1)
print(d['cat'])
# to avoid the keyerror if the key doesnot exist we use get function

# check what is a set 
# Check what is hash map algorithm





