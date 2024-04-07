# Loan Status Prediction

## Overview

The "Loan Status Prediction" project aims to develop a machine learning model that predicts whether a loan application will be approved or denied based on various features provided by the applicant. This project is essential for financial institutions to automate the loan approval process, minimize risks, and improve efficiency.

## Goals

- Develop a machine learning model capable of accurately predicting loan status.
- Analyze and preprocess the dataset to handle missing values, outliers, and feature engineering.
- Evaluate the performance of the model using appropriate evaluation metrics such as accuracy, precision, recall, and F1-score.
- Deploy the trained model into production, enabling real-time loan status predictions.
- Monitor the model's performance over time and update it as necessary to maintain accuracy and reliability.

## Technologies Used

- Python: Programming language for data preprocessing, model development, and deployment.
- Scikit-learn: Python library for machine learning algorithms, model evaluation, and preprocessing techniques.
- Pandas: Data manipulation library for handling datasets and data preprocessing.
- FastApi: Micro web framework for deploying machine learning models as RESTful APIs.
- Docker: Containerization tool for packaging the application and its dependencies.
- AWS (Amazon Web Services): Cloud platform for hosting the application and managing resources.
- Jenkins: Automation server for continuous integration and continuous deployment (CI/CD) pipelines.


## Workflow

1. **Data Collection and Exploration**: Obtain the loan dataset and perform exploratory data analysis (EDA) to understand the data's characteristics and identify patterns.

2. **Data Preprocessing**: Cleanse the dataset by handling missing values, encoding categorical variables, scaling numerical features, and performing feature engineering.

3. **Model Development**: Train and evaluate machine learning models using appropriate algorithms such as logistic regression, random forest, or gradient boosting.

4. **Model Deployment**: Deploy the trained model using Flask as a RESTful API, allowing real-time loan status predictions.

5. **Continuous Integration and Deployment (CI/CD)**: Implement CI/CD pipelines using Jenkins to automate the testing, building, and deployment processes.

6. **Monitoring and Maintenance**: Monitor the deployed model's performance in production, analyze feedback, and update the model as necessary to ensure accuracy and reliability.

## Conclusion

The "Loan Status Prediction" project plays a crucial role in automating the loan approval process for financial institutions, enabling faster decision-making and improving customer experience. By leveraging machine learning techniques and modern technologies, this project showcases the potential for innovation in the finance industry.






# Setup Virtual Environment


```conda```
# Create a virtual environment named jenkins-env with Python 3.11
```
conda create -n jenkins-env python=3.11 -y
```

# Activate the virtual environment
```
conda activate jenkins-env
```

# Install the required packages from requirements.txt
```
pip install -r requirements.txt
```

# Install the current package in development mode
```
pip install .
```

# Test the FASTAPI

```
{
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 1000,
  "Loan_Amount_Term": 1,
  "Credit_History": "1.0",
  "Property_Area": "Rural"
}
```

# Docker Commands
``` ```
# Build a Docker image named loan_pred:v1
```docker build -t loan_pred:v1 .```

# Tag the Docker image for pushing to Docker Hub
```
docker tag loan_pred:v1 impathak/loanpred:v1
```

# Push the Docker image to Docker Hub
```
docker push impathak/loanpred:v1
```

# Run a Docker container named modelv1 based on the impathak/loanpred:v1 image
```
docker run -d -it --name modelv1 -p 8005:8005 impathak/loanpred:v1 bash

```

# Execute the training pipeline inside the running container
```
docker exec modelv1 python prediction_model/training_pipeline.py
```

# Run unit tests using pytest inside the running container
```
docker exec modelv1 pytest -v --junitxml TestResults.xml --cache-clear
```

# Copy the test results XML file from the container to the local directory
```
docker cp modelv1:/code/src/TestResults.xml .
```

# Execute the main.py script inside the container in detached mode
```
docker exec -d -w /code modelv1 python main.py
```

# Start the FASTAPI server inside the container in detached mode
```
docker exec -d -w /code modelv1 uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8005
```




# Installation of Jenkins

# Import the Jenkins GPG key and add the repository to the system
```
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

# Update the package index
```
sudo apt-get update
```

# Install Jenkins
```
sudo apt-get install jenkins
```

# Update the package index and install required dependencies
```
sudo apt update
```
```
sudo apt install fontconfig openjdk-17-jre
```

# Check Java version
```
java -version
```

# Enable Jenkins service to start on boot and start the service
```
sudo systemctl enable jenkins
```
```
sudo systemctl start jenkins
```

# Check the status of Jenkins service
```
sudo systemctl status jenkins
```

 
# Project Snapshot
## Fast Api test

<img src= https://raw.githubusercontent.com/IAMPathak2702/ml-cd-ci-jenkins/main/result/images/FastApi%20Response%20(1).png>


 
## Jenkins Dash Board

<img src= https://raw.githubusercontent.com/IAMPathak2702/ml-cd-ci-jenkins/main/result/images/jenkins%20dashboard.png>

# Build Detail

<img src= https://raw.githubusercontent.com/IAMPathak2702/ml-cd-ci-jenkins/main/result/images/builddetail.png>
