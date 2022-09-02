# Basic - Print all integers from 0 to 150.
for i in range(0,151):
    print(i)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for x in range(5,1005,5):
    print(x)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for way in range(1,101):
    if way % 5 == 0:
        print("Coding")
    if way % 10 == 0:
        print("Coding Dojo")

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

count = 0
for pop in range(0,500001):
    if pop % 2 != 0:
        count += pop
print(count)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for w in range(2018,0,-4):
    print(w)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
print("Flex Counter")

mult = 3
lowNum = 2
highNum = 9

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)

# while count <= 5:
#     print("Looping - ", count)
#     count += 1