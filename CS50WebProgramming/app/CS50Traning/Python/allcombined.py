class hello(object):
    """CS50 Lecture 2"""

    # print ("Hello, world!")
    # name = input("Your Name: ")
    # print ("Hello," + name)
    # print (f"Hello, {name}")
    # n =float( input("Number: "))
    #
    # if n>0:
    #     print (f"{n} is possitive")
    # elif n==0:
    #     print (f"{n} is zero")
    # else:
    #     print (f"{n} is negative")
    # name = "Harry"
    # print(name[0])
    # print(name[1])

    # This is a Python comment
    names = ["Harry", "Ron", "Hermione"]
    # Print the entire list:
    print(names)
    # Print the second element of the list:
    print(names[1])
    # Add a new name to the list:
    names.append("Draco")
    # Sort the list:
    names.sort()
    # Print the new list:
    print(names)
    print(names[0])

    # Tuples are generally used when you need to store just two or three values together, such as the x and y values for a point. In Python code, we use parentheses:
    point = (12.5, 10.6)
    # Create an empty set:
    # Sets are different from lists and tuples in that they are unordered collection of unique values
    s = set()

    # Add some elements:
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    s.add(3)  # second is not added - hans unique
    s.add(1)
    # Print the set:
    print(s)

    # Find the size of the set:
    print(f"The set has {len(s)} elements.")

    """Python Dictionaries or dicts, will be especially useful in this course. A dictionary is a set of key-value 
    pairs, where each key has a corresponding value, just like in a dictionary, each word (the key) has a 
    corresponding definition (the value). In Python, we use curly brackets to contain a dictionary, and colons to 
    indicate keys and values. For example: """

    # Define a dictionary
    houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
    # Print out Harry's house
    print(houses["Harry"])
    # Adding values to a dictionary:
    houses["Hermione"] = "Gryffindor"
    # Print out Hermione's House:
    print(houses["Hermione"])
    for i in [0, 1, 2, 3, 4, 5]:
        print(i)
    for i in range(6):
        print(i)

    # Create a list:
    names = ["Harry", "Ron", "Hermione"]

    # Print each name:
    for name in names:
        print(name)
    name = "Harry"
    for char in name:
        print(char)
    names.append("Draco")
    print(names)
    names.sort()
    print(names)
    # Create an empty set
    # sets will store only uniqe objects
    s=set()
    # Add elements to set
    s.add(1)
    s.add(2)
    s.add(1)
    s.add("Draco")
    print (s)
    s.remove(1)
    print(s)
    print(f"The set has {len(s)} elements")
    for i in [1,2,3,"Draco"]:
        print(i)
