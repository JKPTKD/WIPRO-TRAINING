def funOne():
    print('Hello')

def test_funOuputOne(capsys):
    print('What ever output')
    captur = capsys.readouterr()
    assert 'What' in captur.out 

def test_funOuputTwo(capsys):
    print('What ever output')
    captur = capsys.readouterr()
    assert 'ever' in captur.out 

def test_funOuputThree(capsys):
    print('What ever output')
    captur = capsys.readouterr()
    assert 'output' in captur.out 

def test_funOuputFour(capsys):
    print('What ever output')
    captur = capsys.readouterr()
    assert 'What ever output' in captur.out

def test_funOuputFive(capsys):
    print('What ever output')
    captur = capsys.readouterr()
    assert 'ever output' in captur.out

def test_funOuputSix(capsys):
    print('What ever output')
    captur = capsys.readouterr()
    assert 'What ever' in captur.out

def test_funOuputSeven(capsys):
    funOne()
    captur = capsys.readouterr()
    assert 'Hello' in captur.out
