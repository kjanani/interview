# Janani Kalyanam
# Answer for mocks

'''

Problem description:
Given a list of strings, output the string that occurs the second
most frequent number of times.  If there is more than one such string,
then output an alphabetically ordered list.

'''


import os, sys
from collections import Counter


def find_second_most_freq(input_list):
    '''
    input_list is a list of strings.
    Assume length n (for analyzing time complexity).
    output will also be a list of strings or a string.
    '''
    if(len(input_list) == 0):
        return [];

    # create using strings:counts as key:value pairs, create a dictionary 
    words_counts = dict(Counter(input_list));
    # Time complexity: Order-n

    # convert the dictionary into a list of tuples using items()
    # sort according to the counts of each string in descending order
    words_counts = sorted(words_counts.items(), key = lambda x: x[1], reverse = True);
    # Time complexity: O(m log m) where m is the number of unique strings


    # to find all the strings with the second to top frequency: 
    # (1) find the max (so that you can ignore it)
    # (2) starting appending the second to top frequent string:counts pairs to a list.
    # (3) Stop once you have gone through all the second to top frequency.

    max_freq = words_counts[0][1];
    second_top_frequent_list = [];
    for each in words_counts:

        # skip all the top freq
        if(each[1] == max_freq):
            continue;

        # finished with all the max_freq strings, so start appending the second to top frequence
        # to a list
        if(len(second_top_frequent_list) == 0):
            second_top_frequent_list.append(each);
            continue;

        # make sure that only the second to top freq is appended.  If you start encountering the
        # third to top, then you should break from the loop.
        if(second_top_frequent_list[0][1] == each[1]):
            second_top_frequent_list.append(each);
        else:
            break;

    # time complexity of the for-loop above:  O(p) where p = (number of strings with top-freq) + (number of strings with second-top freq)
    
    # OK, second_top_frequent_list is a list tuples -- each tuple is (string, count) where count is the same
    # for all the tuples in the list.  And that count is the second to top frequency.
    
    # Get rid of the frequencies
    second_top_frequent_list = list(map(lambda x: x[0], second_top_frequent_list));
    # constant time complexity

    # return
    if(len(second_top_frequent_list) > 1): # many strings with second-top frequency, so sort them alphabetically
        return sorted(second_top_frequent_list);
    elif(len(second_top_frequent_list) == 1):  # only one string at the second-top frequency, so return the string itself
        return second_top_frequent_list[0];
    else: # if there are no strings at the second-top frequency, then we return an empty string
        return [];

    # time complexity: O(q log q) where number of strings with second-top freq


    # Total time complexity = O(n + m log m + p + q log q)
    # if n and m are comparable, and p << n,m and q << n,m then complexity if O(m log m)

def alternate_approach(input_list):
     '''
    input_list is a list of strings.
    Assume length n (for analyzing time complexity).
    output will also be a list of strings or a string.
    '''
    if(len(input_list) == 0):
        return [];

    # create using strings:counts as key:value pairs, create a dictionary 
    words_counts = dict(Counter(input_list));
    # Time complexity: Order-n

    # now, let's switch the keys and values and create a dictionary where
    # the keys are counts and the corresponding lists are 

    # convert the dictionary into a list of tuples using items()
    # sort according to the counts of each string in descending order
    words_counts = sorted(words_counts.items(), key = lambda x: x[1], reverse = True);
    # Time complexity: O(m log m) where m is the number of unique strings


    # to find all the strings with the second to top frequency: 
    # (1) find the max (so that you can ignore it)
    # (2) starting appending the second to top frequent string:counts pairs to a list.
    # (3) Stop once you have gone through all the second to top frequency.

    max_freq = words_counts[0][1];
    second_top_frequent_list = [];
    for each in words_counts:

        # skip all the top freq
        if(each[1] == max_freq):
            continue;

        # finished with all the max_freq strings, so start appending the second to top frequence
        # to a list
        if(len(second_top_frequent_list) == 0):
            second_top_frequent_list.append(each);
            continue;

        # make sure that only the second to top freq is appended.  If you start encountering the
        # third to top, then you should break from the loop.
        if(second_top_frequent_list[0][1] == each[1]):
            second_top_frequent_list.append(each);
        else:
            break;

    # time complexity of the for-loop above:  O(p) where p = (number of strings with top-freq) + (number of strings with second-top freq)
    
    # OK, second_top_frequent_list is a list tuples -- each tuple is (string, count) where count is the same
    # for all the tuples in the list.  And that count is the second to top frequency.
    
    # Get rid of the frequencies
    second_top_frequent_list = list(map(lambda x: x[0], second_top_frequent_list));
    # constant time complexity

    # return
    if(len(second_top_frequent_list) > 1): # many strings with second-top frequency, so sort them alphabetically
        return sorted(second_top_frequent_list);
    elif(len(second_top_frequent_list) == 1):  # only one string at the second-top frequency, so return the string itself
        return second_top_frequent_list[0];
    else: # if there are no strings at the second-top frequency, then we return an empty string
        return [];

    # time complexity: O(q log q) where number of strings with second-top freq


    # Total time complexity = O(n + m log m + p + q log q)
    # if n and m are comparable, and p << n,m and q << n,m then complexity if O(m log m)





if __name__ == '__main__':
    
    input1 = ['z','d','a','d','s','a','c','a','m'] # Answer should be a string: d 
    input1 = ['z','d','a','d','s','a','c','a','m', 'm','c'] # Answer should be a list: ['c','d','m'] 
    input1 = ['z'] # Answer should be an empty list: []
    input1 = ['z','z','z','z','z'] # Answer should be: []
    input1 = [] # Answer should be: []
    print(find_second_most_freq(input1))

