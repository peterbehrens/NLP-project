from joblib import load
import spacy



class Model:
    def __init__(self, path_to_clf = "./model.joblib"):
        self.clf = load(path_to_clf) 
        self.nlp = spacy.load('de_core_news_lg')
    
    def predict(self, snippet):
        snippet = self.prepare_snippets(snippet)
        prediction = self.clf.predict(snippet.reshape(1, -1))[0]
        return prediction

    def prepare_snippets(self, snippet, raw_string_return = False, remove_int = False, lowercase = True, stopwords = True, punctuations = True, only_nouns_n_adjs = True, lammatize = True, reduce=True, word_embeddings = True):
        
        if lowercase:
            snippet = snippet.lower()
        snippet = self.nlp(snippet)
        if stopwords:
            snippet = [word for word in snippet if word.is_stop == False]
        if punctuations:
            snippet = [word for word in snippet if word.is_punct == False]
        if only_nouns_n_adjs:
            snippet = [word for word in snippet if (word.pos_ == "NOUN" or word.pos_ == "ADJ")]
        if lammatize:
            snippet = [word.lemma_.strip() for word in snippet]
        if reduce:
            snippet = set(snippet)
        if remove_int:
            snippet = ''.join([i for i in snippet if not i.isdigit()])
            try:
                snippet = self.nlp(snippet)
            except:
                pass
        try:
            snippet = self.nlp(" ".join(snippet))
        except:
            pass
        if word_embeddings:
            snippet = snippet.vector
        
        if raw_string_return:
            return str(snippet.text)
        
        return snippet    