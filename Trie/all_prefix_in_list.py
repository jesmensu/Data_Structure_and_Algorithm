# Find the largest word in the list whose all the prefix is in the list

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

    def word_with_all_prefix(self):
         target_word = ""
         temp_word = ""
         current = self.root
         target_word = self.check_children(current, target_word, temp_word)
         return target_word
    
    def check_children(self, current, target_word, temp_word):
        children = current.children
        for i in range(26):
            if children[i] != None and children[i].end_of_word == True:
                int_of_char = ord("a") + i
                temp_word += chr(int_of_char)
                if len(temp_word)> len(target_word):
                    target_word = temp_word
                target_word = self.check_children(children[i], target_word, temp_word)
                temp_word = temp_word[:-1]
        return target_word

        
t = Trie()
words = ["a", "ap", "app", "appl", "pp", "apply", "apple"]
for word in words:
    t.insert_word(word)
print(t.word_with_all_prefix())
