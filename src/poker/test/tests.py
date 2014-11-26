'''
Created on 24/11/2014

@author: helio
'''
import unittest
from poker.poker import poker, rank_mao, straigth
from poker.dados import straight_flush2, quadra1, full_house1


class Test(unittest.TestCase):


    def testPoker(self):
        self.assertEqual(poker([straight_flush2, quadra1]), straight_flush2)
        self.assertEqual(poker([full_house1, quadra1]), quadra1)
        self.assertEqual(poker([straight_flush2, full_house1]), straight_flush2)
        #self.assertEqual(poker([straight_flush2, straight_flush2]), None)
         
    def testRank_mao(self):
        self.assertEqual(rank_mao(straight_flush2), 9)
        self.assertEqual(rank_mao(quadra1), 8)
        self.assertEqual(rank_mao(full_house1), 7)
        
    def testStraigth(self):
        self.assertEqual(straigth([12,11,10,9,8]), True)
        self.assertEqual(straigth([12,11,11,9,8]), False)
        self.assertEqual(straigth([4,4,4,4,6]), False)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPoker']
    unittest.main()