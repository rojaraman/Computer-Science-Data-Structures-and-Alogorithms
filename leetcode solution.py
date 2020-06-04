# Top N Competitors/Buzzwords 
692. Top K Frequent Words			
from collections import Counter
from heapq import *
class Item:
    def __init__(self,word,freq):
        self.word = word
        self.freq = freq
    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        if self.freq == other.freq:
            return self.word > other.word
        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words)
        top_k = []
        for word in word_freq:
            freq = word_freq[word]
            new_item = Item(word, freq)
            heappush(top_k, new_item)
            if len(top_k) > k:
                heappop(top_k)
        result = [ heappop(top_k).word for _ in range(k)]
        result.reverse()
        return result
       

# Zombie question
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stack_2s = []
        count_1s = 0
        minutes = 0
        len_row = len(grid)
        len_col = len(grid[0])
        for i in range(len_row):
            row = grid[i]
            for j in range(len_col):
                cell = row[j]
                if cell == 1:
                    count_1s+=1
                elif cell == 2:
                    stack_2s.append((i,j))
        if not count_1s:
            return 0
        expected_total_rotten = len(stack_2s) + count_1s
        current_rotten = 0 
        changed_flag = 0
        child = []
        while stack_2s:
            i, j = stack_2s.pop()
            current_rotten += 1
            neighbors = [ (i-1,j), (i+1,j), (i,j-1), (i,j+1) ]
            for x,y in neighbors:
                if x>=0 and x<len_row and y>=0 and y<len_col and grid[x][y] == 1:
                    child.append((x,y))
                    grid[x][y] = 2
            if not stack_2s and child:
                minutes += 1
                stack_2s.extend(child)
                child = []
                
        if current_rotten < expected_total_rotten:
            return -1
        else:
            return minutes

# Product Suggestions 	  
1268. Search Suggestions System
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        results = [ [] for each in range(len(searchWord)) ]
        i_s = 0
        len_searchWord = len(searchWord)
        for i in range(len(products)):
            prod_item = products[i]
            if prod_item[0:i_s+1] == searchWord[0:i_s+1]:
                results[i_s].append(prod_item)
                i_curr = i_s+1
                while i_curr<len_searchWord and i_curr<len(prod_item):
                    if prod_item[i_curr] == searchWord[i_curr]:
                        results[i_curr].append(prod_item)
                        i_curr += 1
                    else:
                        break
            while i_s<len_searchWord and len(results[i_s]) == 3:
                i_s += 1
                
        return results
		
# Trie Node solution
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.isLast = False
        self.children = [None]*26 #list of TrieNodes

class Solution:
      
    def __init__(self):
        self.ind = lambda ch : ord(ch)-ord('a')
        self.root = TrieNode("")
        
    def addToTrie(self, string):
        # adds string to a Trie tree
        root = self.root
        for i in range(len(string)):
            ch = string[i]
            if not root.children[self.ind(ch)]:
                root.children[self.ind(ch)] = TrieNode(ch)
            curr_node = root.children[self.ind(ch)]
            if i == len(string)-1:
                curr_node.isLast = True
            root = curr_node             
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        for prod_item in products:
            if prod_item[0] == searchWord[0]:
                self.addToTrie(prod_item)
            
        startNodes = {}
        root = self.root
        for i in range(len(searchWord)):
            ch = searchWord[i]
            if root and root.children[self.ind(ch)]:
                startNodes[i] = root.children[self.ind(ch)]
                root = root.children[self.ind(ch)]
            else:
                startNodes[i] = None
                root = None
                
        def dfsFind3(node, num_words, word, output):
                if not node:
                    return num_words, output
                if node in visited:
                    memo_result = result[visited[node]][0:num_words]
                    output.extend(memo_result)
                    num_words -= len(memo_result) 
                    return num_words, output
                elif node.isLast:
                    num_words-=1
                    output.append(word+node.char)

                for child in node.children:
                    if child and num_words>0:
                        num_words, output = dfsFind3(child, num_words, word+node.char, output)
                return num_words, output     
                
        visited = {}  
        result = [None]*len(searchWord)
        for i in range(len(searchWord)-1,-1,-1):
            headnode = startNodes[i]   
            _, output = dfsFind3(headnode, 3, searchWord[0:i], [])
            result[i] = output
            visited[headnode] = i
            
        return result
		
# Treasure Island			
# 286. Walls and Gates
from queue import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return rooms
        
        ind_0s = []
        len_row = len(rooms)
        len_col = len(rooms[0])
        for i in range(len_row):
            for j in range(len_col):
                if rooms[i][j] == 0:
                    ind_0s.append((i,j))
        que = ind_0s
        while que:
            i,j = que.pop()
            neighbors = [(i,j-1), (i-1,j), (i,j+1), (i+1,j)]
            if rooms[i][j] == 0:
                parent_distance = 0
            else:
                parent_distance = rooms[i][j]
            for x, y in neighbors:
                if x>=0 and x<len_row and y>=0 and y<len_col and rooms[x][y]!=-1 and rooms[x][y] and \
                                                                            parent_distance+1 < rooms[x][y]:
                        que.append((x,y))
      rooms[x][y] = parent_distance+1			

# 200. Number of Islands	  
# space complexity good
class Node:
    def __init__(self,index=()):
        self.index = index
        self.children = []
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n_row = len(grid)
        n_col = len(grid[0])
        count = 0
        stack = []
        for i in range(0,n_row):
            for j in range(0,n_col):
                if grid[i][j] == '1':
                    stack.append((i,j))
                    count+=1
                    grid[i][j] = "0"
                while stack:
                    x,y = stack.pop()
                    hor_ver = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                    for (a,b) in hor_ver:
                        if a>=0 and a<n_row and b>=0 and b<n_col and grid[a][b]=='1':
                            grid[a][b] = "0"
                            stack.append((a,b))
        return count
# recursion - time complexity good
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recur(ind,grid):
            (i,j) = ind
            n_row = len(grid)
            n_col = len(grid[0])
            grid[i][j] = '0'
            if i+1<n_row and grid[i+1][j] == '1':
                grid = recur((i+1,j),grid)
            if i-1>=0 and grid[i-1][j] == '1':
                grid = recur((i-1,j),grid)
            if j+1<n_col and grid[i][j+1] == '1':
                grid = recur((i,j+1),grid)
            if j-1>=0 and grid[i][j-1] == '1':
                grid = recur((i,j-1),grid)
            
            return grid
            
        if not grid:
            return 0
        count = 0
        n_row = len(grid)
        n_col = len(grid[0])
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == '1':
                    count+=1
                    grid = recur((i,j),grid)
        return count	  
