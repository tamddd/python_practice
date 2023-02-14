class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(self.stack)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def main():
    stack1 = Stack()
    numbers = [1, 2, 3, 4, 5, 6]

    for i in numbers:
        stack1.push(i)

if __name__ == "__main__":
    main()
