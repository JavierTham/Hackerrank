class Stack:
    
    def push(self):
        pass
    
    def pop(self):
        pass
            
class Queue:
    
    def enqueue(self):
        pass
    
    def dequeue(self):
        pass
    
    def print_elem(self):
        pass

if __name__ == "__main__":
    q = int(input())
    queue = Queue()
    
    for i in range(q):
        query = input()
        
        query_type = int(query[0])
        if query_type == 1:
            x = int(query.split(" ")[0])
            queue.enqueue(x)
            
        elif query_type == 2:
            queue.dequeue()
            
        else:
            queue.print_elem()