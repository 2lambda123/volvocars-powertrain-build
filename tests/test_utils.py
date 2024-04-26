from powertrain_build.utils import modulo_sum

from unittest import TestCase


class TestModuloSum(TestCase):
    def test_sum(self):
        self.assertEqual(modulo_sum(3, 4, 5), 2)

    def test_sum_with_modulo_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modulo_sum(3, 4, 0)
