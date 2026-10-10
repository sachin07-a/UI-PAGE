from unittest import result


feedback= "moonlight homestay is amazing amazing place to relax"


def remove_spaces(text):
    text=text.strip()
    print("after removing extra spaces:")
    print(text)
    return text

def remove_duplicates(text):
    text= text.split() 
    print("after removing duplicates:")
    print(text)
    return text

def capitalize(text):
    text= text.title()
    print("after capitalizing first letter:")
    print(text)
    return text

def count_vowels(text):
    count=0
    for char in text.lower():
        if char in "aeiou":
            count+=1

    print("number of vowels in the text:",count)
    return count
     
def find_word_position(text):
    words=text.split()

    if "relax" in words:
        position= words.index("relax") +1
        print("position of 'relax':",position)
    else:
        print("'relax' not found in the text.")
        return -1

def join_words(text):
    words=text.split()
    print("words joined using '-':")
    print("-".join(words))

while True:
    print("\n---Text Processing Menu---")
    print("1. Remove extra spaces")
    print("2. Remove duplicates")
    print("3. Capitalize each word")
    print("4. Count vowels")
    print("5. Find position of 'relax'")
    print("6. Join words using '-'")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        feedback= remove_spaces(feedback)
    elif choice == 2:
        feedback= remove_duplicates(feedback)
    elif choice == 3:
        feedback= capitalize(feedback)
    elif choice == 4:
        count_vowels(feedback)
    elif choice == 5:
        find_word_position(feedback)
    elif choice == 6:
        join_words(feedback)
    elif choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        