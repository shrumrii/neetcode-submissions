class PrefixTreeNode: 

    def __init__(self):
        self.children = {} 
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        q = list(word)
        curr = self.root

        while q: 
            
            letter = q.pop(0) 
            if letter not in curr.children: 
                curr.children[letter] = PrefixTreeNode() 
            curr = curr.children[letter]  

        curr.is_word = True

    def search(self, word: str) -> bool:

        q = list(word) 
        curr = self.root 
        while q: 

            letter = q.pop(0) 
            if letter not in curr.children: 
                return False 
            else: 
                curr = curr.children[letter]
        
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        q = list(prefix) 
        curr = self.root 
        while q: 

            letter = q.pop(0) 
            if letter not in curr.children: 
                return False 
            else: 
                curr = curr.children[letter]

        return True 

        
        