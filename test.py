from gensim.models import Word2Vec

model = gensim.models.KeyedVectors.load_word2vec_format('yelp.vector.bin', binary=True)
print model['hotel']
print model.wv.most_similar(positive=['hotel'])
print model.n_similarity(['birth','date'], ['birth','place'])