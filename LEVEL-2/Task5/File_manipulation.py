from collections import Counter

def count_words(file_path):
    try:
        with open(file_path, 'r')  as file:

            content = file.read().lower()

            words = content.split()

            word_counts = Counter(words)


            sorted_word_counts = sorted(word_counts.items(), key = lambda x: x[0])

            for word, count in sorted_word_counts:
                print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")

    except Exception as e:
        print(f"An error occured: {e}")


file_path = input("Enter file name: ")
    
a = file_path + ".txt"

count_words(a)



            