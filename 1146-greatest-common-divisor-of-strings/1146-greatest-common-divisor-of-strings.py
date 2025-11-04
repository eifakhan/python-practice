class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        len1 = len(str1)
        len2 = len(str2)
        
        gcd_length = math.gcd(len1, len2)
        
        return str1[:gcd_length]      