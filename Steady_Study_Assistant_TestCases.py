import unittest  # Import the unittest library for creating and running tests
import unittest  # Import the unittest library again (duplicate import, can be removed)
from unittest.mock import patch  # Import the patch function from unittest.mock for mocking
from datetime import datetime  # Import the Datetime library to handle date and time
import Steady_Study_Assistant  # Import the Steady_Study_Assistant module to test its functions

# Define a test case class inheriting from unittest.TestCase
class TestOpenAIHelper(unittest.TestCase):

    # Mock the openai.ChatCompletion.create method for this test
    @patch('openai.ChatCompletion.create')
    def test_openai_question_validation_valid(self, mock_create):
        # Set the mock return value
        mock_create.return_value.choices[0].message = {'content': 'yes'}
        # Assert that the function returns 'yes' for a valid question
        self.assertEqual(Steady_Study_Assistant.openai_question_validation("What is the capital of France?"), 'yes')

    # Mock the openai.ChatCompletion.create method for this test
    @patch('openai.ChatCompletion.create')
    def test_openai_question_validation_invalid(self, mock_create):
        # Set the mock return value
        mock_create.return_value.choices[0].message = {'content': 'no'}
        # Assert that the function returns 'no' for an invalid question
        self.assertEqual(Steady_Study_Assistant.openai_question_validation("Help me"), 'no')

    # Mock the openai.ChatCompletion.create method for this test
    @patch('openai.ChatCompletion.create')
    def test_get_openai_validation_response_correct(self, mock_create):
        # Set the mock return value
        mock_create.return_value.choices[0].message = {'content': 'yes'}
        # Assert that the function returns 'yes' for a correct response
        self.assertEqual(Steady_Study_Assistant.get_openai_validation_response("2+2", "4", 0), 'yes')

    # Mock the openai.ChatCompletion.create method for this test
    @patch('openai.ChatCompletion.create')
    def test_get_openai_validation_response_incorrect(self, mock_create):
        # Set the mock return value
        mock_create.return_value.choices[0].message = {'content': 'no'}
        # Assert that the function returns 'no' for an incorrect response
        self.assertEqual(Steady_Study_Assistant.get_openai_validation_response("2+2", "5", 1), 'no')

    # Mock the openai.ChatCompletion.create method for this test
    @patch('openai.ChatCompletion.create')
    def test_get_openai_hint_or_answer_hint(self, mock_create):
        # Set the mock return value
        mock_create.return_value.choices[0].message = {'content': 'Try breaking it down into smaller steps.'}
        # Assert that the function returns a hint when provide_answer is False
        self.assertEqual(Steady_Study_Assistant.get_openai_hint_or_answer("2+2", provide_answer=False), 'Try breaking it down into smaller steps.')

    # Mock the openai.ChatCompletion.create method for this test
    @patch('openai.ChatCompletion.create')
    def test_get_openai_hint_or_answer_answer(self, mock_create):
        # Set the mock return value
        mock_create.return_value.choices[0].message = {'content': 'The answer is 4.'}
        # Assert that the function returns the answer when provide_answer is True
        self.assertEqual(Steady_Study_Assistant.get_openai_hint_or_answer("2+2", provide_answer=True), 'The answer is 4.')

    # Test the personalized greeting function
    def test_personalized_greeting(self):
            # Get the current hour
            current_hour = datetime.now().hour
            # Default greeting is 'Good evening!'
            greeting = "Good evening!"
            # Change greeting based on the time of day
            if current_hour < 12:
                greeting =  "Good morning!"
            elif current_hour < 17:
                greeting =  "Good afternoon!"
            # Assert that the function returns the correct greeting
            self.assertEqual(Steady_Study_Assistant.personalized_greeting(), greeting)
            
# Run the tests
if __name__ == '__main__':
        unittest.main()