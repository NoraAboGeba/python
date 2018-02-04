
import unittest

from task1 import vowel_rem
from task2 import endex
from task3 import calculate
from task4 import calcArea
from task5 import dic



class TestAssignmentOne(unittest.TestCase):

    def test_task_one(self):
        self.assertEqual(vowel_rem('mobile'),'mbl')
        self.assertEqual(vowel_rem('MOBILE'), 'MBL')
        self.assertEqual(vowel_rem('MobIlE'), 'Mbl' )

    def test_leter_para(self):
        self.assertEqual(endex('This is javaScript','i'), [2,5,15])

    def test_fact_num(self):
        self.assertEqual(calculate(3), [[1],[2,4],[3,6,9]])

    def test_list_dic(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        self.assertEqual(dic(l1), d1)




    def test_task_five(self):
        self.assertEqual(calcArea(2,3,'t'),3)
        self.assertEqual(calcArea(4,5,'r'),20)
        self.assertEqual(calcArea(4,4,'c'),  50.26548245743669)

if __name__ == '__main__':
    unittest.main()   
