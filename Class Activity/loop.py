#loops are used to print a lengthy list of numbers using a tiny code.

#exmaple
i = 1
while i<10:
 print (i)
i +=1 #i=i+1
 # and you may use a dot comma or space to appear between the numbers if you wish to print them on a single line by using print(x,end=","). 

#example 2 
count = 2
while count <= 5:
    print("Count is:", count)
    count += 1

# Making use of the range Use the for loop to function
for x in range(0,15):
      print (x)

for x in range(10):
     print (x)

#Nested Loops  -- A loop withon a loop


#Nested loop
a= [1,2,3]
b=[4,5,6]
for c in a:
    for d in b:
        print (c,d)

# Another Example 

for a in range (2):   # 0,1,
    
      for b in range(3) :  #0,1,2
             print("outer loop" ,a , "Inner Loop",b)