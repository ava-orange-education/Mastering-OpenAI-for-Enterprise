import openai

def chat_with_gpt(conversation):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response.choices[0].message.content

def log_feedback(response, feedback):
        try:
            with open("feedback.log", "a") as log_file:
                log_file.write(f"Response: {response}\n")
                log_file.write(f"User Feedback: {feedback}\n")
        except Exception as e:
            print(f"An error occurred while logging feedback: {e}")
    
if __name__ == "__main__":
    conversation = [{"role": "system", "content": "You are a friendly assistant."}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Chatbot: Goodbye!")
            break        
        response = chat_with_gpt(conversation)
        print(f"Chatbot: {response}")
        feedback = input("How was my response? (1-5): ")
        log_feedback(response, feedback)
