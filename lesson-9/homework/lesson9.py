import math
from datetime import date

# 1. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 2. Person Class
class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate  # format: YYYY-MM-DD

    def age(self):
        birth_year, birth_month, birth_day = map(int, self.birthdate.split("-"))
        today = date.today()
        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
        return age


# 3. Calculator Class
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


# 4. Shape and Subclasses
class Shape:
    def area(self): pass
    def perimeter(self): pass

class CircleShape(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius**2
    def perimeter(self): return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side**2
    def perimeter(self): return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# 5. Binary Search Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left: self._insert(node.left, value)
            else: node.left = Node(value)
        else:
            if node.right: self._insert(node.right, value)
            else: node.right = Node(value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node or node.value == value: return node is not None
        if value < node.value: return self._search(node.left, value)
        return self._search(node.right, value)


# 6. Stack Data Structure
class Stack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def is_empty(self): return len(self.items) == 0


# 7. Linked List Data Structure
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev, temp = temp, temp.next
        if temp: prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self): self.items = {}
    def add_item(self, name, price):
        self.items[name] = self.items.get(name, 0) + price
    def remove_item(self, name):
        if name in self.items: del self.items[name]
    def total(self): return sum(self.items.values())


# 9. Stack with Display
class StackDisplay:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def display(self): print(self.items)


# 10. Queue Data Structure
class Queue:
    def __init__(self): self.items = []
    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else None
    def is_empty(self): return len(self.items) == 0


# 11. Bank Class
class Bank:
    def __init__(self): self.accounts = {}

    def create_account(self, acc_no, name, balance=0):
        self.accounts[acc_no] = {"name": name, "balance": balance}

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no]["balance"] += amount

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts and self.accounts[acc_no]["balance"] >= amount:
            self.accounts[acc_no]["balance"] -= amount
        else:
            print("Insufficient funds or account not found")

    def check_balance(self, acc_no):
        return self.
