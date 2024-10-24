class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """将一个单词插入到Trie中"""
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_end_of_word = True

    def search(self, word):
        """在Trie中查找某个单词"""
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_end_of_word

    def delete(self, word):
        """从Trie中删除一个单词"""
        self._delete(self.root, word, 0)

    def _delete(self, node, word, index):
        """辅助函数，用于递归删除Trie中的单词"""
        if index == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0
        char = word[index]
        if char not in node.children:
            return False
        should_delete_child = self._delete(node.children[char], word, index + 1)

        if should_delete_child:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word

        return False

    def search(self, text):
        """查找给定文本中的敏感词"""
        node = self.root
        found_words = []
        for i in range(len(text)):
            node = self.root
            j = i
            while j < len(text) and text[j] in node.children:
                node = node.children[text[j]]
                j += 1
                if node.is_end_of_word:
                    found_words.append(text[i:j])
        return found_words
