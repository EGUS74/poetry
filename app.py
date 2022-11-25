# Environment variables with python

import os
from dotenv import load_dotenv


# Loading the variables from .env
# load_dotenv()

# Run Test|Debug Test
def test_env_variables():
    key = os.environ.get('ACESS_KEY')
    uid = os.environ.get('SECURE_UID')
    assert key
    assert uid

test_env_variables()