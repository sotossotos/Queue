class Queue():
    def __init__(self):
        self.queue=[]
        self.HEAD=0
        self.tail=0
    def enqueue(self,value):
        self.queue.append(value)
        self.tail+=1
    def peek(self):
        return self.queue[self.HEAD]
    def dequeue(self):
        value=self.queue[self.HEAD]
        self.shiftQueueUtilNoSub()
        self.tail-=1
        return value
    def print_queue(self):
        for i in range(self.tail):
            print(f" The {i+1}'th value is {self.queue[i]}")
    def shiftQueueUtilNoSub(self):
        for i in range(1,len(self.queue)):
            self.queue[i-1]=self.queue[i]
        del self.queue[-1]
    def shiftQueueUtilBySub(self):
        temp=[]
        for i in range(1,len(self.queue)):
            temp.append(self.queue[i])
        self.queue=temp.copy()
