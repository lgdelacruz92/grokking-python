from sliding_window.min_window import min_window

def test_min_window_1():
    str1 = 'abcdebdde'
    str2 = 'bde'

    expected = 'bcde'
    result = min_window(str1, str2)
    assert expected == result

def test_min_window_2():
    str1 = 'abcdebdde'
    str2 = 'cbe'

    expected = 'cdebdde'
    result = min_window(str1, str2)
    assert expected == result

def test_min_window_3():
    str1 = 'bbbbbb'
    str2 = 'b'

    expected = 'b'
    result = min_window(str1, str2)
    assert expected == result

def test_min_window_4():
    str1 = 'aebbb'
    str2 = 'be'

    expected = ''
    result = min_window(str1, str2)
    assert expected == result

def test_min_window_5():
    str1 = 'a'
    str2 = 'aaa'

    expected = ''
    result = min_window(str1, str2)
    assert expected == result

def test_min_window_6():
    str1 = 'aa'
    str2 = 'aa'

    expected = 'aa'
    result = min_window(str1, str2)
    assert expected == result

def test_min_window_7():
    str1 = 'affbcaebc'
    str2 = 'abc'

    expected = 'aebc'
    result = min_window(str1, str2)
    assert expected == result

def test_min_window_8():
    str1 = 'abcdbebe'
    str2 = 'bbe'

    expected = 'bebe'
    result = min_window(str1, str2)
    assert expected == result