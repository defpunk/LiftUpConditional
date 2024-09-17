import unittest
from codingdojo import liftupConditional

class TestLiftUpConditional(unittest.TestCase):

    def test_lift_up_conditional_returns_ATrueBTrue_when_input_true_true(self):
        self.assertEqual(liftupConditional.lift_up_conditional(True, True), "ATrueBTrue")

    def test_lift_up_conditional_returns_ATrueBFalse_when_input_true_false(self):
        self.assertEqual(liftupConditional.lift_up_conditional(True, False), "ATrueBFalse")

    def test_lift_up_conditional_returns_AFalseBTrue_when_input_false_true(self):
        self.assertEqual(liftupConditional.lift_up_conditional(False, True), "AFalseBTrue")

    def test_lift_up_conditional_returns_AFalseBFalse_when_input_false_false(self):
        self.assertEqual(liftupConditional.lift_up_conditional(False, False), "AFalseBFalse")


if __name__ == '__main__':
    unittest.main()