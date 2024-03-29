def main():

    with open("books/frankenstein.txt") as frankenstein_file:
        frankenstein_string = frankenstein_file.read()
        
        print("--- Begin report of books/frankenstein.txt ---")
        #print(frankenstein_string)
        print(f"{number_of_words(frankenstein_string)} words found in the document")  
        print("")
        count_characters(frankenstein_string)
  


def number_of_words(input_string):
    words = input_string.split()
    return len(words)

def count_characters(input_string):
    lowercase_string = input_string.lower()
    character_count = {}
    for character in lowercase_string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    sorted_character_count = sorted(character_count.items(), key=lambda x:x[1], reverse=True)
    for character, number_of_occurences in sorted_character_count:
        print(f"The '{character}' character was found '{number_of_occurences}' times")

main()