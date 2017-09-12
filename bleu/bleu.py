import math

# genenral utilities

# preprocess an input sentence
def preproc(sentence, n):
    return ngramify(sentence.lower().split(), n)

# preprocess a list of sentences
def preproc_list(sentence_list, n):
    return [preproc(sentence, n) for sentence in sentence_list]

# construct a list of all n-grams in the sentence
def ngramify(sentence, n):
    k = len(sentence)
    return [' '.join([sentence[i+j] for j in range(n)]) for i in range(k - n + 1)]

# count the number of times a word occurs in a list of words
def count(word, words):
    return sum([1 if word == w else 0 for w in words])

# construct a set which is the union of a list of sets
def union_of_sets(sets):
    return set().union(*sets)

# count the maximum number of times a given word occurs in any reference
def max_clip(word, references):
    reference_counts = [count(word, ref) for ref in references]
    return max(reference_counts)

# return the integer in the list 'ls' which is closest in value to the integer n
def closest(n, ls):
    return min([(m, abs(n - m)) for m in ls], key=lambda x: x[1])[0]

# get the gemetric mean of a list
def geometric_mean(ls):
    return sum(map(lambda x: math.log(x), ls)) / len(ls)

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

def corpus_modified_precision(candidates, references_list):
    score = 0
    gram_len = sum([len(cand) for cand in candidates])
    for cand, refs in zip(candidates, references_list):
        cand_grams = set(cand)
        for gram in cand_grams:
            gram_count = count(gram, cand)
            mclip = max_clip(gram, refs)
            gram_score = min(gram_count, mclip)
            score += gram_score
    return score / gram_len


# utilities to compute brevity penlaty

def best_match_lengths(candidates, references_list):
    candidate_lengths = [len(c) for c in candidates]
    reference_lengths = [[len(r) for r in refs] for refs in references_list]
    return [closest(candidate_lengths[i], reference_lengths[i]) for i in range(len(candidates))]

def effective_reference_length(candidates, references_list):
    return sum(best_match_lengths(candidates, references_list))

def brevity_penalty(candidates, references_list):
    r = effective_reference_length(candidates, references_list)
    c = sum([len(cand) for cand in candidates])
    if c > r:
        return 1
    else:
        return math.exp(1 - r/c)

# compute the bleu score

def bleu_score(raw_candidates, raw_references_list, n):
    candidates_list = [preproc_list(raw_candidates, i+1) for i in range(n)]
    references_lists = [[preproc_list(raw_references, i+1) for raw_references in raw_references_list] for i in range(n)]
    p_values = [corpus_modified_precision(cands, refs_list) for cands,refs_list in zip(candidates_list, references_lists)]
    bp = brevity_penalty(candidates_list[0], references_lists[0])
    p_score = math.exp(geometric_mean(p_values))
    return bp * p_score
