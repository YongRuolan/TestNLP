from math import log


class BM25():
    def __init__(self,docs):
        self.docs = docs
        self.b = 0.75
        self.k = 1.5 #[1.2,2.0]
        self.D = len(self.docs)
        self.avgdl = sum(len(doc) for doc in self.docs)/float(self.D)
        self.idf = {}
        self.dictionary = {}

    def staticsDocs(self):
        for doc in self.docs:
            for word in set(doc):
                if word not in self.dictionary.keys():
                    self.dictionary[word] = 0
                else:
                    self.dictionary[word] = self.dictionary[word]+1

    def IDF(self,q):
        return log((self.D - self.dictionary[q] + 0.5)/(self.dictionary[q]+0.5))

    def tf(self,doc,query):
        worddic = {}
        for word in doc:
            if word in worddic.keys():
                worddic[word] = worddic[word]+1
            else:
                worddic[word] = 0

        # for q in query:
        #     if q in worddic:




    def score(self,doc,query):
        score = 0.0
        for q in query:
            self.IDF(q)*()*(self.k+1)/(+self.k*(1-self.b+self.b*self.D/self.avgdl))





if __name__ == '__main__':
    docs = ['today is friday','how are you']
    bm25 = BM25(docs=docs)
    print(bm25.avgdl)


