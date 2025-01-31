import pandas as pd
# Import necessary libraries
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("./data/Symptom2Disease.csv")


# Download stopwords from nltk
nltk.download('stopwords')

# Define the stopwords list
stop_words = stopwords.words('english')

# Preprocessing function (remove stopwords, lowercase)
def preprocess(text):
    text = text.lower()  # Convert text to lowercase
    text = ' '.join([word for word in text.split() if word not in stop_words])  # Remove stopwords
    return text

# Assuming 'df' is your dataset with symptoms and diseases
# Vectorize the symptoms using TfidfVectorizer
vectorizer = TfidfVectorizer(preprocessor=preprocess)
X = vectorizer.fit_transform(df['text'])  # Symptoms column
y = df['label']  # Disease column

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model (Random Forest in this case)
model = RandomForestClassifier(n_estimators=100, max_depth=10)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
