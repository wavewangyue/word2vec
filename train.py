# -*- coding: utf-8 -*- 

import logging
import os.path
import sys
import multiprocessing
import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import jieba

def w2v_train(fin, fout):
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    
    model = Word2Vec(LineSentence(fin), size=100, window=5, min_count=50, workers=multiprocessing.cpu_count())                 
    model.wv.save_word2vec_format(fout, binary=True)
        

def trans_bin_to_txt(fin, fout):
    model=gensim.models.KeyedVectors.load_word2vec_format(fin, binary=True)
    vocab = model.vocab
    print("vocab size:", len(vocab))
    with open(fout, "w") as w:
        w.write(str(len(vocab)) + " " + str(model.vector_size) + "\n")
        for word in vocab:
            w.write(" ".join([word]+[str(num) for num in model[word]]) + "\n")

if __name__ == "__main__":
    w2v_train("corpus.wiki", "word2vec.wiki.bin")
    #trans_bin_to_txt("word2vec.wiki.bin", "word2vec.wiki.txt")
