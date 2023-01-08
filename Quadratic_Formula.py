import math

def quadratic_roots(a,b,c):
    if a == 0:
        return "The value of 'a' cannot be zero.", "Please input another value for 'a'." #If 'a' is zero the program will output a divide by zero error
    #Find disc value
    dis= (b**2)-(4*a*c)
    #Find the value of the sqaure root of the disriminant as specified by the quadratic formula 
    sqrt_value= math.sqrt(dis)
    
    #Plug the sqaure root of the discriminant into the rest of the quadratic formula
    sol1= (-b + sqrt_value)/(2*a)
    sol2= (-b - sqrt_value)/(2*a)
    
    #Check the condition of the discriminant and return the corresponding values.
    if dis < 0:
        return "Complex Solutions" #Could find the precise answer using the cmath module
    elif dis == 0:
        return "One Real  Solution", sol1 #If there is only one solution both sol1 and sol2 are the same, so you can put either one here 
    else:
        return 'Two real solutions', sol1, sol2

#Test to see if there are any errors in the program. If not the program prints the roots. This gets rid of long, uninformative error messages. 

if __name__ == '__main__':
    try:
        roots = quadratic_roots(0, -7, 12)
        print(roots)
    except Exception as e:
            print(e)