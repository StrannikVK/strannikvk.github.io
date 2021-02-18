class hello(object):
    """CS50 Lecture 2"""
    
    #print ("Hello, world!")
    #name = input("Your Name: ")
    #print ("Hello," + name)
    #print (f"Hello, {name}")
    n =float( input("Number: "))

    if n>0:
        print (f"{n} is possitive")
    elif n==0:
        print (f"{n} is zero")
    else:
        print (f"{n} is negative")

