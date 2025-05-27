import unittest

from trie import Trie,Node

class TrieTest(unittest.TestCase):

    def setUp(self):
        self.trie = Trie(3)

    
    def test_trie_adding_single_character(self):

        self.trie.add("w")

        self.assertTrue("w" in self.trie.starting_node.children)

    def test_trie_search(self):
        self.trie.add("w")
        node = self.trie.search("w").value

        self.assertEqual("w", node)

    def test_trie_adding_a_word(self):

        self.trie.add("triumphant")
        test_case = self.trie.search("tri")

        self.assertNotEqual(None,test_case)
    
    def test_trie_variable_degrees(self):
        word = "califragilisticexpialidocious"
        its_ok = True
        for i in range(1,10):
            trie = Trie(i)
            trie.add(word)

            node = trie.search(word[0:i])
            if not node:
                its_ok = False
                break
        
        self.assertTrue(its_ok)

    def test_trie_frequency_updates(self):

        trie = Trie(3)

        trie.add("sunset")

        node_freq = trie.search("sun").frequency
        self.assertEqual(1,node_freq)
        
        trie.add("sunset")
        trie.add("sunset")

        node_freq = trie.search("sun").frequency
        self.assertEqual(3,node_freq)