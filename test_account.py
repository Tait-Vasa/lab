import pytest
from account import *
class Test:
    def setup_method(self):
        self.p1 = Account('Tait')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == "Tait"
        assert self.p1.get_balance() == 0


    def test_deposit(self):

        assert self.p1.deposit(30) is True
        assert self.p1.get_balance() == 30

        assert self.p1.deposit(-30) is False
        assert self.p1.get_balance() == 30

        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == 30
        
        assert self.p1.deposit(7.50) is True
        assert self.p1.get_balance() == approx(37.50, abs =0.001 )

    def test_withdraw(self):
        assert self.p1.withdraw(15) is False
        assert self.p1.get_balance() == 0

        assert self.p1.deposit(30) is True
        assert self.p1.get_balance() == 30

        assert self.p1.withdraw(15) is True
        assert self.p1.get_balance() == 15

        assert self.p1.withdraw(25) is False
        assert self.p1.get_balance() == 15

        assert self.p1.withdraw(-15) is False
        assert self.p1.get_balance() == 15

        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == 15
        
        assert self.p1.withdraw(7.50) is True
        assert self.p1.get_balance() == approx(7.50, abs = 0.001 )
