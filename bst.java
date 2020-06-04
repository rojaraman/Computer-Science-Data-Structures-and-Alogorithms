package Lab12;

////////////////////////////////////////////////////////////////////////////////////
//
//  Lab 12: Binary Search Tree
//
//  @author Heoliny Jung (user: ojung)
//  Last Edited: 12/6/18
//
////////////////////////////////////////////////////////////////////////////////////

import java.util.Random;

public class BST<Key extends Comparable, Value> {

    private Node root;

    // note: the outer class has direct access to values in this inner class
    private class Node {
        private Key key;
        private Value value;
        private Node lChild;
        private Node rChild;

        // number of nodes at this subtree
        // N for the root == # of nodes in entire tree
        // N for leaf node == 1
        private int N;

        /**
         * Constructs a node with given key and value types.
         * N is the number of nodes in the subtree where this node is the root.
         * @param key key of node in tree
         * @param value value of node
         * @param N number of descendants
         */
        public Node(Key key, Value value, int N) {
            this.key = key;
            this.value = value;
            this.N = N;
            this.lChild = null;
            this.rChild = null;
        }

        /**
         * Gets the number of children this node has.
         * @return number of children
         */
        public int numChildren(){
            if (this.lChild==null&&this.rChild==null){
                return 0;
            }
            else if(!(this.lChild==null)||this.rChild==null){
                return 2;
            }
            else {
                return 1;
            }
        }

        /**
         * Adds a node to the tree.
         * Also increases the N of all nodes to who it applies.
         * @param newNode node to add to tree
         */
        public void addNode(Node newNode){
            int comp = newNode.key.compareTo(key);
            if(comp<0){
                if(lChild==null){
                    lChild = newNode;
                    this.N++;
                }
                else{
                    lChild.addNode(newNode);
                    this.N++;
                }
            }
            else if(comp>0){
                if(rChild==null){
                    rChild = newNode;
                    this.N++;
                }
                else{
                    rChild.addNode(newNode);
                    this.N++;
                }
            }
        }

        /**
         * Gets the value of this node.
         * @return value of node
         */
        public Value getValue(){
            return value;
        }

        /**
         * Processes the in-order walk of this subtree.
         * (left children), (this node), (right children)
         * @return the in-order walk of the tree for this node
         */
        public String inOrder(){
            String out = "";
            if(!(lChild==null)){
                out+=lChild.inOrder();
            }
            out+=this.value.toString()+", ";
            if(!(rChild==null)){
                out+=rChild.inOrder();
            }
            return out;
        }

        /**
         * Processes the pre-order walk of this subtree.
         * (this node), (left children), (right children)
         * @return pre-order walk of the tree for this node
         */
        public String preOrder(){
            String out=this.value.toString()+", ";
            if(!(lChild==null)){
                out+=lChild.preOrder();
            }
            if(!(rChild==null)){
                out+=rChild.preOrder();
            }
            return out;
        }

        /**
         * Processes the post-order walk of this subtree.
         * (left children), (right children), (this node)
         * @return post-order walk of the tree for this node
         */
        public String postOrder(){
            String out = "";
            if(!(lChild==null)){
                out+=lChild.postOrder();
            }
            if(!(rChild==null)){
                out+=rChild.postOrder();
            }
            out+=this.value.toString()+", ";
            return out;
        }

        /**
         * Determines if this subtree is perfectly balanced.
         * @return whether or not the node is balanced
         */
        public boolean nodeBalanced(){
            if(this.numChildren()==1){
                return false;
            }
            else if(this.N==1){
                return true;
            }
            else if(this.rChild.N==this.lChild.N){
                return rChild.nodeBalanced()&&lChild.nodeBalanced();
            }
            else{
                return false;
            }
        }
    }

    /**
     * Gets the number of nodes in the whole tree.
     * @return number of nodes in tree
     */
    public int size() {
        return root.N;
    }

    /**
     * Gets a specific value of a node with key "key"
     * If no node is found, an error message is printed and the node is returned as null.
     * @param key key of node to search for
     * @return value of that node
     */
    public Value get(Key key) {
        Node nextNode = root;
        Value val = null;
        while(!(nextNode==null)){
            if(key.compareTo(nextNode.key)==0){
                val = nextNode.value;
                return val;
            }
            else if(key.compareTo(nextNode.key)<0){
                nextNode = nextNode.lChild;
            }
            else if(key.compareTo(nextNode.key)>0){
                nextNode = nextNode.rChild;
            }
        }
        System.out.println("Error: key not found");
        return val;
    }

    /**
     * Helper method for placing a node in the tree.
     * @param key key of new node
     * @param val value of new node
     */
    public void put(Key key, Value val) {
        if(root==null){
            this.root = new Node(key,val,1);
        }
        else {
            Node newNode = new Node(key, val, 1);
            root.addNode(newNode);
        }
    }

    /**
     * Walks the whole tree in the way described by the parameter "choice".
     * @param choice string in for "in", "pre", or "post" for in-order, pre-order, or post-order.
     * @return string of all nodes in form node1, node2, node3, ..., nodeN
     */
    public String walk(String choice) {
        String walk = "";
        if(root==null){
            walk+="Root is null, cannot walk";
        }
        else if(choice.equals("in")){
            walk += root.inOrder();
            walk=walk.substring(0,walk.length()-2);
        }
        else if(choice.equals("pre")){
            walk += root.preOrder();
            walk = walk.substring(0,walk.length()-2);
        }
        else if(choice.equals("post")){
            walk += root.postOrder();
            walk = walk.substring(0,walk.length()-2);
        }
        else{
            walk+="Error, no such order choice";
        }
        return walk;
    }

    /**
     * Runs a walk of all types and outputs as:
     * "Pre-Order: x, y, z, ...
     * In-Order: z, x, y, ...
     * Post-Order: y, x, z, ..."
     * @return string all walks of tree.
     */
    @Override
    public String toString() {
        String out = "";
        out+="Pre-Order: \n";
        out+=root.preOrder();
        out+="\nIn-Order: \n";
        out+=root.inOrder();
        out+="\nPost-Order: \n";
        out+=root.postOrder();
        return out;
    }

    /**
     * Determines whether two trees are equal by comparing their toString returns.
     * @param obj object to check
     * @return boolean
     */
    @Override
    public boolean equals(Object obj) {
        String walk1 = toString();
        if(obj instanceof BST){
            String walk2 = obj.toString();
            if(walk1.equals(walk2)){
                return true;
            }
        }
        return false;
    }

    /**
     * Helper method for checking whether a tree is perfectly balanced.
     * @return boolean
     */
    public boolean isBalanced(){
        return root.nodeBalanced();
    }

    //simple tests
    public static void main(String[] args) {
        Random rand = new Random();
        BST<Integer, Character> tree = new BST<>();
        for (int i = 0; i < 25; i++) {
            int key = rand.nextInt(26) + 'a';
            char val = (char)key;
            tree.put(key, val);
        }
        // note: not all of these chars will end up being generated from the for loop
        // some of these return values will be null
        System.out.println(tree.get((int)'a'));
        System.out.println(tree.get((int)'b'));
        System.out.println(tree.get((int)'c'));
        System.out.println(tree.get((int)'f'));
        System.out.println(tree.get((int)'k'));
        System.out.println(tree.get((int)'x'));
        System.out.println(tree.walk("pre"));
        System.out.println(tree.walk("in"));
        System.out.println(tree.walk("post"));
        System.out.println(tree);
        System.out.println(tree.isBalanced());
        BST<Integer,Character> tree2 = new BST<>();
        tree2.put((int)'t','t');
        tree2.put((int)'a','a');
        tree2.put((int)'r','r');
        tree2.put((int)'q','q');
        tree2.put((int)'b','b');
        tree2.put((int)'d','d');
        tree2.put((int)'w','w');
        tree2.put((int)'s','s');
        System.out.println(tree2.walk("in"));
        System.out.println(tree2.isBalanced());
        BST<Integer,Character> tree3 = new BST<>();
        tree3.put((int)'l','l');
        tree3.put((int)'e','e');
        tree3.put((int)'p','p');
        tree3.put((int)'f','f');
        tree3.put((int)'n','n');
        tree3.put((int)'c','c');
        tree3.put((int)'z','z');
        System.out.println(tree3.isBalanced());
        System.out.println(tree3.walk("in"));
    }
}