import unittest
from translator import english_to_french, french_to_english


class Teste2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("hello"), "bonjour") 
    
    
    def test2(self): 
        self.assertEqual(english_to_french("good"), "bien")  
        
class Testf2e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("bonjour"), "hello") 
    def test2(self): 
        self.assertEqual(french_to_english("bien"), "good")        

unittest.main()  
