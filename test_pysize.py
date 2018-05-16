import sys
import unittest
from collections import namedtuple

import pysize

class TestPysize(unittest.TestCase):
    def test_empty_list(self):
        empty_list = []
        self.assertEqual(sys.getsizeof(empty_list),
                         pysize.get_size(empty_list))

    def test_list_of_collections(self):
        collection_list = [[], {}, ()]
        pointer_byte_size = 8*len(collection_list)
        empty_list_size = sys.getsizeof([])
        empty_tuple_size = sys.getsizeof(())
        empty_dict_size = sys.getsizeof({})
        expected_size = empty_list_size * 2 + empty_tuple_size +\
                        empty_dict_size + pointer_byte_size

        self.assertEqual(expected_size,
                         pysize.get_size(collection_list))

    def test_no_double_counting(self):
        rep = ["test1"]
        obj = [rep, rep]
        obj2 = [rep]
        self.assertEqual(pysize.get_size(obj), pysize.get_size(obj2) + 8)

    def test_gracefully_handles_self_referential_objects(self):
        class Test(object):
            pass
        obj = Test()
        obj.prop = obj
        obj2 = Test()
        self.assertEqual(pysize.get_size(obj), pysize.get_size(obj.prop))

    def test_strings_pv3_compat(self):
        test_string = "abc"
        self.assertEqual(sys.getsizeof(test_string), pysize.get_size(test_string))

    def test_custom_class(self):

        class Point(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        point = Point(3, 4)
        self.assertEqual(pysize.get_size(point),
                         sys.getsizeof(point) +
                         sys.getsizeof(point.__dict__) +
                         sys.getsizeof('x') +
                         sys.getsizeof(3) +
                         sys.getsizeof('y') +
                         sys.getsizeof(4))

    def test_namedtuple(self):
        Point = namedtuple('Point', ['x', 'y'])
        point = Point(3, 4)
        self.assertEqual(pysize.get_size(point),
                         sys.getsizeof(point) +
                         sys.getsizeof(3) +
                         sys.getsizeof(4))

    def test_subclass_of_namedtuple(self):

        class Point(namedtuple('Point', ['x', 'y'])):
            pass

        point = Point(3, 4)
        self.assertEqual(pysize.get_size(point),
                         sys.getsizeof(point) +
                         sys.getsizeof(point.__dict__) +
                         sys.getsizeof(3) +
                         sys.getsizeof(4))

    def test_subclass_of_namedtuple_with_slots(self):

        class Point(namedtuple('Point', ['x', 'y'])):
            __slots__ = ()

        point = Point(3, 4)
        self.assertEqual(pysize.get_size(point),
                         sys.getsizeof(point) +
                         sys.getsizeof(3) +
                         sys.getsizeof(4))
        
    def test_slots(self):
        class slots1(object):
            __slots__ = ["number1"]
            def __init__(self, number1):
                self.number1 = number1

        class slots2(object):
            __slots__ = ["number1", "number2"]
            def __init__(self, number1,number2):
                self.number1 = number1
                self.number2 = number2

        class slots3(object):
            __slots__ = ["number1", "number2", "number3"]
            def __init__(self, number1, number2, number3):
                self.number1 = number1
                self.number2 = number2
                self.number3 = number3

        s1 = slots1(7)
        s2 = slots2(3, 4)
        s3 = slots3(4, 5, 6)

        version_addition = 0

        if sys.version_info.major == 3:
            version_addition = 4

        # base 40 for the class, 28 per integer, +8 per element
        self.assertEqual(pysize.get_size(s2), pysize.get_size(s1) + 28 + 4 + version_addition)
        self.assertEqual(pysize.get_size(s3), pysize.get_size(s2) + 28 + 4 + version_addition)
        self.assertEqual(pysize.get_size(s3), pysize.get_size(s1) + 56 + 8 + version_addition * 2) # *2 for the num of variables in difference


if __name__ == '__main__':
    unittest.main()
