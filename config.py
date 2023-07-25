import os

PORT_NUMBER = 8080

MONGODB_PORT_NUMBER = 27017
MONGODB_DATABASE_NAME = 'project_db'

# Use os.path.join to create the model and JSON file paths
MODEL_FILE_PATH = os.path.join('static', 'models', 'linear_regression.pkl')
JSON_FILE_PATH = os.path.join('static', 'json_files', 'proj_data.json')
