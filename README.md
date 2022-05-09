# cs5293sp22-project3
final project

The packages below are used in the project's virtual environment to successfully run the project.
~~~
sklearn and pytest
~~~

## Project Overview
The task for this project is to train a model that learns from the training set and be evaluated on the validation set. You need to design your README.md describing your code (as usual) and with instruction clear enough to be followed. The key to this task is to 

1) make it easy for a peer to use your code to execute the model on the valudations set;
2) generate a precision, recall, and f1-score of the code for the dataset. 

* Note to do this, you will have to generate code that will understand where the example redaction is in the training set, generate features, and run the model.


## Steps to Run project3

- **Step1**  
using the command below, Clone the project directory from Github

~~~
git clone https://github.com/Infinite-Zero/cs5293sp22-project3
~~~
Once cloned, go to that folder and run following commands


- **Step2**
Run command to install pipenv to setup the environment
~~~
pip install pipenv
~~~

- **Step3**  
Navigate to directory that we cloned from git and run the below command to install dependencies

~~~
pipenv install sklearn, pytest
~~~

- **Step4**  
Then run the below command by providing URL
~~~
pipenv run python project3.py 
~~~
- **Step5** 

Then run the below command to test the testcases. 

~~~
 pipenv run python -m pytest -v
~~~





