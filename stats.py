def get_num_words(text):
	words = text.split()
	num_words = len(words)
	return num_words


def get_char_num (text):
    num_characters = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in num_characters:
            num_characters[char_lower] += 1
        else:
            num_characters[char_lower] = 1
    return num_characters

def sort_char_counts(num_characters):
    sorted_chars = []
    for char in sorted(num_characters.keys()):
         sorted_chars.append(f"'{char}': {num_characters[char]}")
    return sorted_chars

def sort_on(dict):
    return dict["num"]

def sort_num_order(num_characters):
    num_order = []
    for char in num_characters.keys():
        num_order.append({"char": char, "num": num_characters[char]})
    num_order.sort(reverse=True, key=sort_on)

    return num_order

     
