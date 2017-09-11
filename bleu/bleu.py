# genenral utilities

# preprocess an input sentence
def preproc(sentence, n):
    return ngramify(sentence.lower().split(), n)

# construct a list of all n-grams in the sentence
def ngramify(sentence, n):
    k = len(sentence)
    return [' '.join([sentence[i+j] for j in range(n)]) for i in range(k - n + 1)]

# count the number of times a word occurs in a list of words
def count(word, words):
    return sum([1 if word == w else 0 for w in words])

def union_of_sets(sets):
    return set().union(*sets)

# count the maximum number of times a given word occurs in any reference
def max_clip(word, references):
    reference_counts = [count(word, ref) for ref in references]
    return max(reference_counts)

# utilities to compute precision values

def precision(candidate, references):
    reference_words = union_of_sets([set(ref) for ref in references])
    score = sum([1 if word in reference_words else 0 for word in candidate])
    return "precision, " + str(score) + "/" + str(len(candidate))

def modified_precision(candidate, references):
    candidate_words = set(candidate)
    reference_words = union_of_sets([set(ref) for ref in references])
    counts = [count(word, candidate) if word in reference_words else 0 for word in candidate_words]
    max_clips = [max_clip(word, references) for word in candidate_words]
    score = sum([min(c, mclip) for c,mclip in zip(counts, max_clips)])
    return "modified precision, " + str(score) + "/" + str(len(candidate))
