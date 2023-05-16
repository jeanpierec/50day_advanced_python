#-------------------------------------------------------------------
# Level: BASIC
# Student Management System
# Leyton Jean Piere Castro
#-------------------------------------------------------------------

# Create Class Student
class Student:
    # Constructor
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
    
    # Function to create/append a new student
    def accept(self, name, rollno, marks1, marks2):
        # We can use 'input' method
        ob = Student(name, rollno, marks1, marks2)
        # ls are the list of students
        ls.append(ob)
    
    # Display all students
    def display(self, ob):
        print("Name: ", ob.name)
        print("RollNo: ", ob.rollno)
        print("Marks 1: ", ob.m1)
        print("Marks 2: ", ob.m2)
        print("\n")
    
    # Search function
    def search(self, rn):
        # We need to use the rollNo for search a student
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i

    # Delete function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]
    
    # Update function
    def update(self, rn, no):
        i = obj.search(rn)
        roll = no
        ls[i].rollno = roll

#------------------------------
# Now, we test the code
ls = []
# an object for student class
obj = Student('',0,0,0)

print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
 
ch = int(input("Enter choice:"))

if(ch == 1):
    obj.accept("A", 1, 100, 100)
    obj.accept("B", 2, 90, 90)
    obj.accept("C", 3, 80, 80)
elif(ch == 2):
    print("\n")
    print("\nList of Students\n")
    for i in range(ls.__len__()):
        obj.display(ls[i])
elif(ch == 3):
    print("\n Student Found, ")
    s = obj.search(2)
    obj.display(ls[s])
elif(ch == 4):
    obj.delete(2)
    print(ls.__len__())
    print("List after deletion")
    for i in range(ls.__len__()):
        obj.display(ls[i])
elif(ch == 5):
    obj.update(3, 2)
    print(ls.__len__())
    print("List after updation")
    for i in range(ls.__len__()):
        obj.display(ls[i])
else:
    print("Thank You !")
