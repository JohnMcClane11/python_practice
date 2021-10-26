import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_incorrectly(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_devision_correct(self):
        assert self.calc.division(self, 6, 6) == 1

    def test_devision_incorrect(self):
        assert self.calc.division(self, 7, 7) == 2

    def test_adding(self):
        assert self.calc.adding(self, 1, 2) == 3

    def test_adding_wrong(self):
        assert self.calc.adding(self, 1, 2) == 5

    def test_subtraction(self):
        assert self.calc.subtraction(self, 5, 3) == 2

    def test_subtraction_incorr(self):
        assert self.calc.subtraction(self, 5, 3) == 1