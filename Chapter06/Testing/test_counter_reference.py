from unittest import TestCase
from counter import Counter


class TestCounter(TestCase):

    def test_small(self):
        small_counter = Counter(5, 5)
        small_counter.run()

        self.assertEqual(small_counter.value, 5)

    def test_med(self):
        med_counter = Counter(10, 8)
        med_counter.run()

        self.assertEqual(med_counter.value, 10)

    def test_large(self):
        large_counter = Counter(500, 20)
        large_counter.run()

        self.assertEqual(large_counter.value, 500)
