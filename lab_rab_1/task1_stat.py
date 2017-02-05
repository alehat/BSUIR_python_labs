def text_statistics(str, k, n):
    words_count = []
    word_sum = 0
    n_grams = {}
    word_use = {}
    for sent in str:
        words = sent.split()
        word_sum += len(words)
        words_count.append(len(words))
        for word in words:
            word = word.replace('(', '').replace(')', '').replace(',', '').replace(':', '').\
                replace('"', '').replace(';','').strip()
            if word in word_use:
                word_use[word] += 1
            else:
                word_use[word] = 1
            if len(word) >= n:
                for i in range(len(word) - n + 1):
                    gram = word[i:i + n].lower()
                    if gram in n_grams:
                        n_grams[gram] += 1
                    else:
                        n_grams[gram] = 1
    top_grams = sorted(n_grams.items(), key=lambda l: l[1], reverse=True)
    words_count.sort()
    mid = words_count[len(words_count) / 2] if len(words_count) % 2 == 1 else \
        (words_count[len(words_count) / 2] + words_count[len(words_count) / 2 - 1]) // 2
    return top_grams[:k], word_use, mid, word_sum // len(words_count)

