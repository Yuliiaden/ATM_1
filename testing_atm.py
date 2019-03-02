import unittest
import base_money

class TestRise(unittest.TestCase):
    Atm = base_money.Atm()

    def SetUp(self):
      self.Atm = base_money.Atm()

    def test_rise_1(self):
        self.assertEqual(self.Atm.atm_balance, 10000)

    def test_rise_2(self):
        self.assertEqual(self.Atm.rise_money(100), 10100)

    def test_rise_3(self):
        self.assertEqual(self.Atm.rise_money(-100), 9900)

    def test_rise_4(self):
        self.assertEqual(self.Atm.rise_money(0), 10000)

    def test_rise_5(self):
        self.assertEqual(self.Atm.atm_balance, 100001)

    def test_rise_6(self):
        self.assertEqual(self.Atm.atm_balance, 9999)

    def test_rise_7(self):
        self.assertEqual(self.Atm.atm_balance, -10000)

    def test_rise_8(self):
        self.assertEqual(self.Atm.atm_balance, 0)

class TestPIN(unittest.TestCase):
    Atm = base_money.Atm()

    def SetUp(self):
        self.Atm = base_money.Atm()

    def test_pin_1(self):
        self.assertTrue(self.Atm.enter_pin(777))

    def test_pin_2(self):
        self.assertRaises(base_money.IncorrectPin, self.Atm.enter_pin, 111)




unittest.main()