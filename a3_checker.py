"""A simple checker for types of functions in twitterverse_functions.py."""

from typing import Any, Dict, List
import unittest
import checker_generic
import twitterverse_functions as tf
from io import StringIO

FILENAME = 'twitterverse_functions.py'
PYTA_CONFIG = 'pyta/a3_pyta.txt'
TARGET_LEN = 79
SEP = '='

DATA_FILE = """tomCruise
Tom Cruise
Los Angeles, CA
http://www.tomcruise.com
Official TomCruise.com crew tweets. We love you guys! 
Visit us at Facebook!
ENDBIO
katieH
END
katieH
Katie Holmes

www.tomkat.com
ENDBIO
END"""

QUERY_FILE = """SEARCH
tomCruise
following
followers
FILTER
following katieH
name-includes tom
location-includes CA 
SORT
username
"""

TWITTER_DATA = {'tomCruise': {'name': 'Tom Cruise', 
                              'location': 'Los Angeles, CA', 
                              'web': 'http://www.tomcruise.com', 
                              'bio': 'Official TomCruise.com crew tweets. '+ \
                              'We love you guys!\nVisit us at Facebook!', 
                              'following': ['katieH']}, 
                'katieH': {'name': 'Katie Holmes', 'location': '', 
                           'web': 'www.tomkat.com', 'bio': '', 'following': []}}

QUERY = {'search': {'username': 'tomCruise', 
                    'operations': ['following', 'followers']}, 
         'filter': {'following': 'katieH',  
                    'name-includes': 'tom', 'location-includes': 'CA'}, 
         'sorting': {'sort-by': 'username'}}


class CheckTest(unittest.TestCase):
    """Type checker for assignment functions."""
         
    def test_process_data(self) -> None:
        """Test function process_data."""
        data_keys = ['name', 'location', 'web', 'bio', 'following']
        msg = 'process_data should return a TwitterverseDict'
        open_data_file = StringIO(DATA_FILE)
        result = tf.process_data(open_data_file)
        for user in result:
            self.assertTrue(isinstance(user, str), msg)
            self._has_these_keys(result[user], data_keys, msg)
            for key in result[user]:
                if key == 'following':
                    self.assertTrue(isinstance(result[user][key], list), msg)
                    for item in result[user][key]:
                        self.assertTrue(isinstance(item, str), msg) 
                else:
                    self.assertTrue(isinstance(result[user][key], str), msg)                           
                
    def test_process_query(self) -> None:
        """Test function process_query."""
        query_keys = ['search', 'filter', 'sorting']
        msg = 'process_query should return a valid QueryDict'
        open_query_file = StringIO(QUERY_FILE)
        result = tf.process_query(open_query_file)
        self._has_these_keys(result, query_keys, msg)   
        
        # Search spec
        self._has_these_keys(result['search'], ['username', 'operations'], msg)
        self.assertTrue(isinstance(result['search']['operations'], list), msg)
        for item in result['search']['operations']:
            self.assertTrue(isinstance(item, str), msg) 
        self.assertTrue(isinstance(result['search']['username'], str), msg)                 
                
        # Filter spec
        filter_keys = ['following', 'follower', 'name-includes', 
                       'location-includes', 'bio-includes']
        self._has_these_keys(result['filter'], filter_keys, msg)
        self._is_dict_of_Ks_and_Vs(result['filter'], str, str, msg)        
        
        # Sorting spec
        self._has_these_keys(result['sorting'], ['sort-by'], msg)
        self._is_dict_of_Ks_and_Vs(result['sorting'], str, str, msg) 
        
    def test_get_search_results(self) -> None:
        """Test function get_search_results."""
        
        self._test_returns_list_of(tf.get_search_results, 
                                   [TWITTER_DATA, QUERY['search']], [str])
        
    def test_get_filter_results(self) -> None:
        """Test function get_filter_results."""
        
        self._test_returns_list_of(tf.get_filter_results, 
                                   [TWITTER_DATA, ['tomCruise', 'katieH'], 
                                    QUERY['filter']], [str])  
        
    def test_get_sorted_results(self) -> None:
        """Test function get_sorted_results."""
        
        self._test_returns_list_of(tf.get_sorted_results, 
                                   [TWITTER_DATA, ['tomCruise', 'katieH'], 
                                    QUERY['sorting']], [str, str])  

    def test_all_followers(self) -> None:
        """Test function all_followers."""
        
        self._test_returns_list_of(tf.all_followers, 
                                   [TWITTER_DATA, 'katieH'], [str])     

    def _test_returns_list_of(self, func, args, types):
        """Check that func when called with args returns a list of elements
        of typef from types.

        """

        result = checker_generic.type_check_simple(func, args, list)
        self.assertTrue(result[0], result[1])

        msg = '{} should return a list of length {}'
        self.assertEqual(len(result[1]), len(types),
                         msg.format(func.__name__, len(types)))

        msg = ('Element at index {} in the list returned by {} '
               'should be of type {}. Got {}.')
        for i, typ in enumerate(types):
            self.assertTrue(isinstance(result[1][i], typ),
                            msg.format(i, func.__name__, typ, result[1][i]))
            
    
    def _has_these_keys(self, result: object, valid_keys: List[str], msg: str):
        """Check if result is a dict with keys from a set of valid keys.
        """
        self.assertTrue(isinstance(result, dict), msg)
        
        for k in result:
            self.assertTrue(k in valid_keys, 
                            msg + ', but key ' + str(k) + ' is not in ' + 
                            str(valid_keys))
        

    def _is_dict_of_Ks_and_Vs(self, result: object, key_tp: type, 
                                   val_tp: type, msg: str):
        """Check if result is a dict with keys of type key_tp and values
         of type val_tp.
        """

        self.assertTrue(isinstance(result, dict), msg)

        for (key, val) in result.items():
            self.assertTrue(isinstance(key, key_tp), 
                (msg + ', but one or more keys is not of type ' 
                 + str(key_tp)))
            self.assertTrue(isinstance(val, val_tp), 
                (msg + ', but value '+ str(val) + ' is not of type ' 
                 + str(val_tp)))


checker_generic.ensure_no_io('twitterverse_functions')

print(70 * '=')
print(20 * '=' + ' Start: checking coding style ' + 20 * '=')
checker_generic.run_pyta('twitterverse_functions.py', 'pyta/a3_pyta.txt')
print(20 * '=' + ' End: checking coding style ' + 20 * '=')


print('============ Start: checking parameter and return types ============')
unittest.main(exit=False)
print('============= End: checking parameter and return types =============\n')

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style')
print('  - checking type contract\n')