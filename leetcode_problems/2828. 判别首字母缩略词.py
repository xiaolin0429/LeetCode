"""
示例 1：
输入：words = ["alice","bob","charlie"], s = "abc"
输出：true
解释：words 中 "alice"、"bob" 和 "charlie" 的第一个字符分别是 'a'、'b' 和 'c'。因此，s = "abc" 是首字母缩略词。

示例 2：
输入：words = ["an","apple"], s = "a"
输出：false
解释：words 中 "an" 和 "apple" 的第一个字符分别是 'a' 和 'a'。
串联这些字符形成的首字母缩略词是 "aa" 。
因此，s = "a" 不是首字母缩略词。

示例 3：
输入：words = ["never","gonna","give","up","on","you"], s = "ngguoy"
输出：true
解释：串联数组 words 中每个字符串的第一个字符，得到字符串 "ngguoy" 。
因此，s = "ngguoy" 是首字母缩略词。

提示：
1 <= words.length <= 100
1 <= words[i].length <= 10
1 <= s.length <= 100
words[i] 和 s 由小写英文字母组成
"""


class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        # 检查 s 的长度是否与 words 的数量匹配
        if len(words) != len(s):
            return False

        # 比较每个单词的首字母与 s 中对应的字符
        for i in range(len(words)):
            if words[i][0] != s[i]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAcronym(words=["alice", "bob", "charlie"], s="abc"))
    print(Solution().isAcronym(words=["an", "apple"], s="a"))
    print(Solution().isAcronym(words=["never", "gonna", "give", "up", "on", "you"], s="ngguoy"))
    print(Solution().isAcronym(words=["a", "b", "c"], s="abcd"))
