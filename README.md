# Steady Study Assistant
This project is a Python-based AI assistant designed to help students with their homework-related questions. The AI validates user questions, provides hints or answers, and offers encouragement and feedback based on the student’s progress. Additionally, it checks if the user is rushing through their answers and provides appropriate feedback.

# Features
- Question Validation: Ensures that the user provides a valid question before proceeding.
- Answer Validation: Checks if the student’s answer to a problem is correct.
- Hint and Answer Provision: Offers hints or the correct answer if the student is struggling.
- Personalized Greeting: Greets the user based on the time of day.
- Progress Feedback: Provides feedback and encouragement based on the student’s progress.

# Requirements
- Python 3.x
- OpenAI API key

# Installation
- Clone the repository:
    - git clone https://github.com/LakshanShridhar/ai-homework-assistant.git
    - cd ai-homework-assistant
- Install the required packages:
    - pip install openai
- Set up your OpenAI API key: Replace "your OpenAI API key" with your actual OpenAI API key in the code.

# Usage
- Run the main script:
    - python main.py
- The AI will greet you and prompt you to ask a homework-related question. Make sure to ask a clear and specific question.
- The AI will validate your question and guide you through solving the problem. You can ask for hints or the correct answer if you’re struggling.
- To exit the program, type “quit” when prompted for your answer.

# Example:
AI: Good morning! I'm here to help you with any homework-related questions you have. Please go ahead and describe your problem or ask your question, in complete sentences.
You: How do I solve the multiplication expression 8*5?
AI: Great! Let's work through this together. I'll help guide you, but remember, it's important to try solving it yourself first.
Your attempt: 40
AI: That's correct! Well done! I knew you could do it!

# Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

# License
This project is licensed under the MIT License.