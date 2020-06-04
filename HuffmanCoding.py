import fileinput,math,sys
import Queue
from collections import Counter


#Huffman Code
class HuffmanNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root     
    def children(self):
        return((self.left, self.right))

def create_tree(frequencies):
    p = Queue.PriorityQueue()
    for value in frequencies:
        p.put(value) 			 # 1. Create a leaf node for each symbol and add it to the priority queue
    while p.qsize() > 1:         # 2. While there is more than one node
        l, r = p.get(), p.get()  # 2a. remove two highest nodes
        node = HuffmanNode(l, r) # 2b. create internal node with children
        p.put((l[0]+r[0], node)) # 2c. add new node to queue      
    return p.get()               # 3. tree is complete - return root node


# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
	if isinstance(node[1].left[1], HuffmanNode):
		walk_tree(node[1].left,prefix+"0", code)
	else:
		code[node[1].left[1]]=prefix+"0"
	if isinstance(node[1].right[1],HuffmanNode):
		walk_tree(node[1].right,prefix+"1", code)
	else:
		code[node[1].right[1]]=prefix+"1"

	return (code)

def calculateTotalBytes_withouthuffman(currfreq):
	bytes_fixedlength = (currfreq * 5)
	return bytes_fixedlength


def calculateTotalBytes_withhuffman(codeFreq,currfreq):
	return len(codeFreq) * currfreq

# Reversing a list using reversed() to form a Huffman tree
def Reverse(tuples): 
    new_tup = () 
    for k in reversed(tuples): 
        new_tup = new_tup + (k,) 
    return new_tup 


#Reading the book - book.txt
def read_book(filename):
	temp = ""
	
	for line in fileinput.input(filename):
		line = line.lower()
		for char in line:
			if char not in alphabets:
				line = line.replace(char , "")
		temp += line
	return temp

#removing extra special characters
alphabets = "abcdefghijklmnopqrstuvwxyz.,!?' "
textBook = read_book("book.txt")
counts = list(Counter(textBook).items())

freq = []
for t in counts:
	freq.append(Reverse(t))

node = create_tree(freq)
code = walk_tree(node)

totalFreq = 0
totalBytes = 0
totalhuffman = 0
print "--------------Huffman Coding---------------"
print "Symbol frequency \tCode"
for i in sorted(freq, reverse=True):
	print i[1],"\t", i[0],"\t\t", code[i[1]]
	totalFreq += i[0]
	totalBytes += calculateTotalBytes_withouthuffman(i[0])
	totalhuffman += calculateTotalBytes_withhuffman(code[i[1]], i[0])


print "--------RESULT--------"
print "The text was encoded using", totalhuffman," bits."
print "The text had", totalFreq," valid characters." 
print "Using a 5-bit fixed length encoding, this would have been", totalBytes,"bits long,"
print "So we saved", (totalBytes - totalhuffman)," bits!"
