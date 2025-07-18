'''
    Custom Iterator
'''
 
class MyRange:
    def __init__(self, start, end, step = 1):
        self.current, self.end, self.step = start, end, step
   
    def __iter__(self):
        return self
   
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
 
 
if __name__ == '__main__':
    for i in MyRange(1, 11):
        print(i, end=' ')
 