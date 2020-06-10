def score_words(words):
    return sum(sum(char in 'aeiouy' for char in word) % 2 or 2 for word in words)

n = int(input())
words = input().split()
print(score_words(words))