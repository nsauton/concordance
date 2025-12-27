import unittest
from concordance import build_concordance

'''
"quotes"! (parentheses). comma,! semicolon;. colon:. [brakcets]. {braces}.
123 456 789!
Mr. Gosling?! 
Dr. Richards, Johnny will be here at 3 p.m..
'''

class TestConcordance(unittest.TestCase):
    # Unit tests for the build_concordance function

    def test_basic_concordance(self):
        text = "Hello world. Hello again."
        concordance = build_concordance(text)

        self.assertEqual(concordance["hello"]["count"], 2)
        self.assertEqual(concordance["hello"]["occurrences"], [1, 2])
        self.assertEqual(concordance["world"]["count"], 1)
        self.assertEqual(concordance["world"]["occurrences"], [1])
        self.assertEqual(concordance["again"]["count"], 1)
        self.assertEqual(concordance["again"]["occurrences"], [2])

    def test_abbreviation_not_split(self):
        text = "This is i.e. a test? Dr. Richards, Johnny will be here at 3 p.m.. Mr. Gosling?!"
        concordance = build_concordance(text)

        self.assertIn("i.e.", concordance)
        self.assertEqual(concordance["i.e."]["count"], 1)
        self.assertEqual(concordance["i.e."]["occurrences"], [1])
        self.assertIn("dr.", concordance)
        self.assertEqual(concordance["dr."]["count"], 1)
        self.assertEqual(concordance["dr."]["occurrences"], [2])
        self.assertIn("p.m.", concordance)
        self.assertEqual(concordance["p.m."]["count"], 1)
        self.assertEqual(concordance["p.m."]["occurrences"], [2])
        self.assertIn("mr.", concordance)
        self.assertEqual(concordance["mr."]["count"], 1)
        self.assertEqual(concordance["mr."]["occurrences"], [3])

    def test_contractions(self):
        text = "Don't stop. Don't ever stop."
        concordance = build_concordance(text)

        self.assertIn("don't", concordance)
        self.assertEqual(concordance["don't"]["count"], 2)
        self.assertEqual(concordance["don't"]["occurrences"], [1, 2])

    def test_punctuation_stripping(self):
        text = "(Hello), world! \"quotes\" comma, semicolon; colon: [brackets] {braces}."
        concordance = build_concordance(text)

        self.assertIn("hello", concordance)
        self.assertIn("world", concordance)
        self.assertNotIn("(hello)", concordance)
        self.assertIn("quotes", concordance)
        self.assertNotIn("\"quotes\"", concordance)
        self.assertIn("comma", concordance)
        self.assertNotIn("comma,", concordance)
        self.assertIn("semicolon", concordance)
        self.assertNotIn("semicolon;", concordance)
        self.assertIn("colon", concordance)
        self.assertNotIn("colon:", concordance)
        self.assertIn("brackets", concordance)
        self.assertNotIn("[brackets]", concordance)
        self.assertIn("braces", concordance)
        self.assertNotIn("{braces}", concordance)


    def test_case_insensitivity(self):
        text = "SAME WORDS same words."
        concordance = build_concordance(text)

        self.assertEqual(concordance["same"]["count"], 2)
        self.assertEqual(concordance["same"]["occurrences"], [1, 1])
        self.assertEqual(concordance["words"]["count"], 2)
        self.assertEqual(concordance["words"]["occurrences"], [1, 1])

    def test_case_numbers(self):
        text = "123 456 789!"
        concordance = build_concordance(text)

        self.assertIn("123", concordance)
        self.assertEqual(concordance["123"]["count"], 1)
        self.assertEqual(concordance["123"]["occurrences"], [1])
        self.assertIn("456", concordance)
        self.assertEqual(concordance["456"]["count"], 1)
        self.assertEqual(concordance["456"]["occurrences"], [1])
        self.assertIn("789", concordance)
        self.assertEqual(concordance["789"]["count"], 1)
        self.assertEqual(concordance["789"]["occurrences"], [1])

    def test_hyphenated_words(self):
        text = "Production-ready code."
        concordance = build_concordance(text)

        self.assertIn("production-ready", concordance)


if __name__ == "__main__":
    unittest.main()