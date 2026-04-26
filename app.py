command = ""
started = False
stopped = False
while True :
    command = input('> ').lower()
    if command == "start":
        if started :
            print("car has already started" )
        else:
            started = True
            print("your car has started.")
    elif command == "stop":
        if  stopped :
            print("your car has already stopped")
        else:
            stopped = True
            print("your car has stopped")
    elif command == "help":
        print('''
start - to start the car 
stop - to stop the car
quit - to quit the game''')
    elif command == "quit":
        break
    else:
        print("i don't understand what you are saying ")

#1
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def introduce(self):
        print(f"hi, I'm {self.name}, I'm {self.age} and my grade is {self.grade}")


student1 = Student("reim",16,"A")
student1.introduce()
#2
string = input("")
def clean_input(string):
    print(string.strip().lower().replace(",",""))
clean_input(string)

#3
class Animal:
    def __init__(self,name):
        self.name= name
    def speak(self):
        print("")
class Dog(Animal):
    def speak(self):
        return (f"{self.name} says woof")

class Cat(Animal):
    def speak(self):
        return (f"{self.name} says meow")

dog = Dog("Rex")
cat = Cat("Luna")
print(dog.speak())
print(cat.speak())

#4
cart = []
def add_item(cart,items,price):
    dictionary = {"items":items , "price": price}
    return cart.append(dictionary)

def remove_item(cart,item_to_remove):
    if len(cart) == 0 :
        raise ValueError("can't remove an empty list ")
    for goodies in cart:
        if goodies["items"] == item_to_remove:
            cart.remove(goodies)
    return cart

def total(cart):
    total_price = 0
    for item in cart:
        total_price += item["price"]
    return total_price
def show_cart(cart):
   for item in cart:
        print(f"{item["items"]} ${item["price"]}",end=" ")

add_item(cart, "Bread", 2.5)
add_item(cart, "Milk", 1.8)
add_item(cart, "Eggs", 3.2)
remove_item(cart, "Milk")
show_cart(cart)
final_total = total(cart)
print(f"total:{final_total}")

#5
user_input =input("")
try:
    with open('user_file.txt', 'a+') as f:
        if user_input.lower() == "show":
            f.seek(0)
            print(f.read())
        else:
            f.write(user_input + "\n")
            print("note saved.")

except Exception as e:
    print("oops, somethings went wrong")

#6
import random
lucky_number = random.randint(1,100)
print("try to guess a number from 1 to 100")
guess = 0
command = input("choose mode easy/hard :")
if command.lower() == "easy" :
    guess_count = 10
    print('you have 10 guesses')
elif command.lower() == "hard":
    guess_count = 5
    print("you have 5 guesses")
else:
    print("invalid mode, return to easy mode")
    guess_count = 10
while guess != guess_count:
    user_guesses = int(input("type number: "))
    if user_guesses > lucky_number:
        print(f"too high,{guess_count - guess} left ")
    elif user_guesses < lucky_number:
        print(f" too low, {guess_count - guess} left")
    else:
        print("congratulation, you are tuff")
        break
    guess += 1
    if guess == guess_count:
        print("you lost, better luck next time. ")
        break

#7
class Student:
    def __init__(self,name,grade_list):
        self.name = name
        self.grade_list = grade_list
    def add_grade(self,grade):
        self.grade_list.append(grade)
    def avg_score(self):
        try:
            avg = sum(self.grade_list) / len(self.grade_list)
        except ZeroDivisionError:
            avg = 0
            print("cannot find average of student with no score and and negative score")
        return avg
    def find_highest(self):
        return max(self.grade_list)
    def find_lowest(self):
        return min(self.grade_list)
    def pass_or_fail(self):
        if self.avg_score() >= 50:
            return "pass"
        else:
            return "fail"

class ClassRoom:
    def __init__(self,class_name):
        self.name = class_name
        self.students = []
    def add_student(self,student):
        self.students.append(student)
        return self.students
    def show_top(self):
        if not self.students:
            return "No student in this class"
        top_student = self.students[0]
        for student in self.students:
            if student.avg_score() > top_student.avg_score():
                top_student = student
            return f"Top Performer: {top_student.name} with an average of {top_student.avg_score()}"

anna = Student("Anna", [90, 95, 88])
bob = Student("Bob", [70, 65, 80])

my_class = ClassRoom("Python 101")
print(my_class.add_student(anna))
print(my_class.add_student(bob))
print(my_class.show_top())

#8
import string
import random
all_in_one = string.ascii_letters
include_number=input("include number(yes/no): ")
include_symbol=input("include symbols(yes/no): ")
if include_number.lower() == "yes":
    all_in_one += string.digits
elif include_number.lower() == "no":
    pass
else:
    print("type yes or no only")
if include_symbol.lower() == "yes":
    all_in_one += string.punctuation
elif include_symbol.lower() == "no":
    pass
else:
    print("type yes or no only")
try:
    password_lenght = int(input("pick your password lenght:"))
except (ValueError, NameError):
    print('please enter a valid number,defaulting length to 8')
    pass_word = 8
pass_word = 0
password = ""
while pass_word < password_lenght:
    password += random.choice(all_in_one)
    pass_word += 1
print(f"your password is: {password}")