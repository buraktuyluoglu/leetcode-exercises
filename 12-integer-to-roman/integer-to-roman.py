class Solution:
    def intToRoman(self, num: int) -> str:
        # Define Roman numeral symbols and their corresponding values
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        # Initialize result string
        result = ""
        
        # Iterate through symbol-value pairs
        for i in range(len(values)):
            while num >= values[i]:
                # Subtract the value from num and add the corresponding symbol to the result
                num -= values[i]
                result += symbols[i]
        
        return result