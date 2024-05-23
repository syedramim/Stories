import unittest
from  datetime import time 
from clean_functions import *

class TestCases(unittest.TestCase):

    def test_calculate_downvotes(self):
        #Arrange
        upvotes = 100
        upvote_ratio = 0.7
        
        #Act
        downvotes = calculate_downvotes(upvotes, upvote_ratio)
        
        #Assert
        self.assertEqual(downvotes, 43)
        
    def test_convert_to_time(self):
        #Arrange 
        date = "03:12"
        
        #Act
        dt = convert_to_time(date)
        
        #Assert
        self.assertEqual(dt, time(3,12,0))
        
        
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
