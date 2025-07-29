import tempfile
from fileLineCount import countLines


def test_LineCountFunctional():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as fobj:
        fobj.write('Line#1\nLine#2\nLine#3\nLine#4\n')
        fobj.flush()

        assert countLines(fobj.name) == 4


#write to a file --> function process 
# --> get the result and assert the result