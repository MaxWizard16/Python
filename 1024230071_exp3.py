# Q1
def diff_17(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return 17 - n
print(diff_17(10))
print(diff_17(25))

# Q2
def test_range(n):
    return (100 <= n <= 1000) or (n == 2000)
print(test_range(500))
print(test_range(1500))

# Q3
def reverse_string(s):
    return s[::-1]
print(reverse_string("robot"))

# Q4
def count_case(s):
    counts = {"UPPER": 0, "LOWER": 0}
    for c in s:
        if c.isupper():
            counts["UPPER"] += 1
        elif c.islower():
            counts["LOWER"] += 1
    return counts
print(count_case("RobOtics"))

# Q5
def distinct_list(lst):
    return list(set(lst))
print(distinct_list([1, 2, 2, 3, 4, 4, 5]))

# Q6
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]
print(even_numbers([1,2,3,4,5,6,7,8,9]))

# Q7
def robot():
    def move():
        print("Robot is moving")
    move()
robot()

# Q8
def student(name, age, course):
    pass
student.__code__.co_varnames = ("name", "age", "course")
print("Arguments:", student.__code__.co_varnames)

# Q9
def move_robot(x, y, direction):
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return (x, y)
print(move_robot(0, 0, "up"))
print(move_robot(2, 3, "left"))

# Q10
def classify_temperature(temp):
    if temp < 15:
        return "Cold"
    elif 15 <= temp <= 30:
        return "Moderate"
    else:
        return "Hot"
print(classify_temperature(10))
print(classify_temperature(25))
print(classify_temperature(35))

# Q11
def is_goal_reached(path):
    x, y = 0, 0
    for move in path:
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
    return (x, y) == (2, 0)
print(is_goal_reached(["up", "right", "right", "down"]))
print(is_goal_reached(["up", "up", "right"]))

# Q12
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.student_name)
        print("Class:", self.student_class)

s = Student(1, "John", "CS")
s.display()

# Q13
class Student2:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

student1 = Student2(1, "Alice", "ECE")
student2 = Student2(2, "Bob", "ME")

print(vars(student1))
print(vars(student2))

# Q14
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print(c.area())
print(c.perimeter())

# Q15
class StringHandler:
    def get_String(self):
        self.s = input("Enter a string: ")
    def print_String(self):
        print(self.s.upper())

sh = StringHandler()


# Q16
class Robot:
    def __init__(self, name, task, battery_level=100):
        self.name = name
        self.task = task
        self.battery_level = battery_level

    def perform_task(self):
        if self.battery_level > 0:
            print(f"{self.name} is performing {self.task}")
            self.battery_level -= 10
        else:
            print("Battery too low to perform task")

    def recharge(self):
        self.battery_level = 100
        print(f"{self.name} is recharged")

    def status(self):
        print(f"Name: {self.name}, Task: {self.task}, Battery: {self.battery_level}%")

r = Robot("Robo1", "Cleaning")
r.status()
r.perform_task()
r.status()
r.recharge()
r.status()
