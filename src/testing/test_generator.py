import unittest

from generator import Generator

TEST_CONTENT = ["alkometri",
                "banaani",
                "couscous",
                "diletantti",
                "ensikertalainen",
                "faarao",
                "graafikko",
                "hitsaaja",
                "insinööri",
                "joukkue",
                "kerhotila",
                "luokkakokous",
                "mansikka",
                "noukkia",
                "ostoslista",
                "paviaani",
                "quisling",
                "rakkaus",
                "sydänvärinä",
                "torvi",
                "universaali",
                "vauhdikas",
                "wokki",
                "xylofoni",
                "ympäristöystävällinen",
                "zebra",
                "ångström",
                "ärjyä",
                "örkki"]

class GeneratorTest(unittest.TestCase):

    def setUp(self):


        self.generator = Generator("testing/testing.txt", 3, 8)
        
        for word in TEST_CONTENT:
            self.generator.trie.add(word)

    
    def test_generation_length(self):

        generated_words = self.generator.generate(5)

        self.assertEqual(5, len(generated_words))

    def test_generated_words_length(self):

        generated_words = self.generator.generate(100)

        words_long_enough = True

        for word in generated_words:
            if len(word) != 8:
                words_long_enough = False
                break
        
        self.assertTrue(words_long_enough)
