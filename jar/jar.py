class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Too many cookies")
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies")
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Too few cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size





jar = Jar(12)
jar.deposit(5)
jar.withdraw(1)
print(jar)


