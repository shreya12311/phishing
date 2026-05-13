# Phishing Email Detection System

## Overview
The Phishing Email Detection System is a Machine Learning based cybersecurity project developed using Python and Scikit-learn. 

This system analyzes email messages and predicts whether the email is:
- Phishing
- Safe

The project helps users identify suspicious emails that may contain scams, fake links, password theft attempts, or malicious content.

---

## Objective
The main objective of this project is to improve email security by detecting phishing emails using Machine Learning techniques.

---

## Features
- Detect phishing emails
- Classify emails as Safe or Phishing
- Suspicious keyword detection
- Email verification warning system
- Machine Learning based prediction
- Accuracy score display
- Confusion matrix generation

---

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Machine Learning
- Cybersecurity Concepts

---

## Machine Learning Concepts Used
- CountVectorizer
- Naive Bayes Algorithm
- Feature Extraction
- Text Classification
- Pattern Recognition

---

## Project Structure

PHISHING/
│
├── phishing_detector.py
├── README.md
├── datasets/
│   └── emails.csv
└── screenshots/

---

## Dataset
The dataset contains:
- Phishing emails
- Legitimate/Safe emails

The model trains on these examples to identify suspicious email patterns.

---

## How It Works
1. Load email dataset
2. Convert email text into numerical vectors
3. Train Machine Learning model
4. Detect suspicious keywords
5. Predict whether email is phishing or safe
6. Display warning message for phishing emails

---

## Installation

Install required libraries:

pip install pandas scikit-learn

---

## Run the Project

Run the following command:

python phishing_detector.py

OR

python datasets/phishing_detector.py

---

## Example Output

Enter Email Message :
Click here to verify your bank account

Suspicious Keyword Detected : click
Suspicious Keyword Detected : verify

RESULT : THIS EMAIL IS PHISHING

---

## Cybersecurity Relevance
This project demonstrates how Machine Learning can be used in cybersecurity for:
- Email security
- Threat detection
- Spam filtering
- Phishing prevention

---

## Future Improvements
- Real-time email scanning
- URL analysis
- Attachment scanning
- Flask web interface
- Advanced phishing detection using Deep Learning

---

## Author
Developed as part of Cybersecurity Internship Project.
