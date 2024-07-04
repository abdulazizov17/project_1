class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

# Example usage:
fib_iter = FibonacciIterator()
for i in range(10):
    print(next(fib_iter))
