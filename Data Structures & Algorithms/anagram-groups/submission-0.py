class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    # Initialize a dictionary to store grouped anagrams
        anagram_map = {}

        for s in strs:
            # Sort the string to create a unique key
            # "eat", "tea", and "ate" all become "aet"
            sorted_s = "".join(sorted(s))
            
            # If the key doesn't exist, create an empty list
            if sorted_s not in anagram_map:
                anagram_map[sorted_s] = []
            
            # Append the original string to the corresponding list
            anagram_map[sorted_s].append(s)
        
        # Return all the values (the sublists) from the dictionary
        return list(anagram_map.values())
        