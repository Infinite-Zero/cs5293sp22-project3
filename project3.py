from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import DictVectorizer





def word_count(str):
    """Splits sentences into dictionaries with words labeled by occurence"""
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def readData():
    """
    Reads data and returns the sets
    Entries come in the form (proper input will have 4 entries):
    {user github name}  {set where the data belongs}  {censored name}  {sentence with censored bars over name}
    """
    # url = "https://github.com/cegme/cs5293sp22/blob/main/unredactor.tsv"
    ''''''
    items = []
    f = open('C:\\Users\\Kyle\\PycharmProjects\\textAnalytics\\cs5293sp22\\unredactor.tsv',
             encoding='utf8').read().lower().split('\n')
    for i in f:
        i = i.split('\t')
        items.append(i)
        # print(i)

    trainSent = []  # training sentences
    trainCens = []  # censored word from sentences
    validSent = []  # validation sentences
    validCens = []  # censored word from sentences
    testSent = []  # testing sentences
    testCens = []  # censored word from sentences
    inputsNotAccepted = []
    count = 0
    namesNot = []
    for i in range(1, len(items) - 1):
        # {user github name}  {set where the data belongs}  {censored name}  {sentence with censored bars over name}
        if (len(items[i]) == 4):
            if (items[i][1].lower() == "training"):
                trainSent.append(word_count(items[i][3]))
                trainCens.append(items[i][2])
            elif (items[i][1].lower() == "validation"):
                validSent.append(word_count(items[i][3]))
                validCens.append(items[i][2])
            elif (items[i][1].lower() == "testing" or items[i][1].lower() == "test"):
                testSent.append(word_count(items[i][3]))
                testCens.append(items[i][2])
            else:
                namesNot.append(items[i][1])
                count += 1
        else:
            count += 1

    # print(namesNot)
    # print(count)
    return trainSent, trainCens, validSent, validCens, testSent, testCens






def main():
    """Main function to start the program."""
    # reads data and puts it in arrays
    trainSent, trainCens, validSent, validCens, testSent, testCens = readData()
    #print(trainSent[0])

    #training
    dictVec = DictVectorizer(sparse=False)
    Xtrain = dictVec.fit_transform(trainSent)
    Xtest = dictVec.transform(testSent)
    clf = MultinomialNB()

    trainSupport = clf.fit(Xtrain, trainCens)
    results = trainSupport.predict(Xtest)
    printResults(testCens, results, "training")


    #validation
    dictVec2 = DictVectorizer(sparse=False)
    Xvalid = dictVec2.fit_transform(validSent)
    Xtest = dictVec2.transform(testSent)
    clf2 = MultinomialNB()
    validSupport = clf2.fit(Xvalid, validCens)

    results = validSupport.predict(Xtest)
    printResults(testCens, results, "validation")



def printResults(actual, predicted, type):
    """print the precision, recall, accuracy, and f1 score"""
    print('Precision (%s): %.5f' % (type, precision_score(actual, predicted, average='micro')))
    print('Recall (%s): %.5f' % (type, recall_score(actual, predicted, average='micro')))
    print('Accuracy (%s): %.5f' % (type, accuracy_score(actual, predicted)))
    print('F1 Score (%s): %.5f' % (type, f1_score(actual, predicted, average='micro')))
    print()


if __name__ == "__main__":
    main()