def countLines(filename):
    with open(filename) as fobj:
        return len(fobj.readlines())
