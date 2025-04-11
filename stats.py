
def get_num_words(file_contents):
    word_count = len(file_contents.split(None))
    return word_count

def get_num_char(file_contents):
    char_counts = {}
    file_contents = file_contents.lower()

    for char in file_contents:
            if char.isalpha():
                char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts    

def sort_content(char_counts):
    sorted_list = []

    k_p_pairs = char_counts.items()
    sorted_pairs = sorted(k_p_pairs, key=lambda item: item[1], reverse=True)
    
    for k, v in sorted_pairs:
        sorted_list.append({k: v})

    return sorted_list


    
