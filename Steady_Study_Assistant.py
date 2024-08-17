import openai  # Import the OpenAI library to interact with the OpenAI API
import os  # Import the OS library to interact with the operating system
import time  # Import the Time library to handle time-related tasks
from datetime import datetime  # Import the Datetime library to handle date and time

# Setup OpenAI API key
openai.api_key = "your OpenAI API key" # Replace "your OpenAI API key" with your actual OpenAI API key in the code.

# Function to validate if the user asked a valid question, and respond accordingly if no question was asked
def openai_question_validation(question):
    # Define the messages to be sent to the OpenAI API
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question},
        {"role": "system", "content": (
            "Determine if the user provided a valid question. A valid question is one that is clear, specific, and related to a topic that can be answered. Examples of valid questions include ‘What is the capital of France?’, ‘How do I solve the multiplication expression 8*5?’, and ‘Can you explain photosynthesis?’. An invalid question is one that is vague, lacks context, or cannot be answered as it stands. Examples of invalid questions include ‘Help me’, ‘Question’, ‘I don’t understand’, ‘I need help with’, and ‘help me with a question’. Watch out for trick ‘questions’. These are statements where the user says they need help with a question but doesn’t provide enough context. Examples of trick questions include ‘I need help with a quadratic equation’ and ‘I need help with this math problem’. Count these as invalid unless the user provides enough context. If the user says they need help with a question but provides enough context, count that question as valid. For example, ‘I need help with a quadratic equation, x^2-5x+6 = 0.’ It doesn’t matter if the user uses improper grammar or responds in incomplete sentences. Just determine if they asked a valid question. For example, ‘help me with 5+5’ is still a valid question. The questions don’t have to be exactly like the examples provided above. Sort them into the categories of valid and invalid based on their similarity to the example formats. If the question is valid, respond with ‘yes’. If the question is not valid, respond with ‘no’."
        )}
    ]
    
    # Call the OpenAI API to get a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
        temperature=0.7,
    )
    
    # Return the response from the API
    return response.choices[0].message['content'].strip().lower()

# Function to get a response from OpenAI to validate the student's answer
def get_openai_validation_response(problem, student_answer, mistake_count):
    # Determine the behavior inference based on the mistake count
    behavior_inference = (
        "The student has been struggling a bit with this problem." if mistake_count > 0 else
        "The student seems to be making a good effort to solve this problem."
    )
    
    # Define the messages to be sent to the OpenAI API
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"The student is working on the following problem: {problem}"},
        {"role": "user", "content": f"The student provided this answer: {student_answer}"},
        {"role": "user", "content": behavior_inference},
        {"role": "user", "content": "Is this answer correct? Respond with 'yes' or 'no'."}
    ]
    
    # Call the OpenAI API to get a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=5,
        temperature=0,
    )
    
    # Return the response from the API
    return response.choices[0].message['content'].strip().lower()

# Function to get a hint or the correct answer from OpenAI
def get_openai_hint_or_answer(problem, provide_answer=False, mistake_count=0):
    # Define the user message based on whether to provide the answer or a hint
    user_message = (
        f"The student has made a few attempts and seems to be having difficulty with the problem: {problem}\n"
        f"{'What is the correct answer?' if provide_answer else 'Can you provide a hint to help solve this problem?'}"
    )

    # Define the messages to be sent to the OpenAI API
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]

    # Call the OpenAI API to get a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
        temperature=0.7,
    )
    
    # Return the response from the API
    return response.choices[0].message['content'].strip()

# Function to provide a personalized greeting based on the time of day
def personalized_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning!"
    elif current_hour < 17:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Main function to run the AI assistant
def main():
    
    # Windows clear screen command
    os.system("cls")
    
    # Print a personalized greeting and prompt the user to ask a question
    print(f"AI: {personalized_greeting()} I'm here to help you with any homework-related questions you have. Please go ahead and describe your problem or ask your question. Please try to be as clear as possible to avoid any confusion.")
    
    # Get the user's question
    question = input("You: ").strip()
    
    # Validate the user's question
    question_validation = openai_question_validation(question)
    while "no" in question_validation:
        print("AI: Please provide a valid question.")
        question = input("You: ")
        question_validation = openai_question_validation(question)
    
    # Provide initial feedback and guidance
    print("AI: Great! Let's work through this together. I'll help guide you, but remember, it's important to try solving it yourself first.")
    
    mistake_count = 0
    correct_count = 0
    start_time = time.time()
    
    while True:
        # Get the student's answer
        student_answer = input("Your attempt: ").strip()
        response_time = time.time() - start_time
        
        # Check if the student wants to quit
        if "quit" in student_answer:
            print("AI: Alright, no problem! If you ever have any homework-related questions, feel free to reach out. Have a great day!")
            break

        # Validate the student's answer
        validation_response = get_openai_validation_response(question, student_answer, mistake_count)
        
        # Provide feedback based on progress
        if correct_count > 0 and correct_count % 5 == 0:
            print(f"AI: Great job! You've answered {correct_count} questions correctly so far. Keep up the good work!")
        
        if mistake_count > 0 and mistake_count % 5 == 0:
            print(f"AI: Don't worry about the mistakes. You've made {mistake_count} mistakes, but each one is a learning opportunity. Keep trying!")
        
        # Check if the student's answer is correct
        if 'yes' in validation_response:
            correct_count += 1
            print("AI: That's correct! Well done! I knew you could do it!")
            input("Press [Enter] to continue")
            main()
        else:
            mistake_count += 1
            print(f"AI: That's not quite right. Remember to think through the problem carefully. (Mistakes so far: {mistake_count})")
        
        # Offer help if the student is struggling or answering too quickly
        if response_time < 1 or mistake_count >= 3:
            offer_help = input("AI: It seems like you're finding this tricky, or maybe answering too quickly. Would you like a hint or the final answer? (hint/answer/keep trying/quit): ").strip().lower()
            if offer_help == 'hint':
                hint = get_openai_hint_or_answer(question, provide_answer=False, mistake_count=mistake_count)
                print(f"AI: Hint: {hint}")
                mistake_count = 0  # Reset mistake count after providing a hint
            elif offer_help == 'answer':
                answer = get_openai_hint_or_answer(question, provide_answer=True, mistake_count=mistake_count)
                print(f"AI: {answer}")
                mistake_count = 0  # Reset mistake count after providing the answer
                input("Press [Enter] to continue")
                main()
            elif offer_help == "quit":
                print("AI: Alright, no problem! If you ever have any homework-related questions, feel free to reach out. Have a great day!")
                break
            else:
                mistake_count = 0  # Reset mistake count after the user says they prefer to keep trying
                print("AI: No worries, keep trying! I'm here if you need help.")
                
        start_time = time.time()
        
if __name__ == "__main__":
    main()