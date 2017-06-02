#fastest
isPalindrome = lambda (s) : s == s[::-1]

#deals with ints
isPalindromeInts = lambda (s) : str(s) == str(s)[::-1]

#normally in english palindromes ignore punctuation, case, and whitespace
import re
def isEnglishPalindrome(s):
  pattern = re.compile(r"\W+")
  s = re.sub(pattern,"",s).lower()
  return s == s[::-1]

#basic tests
if __name__ == "__main__":
  print(isPalindrome("aba"))
  print(isPalindrome("abc"))
  print(isPalindromeInts(121))
  print(isPalindromeInts(123))
  print(isPalindromeInts("121"))
  print(isPalindromeInts("123"))
  print(isEnglishPalindrome("A man, a plan, a canal -- Panama"))
  print(isEnglishPalindrome("Gullible is a palindrome is a palindrome!")) 
