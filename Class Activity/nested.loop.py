#Nested loop
a= [2,3,4]
b=[5,6,7]
for c in a:
    for d in b:
        print (c,d)

# Another Example 

for a in range (2):   # 0,1,
    
      for b in range(3) :  #0,1,2
             print("outer loop" ,a , "Inner Loop", b)