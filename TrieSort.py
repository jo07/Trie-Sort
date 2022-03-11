import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for w in word:
            current = current.children[w]
        current.count += 1

class TrieSort:
    def __init__(self):
        self.res = []
        self.max_num_len = 0
        
    def buildTrie(self, nums):
        trie = Trie()
        self.max_num_len = len(str(max(nums))) # We get the highest number's max value of digits 
        for num in nums:
            num_len = len(str(num))
            zero_len = self.max_num_len - num_len
            trie.insert('0'* zero_len + str(num))
        return trie.root

    def trieSort(self, node, word, depth):
        for i in range(0, 10):
            i = str(i)
            if not node.children.get(i):
                continue
            if depth == self.max_num_len-1:
                self.res += [int(word+i)] * node.children.get(i).count
            self.trieSort(node.children.get(i), word + i, depth +1)
            
    def sort(self, nums):
        trie = self.buildTrie(nums)
        # we start at root node with an empty word and at depth zero
        self.trieSort(trie, "", 0)
        return self.res