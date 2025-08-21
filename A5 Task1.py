#Task 1: Create a Dictionary of Student Marks
d={'Alice':50,'John':90,'Jessie':86,'Tom':25}
Name=input("Enter the students's name:")
if Name in d:
    print(Name+"'s Marks:",d[Name])
else:
    print("Student not found")