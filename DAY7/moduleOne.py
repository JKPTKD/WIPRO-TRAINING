#import fiboPrintOne
from fiboPrintOne import fiboPrint
import nestedFunOne
import sys 

if __name__ == '__main__':
    fiboPrint(6)
    nestedFunOne.Outer(10)
    #print(os.environ)
    print(sys.path)
    sys.path.append(r'D:\wipro3July2025\Wipro3July2025\daySix')
    print(sys.path)
    import recurOne

    recurOne.recur(1)
