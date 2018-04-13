#russel john cortez
#MIDTERM

def match_a():
    print ("Function match_a() \n")

    russ1 = input("Enter 1st input:")
    russ2 = input("Enter 2nd input:")
    russ3 = input("Enter 3rd input:")

    russ22 = []
    russ33 = []
    russ11 = []

    for i in russ:
        if len(i) != 1:
            if i == i[::-1]:
                russ.append(i)

    for i in russ2:
        if len(i) != 1:
            if i == i[::-1]:
                russ22.append(i)

    for i in russ3:
        if len(i) != 1:
            if i == i[::-1]: 
               russ33.append(i)

    print ("1st output: ", len(russ11))
    print("2nd output: ", len(russ22))
    print ("3rd output: ", len(russ33))


match_a()
print ("\n\n")


def front_x():
    print ("Function front_x()\n")

    russ1 = input("Enter 1st input:")
    russ2 = input("Enter 2nd input:")
    russ3 = input("Enter 3rd input:")

    russ11 = []
    russ111 = []
    russ22 = []
    russ222 = []
    russ33 = []
    russ333 = []

    for i in russ1:
        if i.startswith('x'): 
            russ11.append(i)
        else:
            russ111.append(i) 

    print ("1st output: ", sorted(russ11) + sorted(russ111)) 

    for i in russ2:
        if i.startswith('x'): 
            russ22.append(i)
        else:
            russ222.append(i)  

    print ("2nd output: ", sorted(russ22) + sorted(russ222)) 

    for i in russ3:
        if i.startswith('x'): 
            russ33.append(i)
        else:
            russ333.append(i)  

    print ("3rd output: ", sorted(russ33) + sorted(russ333)) 


front_x()
