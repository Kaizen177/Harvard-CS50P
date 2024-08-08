class Jar:
    def __init__(self, capacity=12,size=0):
        self.capacity=capacity
        self.size=size

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        self.size+=n

    def withdraw(self, n):
        self.size-=n

    #capacity getter
    @property
    def capacity(self):
        return self._capacity

    #capacity setter
    @capacity.setter
    def capacity(self,cap):
        if isinstance(cap,int) and cap>=0:
            self._capacity=cap
        else: raise ValueError


    #size getter
    @property
    def size(self):
        return self._size

    #size setter
    @size.setter
    def size(self,size):
        if isinstance(size,int) and 0<=size<=self.capacity:
            self._size=size
        else: raise ValueError

    def __eq__(self, other):
        if isinstance(other, Jar):
            return self.capacity == other.capacity and self.size == other.size
        return NotImplemented

