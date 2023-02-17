"""
COMPUTER APPLICATIONS IN CIVIL ENGINEERING CE 257
ASSIGNMENT THREE
Program made by 6942221
        My Github Link ( https://github.com/FBNarh )
"""
import numpy as np
#Along the x direction
L = 12      #Length of beam in meters (m)
w = 10      #Load intensity in (kN/m)

#Question a
'''
    Bending moment(M) and shear force(V) at the end x=0
'''
x = 0
M = (w*(-6*x**2 + 6*L*x-L**2))/12       #Bending moment expression
V = w*((L/2) - x)                       #Shear force expression

a1 = 'The bending moment at the end x=0 is '
a2 = 'the shear force at the end x=0 is '

print()
print('(a.i) ' + a1 + str(M) + ' and', a2 + str(V) + ' .')
    #Bending moment(M) and shear force(V) at the end x=L ; L=12
x = L
M = (w*(-6*x**2 + 6*L*x-L**2))/12
V = w*((L/2) - x)

a3= 'The bending moment at the end x=L is '
a4= 'the shear force at the end x=L is '

print()
print('(a.ii) ' + a3 + str(M) + ' and', a4 + str(V) + ' .')

#Question b
'''
    When the bending moment(M) is zero, the expression becomes x**2 - Lx + L**2/6 = 0
'''
    #From the expression
a = 1
b = -L
c = L**2/6
    #Finding the roots using the Almighty formula;
discriminant = b**2 - 4*a*c
root_1b = (-b + np.sqrt(discriminant))/2*a
root_2b = (-b - np.sqrt(discriminant))/2*a

print()
print('(b) The points of contra-flexure (i.e. M=0) are {0} and {1} .'.format(root_1b,root_2b))

#Question c
'''
    When the shear force(V) is zero, x = L/2
'''
x = L/2

print()
print('(c) The point at which the shear force will be zero is {0} .'.format(x))

#Question d
p = 0       #Start of array
s = 0.01    #Steps of the array (10mm=0.01m)
q = L + s   #Stop of array
x = np.arange(p,q,s)            #Numpy arange function
M = (w*(-6*x**2 + 6*L*x-L**2))/12

print()
print('(d) Using the initialized variable,the bending moment at each step in the array is {0} .'.format(M))

#Question e
    #Follow-up with same variables and values from question d
V = w*((L/2) - x)

print()
print('(e) The shear force for each step along the span is {0} .'.format(V))

#Question f
'''
    Let the absolute value of the bending moment array in (d) be AV
    Also let the minimum AV be m_AV
'''
AV = abs(M)
m_AV = min(AV)
"""
When the bending moment is m_AV, we get an expression x**2 - Lx + (L**2/6)+(2*m_AV)/w = 0
"""
    #From the above expression
a = 1
b = -L
c = (L**2/6)+(2*m_AV)/w
#Using the Almighty formula the roots are:
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a

print()
print('(f) The points along L at which the absolute values of the bending moment array in (d) is minimum are {0} and {1} .'.format(root_1f,root_2f))

#Question g
'''
Let the relative errors be r_e
'''
r_e1 = ((root_1b - root_1f)/root_1b*100)
r_e2 = ((root_2f - root_2b)/root_2f*100)

print()
print('(g) The relative errors between the estimated points of contra-flexure in (b) and (f) are {0}% and {1}% .'.format(r_e1,r_e2))

#Question h
"""
Let the maximum bending moment be max_M and the minimum bending moment be min_M
"""
#Considering the maximum bending moment
max_M = max(M)
"""
When the bending moment is max_M, we get an expression x**2 - Lx + (L**2/6)+(2*max_M)/w = 0
"""
a = 1
b = -L
c = (L**2/6)+(2*max_M)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1 = (-b + np.sqrt(discriminant))/2*a
root_2 = (-b - np.sqrt(discriminant))/2*a

print()
print('(h.1) The points at which the maximum bending moment occur are {0} and {1} .'.format(root_1,root_2))

#For the minimum bending moment
min_M = min(M)
"""
When the bending moment is min_M, we get an expression x**2 - Lx + (L**2//6)+(2*min_M)/w = 0
"""
a = 1
b = -L
c = (L**2//6)+(2*min_M)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1 = (-b - np.sqrt(discriminant))/2*a
root_2 = (-b + np.sqrt(discriminant))/2*a

print()
print('(h.2) The points at which the minimum bending moment occur are {0} and {1} .'.format(root_1,root_2))

    #My Github Link https://github.com/FBNarh
