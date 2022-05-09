# cs5293sp22-project3
final project

### Author: Kyle Teel

## Project Video Walkthrough

https://user-images.githubusercontent.com/38758663/167444731-7d46f68c-1bd4-4487-b191-ebf368fb3051.mp4



The packages below are used in the project's virtual environment to successfully run the project.
~~~
sklearn and pytest
~~~

# Project Overview
The task for this project is to train a model that learns from the training set and be evaluated on the validation set. You need to design your README.md describing your code (as usual) and with instruction clear enough to be followed. The key to this task is to 

1) make it easy for a peer to use your code to execute the model on the valudations set;
2) generate a precision, recall, and f1-score of the code for the dataset. 

* Note to do this, you will have to generate code that will understand where the example redaction is in the training set, generate features, and run the model.



## Steps to Run project3.py

- **Step 1**  
using the command below, Clone the project directory from Github

~~~
git clone https://github.com/Infinite-Zero/cs5293sp22-project3
~~~
Once cloned, go to that folder and run following commands


- **Step 2**  
Run command to install pipenv to setup the environment
~~~
pip install pipenv
~~~

- **Step 3**  
Navigate to directory that we cloned from git and run the below command to install dependencies

~~~
pipenv install sklearn, pytest
~~~

- **Step 4**  
Then run the below command to run the project

~~~
pipenv run python project3.py 
~~~

- **Step 5**  
Then run the below command to test the test cases

~~~
 pipenv run python -m pytest -v
~~~



## Methods
### readData
The readData method will read the unredactor.tsv file and split the information into the 3 categories: training, validation, and testing data.
This data will be ignored if it does not have 4 entries (separated by the tab). 
Additionally, it will be ignored if the second input (the field that designated the data set it belongs to) does not match the categories listed above.
Once separated, it will take the data and sends it to word_count which returns a dictionary and return it to the caller.

### wordCount
This will separate the input sentences into a dictionary with the frequency of the word as each word's definition.
The dictionary is returned after the sentence goes through all the words.

### model
This method will make the learning model for the computer to learn off of. It uses a dictionary vectorizor to make the data into lists of mappings like similar to the dictionary.
From here, I used it with the naive bayes model for the prediction of the data. This prediction is then send to the printResults method, which will calculate the precision, recall, accuracy, and f1 score and print it.

### printResults
This will calculate the precision, recall, accuracy, and f1 score using sklearn and print them in an orderly fashion.


## Tests
In the tests, I tested the reading of data in the project3.py file

### test_readData
This checked that the lengths of the inputs would match the length of the outputs for all lists, and that they were not of length 0.
