import pytest

from project3 import *

def test_readData():
    trainSent, trainCens, validSent, validCens, testSent, testCens = readData()
    assert len(trainSent) == len(trainCens)
    assert len(validSent) == len(validCens)
    assert len(testSent) == len(testCens)

