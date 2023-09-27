$Tree$

[TOC]

## Define  
A class of Connected undirected graphs without loops.

- root node: A node without forward nodes, and a tree has only one root node.
- leaf node: A node that has no children.
- depth: Number of edges in the simple path from node to root node. The depth of the tree is the maximum node depth in the tree.

## Property

- There exists and only exists one single simple path between any two points of the tree.
- $number(E) = number(V) - 1$
- Delete an edge, the Tree will become disconnected;  
  Add an edge, the Tree will have a loop.

## Include

### Binary tree

- Define  
  A tree in which each node has at most two children, which are referred to as the left child and the right child.

- Property
  * Traversal of Tree
    - Depth-First Traversal
      - Preorder Traversal
        ```c
        void traversal(Node* root, vector<Node*> arr) {
          arr.push_back(root);
          traversal(root->left);
          traversal(root->right);
        }
        ```

      - Inorder Traversal
        ```c
        void traversal(Node* root, vector<Node*> arr) {
          traversal(root->left);
          arr.push_back(root);
          traversal(root->right);
        }
        ```

      - Postorder Traversal
        ```c
        void traversal(Node* root, vector<Node*> arr) {
          traversal(root->left);
          traversal(root->right);
          arr.push_back(root);
        }
        ```

    - Breadth-First Traversal: level trversal

- Include
  * Complete Binary Tree
    - Define  
      A binary tree in which all leaf nodes have the same height.

    - Property
      - Number of nodes with depth $h$: $2^h$  
        Number of nodes in a complete binary tree with depth $h$: $2^{h+1} - 1$  
        Number of non leaf nodes: $2^h - 1$  
        Number of leaf nodes: $2^h$  

        - Proof
          $$
          \sum\limits_{i=0}^h 2^i = \frac{1 - 2^h}{1 - 2} = 2^h - 1  \tag{geometric sequence summation}
          $$

