
import time

def speed_typing_test(text):
    print("Type the following text as quickly and accurately as possible:")
    print(text)
    input("Press Enter to start...")
    
    start_time = time.time()
    user_input = input().strip()
    end_time = time.time()
    
    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    
   
    correct_chars = sum([1 for a, b in zip(user_input, text) if a == b])
    total_chars = max(len(user_input), len(text))
    accuracy = correct_chars / total_chars * 100
    
    print("Time taken:", round(time_taken, 2), "seconds")
    print("Words typed:", words_typed)
    print("Accuracy:", round(accuracy, 2), "%")


text = "The quick brown fox jumps over the lazy dog."


speed_typing_test(text)
