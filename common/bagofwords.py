import numpy as np


class BagOfWords:
    def __init__(self, texts, k=0):
        if k <= 0:
            k = len(set(' '.join(texts).split()))

        bag = dict()
        for comment in texts:
            for word in comment.split(' '):
                if word not in bag.keys():
                    bag[word] = 1
                else:
                    bag[word] += 1
        self.bow_vocabulary = dict(sorted(bag.items(), key=lambda item: item[1], reverse=True)[:k])

    def bow_vocabulary(self):
        return self.bow_vocabulary

    def text_to_bow(self, text):
        bow = [0] * len(self.bow_vocabulary)
        voc_map = dict()

        for num, w in enumerate(self.bow_vocabulary, start=0):
            voc_map[w] = num

        for token in text.split(' '):
            if token in voc_map:
                bow[voc_map[token]] += 1

        return np.array(bow, 'float32')
