import jieba
import sys

fin = sys.argv[1]
fout = sys.argv[2]

def segment_by_word(s):
    return [word.strip() for word in jieba.cut(s) if word.strip() != ""]

def segment_by_char(s):
    return [c for c in s if c != " "]

with open(fin, "r", encoding="utf-8") as f:
    with open(fout, "w", encoding="utf-8") as w:
        for i, line in enumerate(f):
            if i % 10000 == 0:
                print(i)
            line = line.strip().lower()
            if line == "": continue
            s = line
            words = segment_by_word(s)
            #words = segment_by_char(s)
            w.write(" ".join(words) + "\n")
