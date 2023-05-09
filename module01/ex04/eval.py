class Evaluator:
    def parse(worlds,coefs):
        if not isinstance(worlds,list):
            return -1
        if not isinstance(coefs,list):
            return -1
        for i , j in zip(worlds,coefs):
            if not isinstance(i,str) or not isinstance(j,float) : # or j < 0:
                return -1
    def zip_evaluate(words, coefs):
        if -1 == Evaluator.parse(words,coefs):
            return -1
        if len(words) != len(coefs):
            return -1
        sum = 0
        for word, coef in zip(words, coefs):
            sum += coef * len(word)
        return sum
    def enumerate_evaluate(words, coefs):
        if len(words) != len(coefs):
            return -1
        sum = 0
        for index, word in enumerate(words):
            sum += coefs[index] * len(word)
        return sum
# words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
# print(Evaluator.enumerate_evaluate(words, coefs))
