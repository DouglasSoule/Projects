with open('iliad.txt') as iliad:
    most_common_words = {}
    for line in iliad:
        # print(line)
        # break
        word_list = line.split()
        # print(word_list)
        # break
        for word in word_list:
            most_common_words[word] = most_common_words.get(word, 0) + 1

    most_common_word = None
    highest_count = None
    for word, count in most_common_words.items():
        if highest_count is None or count > highest_count:
            most_common_word = word
            highest_count = count

    print(most_common_word)
    print(highest_count)
    print(most_common_words)
    
