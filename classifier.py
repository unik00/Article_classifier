from os import listdir
from CocCocTokenizer import PyTokenizer
from math import log
import numpy as np

T = PyTokenizer(load_nontone_data=True)

trained = dict()
total = dict()


def normalize(s):
    return s.lower()


def train(cl):
    trained[cl] = dict()
    total[cl] = 0

    for file in listdir("data/train/" + cl):
        # print(file)
        with open("data/train/" + cl + "/" + file, "r") as f:
            content = ''.join(f.readlines())
            tokens = T.word_tokenize(content, tokenize_option=0)
            for token in tokens:
                if normalize(token) not in trained[cl]:
                    trained[cl][normalize(token)] = 1
                else:
                    trained[cl][normalize(token)] += 1
                total[cl] += 1


def get(cl, token):
    token = normalize(token)
    if token not in trained[cl]:
        a = 0
    else:
        a = trained[cl][token]
    return (a + 1) / (total[cl] + 2)


def get_class_prob(cl):
    sum = 0
    for key in total:
        sum += total[key]

    if cl not in total:
        a = 0
    else:
        a = total[cl]

    return (a + 1) / (sum + 2)


def predict(doc):
    prob_chinhtri = log(get_class_prob("chinhtri"))
    prob_giaoduc = log(get_class_prob("giaoduc"))
    prob_thethao = log(get_class_prob("thethao"))

    tokens = T.word_tokenize(doc, tokenize_option=0)
    for token in tokens:
        prob_chinhtri += log(get("chinhtri", token))
        prob_giaoduc += log(get("giaoduc", token))
        prob_thethao += log(get("thethao", token))

    labels = ["Chính trị", "Giáo dục", "Thể thao"]

    arg_max = np.argmax([prob_chinhtri, prob_giaoduc, prob_thethao])
    print(labels[arg_max])


if __name__ == "__main__":
    train("chinhtri")
    train("giaoduc")
    train("thethao")
    with open("input.txt", "r") as f:
        doc = ''.join(f.readlines())
        # print(doc)
        predict(doc)

    pass