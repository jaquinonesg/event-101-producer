#To run the project

# Run in local
python -m venv venv
pip install -r requirements.txt


# Run test
pytest


# Deploy
serverless plugin install -n serverless-python-requirements
serverless deploy