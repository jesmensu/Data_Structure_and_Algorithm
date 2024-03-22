#  For substring, we can first take all the sufix and then if we take all the prefixes of all sufix,
#  we will get all the substring

# If we will create trie with the sufixes of the word, then take the prefixes, we will get all the distinct substring  


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
            
    def get_all_prefix(self):
        current = self.root
        prefixes = []
        temp_string = ""
        prefixes.append(temp_string)
        prefixes = self.check_the_children(current, prefixes, temp_string)
        return prefixes

    def check_the_children(self, current, prefixes, temp_string):
        children = current.children
        for i in range(26):
            if children[i] != None:
                int_for_char = ord("a") + i
                st = chr(int_for_char)
                temp_string += st
                prefixes.append(temp_string)
                prefixes = self.check_the_children(children[i], prefixes, temp_string)
                temp_string = temp_string.rstrip(temp_string[-1])
        return prefixes

    def distinct_substring(self, word):
        list_of_sufixes = []
        for i in range(len(word)):
            list_of_sufixes.append(word[i:])
            self.insert_word(word[i:])
        prefixes = self.get_all_prefix()
        print(prefixes)

  
t = Trie()
# t.distinct_substring("apple")
# t.insert_word("apple")
t.distinct_substring("ababa")
