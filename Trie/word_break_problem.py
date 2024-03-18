class Node:
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    def insert_word(self, word):
        current = self.root
        for ch in word:
            index = ord(ch) - ord("a")
            if current.children[index] == None:
                current.children[index] = Node()
            current = current.children[index]
        current.end_of_word = True

    def search_word(self, word):
        current = self.root
        for ch in word:
            index = ord(ch) - ord("a")
            if current.children[index] == None:
                return False
            current = current.children[index]
        else:
            if current.end_of_word == True:
                return True  
            else:
                return False  
            
    def word_break(self, key_word):
        if len(key_word) == 0:
            return True
        res = None
        for i in range(1, len(key_word)+1):
            first_part = key_word[:i]
            second_part = key_word[i:]
            res = self.search_word(first_part)
            if res == True and self.word_break(second_part) == True:
                return True
        return False


words = ["i", "like", "sam", "samsung", "mobile"]
key_word = "ilikesam"

t = Trie()
for i in words:
    t.insert_word(i)

print(t.search_word("like"))
print(t.word_break(key_word))
