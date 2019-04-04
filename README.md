# SWOW-eval
This project describes a new task for evaluating pre-trained word embeddings. In particular, we present the intrinsic evaluation task originally named **SWOW-8500**, and employs a large word association dataset called the [Small World of Words (SWOW)](https://smallworldofwords.org/en/). 

This repository also serves as the go-to page regarding our paper titled *"SWOW-8500: Word Association Task for Intrinsic Evaluation of Word Embeddings"*, accepted at the [RepEval2019](https://repeval2019.github.io/index) workshop, collocated with the 2019 Annual Conference of the North American Chapter of the Association for Computational Linguistics ([NAACL 2019](https://naacl2019.org) June 2–7, 2019, at Minneapolis, United States.

## Index
0. [TL;DR](#the-gist)
1. [Word Associations](#word-associations)
2. [Word Embeddings](#word-embeddings)
3. [Intrinsic and Extrinsic Evaluation](#intrinsic-and-extrinsic-evaluation)
4. [How to Run](#how-to-run)
5. [Results](#results)
6. [Further Reading](#further-reading)

## The Gist

## Word Associations
<img align="right" src="https://github.com/avi-jit/SWOW-eval/blob/master/wordgame.jpg" data-canonical-src="https://github.com/avi-jit/SWOW-eval/blob/master/wordgame.jpg" width="320" height="200"/>

Word Association games are those wherein a participant is asked to utter the first (or first few) words that occur to him/her when given a trigger / cue / stimulus word. For example, given the cue KING, one could respond with RULE, QUEEN, KINGDOM, or even KONG (from the film King Kong). Word associations have long intrigued psychologists including Carl Jung and hence large studies have been conducted in this direction. Some prominent datasets which collect user responses to word association games are enumerated as follows:<br>

* [USF-FA](http://vlado.fmf.uni-lj.si/pub/networks/data/dic/fa/FreeAssoc.htm): University of Southern Florida Free Association norms have single-word association responses from an average of 149 participants per cue for a set of 5,019 cue words.
* [EAT](http://rali.iro.umontreal.ca/rali/?q=en/Textual%20Resources/EAT): Edinburgh Association Thesaurus collects 100 responses per cue for a total of 8,400 cues. 
* [JeuxDeMots](http://www.jeuxdemots.org/jdm-accueil.php): is a crowdsourced game which has collected over 5 million french word associations so far. 
* **[SWOW (Small World of Words)](https://smallworldofwords.org/en/project)**: lists word association and participant data for 100 primary, secondary and tertiary responses to 12,292 cues, collected from over 90,000 participants. 
* [Birkbeck norms](https://books.google.co.in/books?id=loDxzOXCRlYC&printsec=frontcover): contain 40 to 50 responses for over 2,600 cues in British English.


## Word Embeddings
Word Embeddings are vector representation of words, i.e. an array of floating point numbers for each word. This helps computers make more sense out of the mystical natural langauge we humans use, and has been fairly helpful in recent developments in Natural Language Processing (think Machine Translation), Information Retrieval (think Search Engines), and Image Captioning (think Google Images or GIF search). In layman terms, the secret lies in letting related words have similar vectors, but there have been a slew of approaches to come up with such word embeddings. We list down some of the most popular, as well as the most effective ones so far. We have used the pretrained versions of these in our experimentation and you shall find them in the folder `WordVectors`:
* **Word2Vec Skip Gram** ([Mikolov et al. 2013a](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf) ; [Mikolov et al. 2013b](https://arxiv.org/pdf/1301.3781.pdf)) trained on Google News. [[Download]](http://code.google.com/archive/p/word2vec/) 
* **GloVe** ([Pennington et al. 2014](https://www.aclweb.org/anthology/D14-1162)) trained on Wikipedia 2014 and Gigaword 5. [[Download]](http://nlp.stanford.edu/projects/glove/)
* **FastText** ([Bojanowski et al. 2017](https://aclweb.org/anthology/Q17-1010)) trained with subword information on Common Crawl (600B tokens). [[Download]](http://fasttext.cc/docs/en/english-vectors.html)
* **ConceptNet Numberbatch** ([Speer et al. 2017](https://arxiv.org/pdf/1612.03975.pdf)) trained on a knowledge graph and some text corpora. [[Download]](http://github.com/commonsense/conceptnet-numberbatch)
* **Count based** ([Baroni et al. 2014](https://www.aclweb.org/anthology/P14-1023)) which is the result of reducing dimensionality of a large count matrix. [[Download]](http://clic.cimec.unitn.it/dm/)

You shall also find a **Base Random** embedding in the folder `WordVectors`, which is a baseline developed by randomly allotting 300 floating numbers to each word in the common vocabulary of the above five embeddings.

## Intrinsic and Extrinsic Evaluation

It is of natural interest to the NLP community to identify evaluation metrics for word embeddings. Besides direct performance measurement on downstream tasks (also called **Extrinsic Evaluation**) like Sentiment Classification, Question Answering, and Chunking, there have also been proposed several **Intrinsic Evaluation** measures such as [WordSim-353](http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/) and [SimLex](https://fh295.github.io//simlex.html). While Extrinsic Evaluations use word embeddings as input features to a downstream task and measure changes in performance metrics specific to that task, Intrinsic Evaluations directly test for syntactic or semantic relationships between word ([Schnabel et al. 2015](https://www.aclweb.org/anthology/D15-1036). Another way to tell apart Intrinsic from Extrinsic evaluations is the lack of any trainable parameters in the former. 

Intrinsic tasks are useful as long as they can accurately predict a model's performance on Extrinsic evaluations, since at the end of the day, the ability to solve downstream tasks is all that matters. Here are a few resources and existing projects that aim to bridge the gap between the two, by experimenting thoroughly with multiple tasks and multiple embeddings:

* [VecEval](https://github.com/NehaNayak/veceval): a repository to run severael Extrinsic Evaluation tasks (slightly outdated) by [Nayak et al. 2016](https://cs.stanford.edu/~angeli/papers/2016-acl-veceval.pdf).
* [wordvectors.org](https://github.com/mfaruqui/eval-word-vectors): a repository to run several Intrinsic Evaluation tasks, by [Faruqui and Dyer 2014](https://www.manaalfaruqui.com/papers/acl14-vecdemo.pdf).
* [ACL SOTA](https://aclweb.org/aclwiki/Similarity_(State_of_the_art)): maintains benchmark pages for word similarity.
* [Vecto AI](https://github.com/vecto-ai/word-benchmarks): an exhaustive collection of Intrinsic tasks, beyond word similarity and relatedness. [Vecto](https://vecto.readthedocs.io/en/docs/tutorial/index.html) is also a library to help run experiments in distributional semantics.


## How to Run

## Results


## Further Reading
[Carl Jung on word associations](https://www.all-about-psychology.com/association-method.html)
