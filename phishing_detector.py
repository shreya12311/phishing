import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

print("======================================")
print("   PHISHING EMAIL DETECTION SYSTEM")
print("======================================\n")

# Load Dataset
data = pd.read_csv("datasets/emails.csv")

# Convert email text into numerical data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["text"])

# Labels
y = data["label"]

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train Machine Learning Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy :", round(accuracy * 100, 2), "%\n")

# Confusion Matrix
print("Confusion Matrix :")
print(confusion_matrix(y_test, predictions))
print()

# Suspicious Keywords
suspicious_words = [
    "click",
    "verify",
    "password",
    "urgent",
    "winner",
    "free",
    "reward",
    "bank",
    "account"
]

# User Input
email = input("Enter Email Message : ")

print("\nChecking for suspicious keywords...\n")

found = False

for word in suspicious_words:
    if word in email.lower():
        print("Suspicious Keyword Detected :", word)
        found = True

if not found:
    print("No suspicious keywords detected.")

# Convert input email into vector
email_vector = vectorizer.transform([email])

# Predict result
result = model.predict(email_vector)

print("\n======================================")

if result[0] == "phishing":

    print("RESULT : THIS EMAIL IS PHISHING")
    print("\nWARNING : Suspicious activity detected!")
    print("This email may steal passwords or bank details.")

    verify = input("\nDo you still want to open this email? (yes/no): ")

    if verify.lower() == "yes":
        print("\nAccess Granted With Risk Warning!")
    else:
        print("\nEmail Blocked Successfully!")

else:
    print("RESULT : THIS EMAIL IS SAFE")

print("======================================")
sender = input("Enter Sender Email : ")

trusted_domains = ["gmail.com", "amazon.com", "google.com"]

domain = sender.split("@")[-1]

if domain in trusted_domains:
    print("Trusted Domain Detected")
else:
    print("Warning : Unknown or Suspicious Domain")