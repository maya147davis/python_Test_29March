def most_common_word(story: tuple) -> str:
    word_count = {}
    words = " ".join(story).lower().split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    max_count = 0
    most_common = None
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_common = word

    return most_common


user_input = input("Enter the story as a tuple of strings (e.g., 'line1', 'line2', 'line3'): ")

story_tuple = tuple(s.strip()[1:-1] for s in user_input.split(","))

print("Most common word:", most_common_word(story_tuple))