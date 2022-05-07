#スタック/最後に取り入れた要素を取り出せるデータ構造
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
print(stack.is_empty())
#追加
stack = Stack()
stack.push(1)
print(stack.is_empty())
#pop取り除く
stack = Stack()
stack.push(1)
item = stack.pop()
print(item)
print(stack.is_empty())

stack = Stack()
for i in range(0,5):
  stack.push(i)

print(stack.peek())
print(stack.size())

stack = Stack()
for c in "Hello":
  stack.push(c)

reverse = ""

while stack.size():
  reverse += stack.pop()

print(reverse)

#キュー/最初に取り入れた要素を一番初めに取り出せるデータ構造
class Queue:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

a_queue = Queue()
print(a_queue.is_empty())

a_queue = Queue()
for i in range(5):
  a_queue.enqueue(i)

print(a_queue.size())


a_queue = Queue()

for i in range(5):
    a_queue.enqueue(i)

while a_queue.size():
  print(a_queue.dequeue())

print()
print(a_queue.size())