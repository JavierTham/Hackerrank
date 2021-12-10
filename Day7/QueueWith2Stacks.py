class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        self.stack.pop(-1)
            
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def print_elem(self):
        print(self.queue[0])

if __name__ == "__main__":
    q = int(input())
    queue = Queue()
    
    for i in range(q):
        query = input()
        
        query_type = int(query[0])
        if query_type == 1:
            x = int(query.split(" ")[1])
            queue.enqueue(x)
            
        elif query_type == 2:
            queue.dequeue()
            
        else:
            queue.print_elem()