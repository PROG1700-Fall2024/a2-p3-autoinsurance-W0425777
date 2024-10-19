#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Welcome message
    print("\nHi, Welcome the Nscc Car Insurance Calculator!\n")

    #Ask female or male
    S = input("Are you 'Female' or 'Male': ").lower()

    #ask age

    age = float(input("\nEnter your age: "))

         #if and for gender and age
    if age >= 40 and age <=70:
        rate = .10
    elif S == "female" and (age >= 15) and (age < 25):
        rate = .20
    elif S == "female" and (age >=25) and (age < 40):
        rate = .15
    elif S == "male" and (age >= 15) and (age < 25):
        rate = .25
    elif S == "male" and (age >=25) and (age < 40):
        rate = .17

    #if they are inside age range
    if age >= 15 and (age <=70):
        car = float(input("\nEnter the purchase price of the vehicle: "))
        #ask how much car is
        total = (car * rate)/12
        print("\nYour monthly insurance will be: ${0:.2f}\n".format(total))
    else:
        print("\nSorry you do not meet our requirments for insurance.\n")
    #else for outside age range

    #math for car * rate / 12
    
    #display total 

    # YOUR CODE ENDS HERE

main()