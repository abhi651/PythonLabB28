""" write a program for Merge Sort""" 

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

def merge_sort(lst):
   pass   
        
# DO NOT TOUCH THE BELOW CODE
class TestMergeSort(unittest.TestCase):
    
    def test_01(self):
        lst = [1,4,3,2]
        new_lst = [1,2,3,4]
        self.assertEqual(merge_sort(lst),new_lst)

    def test_02(self):
        lst = [0,0,0,0]
        new_lst = [0,0,0,0]
        self.assertEqual(merge_sort(lst),new_lst)

    def test_03(self):
        lst = [-1,4,0,2]
        new_lst = [-1,0,2,4]
        self.assertEqual(merge_sort(lst),new_lst)

    def test_04(self):
        lst = [11,101,1, 110111,1101]
        new_lst = [1,11,101,1101,110111]
        self.assertEqual(merge_sort(lst),new_lst)


if __name__ == '__main__':
    unittest.main(verbosity=2)