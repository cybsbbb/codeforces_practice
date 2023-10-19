class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res = []
        word_map = defaultdict(list)
        self.findneighbors(beginWord, wordList, word_map)
        for word in wordList:
            self.findneighbors(word, wordList, word_map)
        queue = deque()
        # curword, length, prenode       
        queue.append(graphnode(beginWord, [], 1))
        visited = set()
        visited.add(beginWord)
        while queue:
            cur = queue.popleft()
            cur_word = cur.word
            cur_level = cur.level
            pre_word = cur.pre
            if cur_word == endWord:
                self.dfs(beginWord, cur, [cur_word], res)
            neis = word_map[cur_word]
            for nei in neis:
                # if nei.word == endWord:
                #     self.dfs(beginWord, cur, [cur_word], res)
                if nei.word not in visited:
                    visited.add(nei.word)
                    nei.level = cur_level + 1
                    nei.pre.append(cur)
                    queue.append(nei)
                elif nei.word in visited:
                    print(cur_word, cur_level, nei.word, nei.level, len(nei.pre))
                    print(visited)
                    # print(nei.level, cur_level)
                    if nei.level == cur_level + 1:
                        nei.pre.append(cur)
        return res

    def dfs(self, beginword, curword, cur_res, res):
        if curword.word == beginword:
            res.append(cur_res[::-1])
            return
        pre = curword.pre
        for preword in pre:
            cur_res.append(preword.word)
            self.dfs(beginword, preword, cur_res, res)
            cur_res.pop()

    def findneighbors(self, word, wordList, word_map):
        word_list = list(word)
        for i in range(0, len(word)):
            cur_char = word_list[i]
            for j in range(ord('a'), ord('z') + 1):
                replace_char = chr(j)
                if replace_char == cur_char:
                    continue
                word_list[i] = replace_char
                changed_word = "".join(word_list)
                if changed_word in wordList:
                    word_map[word].append(graphnode(changed_word, [], -1))
                word_list[i] = cur_char


class graphnode():
    def __init__(self, word, pre, level):
        self.word = word
        self.pre = pre
        self.level = level