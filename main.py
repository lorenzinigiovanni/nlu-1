import spacy
from spacy import displacy


def getDependecyPaths(sentence):
    doc = nlp(sentence)
    list1 = []

    for token in doc:
        list2 = []
        while(token.head != token):
            list2.append(token.text)
            list2.append('--' + token.dep_ + '->')
            token = token.head
        list2.append(token.text)
        list2.append('--' + token.dep_ + '->')
        list2.append('ROOT')
        list1.append(list2[::-1])

    return list1


def getSubtrees(sentence):
    doc = nlp(sentence)
    list1 = []

    for token in doc:
        list2 = []
        for descendant in token.subtree:
            if(descendant != token):
                list2.append(descendant)
        list1.append((token.text, list2))

    return list1


def formsASubtree(sentence, tokenList):
    doc = nlp(sentence)
    tokenSet = set(tokenList)

    subtrees = []

    for token in doc:
        list2 = []
        for descendant in token.subtree:
            list2.append(descendant.text)
        subtrees.append(list2)

    for subtree in subtrees:
        subtreeSet = set(subtree)
        if(tokenSet == subtreeSet):
            return True

    return False


def getSpanHead(span):
    doc = nlp(span)

    root = [token for token in doc if token.head == token][0]

    return root.text


def getSpans(sentence):
    doc = nlp(sentence)

    nsubj = []
    for token in doc:
        lista = []
        if(token.dep_ == 'nsubj'):
            for descendant in token.subtree:
                lista.append(descendant.text)
            nsubj.append(' '.join(lista))

    dobj = []
    for token in doc:
        lista = []
        if(token.dep_ == 'dobj'):
            for descendant in token.subtree:
                lista.append(descendant.text)
            dobj.append(' '.join(lista))

    iobj = []
    for token in doc:
        lista = []
        if(token.dep_ == 'iobj'):
            for descendant in token.subtree:
                lista.append(descendant.text)
            iobj.append(' '.join(lista))

    return {'nsubj': nsubj, 'dobj': dobj, 'iobj': iobj}


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
