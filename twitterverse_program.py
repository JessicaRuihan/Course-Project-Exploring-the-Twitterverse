"""CSC108: Fall 2020 -- Assignment 3: Twitterverse 

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Diane Horton, 
Michael Liut, Jacqueline Smith, and Anya Tafliovich.
"""

import twitterverse_functions as tf

if __name__ == '__main__':
    
    data_filename = input('Data file: ')
    data_file = open(data_filename, 'r')
    data = tf.process_data(data_file)
    data_file.close()
    
    query_filename = input('Query file: ')
    query_file = open(query_filename, 'r')
    query = tf.process_query(query_file)
    query_file.close()
        
    search_results = tf.get_search_results(data, query['search'])
    filtered_results = tf.get_filter_results(data, search_results, 
                                             query['filter'])
    sorted_results = tf.get_sorted_results(data, filtered_results, 
                                              query['sorting'])
    
    print(sorted_results)
    