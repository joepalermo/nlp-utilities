from bleu import preproc, precision, modified_precision

"""
Testing that the results from http://www.aclweb.org/anthology/P02-1040.pdf
(BLEU: a Method for Automatic Evaluation of Machine Translation) can be
replicated
"""

# unigrams

print("testing unigrams")
print("example 1")
candidate = preproc("the the the the the the the", 1)
ref1 = preproc("The cat is on the mat", 1)
ref2 = preproc("There is a cat on the mat", 1)
references = [ref1, ref2]
print("candidate 1")
print(precision(candidate, references))
print(modified_precision(candidate, references))

print("example 2")
candidate1 = preproc("It is a guide to action which ensures that the military always obeys the commands of the party", 1)
candidate2 = preproc("It is to insure the troops forever hearing the activity guidebook that party direct", 1)
ref1 = preproc("It is a guide to action that ensures that the military will forever heed Party commands", 1)
ref2 = preproc("It is the guiding principle which guarantees the military forces always being under the command of the Party", 1)
ref3 = preproc("It is the practical guide for the army always to heed the directions of the party", 1)
references = [ref1, ref2, ref3]
print("candidate 1")
print(precision(candidate1, references))
print(modified_precision(candidate1, references))
print("candidate 2")
print(precision(candidate2, references))
print(modified_precision(candidate2, references))

# bigrams

print("\ntesting bigrams")
print("example 1")
candidate = preproc("the the the the the the the", 2)
ref1 = preproc("The cat is on the mat", 2)
ref2 = preproc("There is a cat on the mat", 2)
references = [ref1, ref2]
print("candidate 1")
print(precision(candidate, references))
print(modified_precision(candidate, references))

print("example 2")
candidate1 = preproc("It is a guide to action which ensures that the military always obeys the commands of the party", 2)
candidate2 = preproc("It is to insure the troops forever hearing the activity guidebook that party direct", 2)
ref1 = preproc("It is a guide to action that ensures that the military will forever heed Party commands", 2)
ref2 = preproc("It is the guiding principle which guarantees the military forces always being under the command of the Party", 2)
ref3 = preproc("It is the practical guide for the army always to heed the directions of the party", 2)
references = [ref1, ref2, ref3]
print("candidate 1")
print(precision(candidate1, references))
print(modified_precision(candidate1, references))
print("candidate 2")
print(precision(candidate2, references))
print(modified_precision(candidate2, references))
