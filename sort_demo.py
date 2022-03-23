"""CSC108: Fall 2020 -- Assignment 3: Twitterverse 

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Diane Horton, 
Michael Liut, Jacqueline Smith, and Anya Tafliovich.

---

This file demonstrates how you can control a sorting function by giving it a 
function to use when comparing two elements of the list.

Notice that we sort the list of strings by putting the ones that are
"smallest" in a sense at the front, but we later sort a list of dicts by
putting the ones that are "biggest" in a sense at the front. What determines
this orientation (ascending or descending order) is the return value from the
function we pass to sort. We simply need that function to return -1 if the
first argument should appear before the second argument in the final sorted
list, +1 if it should appear after, and 0 if their relative order doesn't
matter.

In this demo, and in the provided Twitter sorting function, we're using the
insertion sort algorithm. This could be replaced with any other sorting 
algorithm; we just chose one that you've already learned.
"""

from typing import Dict, Callable


def biggest_max(d1: Dict[str, int], d2: Dict[str, int]) -> int:
    """Return -1 if the maximum value in d1 is bigger than the maximum value 
    in d2, 1 if it is smaller, and 0 if they are equal.
    
    The examples below also show how to write multi-line docstring examples, 
    using ... to start lines that are continuations of the previous one.
    
    >>> biggest_max({"Jo": 2, "Nate": 99, "Mari": 45}, 
    ... {"Reuben": 54, "Zoya": 11, "Jiaqi": 9})
    -1
    >>> biggest_max({"Reuben": 54, "Zoya": 11, "Jiaqi": 9}, 
    ... {"Jo": 2, "Nate": 99, "Mari": 45})
    1
    """
    
    d1_max = max(d1.values())
    d2_max = max(d2.values())
    if d1_max > d2_max:
        return -1
    elif d1_max < d2_max:
        return 1
    else:
        return 0
    
    
def shorter(s1: str, s2: str) -> int:
    """Return -1 if string s1 is shorter than string s2, 1 if it is longer,
    and 0 if they have equal length.
    
    >>> shorter('cat', 'kitten')
    -1
    >>> shorter('meow', 'cat')
    1
    >>> shorter('cat', 'dog')
    0
    """
    
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    else:
        return 0
    
    
def my_sort(data: list, cmp: Callable) -> None:
    """Sort the data list using the comparison function cmp.
    
    Precondition: cmp takes exactly two arguments of the same time as the items
    in data.
    
    >>> L = ["Once", "upon", "a", "time", 
    ... "there", "was", "a", "curious", "girl"]
    >>> # Sort the list using Python's default behaviour. 
    >>> # It will sort alphabetically, first uppercase, then lowercase letters.
    >>> L.sort()
    >>> L
    ['Once', 'a', 'a', 'curious', 'girl', 'there', 'time', 'upon', 'was']
    >>> # Now sort it so that we control how pairs of list items are compared.
    >>> # Tell sort to compare using function shorter.  The shorter strings
    >>> # will be at the front of the updated list.
    >>> my_sort(L, shorter)
    >>> L
    ['a', 'a', 'was', 'Once', 'girl', 'time', 'upon', 'there', 'curious']
    >>> # Now try sorting a list of dictionaries.
    >>> L2 = [{"Myrka": 23, "Harbinder": 18}, {"Jo": 2, "Nate": 99, "Mari": 45}, 
    ... {"Reuben": 54, "Zoya": 11, "Jiaqi": 9}, {"Zara": 2}]
    >>> # We actually can't sort a list of dictionaries using Python's default sort. 
    >>> # How would it decide how to order the dictionaries?
    >>> # Uncomment the line below to see the error.
    >>> # L2.sort()
    >>> # Now tell Python to sort using the biggest_max function.  Dictionaries
    >>> # whose maximum key is largest will be at the front of the updated list.
    >>> my_sort(L2, biggest_max)
    >>> L2
    [{'Jo': 2, 'Nate': 99, 'Mari': 45}, \
{'Reuben': 54, 'Zoya': 11, 'Jiaqi': 9}, {'Myrka': 23, 'Harbinder': 18}, \
{'Zara': 2}]
    """
    
    # Insertion sort
    for i in range(1, len(data)):
        current = data[i]
        position = i
        while position > 0 and cmp(data[position - 1], current) > 0:
            data[position] = data[position - 1]
            position = position - 1 
        data[position] = current 
    
    
if __name__ == "__main__":
    
    import doctest
    doctest.testmod()
      