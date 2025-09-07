# 1
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} | {self.description} | Due: {self.due_date} | Status: {self.status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        return False

    def list_all_tasks(self):
        return self.tasks

    def list_incomplete_tasks(self):
        return [task for task in self.tasks if task.status == "Incomplete"]


def todo_cli():
    todo = ToDoList()

    while True:
        print("\nToDo Menu:")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Task title: ")
            desc = input("Task description: ")
            due = input("Due date: ")
            todo.add_task(Task(title, desc, due))
            print("Task added!")

        elif choice == "2":
            title = input("Enter task title to mark complete: ")
            if todo.mark_task_complete(title):
                print("Task marked complete.")
            else:
                print("Task not found.")

        elif choice == "3":
            for t in todo.list_all_tasks():
                print(t)

        elif choice == "4":
            for t in todo.list_incomplete_tasks():
                print(t)

        elif choice == "5":
            break
        else:
            print("Invalid choice!")

# 2
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}\n{self.content}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        return self.posts

    def posts_by_author(self, author):
        return [p for p in self.posts if p.author == author]

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, title, new_content):
        for p in self.posts:
            if p.title == title:
                p.content = new_content

    def latest_posts(self, n=3):
        return self.posts[-n:]


def blog_cli():
    blog = Blog()

    while True:
        print("\nBlog Menu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Show Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
            print("Post added!")

        elif choice == "2":
            for p in blog.list_all_posts():
                print(p)

        elif choice == "3":
            author = input("Author: ")
            for p in blog.posts_by_author(author):
                print(p)

        elif choice == "4":
            title = input("Title of post to delete: ")
            blog.delete_post(title)
            print("Deleted.")

        elif choice == "5":
            title = input("Title of post to edit: ")
            content = input("New content: ")
            blog.edit_post(title, content)
            print("Edited.")

        elif choice == "6":
            for p in blog.latest_posts():
                print(p)

        elif choice == "7":
            break
        else:
            print("Invalid choice!")

# 3
class Account:
    def __init__(self, acc_no, holder, balance=0):
        self.acc_no = acc_no
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account: {self.acc_no}, Holder: {self.holder}, Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.acc_no] = acc

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def transfer(self, from_acc, to_acc, amount):
        acc1 = self.get_account(from_acc)
        acc2 = self.get_account(to_acc)
        if acc1 and acc2 and acc1.withdraw(amount):
            acc2.deposit(amount)
            return True
        return False


def bank_cli():
    bank = Bank()

    while True:
        print("\nBank Menu:")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. List Accounts")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            acc_no = input("Account number: ")
            holder = input("Holder name: ")
            bank.add_account(Account(acc_no, holder))
            print("Account created!")

        elif choice == "2":
            acc_no = input("Account number: ")
            acc = bank.get_account(acc_no)
            print(acc if acc else "Not found")

        elif choice == "3":
            acc_no = input("Account number: ")
            amount = float(input("Amount: "))
            acc = bank.get_account(acc_no)
            if acc:
                acc.deposit(amount)
                print("Deposited.")
            else:
                print("Account not found.")

        elif choice == "4":
            acc_no = input("Account number: ")
            amount = float(input("Amount: "))
            acc = bank.get_account(acc_no)
            if acc and acc.withdraw(amount):
                print("Withdrawn.")
            else:
                print("Error (account not found or insufficient funds).")

        elif choice == "5":
            from_acc = input("From account: ")
            to_acc = input("To account: ")
            amount = float(input("Amount: "))
            if bank.transfer(from_acc, to_acc, amount):
                print("Transfer complete.")
            else:
                print("Transfer failed.")

        elif choice == "6":
            for acc in bank.accounts.values():
                print(acc)

        elif choice == "7":
            break
        else:
            print("Invalid choice!")



