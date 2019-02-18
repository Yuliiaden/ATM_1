import unittest
import base_money

class TestRise(unittest.TestCase):
    atm_balance = base_money.Atm.atm_balance

    def test_rise_1(self):
        self.assertEqual(base_money.Atm.atm_balance, 10000)

    def test_rise_2(self):
        self.assertEqual(base_money.Atm.rise_money(self, 100), 10100)

    def test_rise_3(self):
        self.assertEqual(base_money.Atm.rise_money(self, -100), 9900) #это имеет смысл?нас интересует же пополнение...

    def test_rise_4(self):
        self.assertEqual(base_money.Atm.rise_money(self, 0), 10000)

    def test_rise_5(self):
        self.assertEqual(base_money.Atm.atm_balance, 100001)

    def test_rise_6(self):
        self.assertEqual(base_money.Atm.atm_balance, 9999)

    def test_rise_7(self):
        self.assertEqual(base_money.Atm.atm_balance, -10000)

    def test_rise_8(self):
        self.assertEqual(base_money.Atm.atm_balance, 0)

  


unittest.main()