'''Given a string s, find the length of the longest substring without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
        
def main():
    str = input("Enter a string: ")
    solution = Solution()
    res = solution.lengthOfLongestSubstring(str)
    print(res)
if __name__ == "__main__":
    main()