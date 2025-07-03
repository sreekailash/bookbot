def get_num_words(text) -> int:
    return len(text.split())
    
def get_char_count(text) -> dict:
    chars_split = list(text.lower())
    unique_chars = set(chars_split)
    
    char_dict = {char:chars_split.count(char) for char in unique_chars}
    return char_dict

def get_sorted_list(char_dict) -> list:
    
    def sort_on(chars_list):
        return chars_list['num']
    
    chars_list = [{"name": k, "num": v} for k, v in list(char_dict.items())]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list