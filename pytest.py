import pytest

import calculation

class TestCal(object):
    def setUp_method(self, method):
        print('method={}'.format(method.__name__))
        self.cal = calculation.Cal()
        
    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        del self.cal
        
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1, 1) == 4
        
    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            cal = calculation.Cal()
            cal.add_num_and_double('1', '1')
            
        
# release_name = 'lesson2'

# class CalTest(unittest.TestCase):
#     def setUp(self):
#         print('setup')
#         self.cal = calculation.Cal()
        
#     def tearDown(self):
#         print('clean up')
#         del self.cal
    
#     # @unittest.skip('skip!')
#     @unittest.skipIf(release_name=='lesson2', 'skip!')
#     def test_add_num_and_double(self):
#         cal = calculation.Cal()
#         self.assertEqual(cal.add_num_and_double(1, 1), 4)
        
#     def test_add_num_and_double_raise(self):
#         cal = calculation.Cal()
#         with self.assertRaises(ValueError):
#             cal.add_num_and_double('1', '1')
        
# if __name__ == '__main__':
#     unittest.main()