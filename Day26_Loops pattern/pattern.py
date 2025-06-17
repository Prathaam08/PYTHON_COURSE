'''
Q1 :

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

'''

for i in range (1 , 6):
    for j in range(1 , 6):
        print('*', end = ' ')
    print()

print()

'''
Q2 :

*
* *
* * *
* * * *
* * * * *

'''

for i in range( 1 , 6):
    for j in range( 1 , i + 1):
        print("*" , end = " ")
    print()
print()

'''
Q3 :

* * * * *
* * * *
* * *
* *
*

'''

for i in range( 5 , 0 , -1):
    for j in range(  i ):
        print("*" , end = ' ')
    print()
print()

'''
Q4 :

1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

'''

for i in range( 1 , 6 ):
    for j in range ( 1 , i+1):
        print(j , end = " ")
    print()
print()

'''
Q5 :

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

'''

for i in range(5 , 0 , -1):
    for j in range(i , 0 , -1):
        print(j , end = " ")
    print()
print()

'''
Q6 :

        *   
      * * *  
    * * * * *  
  * * * * * * * 
* * * * * * * * *

'''
rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print("  ", end="")  
    
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()
