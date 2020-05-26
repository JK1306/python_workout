class Queue:
    def __init__(self):
        self.queue = []
        self.start = -1
        self.end = -1
    
    def Dequeue(self):
        if self.start == -1:
            print("Queue is Empty")
        else:
            if self.start == self.end:
                self.start -= 1
            self.queue.pop(self.start)
            self.end -= 1
            # if self.start == self.end:
            

    def Enqueue(self,val):
        if self.start == -1:
            self.start +=1
        self.end +=1
        self.queue.insert(self.end,val)
    
    def traverseQueue(self):
        if self.start != self.end:
            for x in self.queue:
                print(x)
        else:
            print("This is Empty Queue")

q = Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(2)
q.Enqueue(3)
q.traverseQueue()
print('__------------------------')
q.Dequeue()
q.traverseQueue()
print('&&&&&&&&&&&&&&&&&&&')
q.Dequeue()
q.Dequeue()
q.Dequeue()
q.traverseQueue()