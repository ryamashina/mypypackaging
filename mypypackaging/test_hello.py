#import unittest
import pytest
import seaborn as sns 
from divepackaging.hello import main


@pytest.fixture
def test_file():
    tips = sns.load_dataset('tips')
    return tips

def test_hello_main(test_file):
    """test method for main
    """
    main()
    #print(test_file)
    #assert 1==2
