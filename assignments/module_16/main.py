"""
Text Analyzer design: a dict counts words, a set tracks unique words, and lists
store sorted/searchable values. Sorting ranks frequencies; binary search finds
words; dynamic programming computes LCS. These choices give expected O(n)
counting, O(w log w) ranking, O(log w) lookup, and O(m*n) LCS time.
"""

import string


# O(n) time and space in the input text length.
def tokenize(text):
    clean = text.translate(str.maketrans("", "", string.punctuation))
    return clean.lower().split()


# O(n) expected time and O(w) space for n tokens and w unique words.
def word_frequencies(text):
    counts = {}
    for word in tokenize(text):
        counts[word] = counts.get(word, 0) + 1
    return counts


# O(log w) time and O(1) space on a sorted word list.
def binary_search(words, target):
    low, high = 0, len(words) - 1
    while low <= high:
        middle = (low + high) // 2
        if words[middle] == target:
            return middle
        if words[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


# O(m*n) time and O(n) space for token sequences of lengths m and n.
def lcs_length(first, second):
    row = [0] * (len(second) + 1)
    for left in first:
        next_row = [0]
        for j, right in enumerate(second, 1):
            next_row.append(row[j - 1] + 1 if left == right
                            else max(row[j], next_row[-1]))
        row = next_row
    return row[-1]


# O(n) time and O(1) extra space.
def readability(words, text):
    sentences = max(1, sum(text.count(end) for end in ".!?"))
    syllables = sum(max(1, sum(char in "aeiouy" for char in word)) for word in words)
    return {
        "average words per sentence": len(words) / sentences,
        "average word length": sum(map(len, words)) / len(words) if words else 0,
        "estimated syllables per word": syllables / len(words) if words else 0,
    }


# O(n + w log w + m*n) time, dominated by sorting and LCS.
def analyze(text, comparison):
    words = tokenize(text)
    counts = word_frequencies(text)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    by_word = sorted(counts)
    print("Top words:", ranked[:10])
    print("Least common words:", sorted(counts.items(), key=lambda item: (item[1], item[0]))[:10])
    print(f"Total words: {len(words)} | Unique words: {len(set(words))}")
    print(f"Average word length: {sum(map(len, words)) / len(words) if words else 0:.2f}")
    search = input("Word to search for: ").lower().strip(string.punctuation)
    index = binary_search(by_word, search)
    print(f"{search!r} {'found' if index >= 0 else 'not found'}")
    print(f"LCS length: {lcs_length(words, tokenize(comparison))}")
    print("Readability:", readability(words, text))


if __name__ == "__main__":
    analyze(
        "Python makes data analysis clear. Python uses useful structures, and "
        "data structures help organize useful information.",
        "Data analysis uses clear structures. Python helps organize information.",
    )
