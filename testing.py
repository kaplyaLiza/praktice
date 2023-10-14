import unittest
import random
from functions import bubble_sort, ins_sort, heap_sort, cocktail_shaker_sort, merge_sort, quick_sort


class TestSortingAlgorithms(unittest.TestCase):
    def test_easy_case(self):
        arr = [3, 1, 2]
        self.assertEqual(bubble_sort(arr.copy()), sorted(arr))
        self.assertEqual(ins_sort(arr.copy()), sorted(arr))
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))
        self.assertEqual(merge_sort(arr.copy()), sorted(arr))
        self.assertEqual(quick_sort(arr.copy()), sorted(arr))
        self.assertEqual(cocktail_shaker_sort(arr.copy()), sorted(arr))

    def test_small_random_array(self):
        arr = random.sample(range(10000), 100)
        self.assertEqual(bubble_sort(arr.copy()), sorted(arr))
        self.assertEqual(ins_sort(arr.copy()), sorted(arr))
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))
        self.assertEqual(merge_sort(arr.copy()), sorted(arr))
        self.assertEqual(quick_sort(arr.copy()), sorted(arr))
        self.assertEqual(cocktail_shaker_sort(arr.copy()), sorted(arr))

    def test_large_random_array(self):
        arr = random.sample(range(1000000), 100000)
        self.assertEqual(bubble_sort(arr.copy()), sorted(arr))
        self.assertEqual(ins_sort(arr.copy()), sorted(arr))
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))
        self.assertEqual(merge_sort(arr.copy()), sorted(arr))
        self.assertEqual(quick_sort(arr.copy()), sorted(arr))
        self.assertEqual(cocktail_shaker_sort(arr.copy()), sorted(arr))

    def test_sorted_array(self):
        arr = list(range(100))
        self.assertEqual(bubble_sort(arr.copy()), sorted(arr))
        self.assertEqual(ins_sort(arr.copy()), sorted(arr))
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))
        self.assertEqual(merge_sort(arr.copy()), sorted(arr))
        self.assertEqual(quick_sort(arr.copy()), sorted(arr))
        self.assertEqual(cocktail_shaker_sort(arr.copy()), sorted(arr))

    def test_almost_sorted_array(self):
        arr = list(range(100))
        random.shuffle(arr)
        self.assertEqual(bubble_sort(arr.copy()), sorted(arr))
        self.assertEqual(ins_sort(arr.copy()), sorted(arr))
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))
        self.assertEqual(merge_sort(arr.copy()), sorted(arr))
        self.assertEqual(quick_sort(arr.copy()), sorted(arr))
        self.assertEqual(cocktail_shaker_sort(arr.copy()), sorted(arr))

    def test_inverted_sorted_array(self):
        arr = list(range(100, 0, -1))
        self.assertEqual(bubble_sort(arr.copy()), sorted(arr))
        self.assertEqual(ins_sort(arr.copy()), sorted(arr))
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))
        self.assertEqual(merge_sort(arr.copy()), sorted(arr))
        self.assertEqual(quick_sort(arr.copy()), sorted(arr))
        self.assertEqual(cocktail_shaker_sort(arr.copy()), sorted(arr))

    def test_empty_array(self):
        arr = []
        self.assertEqual(bubble_sort(arr.copy()), sorted(arr))
        self.assertEqual(ins_sort(arr.copy()), sorted(arr))
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))
        self.assertEqual(merge_sort(arr.copy()), sorted(arr))
        self.assertEqual(quick_sort(arr.copy()), sorted(arr))
        self.assertEqual(cocktail_shaker_sort(arr.copy()), sorted(arr))

    def test_random_length_and_values(self):
        arr = random.sample(range(10000), random.randint(1, 100))
        self.assertEqual(bubble_sort(arr.copy()), sorted(arr))
        self.assertEqual(ins_sort(arr.copy()), sorted(arr))
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))
        self.assertEqual(merge_sort(arr.copy()), sorted(arr))
        self.assertEqual(quick_sort(arr.copy()), sorted(arr))
        self.assertEqual(cocktail_shaker_sort(arr.copy()), sorted(arr))
