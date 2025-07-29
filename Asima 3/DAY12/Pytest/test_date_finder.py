from date_finder import find_dates_with_groups, find_dates_iterative

def test_find_dates_with_groups():
    text = "Today is 18-07-2025. My birthday is 01-01-1990. Another date: 31-12-2023. Invalid: 1-2-3"
    expected = [('18', '07', '2025'), ('01', '01', '1990'), ('31', '12', '2023')]
    assert find_dates_with_groups(text) == expected

def test_find_dates_iterative():
    text = "Today is 18-07-2025. My birthday is 01-01-1990. Another date: 31-12-2023. Invalid: 1-2-3"
    expected = ['18-07-2025', '01-01-1990', '31-12-2023']
    assert find_dates_iterative(text) == expected
