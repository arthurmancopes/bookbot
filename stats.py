def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_char_counts(char_counts):
    char_list = [{"char": c, "num": n} for c, n in char_counts.items()]
    def get_num(item):
        return item["num"]
    char_list.sort(key=get_num, reverse=True)
    return char_list
