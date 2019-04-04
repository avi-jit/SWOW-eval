# final one: 4 April 2019
# to be uploaded on Github

import gensim
from gensim.models import KeyedVectors
import pickle
from os import listdir
import sys
import warnings
from math import sqrt

def read_word_vectors(filename):
    word_vectors = KeyedVectors.load_word2vec_format(filename, binary=False)
    return word_vectors
    try:
        word_vectors = KeyedVectors.load_word2vec_format(filename, binary=False)
        return word_vectors
    except:
        print("Error in reading word vectors from:",filename)
        return -1

def read_wv_pickle(filename):
    word_vectors = pickle.load(open(filename+'.pkl',"rb"))
    return word_vectors

# cr_dict or <evalfile> must be a pickle containing a dictionary of the format:
# {cue1: [r1,r2,r3], cue2: [r1,r2], ...}
def read_eval_file(filename):
    try:
        eval_file = open(filename,'rb')
        cr_dict = pickle.load(eval_file)
        eval_file.close()
        return cr_dict
    except:
        print("Error in reading evaluation file:",filename)
        return -1

def evaluate(wv, cr_dict, debug):
    found = 0 # number of cues taken into account.
    TP, TN, FP, FN = 0,0,0,0 # not counting those whose cues are missing altogether.
    nan, multi_word, missing = 0, 0, 0
    for cue in cr_dict.keys():
        if type(cue) != type(''): # eg. if some nan comes in.
            nan += 1
            continue
        if ' ' in cue or '_' in cue: # To-Do: unify the handling of multi word cues and responses.
            multi_word += 1
            continue
        try:
            n = len(cr_dict[cue]) # n ignored!
            predictions = set([w[0].lower() for w in wv.most_similar(positive=[cue],topn=n)])
        except: # cue not found in wv's vocab.
            missing+=1
            continue
        truth = set(cr_dict[cue])
        found += 1
        tp = predictions.intersection(truth)
        fp = predictions.difference(truth) # we thought they're true but weren't. PRECISION.
        fn_old = truth.difference(predictions) # were true but we couldn't guess. RECALL.
        fn = []
        for w in fn_old:
            try:
                _ = wv[w]
                fn.append(w)
            except:
                continue
        if(debug==1):
            print('\n',cue,':')
            print("TP:",tp)
            print("FP:",fp)
            print("FN:",fn)
        tn = 0
        TP += len(tp)
        FP += len(fp)
        FN += len(fn)
    TN = 0 # we're not accounting for what weren't guessed nor were true.
    precision = TP / (TP + FP)          # denominator is all predictions.
    recall = TP / (TP + FN)             # denominator is all truths.
    f1 = (2 * precision * recall) / (precision + recall)
    accuracy = (TP + TN) / (TP + FP)    # denominator is all predictions.
    error = (FP) / (TP + FP)            # denominator is all predictions.
    # Confidence Interval for ERROR.
    n = TP + FN                         # all truths.
    CI = 99
    if CI == 90:
        const = 1.64
    elif CI == 95:
        const = 1.96
    elif CI == 99:
        const = 2.58
    CI_span = const * sqrt(error * (1-error) / n)
    return precision, recall, f1, found, accuracy, error, CI, CI_span

def perfile(f,eval=eval,debug=0):
    if f[-3:]!='txt':
        return
    try:
        wv = read_word_vectors(f)
    except:
        print("not found")
    precision, recall, f1, found, accuracy, error, CI, CI_span = evaluate(wv,eval,debug)
    print("{:30}\t P:{:1.3f}  R:{:1.3f}  F1:{:1.3f}  found:{}  Accuracy:{:1.3f}  Error:{:1.3f}  CI:{:1.3f}  CI span:{:1.3f}".format(str(f).split('/')[-1][:-8], precision, recall, f1, found, accuracy, error, CI, CI_span))

if __name__ == '__main__':
    debug = int(sys.argv[1]) # 0 for no debugging. 1 for showing tp,fp,fn. 2 maybe later.
    eval_file = str(sys.argv[2])
    word_vec_file = sys.argv[3]
    eval = read_eval_file(filename = eval_file)
    print("Evaluation file read.")
    if word_vec_file == '_':
        word_vec_folder = str(sys.argv[4])
        for f in listdir(word_vec_folder):
            perfile(word_vec_folder+str(f),eval,debug)
    else:
        perfile(word_vec_file,eval,debug)

# Sample execution commands:
# python SWOW_eval.py <debug> <evalFile> <vecFile>
# python SWOW_eval.py <debug> <evalFile> _ <vecFolder>

# python SWOW_eval.py 1 Apr_3_cr_dict_min20.pkl numberbatch_65876
# python SWOW_eval.py 0 Apr_3_cr_dict_min20.pkl _ wordVectors/
