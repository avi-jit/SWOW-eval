# SWOW-eval
This project describes a new task for evaluating pre-trained word embeddings. In particular, we present the intrinsic evaluation task originally named **SWOW-8500**, and employs a large word association dataset called the [Small World of Words (SWOW)](https://smallworldofwords.org/en/). 

This repository also serves as the go-to page regarding our paper titled [SWOW-8500: Word Association Task for Intrinsic Evaluation of Word Embeddings](https://www.aclweb.org/anthology/papers/W/W19/W19-2006/), accepted at the [RepEval2019](https://repeval2019.github.io/program/) workshop, collocated with the 2019 Annual Conference of the North American Chapter of the Association for Computational Linguistics ([NAACL 2019](https://naacl2019.org) June 2–7, 2019, at Minneapolis, United States.

## Contributors

### [Avijit Thawani](https://avi-jit.github.io/) (author)
BTech and MTech in Computer Science and Engineering, Indian Institute of Technology (BHU) Varanasi. <br>
PhD student, Department of Computer Science, Viterbi School of Engineering, University of Southern California. <br>
**Contact**: avijit.thawani.cse14@iitbhu.ac.in

### [Biplav Srivastava](https://researcher.watson.ibm.com/researcher/view.php?person=us-biplavs)
Distinguished Data Scientist and Master Inventor, IBM New York.

### [Anil K Singh](http://anilkumarsingh.me)
Associate Professor, Department of Computer Science and Engineering, Indian Institute of Technology (BHU) Varanasi.

## Index
1. [Word Associations](#word-associations)
2. [Word Embeddings](#word-embeddings)
3. [Intrinsic and Extrinsic Evaluation](#intrinsic-and-extrinsic-evaluation)
4. [How to Run](#how-to-run)
5. [Results](#results)
6. [Further Reading](#further-reading)
7. [License](#license)

## Word Associations
<img align="right" src="https://github.com/avi-jit/SWOW-eval/blob/master/wordgame.jpg" data-canonical-src="https://github.com/avi-jit/SWOW-eval/blob/master/wordgame.jpg" width="320" height="200"/>

Word Association games are those wherein a participant is asked to utter the first (or first few) words that occur to him/her when given a trigger / cue / stimulus word. For example, given the cue KING, one could respond with RULE, QUEEN, KINGDOM, or even KONG (from the film King Kong). Word associations have long intrigued psychologists including Carl Jung and hence large studies have been conducted in this direction. Some prominent datasets which collect user responses to word association games are enumerated as follows:<br>

* [USF-FA](http://w3.usf.edu/FreeAssociation/): University of Southern Florida Free Association norms have single-word association responses from an average of 149 participants per cue for a set of 5,019 cue words.
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
* [WE Benchmarks](https://github.com/kudkudak/word-embeddings-benchmarks/): another collection of benchmarks for intrinsic evaluation of pretrained embeddings.

## How to Run
There are two fairly interactive and easy-to-read scripts (Python 3) in this repository:
* `SWOW subset.ipynb`: A Jupyter Notebook that takes you from the original Small World of Words dataset, to a specific format of SWOW-NNNN subset in the form of cue: response. You could set different conditions like modifying the minimum count (frequency) of a cue-response pair, to be acceptable into your custom word association dataset. This results in a simple pickle file, used by the following script.
* `SWOW_eval.py`: This reads one or more pretrained embeddings (in FastText .txt format), and an evaluation file (which is the output of the above Jupyter Notebook). It then displays the Precision, Recall, Accuracy, Confidence Interval, OOV (out-of-vocabulary) words for the word association task.

To evaluate a single word embedding file: 

`python SWOW_eval.py 1 Apr_3_cr_dict_min20.pkl numberbatch_65876.txt` <br>
`python SWOW_eval.py <debug> <evalFile> <vecFile>`

To evaluate multiple embedding files (saved within a specific folder):

`python SWOW_eval.py <debug> <evalFile> _ <vecFolder>` <br>
`python SWOW_eval.py 0 Apr_3_cr_dict_min20.pkl _ wordVectors/`

## Results
We found that with the new Word Association tasks, we not only save up on a lot of (expensive and time-consuming) human annotation process, but also report much better confidence intervals on intrinsic evaluation tasks. Performance on SWOW-8500 has been shown to correlate with both (1) existing Word Similarity/Relatedness tasks (Intrinsic Evaluation), as well as (2) multiple Downstream tasks (Extrinsic Evaluation). For further details, please refer to our paper (link shall be posted upon publication).

## Further Reading
* [Carl Jung on word associations](https://www.all-about-psychology.com/association-method.html)
* Problems With Evaluation of Word Embeddings Using Word Similarity Tasks, by [Faruqui et al. 2016](https://arxiv.org/pdf/1605.02276.pdf)
* [NLP-progress](http://nlpprogress.com/): Repository to track the progress in Natural Language Processing (NLP), including the datasets and the current state-of-the-art for the most common NLP tasks.
* A Survey of Word Embeddings Evaluation Methods, by [Amir Bakarov 2018](https://arxiv.org/pdf/1801.09536.pdf)
* Learning word embeddings from the Small World of Words dataset, by [De Deyne et al. 2018](https://simondedeyne.me/articles/2016.DeDeyne.Predicting%20human%20similarity%20judgements.COLING.pdf)
* [Society of Mind](https://en.wikipedia.org/wiki/Society_of_Mind) by Marvin Minsky, the inspiration behind this project.

## License
Code is licensed under MIT, however available embeddings distributed within package might be under different license. If you are unsure please reach to authors (references are included in docstrings)
