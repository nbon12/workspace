from unittest import TestCase, mock, expectedFailure

from pricer import Pricer

class TestClassAttribute(TestCase):

    def test_patch_instance_attribute(self):
        pricer = Pricer()
        pricer.DISCOUNT = 0.5
        self.assertAlmostEqual(pricer.get_discounted_price(100), 50.0)