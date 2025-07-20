from capitalize_words import capitalize_words

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming language") == "Python Programming Language"
    assert capitalize_words("  multiple   spaces ") == "Multiple Spaces"
    assert capitalize_words("") == ""
    assert capitalize_words("a b c") == "A B C"
