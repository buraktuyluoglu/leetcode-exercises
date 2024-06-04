class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words_len = word_len * len(words)
        words_count = Counter(words)
        
        result = []
        
        for i in range(len(s) - total_words_len + 1):
            seen = {}
            for j in range(len(words)):
                word_start = i + j * word_len
                word = s[word_start:word_start + word_len]
                if word in words_count:
                    if word in seen:
                        seen[word] += 1
                    else:
                        seen[word] = 1
                    
                    if seen[word] > words_count[word]:
                        break
                else:
                    break
            
            if seen == words_count:
                result.append(i)
        
        return result