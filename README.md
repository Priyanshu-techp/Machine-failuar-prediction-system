# Machine Failure Prediction System

This is a Streamlit web app to predict machine failure using sensor and environmental data.  
It uses a trained machine learning model (`model.pkl`) to classify failure chances.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py


##Files Info
Data - This folder contains both raw and clean data.

Notebook - This folder includes:
- clean.ipynb: Used to clean the data and perform EDA and visualization.
- model.ipynb: Used to create, train, and tune the machine learning model.

Deploy - This folder contains:
- app.py: Used to create the web interface.
- model.pkl: The trained model used for prediction.

.gitignore - Used to exclude unnecessary files/folders from the Git repository.

README.md - This file; contains the complete project description.

requirements.txt - Contains all the libraries/modules used in the project.


##Author
Priyanshu Pandey