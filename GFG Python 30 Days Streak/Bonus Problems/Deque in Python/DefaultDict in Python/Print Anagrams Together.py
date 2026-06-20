from collections import defaultdict
class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        mp = defaultdict(list)
        for word in arr:
            key = ''.join(sorted(word))
            mp[key].append(word)
        return list(mp.values())