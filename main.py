path_to_file = "books/frankenstein.txt"

def convert(dictionary):
    return [{key: value} for key, value in dictionary.items()]

def main():
    key_value = {}
    
    with open(path_to_file) as f:
        file_contents = f.read()
        lowered = file_contents.lower()
        words = lowered.split()
        
        # Initialize the dictionary with specified characters
        characters_to_count = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h']
        for char in characters_to_count:
            key_value[char] = 0
        
        # Count each character in the text
        for letter in lowered:
            if letter in key_value:
                key_value[letter] += 1

    # Get the number of words
    num_words = len(words)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words} words found in the document\n")
    
    for char in characters_to_count:
        print(f"The '{char}' character was found {key_value[char]} times")

if __name__ == "__main__":
    main()
