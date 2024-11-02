import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        input = [data.Book("Johnny", "Sixty"), data.Book("Hagrid", "Harry Pooter"),
                 data.Book("Dillon", "Ant King"), data.Book("Charles", "King Arthur")]
        result = lab6.selection_sort_books(input)
        expected = [data.Book("Dillon", "Ant King"), data.Book("Hagrid", "Harry Pooter"),
            data.Book("Charles", "King Arthur"), data.Book("Johnny", "Sixty")]
        self.assertEqual(expected,result)

    def test_selection_sort_books_2(self):
        input = [data.Book("johnson", "twenty"), data.Book("Bobby", "Maze runner"),
                 data.Book("lucas", "ant man"), data.Book("Charles", "King Arthur")]
        result = lab6.selection_sort_books(input)
        expected = [data.Book("lucas", "ant man"), data.Book("Charles", "King Arthur"),
            data.Book("Bobby", "Maze runner"), data.Book("johnson", "twenty")]
        self.assertEqual(expected,result)


    # Part 2
    def test_swap_case_1(self):
        input = "BanAna"
        result = lab6.swap_case(input)
        expected = "bANaNA"
        self.assertEqual(expected, result)

    def test_swap_case_2(self):
        input = "aPPle456"
        result = lab6.swap_case(input)
        expected = "AppLE456"
        self.assertEqual(expected, result)

    # Part 3
    def test_str_translate(self):
        input = "banana"
        input2 = "a"
        input3 = "i"
        result = lab6.str_translate(input, input2, input3)
        expected = "binini"
        self.assertEqual(expected, result)

    def test_str_translate_2(self):
        input = "aildhfwliuhaepf"
        input2 = "i"
        input3 = "p"
        result = lab6.str_translate(input, input2, input3)
        expected = "apldhfwlpuhaepf"
        self.assertEqual(expected, result)


    # Part 4
    def test_histogram_1(self):
        input = "banana"
        result = lab6.histogram(input)
        expected = {"b":1,"a":3,"n":2}
        self.assertEqual(expected,result)

    def test_histogram_2(self):
        input = "banana 123"
        result = lab6.histogram(input)
        expected = {"b":1,"a":3,"n":2," ":1,"1":1,"2":1,"3":1}
        self.assertEqual(expected,result)





if __name__ == '__main__':
    unittest.main()
