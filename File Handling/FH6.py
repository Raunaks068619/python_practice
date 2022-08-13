from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("No.of words in file :",word_count("FH1.txt"))
