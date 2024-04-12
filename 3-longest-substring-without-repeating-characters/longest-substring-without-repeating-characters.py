class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        char_index = {}  # Dictionary to store the index of each character
        
        max_length = 0
        start = 0  # Start index of the current substring
        
        for i, char in enumerate(s):
            # If the character is already in the substring,
            # update the start index to the next index of the previous occurrence + 1
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            
            # Update the index of the current character
            char_index[char] = i
            
            # Update the maximum length if needed
            max_length = max(max_length, i - start + 1)
        
        return max_length
