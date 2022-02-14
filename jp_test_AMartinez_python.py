raw_corpus = "Mary had a little lamb its fleece was white as snow;\n"\
"And everywhere that Mary went, the lamb was sure to go.\n"\
"It followed her to school one day, which was against the rule;\n"\
"It made the children laugh and play, to see a lamb at school.\n"\
"And so the teacher turned it out, but still it lingered near,\n"\
"And waited patiently about till Mary did appear.\n"\
"Why does the lamb love Mary so?\" the eager children cry;\"Why, Mary loves the lamb, you know\" the teacher did reply.\"\n"

# supports 1 word string input for ngrams > 1

n, string = input().split(',')
n = int(n)

def get_ngrams(raw_corpus, n):
  ngrams = []
  corpus = raw_corpus.replace(";", " ").replace("?", "").replace(",", "").replace(".", " ").replace("\"", "").replace("\n", " ").lower()
  splitc = corpus.split()
  for i, w in enumerate(splitc):
    ngram = ""
    if i+n < len(splitc):
      for j in range(n):
        ngram += splitc[i+j] + " "
      ngrams.append(ngram.rstrip())
  return ngrams

ngrams = get_ngrams(raw_corpus, n)

def get_counts(ngrams):
  counts = {}
  for ng in ngrams:
    counts[ng] = ngrams.count(ng)
  return counts

# get observed probabilities
def get_obs_proba(ngrams):
  counts = get_counts(ngrams)
  proba = {}
  for ng in ngrams:
    proba[ng] = counts[ng] / len(ngrams)
  return proba

# print(sum(get_obs_proba(ngrams).values())) # checksum == 1

def get_input_proba(string, ngrams):
# get all ngrams that start with input string
  ngs_starting_w_input = []
  for ng in ngrams:
    if ng.startswith(string+" "):
      ngs_starting_w_input.append(ng)

  # get proba of all ngs_starting_w_input
  probas = []
  for ng in ngs_starting_w_input:
    continuation = ng.lstrip(string).lstrip()
    proba = ngs_starting_w_input.count(ng) / len(ngs_starting_w_input)
    probas.append(continuation+","+format(proba, ".3f"))
  output = ""
  for p in probas:
    output += p + ";"
  print(output.rstrip(";"))

# supports 1 word string input for ngrams > 1
get_input_proba(string, ngrams)
