import random as random2
import time

def main():
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful and versatile programming language.",
        "Practice makes perfect!"
    ]

    print("Welcome to the Dhanvi`s Typing Speed Tester!")

    while True:
        text = random2.choice(texts)
        print("\nType the following:")
        print('text :', text)
        input("Press Enter when ready you are ready to type........")
        start_time = time.time()
        user_input = input("Start typing above given sample ")
        end_time = time.time()

        elapsed_time = end_time - start_time
        words = text.split()
        num_words = len(words)
        num_characters = len(user_input)
        typing_speed = (num_words / elapsed_time) * 60
        accuracy = calculate_accuracy(text, user_input)

        print(f"\nTyping Speed: {typing_speed:.2f} WPM")
        print(f"Accuracy: {accuracy:.2%}")

        play_again = input("\nDo you want to try again? (yes/no): ").lower()
        if play_again != "yes":
            break

def calculate_accuracy(text, user_input):
    text_words = text.split()
    user_words = user_input.split()
    correct_words = 0

    for t_word, u_word in zip(text_words, user_words):
        if t_word == u_word:
            correct_words += 1

    return correct_words / len(text_words)

if __name__ == "__main__":
    main()
