import logging
 
class MyClass:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.warning('MyClass Logger initialized')
 
 
if __name__ == '__main__':
    obj1 = MyClass()
    obj2 = MyClass()
 