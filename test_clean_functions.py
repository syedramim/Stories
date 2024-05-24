import unittest
from datetime import time, datetime
from clean_functions import *

class TestCases(unittest.TestCase):

    def test_calculate_downvotes(self):
        # Arrange
        upvotes = 100
        upvote_ratio = 0.7
        
        # Act
        downvotes = calculate_downvotes(upvotes, upvote_ratio)
        
        # Assert
        self.assertEqual(downvotes, 42.85714285714286)

    def test_convert_to_time(self):
        # Arrange
        string = "14:30"
        
        # Act
        result = convert_to_time(string)
        
        # Assert
        self.assertEqual(result, datetime.strptime("14:30", "%H:%M"))

    def test_handle_date(self):
        # Arrange
        created_time = 1652995200  # equivalent to May 20, 2022 00:00:00 UTC
        
        # Act
        result = handle_date(created_time)
        
        # Assert
        expected_result = {"date": "05-19-2022", "time_of_day": "Evening"}
        self.assertEqual(result, expected_result)

    def test_get_fre_score_level(self):
        # Arrange
        score = 55
        
        # Act
        result = get_fre_score_level(score)
        
        # Assert
        self.assertEqual(result, "Fairly Difficult")

    def test_get_word_list(self):
        # Arrange
        string = "Hello, world! This is a test."
        
        # Act
        result = get_word_list(string)
        
        # Assert
        self.assertEqual(result, ["Hello", "world", "This", "is", "a", "test"])

    def test_divider(self):
        # Arrange
        num1 = 10
        num2 = 2
        
        # Act
        result = divider(num1, num2)
        
        # Assert
        self.assertEqual(result, 5.0)

    def test_get_avg_word_length(self):
        # Arrange
        arr = ["Hello", "world"]
        
        # Act
        result = get_avg_word_length(arr)
        
        # Assert
        self.assertEqual(result, 5.0)

    def test_get_sentences(self):
        # Arrange
        string = "Hello world. This is a test."
        
        # Act
        result = get_sentences(string)
        
        # Assert
        self.assertEqual(len(result), 2)

    def test_get_sentiment(self):
        # Arrange
        string = "I love sunny days."
        
        # Act
        result = get_sentiment(string)
        
        # Assert
        self.assertAlmostEqual(result.polarity, 0.5, places=1)
        self.assertAlmostEqual(result.subjectivity, 0.6, places=1)

    def test_get_syllable_count(self):
        # Arrange
        string = "Hello world"
        
        # Act
        result = get_syllable_count(string)
        
        # Assert
        self.assertEqual(result, 3)

    def test_get_reading_score(self):
        # Arrange
        string = "The quick brown fox jumps over the lazy dog."
        
        # Act
        result = get_reading_score(string)
        
        # Assert
        self.assertGreater(result, 0)

    def test_get_reading_grade(self):
        # Arrange
        string = "The quick brown fox jumps over the lazy dog."
        
        # Act
        result = get_reading_grade(string)
        
        # Assert
        self.assertEqual(result, '3rd and 4th grade')

    def test_get_story_sent_info(self):
        # Arrange
        sentences = get_sentences("Hello world. This is a test.")
        
        # Act
        result = get_story_sent_info(sentences)
        
        # Assert
        expected_keys = [
            "amount_sentences", "avg_words_per_sentence", "avg_syllables_per_sentence",
            "avg_polarity_per_sentence", "avg_subjectivity_per_sentence", "avg_readscore_per_sentence"
        ]
        for key in expected_keys:
            self.assertIn(key, result)
        
        self.assertEqual(result["amount_sentences"], 2)
        self.assertAlmostEqual(result["avg_words_per_sentence"], 3.0, places=1)
        self.assertAlmostEqual(result["avg_syllables_per_sentence"], 3.5, places=1)
        self.assertAlmostEqual(result["avg_polarity_per_sentence"], 0.0, places=1)
        self.assertAlmostEqual(result["avg_subjectivity_per_sentence"], 0.0, places=1)
        self.assertGreater(result["avg_readscore_per_sentence"], 0)

    def test_info(self):
        # Arrange
        string = "Hello world. This is a test."
        
        # Act
        result = info(string, False)
        
        # Assert
        expected_keys = [
            "story_length", "story_word_count", "story_avg_word_length", "story_syllables", 
            "story_reading_score", "story_reading_grade", "story_reading_difficulty", 
            "story_polarity", "story_subjectivity", "amount_sentences", 
            "avg_words_per_sentence", "avg_syllables_per_sentence", 
            "avg_polarity_per_sentence", "avg_subjectivity_per_sentence", 
            "avg_readscore_per_sentence"
        ]
        for key in expected_keys:
            self.assertIn(key, result)
        
        self.assertEqual(result["story_length"], len(string))
        self.assertEqual(result["story_word_count"], 6)
        self.assertAlmostEqual(result["story_avg_word_length"], 3.5, places=1)
        self.assertEqual(result["story_syllables"], 7)
        self.assertGreater(result["story_reading_score"], 0)
        self.assertIsInstance(result["story_reading_grade"], str)
        self.assertIsInstance(result["story_reading_difficulty"], str)
        self.assertAlmostEqual(result["story_polarity"], 0.0, places=1)
        self.assertAlmostEqual(result["story_subjectivity"], 0.0, places=1)
        self.assertEqual(result["amount_sentences"], 2)
        self.assertAlmostEqual(result["avg_words_per_sentence"], 3.0, places=1)
        self.assertAlmostEqual(result["avg_syllables_per_sentence"], 3.5, places=1)
        self.assertAlmostEqual(result["avg_polarity_per_sentence"], 0.0, places=1)
        self.assertAlmostEqual(result["avg_subjectivity_per_sentence"], 0.0, places=1)
        self.assertGreater(result["avg_readscore_per_sentence"], 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)

