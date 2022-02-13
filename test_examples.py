import requests
import pytest

class TestExamples():
    def test_check_math(self):
        a = 5
        b = 9
        expected_sun = 14
        assert a + b == 14, f"a + b is not {expected_sun}"

    def test_check_math2(self):
        a = 5
        b = 11
        expected_sun = 14
        assert a + b == 14, f"a + b is not {expected_sun}"