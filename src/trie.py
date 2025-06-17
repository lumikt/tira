#Work in progress, aikainen hahmotelma rakenteesta.


class Node:

    def __init__(self, character):
        self.value = character # Contains the string of the current node
        self.children = {}  # A dictionary of child nodes which follow from current nodes
        self.frequency = 1 # The amount of times the node string has been added to data, used to calc probabilities


    def add(self, node):
        '''
        Assign a new child to the children-dictionary with the string value of the node being added as 
        key and the node object itself as the value.
        '''

        self.children[node.value]=(node)

        return True


    def __str__(self):
        return f'Node: "{self.value}" with frequency {self.frequency}, children are {self.children}'
    
    def __repr__(self):
        return f'Node({self.value})'


class Trie:
    def __init__(self, degree = 2):
        self.starting_node = Node('') # Init an empty starting node for the trie
        self.degree = degree # Markov chain degree selection determines depth of the trie (degree + 1)
 

    def add(self, word):
        '''
        Adds a word to the trie-structure. Depending on the degree of the trie, the word is stored in 
        degree + 1 long strings in the trie.
        Args:
            word (string): string to add to the trie
        '''
        for i in range(0,len(word)):

            # Create the string to be added to the trie, e.g. if adding "super" into a 2-degree trie,
            # the word is split into sup, upe, per, pe and r, and added into the trie.
            new_node = word[i:i+self.degree+1]

            # Check if a node exists for the string being added
            node = self.search(new_node[0])

            if not node:
                # If no node is found, a new node is initialized and added for the starting
                # character of the string
                self.starting_node.add(Node(new_node[0]))
            else:
                # If a node is found, the node frequency is updated
                node.frequency += 1
            
            
            for j in range(1,len(new_node)):
                # Check that nodes exist for all parts of the string being added,
                # e.g. for "sup", check that "su" and "sup" exist in the trie, if not
                # then they are added

                node_key = new_node[0:j]
                found_node = self.search(node_key)
                
                
                node_to_add = new_node[0:j+1]

                if node_to_add in found_node.children:
                    # If a node is found, update the frequency
                    found_node.children[node_to_add].frequency += 1                    
                else:
                    # If no node is found, add the node to the list of children
                    found_node.add(Node(node_to_add))
            
            
    def search(self, key):
        '''
        Searches the trie structure with the given key, returns node-object if there is one
        or a None if there is no node.
        Args:
            key (str): the string that is being searched for
        '''

        if key == "":
            return self.starting_node
            
        node = self.search_helper(key, self.starting_node)

        return node


    def search_helper(self, key, node):
        '''
        Helper function for search(). Recursively traverses the trie to find the node matching given key.
        Returns node-object if found, otherwise returns None.
        Args:
            key (str): the string being searched
            node (Node): the node object from which to search
        '''
        
        if key in node.children:
            return node.children[key]


        for i in range(1, len(key)):
            if key[0:i] in node.children:
                return self.search_helper(key, node.children[key[0:i]])
        return None


    def __str__(self):
        return f'{self.starting_node}'
