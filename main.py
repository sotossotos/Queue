from queue import Queue
def main():
    print("This is Running !")
    que=Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.print_queue()
    que.dequeue()

    print(f"{que.peek()}")
    que.print_queue()
    #print(f"{que.tail}")

if __name__=="__main__":
    main()