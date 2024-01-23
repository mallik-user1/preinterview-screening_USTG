class CircularQueue:
    def __init__(self, max_length=5):
        self.queue = {}
        self.max_length = max_length
        self.front = 0
        self.rear = 0

    def enqueue(self, element):
        # Check if the queue is full
        if (self.front + 1) % self.max_length == self.rear:
            # Queue is full, delete the latest added element
            deleted_element = self.queue[self.rear]
            del self.queue[self.rear]
            self.rear = (self.rear + 1) % self.max_length
            print(f"Queue full. Deleted element: {deleted_element}")

        # Add the new element to the queue
        self.queue[self.front] = element
        self.front = (self.front + 1) % self.max_length

    def display(self):
        print("Current Queue:", list(self.queue.values()))


cq = CircularQueue(max_length=6)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()  # Output: [1, 2, 3, 4, 5]

cq.enqueue(6)
cq.display()  # Output: [2, 3, 4, 5, 6]
