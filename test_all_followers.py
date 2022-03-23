"""CSC108: Fall 2020 -- Assignment 3: Twitterverse 

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Diane Horton, 
Michael Liut, Jacqueline Smith, and Anya Tafliovich.
"""

import unittest
import twitterverse_functions


class TestAllFollowers(unittest.TestCase):
    """Test cases for function twitterverse_functions.all_followers
    """
    def test_empty1(self) -> None:
        """Test all followers that a empty string has no followers if 
        twitter_data size is one.
        """
        twitter_data = \
            {'katieH': {'name': 'Katie Holmes', 'location': '',
                        'web': 'www.tomkat.com', 'bio': '', 'following': []}}  
        actual = twitterverse_functions.all_followers(twitter_data, '')
        expected = []
        self.assertEqual(actual, expected)
    
    def test_empty2(self) -> None:
        """Test all followers that a empty string has no followers if
        twitter_data size is two or more .
        """ 
        twitter_data = \
            {'tomCruise': {'name': 'Tom Cruise', 
                           'location': 'Los Angeles, CA', 
                           'web': 'http://www.tomcruise.com', 
                           'bio': 'Official TomCruise.com crew tweets. '+ \
                           'We love you guys!\nVisit us at Facebook!', 
                           'following': ['katieH']}, 
             'katieH': {'name': 'Katie Holmes', 'location': '', 
                        'web': 'www.tomkat.com', 'bio': '', 'following': []}}
        actual = twitterverse_functions.all_followers(twitter_data, '')
        expected = []
        self.assertEqual(actual, expected)    
    
    def test_zero_follower1(self) -> None:
        """Test all_followers that a user has no followers if twitter_data size 
        is one. 
        """        
        twitter_data = \
            {'katieH': {'name': 'Katie Holmes', 'location': '',
                        'web': 'www.tomkat.com', 'bio': '', 'following': []}}
        actual = twitterverse_functions.all_followers(twitter_data, 'tomCruise')
        expected = []
        self.assertEqual(actual, expected)        
          
    def test_zero_follower2(self) -> None:
        """Test all_followers that a user may not have followers if
        twitter_data size is two or more.
        """
        twitter_data = \
            {'tomCruise': {'name': 'Tom Cruise', 
                           'location': 'Los Angeles, CA', 
                           'web': 'http://www.tomcruise.com', 
                           'bio': 'Official TomCruise.com crew tweets. '+ \
                           'We love you guys!\nVisit us at Facebook!', 
                           'following': ['katieH']}, 
             'katieH': {'name': 'Katie Holmes', 'location': '', 
                        'web': 'www.tomkat.com', 'bio': '', 'following': []}}
        actual = twitterverse_functions.all_followers(twitter_data, 'tomCruise')
        expected = []
        self.assertEqual(actual, expected)    
        
    def test_single_follower(self) -> None:
        """Test all_followers with a user followed by one other user.
        """
        
        twitter_data = \
            {'tomCruise': {'name': 'Tom Cruise', 
                           'location': 'Los Angeles, CA', 
                           'web': 'http://www.tomcruise.com', 
                           'bio': 'Official TomCruise.com crew tweets. '+ \
                           'We love you guys!\nVisit us at Facebook!', 
                           'following': ['katieH']}, 
             'katieH': {'name': 'Katie Holmes', 'location': '', 
                        'web': 'www.tomkat.com', 'bio': '', 'following': []}}
        actual = twitterverse_functions.all_followers(twitter_data, 'katieH')
        expected = ['tomCruise']
        msg = "Expected {}, but got {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    
    
    def test_two_follower(self) -> None:
        """Test all_followers with twitter_data size of two or more with a user 
        followed by two other users 
        """
        twitter_data = \
            {'tomCruise': {'name': 'Tom Cruise', 
                           'location': 'Los Angeles, CA', 
                           'web': 'http://www.tomcruise.com', 
                           'bio': 'Official TomCruise.com crew tweets. '+ \
                           'We love you guys!\nVisit us at Facebook!', 
                           'following': ['katieH']}, 
             'marryM': {'name': 'Marry Mason', 'location': '', 
                        'web': '', 'bio': '', 'following': ['katieH']},
             'katieH': {'name': 'Katie Holmes', 'location': '', 
                        'web': 'www.tomkat.com', 'bio': '', 'following': []}}
        
        
        actual =  actual = twitterverse_functions.all_followers(twitter_data, 
                                                                'katieH')
        expected = ['tomCruise', 'marryM']
        self.assertEqual(actual, expected)
        
    def test_three_follower(self) -> None:
        """Test all_followers with twitter_data size two or more with a user 
        followed by three or more users 
        """
        twitter_data = \
            {'tomCruise': {'name': 'Tom Cruise', 
                            'location': 'Los Angeles, CA', 
                            'web': 'http://www.tomcruise.com', 
                            'bio': 'Official TomCruise.com crew tweets. '+ \
                            'We love you guys!\nVisit us at Facebook!', 
                            'following': ['katieH']}, 
            'williamG': {'name': 'William Gake', 'location': '', 'web': '', 
                         'bio': '', 'following': ['katieH']},
            'marryM': {'name': 'Marry Mason', 'location': '', 
                       'web': '', 'bio': '', 'following': ['katieH']},
            'katieH': {'name': 'Katie Holmes', 'location': '', 
                       'web': 'www.tomkat.com', 'bio': '', 
                       'following': []}}       
        actual = twitterverse_functions.all_followers(twitter_data, 
                                                                    'katieH')
        expected = ['tomCruise', 'williamG', 'marryM']
        self.assertEqual(actual, expected)   
        
        
    
                                                                        
    
    
if __name__ == '__main__':
    unittest.main(exit=False)
        