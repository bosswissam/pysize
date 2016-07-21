import sys
import unittest

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


if __name__ == '__main__':
    unittest.main()
