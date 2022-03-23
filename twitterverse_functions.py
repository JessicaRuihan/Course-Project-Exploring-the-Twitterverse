"""CSC108: Fall 2020 -- Assignment 3: Twitterverse 

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Diane Horton, 
Michael Liut, Jacqueline Smith, and Anya Tafliovich.
"""

# You can add or remove imports from the typing module as needed
from typing import Callable, Dict, List, TextIO

"""Type descriptions of TwitterverseDict, QueryDict, SearchDict, FilterDict, 
and SortingDict dictionaries. 

We use these types to simplify our type contracts, and to capture additional
information about each type, as indicated below.

You should use these types in your type contracts, inside single quotes.
e.g. def process_data(file: TextIO) -> 'TwitterverseDict':

TwitterverseDict
Twitterverse dictionary: Dict[str, Dict[str, object]]
    - each key is a username (a str)
    - each value is a Dict[str, object] with items as follows:
        - key 'name', value represents a user's name (a str)
        - key 'location', value represents a user's location (a str)
        - key 'web', value represents a user's website (a str)
        - key 'bio', value represents a user's bio (a str)
        - key 'following', value usernames of users this user is following 
          (a List[str])

QueryDict
Query dictionary: Dict[str, Dict[str, object]]
    - key 'search', value represents a search specification dictionary
    - key 'filter', value represents a filter specification dictionary
    - key 'sorting', value represents a sorting specification dictionary

SearchDict
Search specification dictionary: Dict[str, object]
    - key 'username', value represents username to begin search at (a str)
    - key 'operations', value represents the operations to perform 
      (a List[str])

FilterDict
Filter specification dictionary: Dict[str, str]
    - key 'following' might exist, value represents a username (a str)
    - key 'follower' might exist, value represents a username (a str)
    - key 'name-includes' might exist, value represents str to match 
      (a case-insensitive match)
    - key 'location-includes' might exist, value represents str to match 
      (a case-insensitive match)
    - key 'bio-includes' might exist, value represents str to match 
      (a case-insensitive match)

SortingDict
Sorting specification dictionary: Dict[str, str]
    - key 'sort-by', value represents how to sort results (a str)

"""
# A Set of Constants.
USER = 'username'
NAME = 'name'
LOCAT = 'location'
WEB = 'web'
BIO = 'bio'
FO = 'following'
BE_FO = 'follower'
BE_FOS = 'followers'
SEARCH = 'search'
FILTER = 'filter'
OP = 'operations'
LOCAT_IN = 'location-includes'
NAME_IN = 'name-includes'
BIO_IN = 'bio-includes'
SORT = 'SORT'
SORT_BY = 'sort-by'
SORT_IN = 'sorting'
POPU = 'popularity'

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####
SAMPLE_FILE = """Jessica Guo

http://www.jessica666.com
happy
every
day
ENDBIO
Sophia
Sherry
Lexi
Meixi
END
Sophia
Sophia Wang
Davis, CA

apple
ENDBIO
Jessica
Sherry
Meixi
END
Sherry
Sherry Zheng
MN, US

banana
ENDBIO
Jessica
Sophia
END
Meixi
Meixi Yu
Chicago, US


ENDBIO
Jessica
Sophia
END
Lexi
Lexi Licheng
mn, us


ENDBIO
END
"""

QUERY_FILE1 = """SEARCH
Jessica
following
following
followers
FILTER
location-includes US
following Jessica
SORT
popularity
"""

QUERY_FILE2 = """SEARCH
Sophia
followers
FILTER
bio-includes a
follower Sherry
SORT
name
"""

SAMPLE_DATA = {'Jessica': {'name': 'Jessica Guo', 'location': '',
                           'web': 'http://www.jessica666.com', 
                           'bio': 'happy\nevery\nday', 
                           'following': ['Sophia', 'Sherry', 'Lexi', 'Meixi']},
               'Sophia': {'name': 'Sophia Wang', 'location': 'Davis, CA', 
                          'web': '', 'bio': 'apple', 'following': ['Jessica',
                                                                   'Sherry', 
                                                                   'Meixi']},
               'Sherry': {'name': 'Sherry Zheng', 'location': 'MN, US', 
                          'web': '', 'bio': 'banana', 'following': ['Jessica',
                                                                    'Sophia']},
               'Meixi': {'name': 'Meixi Yu', 'location': 'Chicago, US', 
                         'web': '', 'bio': '', 'following': ['Jessica', 
                                                             'Sophia']}, 
               'Lexi': {'name': 'Lexi Licheng', 'location': 'mn, us', 'web': '',
                        'bio': '', 'following': []}}

SAMPLE_QUERY1 = {'search': {'username': 'Jessica', 'operations': ['following',
                                                                  'following',
                                                                  'followers']},
                 'filter': {'location-includes': 'US', 'following': 'Jessica'},
                 'sorting': {'sort-by': 'popularity'}}

SAMPLE_QUERY2 = {'search': {'username': 'Sophia', 'operations': ['followers']},
                 'filter': {'bio-includes': 'a', 'follower': 'Sherry'},
                 'sorting': {'sort-by': 'name'}}

     
def process_data(file: TextIO) -> 'TwitterverseDict':
    """Return the Twitterverse dictionary containing the Twitter data in file.
    No examples for file reading functions.
    """
    result = {}
    line = file.readline().strip()
    while line != '':
        result_inner = {}
        key = line
        line = file.readline().strip()
        name = line
        result_inner[NAME] = name
        line = file.readline().strip()
        location = line
        result_inner[LOCAT] = location
        line = file.readline().strip()
        web = line
        result_inner[WEB] = web
        line = file.readline()
        while line != 'ENDBIO\n':
            bio = line
            if BIO not in result_inner:
                result_inner[BIO] = bio 
            else:
                result_inner[BIO] += bio
            line = file.readline()
        if BIO in result_inner:
            result_inner[BIO] = result_inner[BIO].strip()
        follow = []
        line = file.readline().strip()
        while line != 'END':
            follow.append(line)
            line = file.readline().strip()
        result_inner[FO] = follow
        result[key] = result_inner
        line = file.readline().strip()
    return result
 
def process_query(file: TextIO) -> 'QueryDict':
    """Read the file and return the query in the query dictionary format.
    No examples for file reading functions.
    """
    result = {}
    result[SEARCH] = {}
    result[FILTER] = {}
    result[SORT_IN] = {}    
    line = file.readline().strip()
    while line != '':
        while line == 'SEARCH':
            line = file.readline().strip()
            result[SEARCH][USER] = line
        operations = []
        line = file.readline().strip()
        while line != 'FILTER':
            operations.append(line)
            line = file.readline().strip()
        result[SEARCH][OP] = operations
        line = file.readline().strip()
        while line != 'SORT':
            result[FILTER][line.split()[0]] = line.split()[-1]
            line = file.readline().strip()
        line = file.readline().strip()
        result[SORT_IN][SORT_BY] = line
        line = file.readline().strip()
    return result
     
def all_followers(dct: 'TwitterverseDict', username: str) -> List[str]:
    """Identify all the usernames that are following the user specified by the 
    second parameter and return them as a list.
    >>> all_followers(SAMPLE_DATA,'Jessica')
    ['Sophia', 'Sherry', 'Meixi']
    >>> all_followers(SAMPLE_DATA,'Lexi')
    ['Jessica']
    """
   
    followers = []
    for i in dct:
        if username in dct[i][FO]:
            followers.append(i)        
    return followers

def all_following(dct: 'TwitterverseDict', username: str) -> List[str]:
    """Identify all the usernames that are followed by the user specified by the 
    second parameter and return them as a list.
    >>> all_following(SAMPLE_DATA,'Jessica')
    ['Sophia', 'Sherry', 'Lexi', 'Meixi']
    >>> all_following(SAMPLE_DATA,'Lexi')
    []
    """
    return dct[username][FO]

def helper_1(dct: 'TwitterverseDict', current_lst: List[str]) -> List[str]:
    """Return a list if strings that have performed 'following' search 
    specification on current_lst.
    >>> helper_1(SAMPLE_DATA, ['Sophia', 'Sherry', 'Lexi', 'Meixi'])
    ['Jessica', 'Sherry', 'Meixi', 'Sophia']
    >>> helper_1(SAMPLE_DATA, ['Jessica', 'Sherry', 'Meixi', 'Sophia'])
    ['Sophia', 'Sherry', 'Lexi', 'Meixi', 'Jessica']
    """
    result = []
    for i in current_lst:
        for j in all_following(dct, i):
            if j not in result:
                result.append(j)
    return result 

def helper_2(dct: 'TwitterverseDict', current_lst: List[str]) -> List[str]:
    """Return a list if strings that have performed 'follower' search
    specification on current_lst
    >>> helper_2(SAMPLE_DATA, ['Jessica', 'Sherry'])
    ['Sophia', 'Sherry', 'Meixi', 'Jessica']
    >>> helper_2(SAMPLE_DATA, ['Lexi'])
    ['Jessica']
    """
    result = []
    for i in current_lst:
        for j in all_followers(dct, i):
            if j not in result:
                result.append(j)
    return result     
        

def get_search_results(dct1: 'TwitterverseDict', 
                       dct2: 'SearchDict') -> List[str]:  
    """Perform the specified search on the given Twitter data, and return a list
    of strings representing usernames that match the search criteria.
    >>> get_search_results(SAMPLE_DATA, SAMPLE_QUERY1[SEARCH])
    ['Sophia', 'Sherry', 'Meixi', 'Jessica']
    >>> get_search_results(SAMPLE_DATA, SAMPLE_QUERY2[SEARCH])
    ['Jessica', 'Sherry', 'Meixi']
    """ 
    new_lst = [dct2[USER]]
    for i in dct2[OP]:
        if i == FO:
            new_lst = helper_1(dct1, new_lst)
        elif i == BE_FOS:
            new_lst = helper_2(dct1, new_lst)
    return new_lst

        
def helper_3(lst: List[str], filt: str, dct3: 'FilterDict',
             dct1: 'TwitterverseDict') -> List:
    """Return the list after applying Filter 'following' or 'follower'.
    >>> helper_3(['Sophia', 'Sherry', 'Meixi', 'Jessica'], 'following',\
    SAMPLE_QUERY1['filter'], SAMPLE_DATA)
    ['Sophia', 'Sherry', 'Meixi']
    >>> helper_3(['Sherry', 'Meixi'], 'follower', SAMPLE_QUERY2['filter'],\
    SAMPLE_DATA)
    []
    """
    result = []
    if filt == FO:
        for user in lst:
            if dct3[FO] in all_following(dct1, user):
                result.append(user)
    elif filt == BE_FO:
        for user in lst:
            if dct3[BE_FO] in all_followers(dct1, user):
                result.append(user)
    return result
        

def helper_4(lst: List[str], filt: str, dct3: 'FilterDict',
             dct1: 'TwitterverseDict') -> List:
    """Retrun the list after applying the Filter 'location-includes',
    or 'bio-includes'.
    >>> helper_4(['Meixi', 'Jessica'], 'location-includes',\
    SAMPLE_QUERY1['filter'], SAMPLE_DATA)
    ['Meixi']
    >>> helper_4(['Meixi', 'Lexi'], 'location-includes',\
    SAMPLE_QUERY1['filter'], SAMPLE_DATA)
    ['Meixi', 'Lexi']
    """
    result = []
    if filt == LOCAT_IN:
        for user in lst:
            if dct3[filt].lower() in dct1[user][LOCAT].lower():
                result.append(user)
    elif filt == BIO_IN:
        for user in lst:
            if dct3[filt].lower() in dct1[user][BIO].lower():
                result.append(user)
    return result       

def helper_5(lst: List[str], dct3: 'FilterDict') -> List:
    """Retrun the list after applying the Filter 'name-includes'.
    >>> helper_5(['Meixi', 'Lexi'], {'name-includes': 'm'})
    ['Meixi']
    >>> helper_5(['Meixi', 'Lexi'], {'name-includes': 'a'})
    []
    """
    result = []
    for user in lst:
        if dct3[NAME_IN].lower() in user.lower():
            result.append(user)
    return result
    
        
def get_filter_results(dct1: 'TwitterverseDict',
                       lst: List[str], dct3: 'FilterDict') -> List[str]: 
    """Apply the specified filters to the given username list one at a time to 
    produce the filtered list, and return the resulting list of usernames.
    >>> get_filter_results(SAMPLE_DATA, ['Sophia', 'Sherry', 'Meixi',\
    'Jessica'],SAMPLE_QUERY1[FILTER])
    ['Sherry', 'Meixi']
    >>> get_filter_results(SAMPLE_DATA, ['Jessica', 'Sherry', 'Meixi'],\
    SAMPLE_QUERY2[FILTER])
    ['Jessica']
    """
    for filt in dct3:
        if 'follow' in filt:
            lst = helper_3(lst, filt, dct3, dct1)
        elif filt == NAME_IN:
            lst = helper_5(lst, dct3)
        else:
            lst = helper_4(lst, filt, dct3, dct1)
    return lst
            

def compare_by_name(dct1: 'TwitterverseDict', s1: str, s2: str) -> int:
    """return -1 if s1's name should appear before s2, 1 if the s1's name should
    appear after s2. If they are tied, return -1 if s1's username should appear 
    before s2, 1 if the s1's username should appear after s2.
    >>> compare_by_name(SAMPLE_DATA, 'Jessica', 'Sherry')
    -1
    >>> compare_by_name(SAMPLE_DATA, 'Sophia', 'Sherry')
    1
    """
    if dct1[s1][NAME] < dct1[s2][NAME]:
        return -1
    elif dct1[s1][NAME] > dct1[s2][NAME]:
        return 1
    else:
        if s1 < s2:
            return -1
        elif s1 > s2:
            return 1
    return None

def compare_by_popularity(dct1: 'TwitterverseDict', s1: str, s2: str) -> int:
    """return -1 if s1 has less followers than s2, 1 if s1 has more followers 
    than s2. If they are tied, return -1 if s1's username should appear 
    before s2, 1 if the s1's username should appear after s2.
    >>> compare_by_popularity(SAMPLE_DATA, 'Sophia', 'Sherry')
    1
    >>> compare_by_popularity(SAMPLE_DATA, 'Meixi', 'Sophia')
    -1
    """
    if len(all_followers(dct1, s1)) < len(all_followers(dct1, s2)):
        return -1
    elif len(all_followers(dct1, s1)) > len(all_followers(dct1, s2)):
        return 1
    else:
        if s1 < s2:
            return -1
        elif s1 > s2:
            return 1
    return None

def tweet_sort(twitter_data: 'TwitterverseDict', results: List[str], 
               comparison_func: Callable[['TwitterverseDict', str, str], int]
               ) -> None:
    """Modify results to be sorted using the comparison function comparison_func 
    and the data in twitter_data.
    
    The type Callable[['TwitterverseDict', str, str], int] means a function
    that takes three arguments - a TwitterverseDict, and two strings to compare,
    and returns an int. 
    
    Add examples below once you have written your own comparison functions to
    compare order usernames by name and popularity.
    >>> lst1 = ['Meixi', 'Sophia']
    >>> tweet_sort(SAMPLE_DATA, lst1, compare_by_popularity)
    >>> lst1
    ['Meixi', 'Sophia']
    >>> lst2 = ['Sophia', 'Jessica', 'Sherry']
    >>> tweet_sort(SAMPLE_DATA, lst2, compare_by_name)
    >>> lst2
    ['Jessica', 'Sherry', 'Sophia']
    """
    
    # An implementation of Insertion Sort that uses a comparison function
    for i in range(1, len(results)):
        current = results[i]
        position = i
        while position > 0 and \
                comparison_func(twitter_data, results[position - 1], 
                                current) > 0:
            results[position] = results[position - 1]
            position = position - 1 
        results[position] = current
        
        
def get_sorted_results(dct: 'TwitterverseDict',
                       lst: List[str], dct4: 'SortingDict') -> List[str]:
    """Sort the results based on the given sorting specification and return the 
    final results list.
    >>> get_sorted_results(SAMPLE_DATA, ['Sherry', 'Meixi'],\
    SAMPLE_QUERY1[SORT_IN])
    ['Meixi', 'Sherry']
    >>> get_sorted_results(SAMPLE_DATA, ['Jessica'], SAMPLE_QUERY2[SORT_IN])
    ['Jessica']
    """
    if dct4[SORT_BY] == NAME:
        tweet_sort(dct, lst, compare_by_name)
    elif dct4[SORT_BY] == POPU:
        tweet_sort(dct, lst, compare_by_popularity)
    else:
        lst.sort()
    return lst
    
  
       

if __name__ == '__main__':
    import doctest
    
    # Uncomment the call to doctest.testmod() to automatically run your
    # docstring examples when you run the twitterverse_functions.py file.
    # Note that your docstring examples must be perfectly formatted 
    # to be able to do this.
    
    doctest.testmod()
    