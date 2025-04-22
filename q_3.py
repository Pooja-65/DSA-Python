'''Given a string s, find the length of the longest substring without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        for i in range(len(s)):
            my_str=s[i]
            while(i+1<len(s) and s[i+1] not in my_str):
                my_str = my_str+s[i+1]
                i+=1
            if len(my_str)>max_len:
                max_len = len(my_str)
        return max_len
def main():
    str = input("Enter a string: ")
    solution = Solution()
    res = solution.lengthOfLongestSubstring(str)
    print(res)
if __name__ == "__main__":
    main()