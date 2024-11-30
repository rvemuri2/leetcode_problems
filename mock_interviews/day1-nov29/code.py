from collections import Counter
def WordOccurrence(sentence: str) -> dict: 


    words = Counter()

    result = sentence.split(" ")


# a 
# ab.
# abc

    for word in result:
        length = 0

        for i in word:
            if(i.isalpha()):
                length += 1

        words[length] += 1

    return words

print(WordOccurrence("a ab. abc"))

# Time Complexity: O(n * m ) = O(N)
# Space Complexity: O(N)
    # 1 -> 1, 2 -> 1, 3 -> 1
