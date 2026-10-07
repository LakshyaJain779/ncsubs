class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        
        for letter in s.upper():
            if ((ord(letter) >= 48 and ord(letter) <= 57) or (ord(letter) >= 65 and ord(letter) <= 90)):
                    string += letter

        
        return string[::-1]==string
        