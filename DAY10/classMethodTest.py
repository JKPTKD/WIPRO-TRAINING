'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:17-July-2025
   Purpose:Class method test
'''
class MyClass:
    def instMethod(self):
        pass
 
    @classmethod
    def classMethod(cls):
        pass
 
    @staticmethod
    def statMethod():
        pass
 
 
if __name__ == '__main__':
    print(MyClass.instMethod)
    print(type(MyClass.instMethod))
    print('*' * 40)
    print(MyClass.classMethod)
    print(type(MyClass.classMethod))
    print(MyClass.classMethod.__self__)
    print('*' * 40)
    print(MyClass.statMethod)
    print(type(MyClass.statMethod))
    print('*' * 40)  