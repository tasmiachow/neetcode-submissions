class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        curr = self.root 
        for c in word: 
            if c not in curr.children: 
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True 

    def search(self, word: str) -> bool:
        '''
        initial mistake: was to continue in the for loop
        but it does not go to the correct depth it will     stay at the root. '..y' might not be in root.children  
        '''
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)

