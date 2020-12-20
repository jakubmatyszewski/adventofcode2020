import ch1
import ch2


def test_ch1():
    test_input = ch1.from_txt('test_input.txt')
    assert ch1.challenge(test_input) == 37


def test_ch2():
    test_input = ch2.from_txt('test_input.txt')
    assert ch2.challenge(test_input) == 26
