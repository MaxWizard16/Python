 # Q1
L = [11, 12, 13, 14]
L.extend([50, 60])
print("After adding:", L)
if 11 in L: L.remove(11)
if 13 in L: L.remove(13)
print("After removing:", L)
L.sort()
print("Ascending:", L)
L.sort(reverse=True)
print("Descending:", L)
print("13 in list?", 13 in L)
print("Count:", len(L))
print("Sum:", sum(L))
print("Sum of odd:", sum(x for x in L if x % 2 != 0))
print("Sum of even:", sum(x for x in L if x % 2 == 0))
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
print("Sum of primes:", sum(x for x in L if is_prime(x)))
L.clear()
print("Cleared list:", L)
del L

# Q2
nums = [1, 2, 3, 4, 5]
total = 0
for n in nums:
    total += n
print("Sum =", total)

# Q3
nums = [1, 2, 3, 4]
product = 1
for n in nums:
    product *= n
print("Product =", product)

# Q4
array = [[["*" for _ in range(6)] for _ in range(4)] for _ in range(3)]
print(array)

# Q5
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D[8] = 8.8
D.pop(2, None)
print("6 in dict?", 6 in D)
print("Count:", len(D))
print("Sum of values:", sum(D.values()))
D[3] = 7.1
D.clear()
print("Cleared dict:", D)

# Q6
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}
S1.update([55, 66])
S1.discard(10)
S1.discard(30)
print("40 in S1?", 40 in S1)
print("Union:", S1 | S2)
print("Intersection:", S1 & S2)
print("Difference:", S1 - S2)

# Q7
import random, string
for _ in range(5):
    length = random.randint(6, 8)
    s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    print(s)
for num in range(600, 801):
    if is_prime(num):
        print(num, end=" ")
print()
for num in range(100, 1001):
    if num % 7 == 0 and num % 9 == 0:
        print(num, end=" ")
print()

# Q8
exam_st_date = (11, 12, 2025)
print("The examination will start from: %i / %i / %i" % exam_st_date)

# Q9
nums = [10, 12, 15, 23, 30, 40]
for n in nums:
    if n % 5 == 0:
        print(n)

# Q10
num = 17
is_even = (num % 2 == 0)
print("Even?" if is_even else "Odd?")

# Q11
text = "Emma is a good girl. Emma loves coding. Emma is smart."
print("Emma appears", text.count("Emma"), "times")

# Q12
list1 = [10, 21, 4, 45, 66, 93]
list2 = [12, 14, 17, 20, 25]
new_list = [x for x in list1 if x % 2 != 0] + [y for y in list2 if y % 2 == 0]
print(new_list)

# Q13
positions = [(2,3), (4,5), (6,7), (7,8)]
even_positions = [pos for pos in positions if pos[0] % 2 == 0]
print(even_positions)

# Q14
sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
above_3 = [sid for sid, val in sensor_data.items() if val > 3.0]
print(above_3)

# Q15
commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
commands_executed = {"MOVE", "TURN_LEFT", "STOP"}
print(commands_received - commands_executed)
