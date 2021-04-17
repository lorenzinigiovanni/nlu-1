# NLU First Assignment

Student:
- **Name:** Giovanni
- **Surname:** Lorenzini
- **Student number:** 223715

## Requirements

To run this project is necessary to have `Python` and `SpaCy`. To install `SpaCy` follow the instructions either for `pip` or `conda`.

### Install `SpaCy` with `conda`

```shell
$ conda install -c conda-forge spacy
$ python -m spacy download en_core_web_sm
```

### Install `SpaCy` with `pip`

```shell
$ pip install -U pip setuptools wheel
$ pip install -U spacy
$ python -m spacy download en_core_web_sm
```

## Report

### 1. Extract a path of dependency relations from the ROOT to a token

The function `getDependecyPaths(sentence)` get in input a `string` representing a sentence and return a `list` of dependecy paths.

Each dependency path is structured as follow:
```python
['word1', '--dep1->', 'word2', '--dep2->', 'word3']
```
For example:
```python
['ROOT', '--ROOT->', 'saw', '--prep->', 'with', '--pobj->', 'telescope']
```

To obtain the dependecy path the code cycle over all the tokens and calls `token.head` to obtain the `head` of a given token until it reaches the `ROOT`. At the end the list is reversed throught `[::-1]` operator to obtain it ordered starting from `ROOT`.

### 2. Extract subtree of a dependents given a token

The function `getSubtrees(sentence)` get in input a `string` representing a sentence and return a `list` of subtrees.

Each subtree is structured as follow:
```python
('token', [listOfSubtreeWords])
```
where the list of subtree words are ordered w.r.t. sentence order.
For example:
```python
('with', ['a', 'telescope'])
```

For each token in a `Doc` the code extract a subtree and add each subtree element except from the token itself to a list. The list is then added to a touple composed of `(token, list)` that in the end are append to the returned list.

### 3. Check if a given list of tokens (segment of a sentence) forms a subtree

The function `formsASubtree(sentence, tokenList)` get in input a `string` representing a sentence and a `list of string` (the tokens) and return a `Boolean` value.

To check if a list of tokens is a subtree I made a `set` from the input tokens and a `set` from every subtree and then I compared them. If the sets are equal then the list of tokens forms a subtree and so the function returns `True`.

### 4. Identify head of a span, given its tokens

The function `getSpanHead(span)` get in input a `string` representing a span and return the head of the span.

To obtain the root of the span I used this code:
```python
root = [token for token in doc if token.head == token][0]
```
and then I returned:
```python
return root.text
```

### 5. Extract sentence subject, direct object and indirect object spans

The function `getSpans(sentence)` get in input a `string` representing a sentence and return the spans for subject (`nsubj`), direct object (`dobj`) and indirect object (`iobj`). 

The return is structured as follow:
- a dictionary that categorize the three types of spans;
- in every dictionary there are a list of the spans of that type.

For example:
```python
{'nsubj': ['I'], 'dobj': ['the man'], 'iobj': []}
```

To obtain the three types of span, the code cycle over all the tokens and check if `token.dep_` is of the type that we want. If it's true then the subtree of that token will be append to the right list.

## Test

Test code:
```python
sentence = 'I saw the man with a telescope.'
span = 'I saw the man'

nlp = spacy.load("en_core_web_sm")

print("Question 1:")
dependencyPaths = getDependecyPaths(sentence)
for dependencyPath in dependencyPaths:
    print(dependencyPath)
print("")

print("Question 2:")
subtrees = getSubtrees(sentence)
for subtree in subtrees:
    print(subtree)
print("")

print("Question 3:")
print(formsASubtree(sentence, ['man', 'telescope']))
print(formsASubtree(sentence, ['a', 'telescope', 'with']))
print("")

print("Question 4:")
spanHead = getSpanHead(span)
print(spanHead)
print("")

print("Question 5:")
spans = getSpans(sentence)
print(spans)
print("")
```

Output:
```
Question 1:
['ROOT', '--ROOT->', 'saw', '--nsubj->', 'I']
['ROOT', '--ROOT->', 'saw']
['ROOT', '--ROOT->', 'saw', '--dobj->', 'man', '--det->', 'the']
['ROOT', '--ROOT->', 'saw', '--dobj->', 'man']
['ROOT', '--ROOT->', 'saw', '--prep->', 'with']
['ROOT', '--ROOT->', 'saw', '--prep->', 'with', '--pobj->', 'telescope', '--det->', 'a']
['ROOT', '--ROOT->', 'saw', '--prep->', 'with', '--pobj->', 'telescope']
['ROOT', '--ROOT->', 'saw', '--punct->', '.']

Question 2:
('I', [])
('saw', ['I', 'the', 'man', 'with', 'a', 'telescope', '.'])
('the', [])
('man', ['the'])
('with', ['a', 'telescope'])
('a', [])
('telescope', ['a'])
('.', [])

Question 3:
False
True

Question 4:
saw

Question 5:
{'nsubj': ['I'], 'dobj': ['the man'], 'iobj': []}
```
