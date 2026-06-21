'''You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.'''

from ast import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count
        word_map = {}
        
        for word in words:
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1
        
        result_indices = []
        
        for i in range(len(s) - total_length + 1):
            seen_words = {}
            j = 0
            
            while j < word_count:
                word_index = i + j * word_length
                current_word = s[word_index:word_index + word_length]
                
                if current_word in word_map:
                    if current_word in seen_words:
                        seen_words[current_word] += 1
                    else:
                        seen_words[current_word] = 1
                    
                    if seen_words[current_word] > word_map[current_word]:
                        break
                else:
                    break
                
                j += 1
            
            if j == word_count:
                result_indices.append(i)
        
        return result_indices
                    