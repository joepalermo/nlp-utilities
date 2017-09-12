from bleu import *

"""
Testing that the results from http://www.aclweb.org/anthology/P02-1040.pdf
(BLEU: a Method for Automatic Evaluation of Machine Translation) and from
here (http://www.nltk.org/_modules/nltk/translate/bleu_score.html) can be
replicated
"""

# some unit testing

# print("test closest")
assert closest(5, [4, 7, 9]) == 4
assert closest(15, [4, 7, 9]) == 9

# visual test of n-grams

# test = preproc("The cat is on the mat", 1)
# test2 = preproc("The cat is on the mat", 2)
# print(test)
# print(test2)
#
# # unigrams
#
# print("testing unigrams")
# print("example 1")
# candidate = preproc("the the the the the the the", 1)
# ref1 = preproc("The cat is on the mat", 1)
# ref2 = preproc("There is a cat on the mat", 1)
# references = [ref1, ref2]
# print("candidate 1")
# print(precision(candidate, references))
# print(modified_precision(candidate, references))
#
# print("example 2")
# candidate1 = preproc("It is a guide to action which ensures that the military always obeys the commands of the party", 1)
# candidate2 = preproc("It is to insure the troops forever hearing the activity guidebook that party direct", 1)
# ref1 = preproc("It is a guide to action that ensures that the military will forever heed Party commands", 1)
# ref2 = preproc("It is the guiding principle which guarantees the military forces always being under the command of the Party", 1)
# ref3 = preproc("It is the practical guide for the army always to heed the directions of the party", 1)
# references = [ref1, ref2, ref3]
# print("candidate 1")
# print(precision(candidate1, references))
# print(modified_precision(candidate1, references))
# print("candidate 2")
# print(precision(candidate2, references))
# print(modified_precision(candidate2, references))
#
# # bigrams
#
# print("\ntesting bigrams")
# print("example 1")
# candidate = preproc("the the the the the the the", 2)
# ref1 = preproc("The cat is on the mat", 2)
# ref2 = preproc("There is a cat on the mat", 2)
# references = [ref1, ref2]
# print("candidate 1")
# print(precision(candidate, references))
# print(modified_precision(candidate, references))
#
# print("example 2")
# candidate1 = preproc("It is a guide to action which ensures that the military always obeys the commands of the party", 2)
# candidate2 = preproc("It is to insure the troops forever hearing the activity guidebook that party direct", 2)
# ref1 = preproc("It is a guide to action that ensures that the military will forever heed Party commands", 2)
# ref2 = preproc("It is the guiding principle which guarantees the military forces always being under the command of the Party", 2)
# ref3 = preproc("It is the practical guide for the army always to heed the directions of the party", 2)
# references = [ref1, ref2, ref3]
# print("candidate 1")
# print(precision(candidate1, references))
# print(modified_precision(candidate1, references))
# print("candidate 2")
# print(precision(candidate2, references))
# print(modified_precision(candidate2, references))

# full scale testing

candidates = preproc_list(["It is a guide to action which ensures that the military always obeys the commands of the party",
                           "It is to insure the troops forever hearing the activity guidebook that party direct"], 1)
references_list = [preproc_list(["It is a guide to action that ensures that the military will forever heed Party commands",
                            "It is the guiding principle which guarantees the military forces always being under the command of the Party",
                            "It is the practical guide for the army always to heed the directions of the party"], 1)]
references_list *= 2 # since there are 2 candidates

# visual test of length matching

# print([len(cand) for cand in candidates])
# print([[len(ref) for ref in refs] for refs in references_list])
# print(best_match_lengths(candidates, references_list))
# print("c: " + str(sum([len(cand) for cand in candidates])))
# print("r: " + str(effective_reference_length(candidates, references_list)))
# print("brevity penalty: " + str(brevity_penalty(candidates, references_list)))

assert effective_reference_length(candidates, references_list) == 34  # 18 + 16

# visual test of precision computation

# print(corpus_modified_precision([candidates[0]], [references_list[0]])) # equivalent to 17/18
# print(corpus_modified_precision([candidates[1]], [references_list[1]])) # equivalent to 8/14
# print(corpus_modified_precision(candidates, references_list))

# testing bleu

raw_candidates = ["It is a guide to action which ensures that the military always obeys the commands of the party"]
raw_references_list = [["It is a guide to action that ensures that the military will forever heed Party commands",
                       "It is the guiding principle which guarantees the military forces always being under the command of the Party",
                       "It is the practical guide for the army always to heed the directions of the party"]]
print(bleu_score(raw_candidates, raw_references_list, 4))

raw_candidates = ["It is a guide to action which ensures that the military always obeys the commands of the party",
                  "he read the book because he was interested in world history"]

raw_references_list = [["It is a guide to action that ensures that the military will forever heed Party commands",
                       "It is the guiding principle which guarantees the military forces always being under the command of the Party",
                       "It is the practical guide for the army always to heed the directions of the party"],
                       ["he was interested in world history because he read the book"]]
print(bleu_score(raw_candidates, raw_references_list, 4))
