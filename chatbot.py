import datetime
import os

# Function to save the user's mood to a file
def save_user_mood(user_name, mood):
    with open(f"{user_name}_moods.txt", "a") as file:
        file.write(f"{datetime.datetime.now()}: {mood}\n")

# Function to load the user's mood history
def load_user_mood_history(user_name):
    if os.path.exists(f"{user_name}_moods.txt"):
        with open(f"{user_name}_moods.txt", "r") as file:
            return file.readlines()
    return []

# Function to get a response based on user input
def get_response(user_input, user_name):
    user_input = user_input.lower()
    
    # Define responses based on specific keywords or phrases
    if "sad" in user_input:
        save_user_mood(user_name, "sad")
        return f"I'm sorry to hear that, {user_name}! Your motivational quote is: If you think you are too small to make a difference, try sleeping with a mosquito. -Ghandi.  How else are you feeling?"
    elif "angry" in user_input:
        save_user_mood(user_name, "angry")
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Anger makes dull men witty, but it keeps them poor. -Elizabeth I.  How else are you feeling?"
    elif "self-conscious" in user_input:
        save_user_mood(user_name, "self-conscious")
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Knowing yourself is the beginning of all wisdom. -Aristotle.  How else are you feeling?"
    elif "anxious" in user_input:
        save_user_mood(user_name, "anxious")
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: As long as you are breathing, there is more right with you than wrong with you, no matter what is wrong. -Jon Kabat-Zinn.  How else are you feeling?"
    elif "unhappy" in user_input:
        save_user_mood(user_name, "unhappy")
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: There is no path to happiness. Happiness is the path. –Buddha.  How else are you feeling?"
    elif "annoyed" in user_input:
        save_user_mood(user_name, "annoyed")
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Everything that irritates us about others can lead us to an understanding of ourselves. – Carl Jung.  How else are you feeling?"
    elif "frustrated" in user_input:
        save_user_mood(user_name, "frustrated")
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Good decisions come from experience. Experience comes from making bad decisions. – Mark Twain  How else are you feeling?"
    elif "bored" in user_input:
        save_user_mood(user_name, "bored")
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Is life not a thousand times too short for us to bore ourselves? – Friedrich Nietzsche  How else are you feeling?"
    elif "lonely" in user_input:
        save_user_mood(user_name, "lonely")
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Feeling sorry for yourself, and your present condition, is not only a waste of energy but the worst habit you could possibly have. – Dale Carnegie  How else are you feeling?"
    elif "bye" in user_input or "goodbye" in user_input:
        return f"Goodbye, {user_name}! Have a great day!"
    else:
        return f"I'm sorry, {user_name}, I don't understand that. Can you please rephrase?"

# Function to get the current greeting based on the time of day
def get_greeting():
    now = datetime.datetime.now()
    current_hour = now.hour
    if current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

# Main function to run the chatbot, checking for previous mood history
def main():
    print("Hello! Welcome to the simple Python chatbot!")
    
    user_name = input("What's your name? ")
    greeting = get_greeting()
    
    mood_history = load_user_mood_history(user_name)
    if mood_history:
        print(f"Welcome back, {user_name}! Here's your mood history:")
        print("".join(mood_history))
        print(f"{greeting}, {user_name}! Any negative mood today? (sad, angry, self-conscious, anxious, unhappy, annoyed, frustrated, bored? I'm here to turn that frown updside down.")
    else:
        print(f"{greeting}, {user_name}! Any negative mood today? (sad, angry, self-conscious, anxious, unhappy, annoyed, frustrated, bored? I'm here to turn that frown updside down.")

    print("Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            break
        response = get_response(user_input, user_name)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()