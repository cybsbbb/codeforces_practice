import sys
import heapq
import collections
from typing import *

# LeetCode: 3008


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # KMP algorithm
        def build_prefix(pattern):
            prefix_matches = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = prefix_matches[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                prefix_matches[i] = j
            return prefix_matches

        def kmp_match(pattern, text, prefix_matches):
            occurrences = []
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = prefix_matches[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == len(pattern):
                    occurrences.append(i - j + 1)
                    j = prefix_matches[j - 1]
            return occurrences

        prefix_a = build_prefix(a)
        prefix_b = build_prefix(b)

        index_a =  kmp_match(a, s, prefix_a)
        index_b =  kmp_match(b, s, prefix_b)

        ans = []
        j = 0
        for i in range(len(index_a)):
            while j < len(index_b) and index_b[j] < index_a[i] - k:
                j += 1
            if j < len(index_b) and abs(index_a[i] - index_b[j]) <= k:
                ans.append(index_a[i])

        return ans
