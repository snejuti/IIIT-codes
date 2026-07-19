# %%
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# %%
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# %%
# Download the small NLTK data packages for tokenizing, stopwords, and lemmatization
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

STOP_WORDS = set(stopwords.words('english'))
LEMMATIZER = WordNetLemmatizer()

# %% [markdown]
# # STEP 1: Load Dataset

# %%

# Load the original AG News training and testing datasets
train_df = pd.read_csv(r"D:\Users\ANAMIKA\Documents\IIIT\AVG\train.csv")
test_df = pd.read_csv(r"D:\Users\ANAMIKA\Documents\IIIT\AVG\test.csv")

# %%
print("Training Data")
print(train_df.head())

print("\nTesting Data")
print(test_df.head())

# %%
# Mapping numeric class labels to category names
CLASS_MAP = {
    1: "World",
    2: "Sports",
    3: "Business",
    4: "Sci/Tech"
}

# %%
# Combine Title and Description into a single text column
train_df["text"] = (
    train_df["Title"].astype(str) + " " + train_df["Description"].astype(str)
)

test_df["text"] = (
    test_df["Title"].astype(str) + " " + test_df["Description"].astype(str)
)

# %%
# Convert numeric labels into category names
train_df["category"] = train_df["Class Index"].map(CLASS_MAP)
test_df["category"] = test_df["Class Index"].map(CLASS_MAP)

# %%
# Keep only the required columns
train_df = train_df[["text", "category"]]
test_df = test_df[["text", "category"]]

# %%
# Remove any missing values (if present)
train_df = train_df.dropna().reset_index(drop=True)
test_df = test_df.dropna().reset_index(drop=True)

# %%
# Display size
print("Training Dataset Shape:", train_df.shape)
print("Test Dataset Shape:", test_df.shape)

# %%
print("\nTraining Category Distribution:")
print(train_df["category"].value_counts())

# %%
# Display the first five rows
train_df.head(10)

# %% [markdown]
# # STEP 2: Text Cleaning

# %%
import re

def clean_text(text):
    """
    Cleans the input text by:
    1. Converting to lowercase.
    2. Removing URLs.
    3. Removing punctuation and numbers.
    4. Removing extra spaces.
    """

    # Convert text to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove punctuation and numbers
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

# %%
# Apply text cleaning to both datasets
train_df["clean_text"] = train_df["text"].apply(clean_text)
test_df["clean_text"] = test_df["text"].apply(clean_text)

# %%
# Display original vs cleaned text
comparison = pd.DataFrame({
    "Original Text": train_df["text"].head(5),
    "Cleaned Text": train_df["clean_text"].head(5)
})

comparison

# %% [markdown]
# # STEP 3: Tokenization

# %%
def tokenize(text):
    """Split cleaned text into a list of word tokens."""
    return word_tokenize(text)

# %%
# Apply tokenization on both
train_df["tokens"] = train_df["clean_text"].apply(tokenize)
test_df["tokens"] = test_df["clean_text"].apply(tokenize)


# %%
#Display te first dew tokenize articles
train_df[["clean_text", "tokens"]].head()


# %%
train_df[["clean_text", "tokens"]].head()

# %% [markdown]
# # STEP 4: StopWord Removal

# %%
# Function to remove stopwords
def remove_stopwords(tokens):
    """
    Removes common English stopwords from a list of tokens.
    """
    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]
    return filtered_tokens

# Apply stopword removal
train_df["filtered_tokens"] = train_df["tokens"].apply(remove_stopwords)
test_df["filtered_tokens"] = test_df["tokens"].apply(remove_stopwords)

# Compare before and after
comparison = pd.DataFrame({
    "Before": train_df["tokens"].head(5),
    "After": train_df["filtered_tokens"].head(5)
})

comparison

# %%
def remove_stopwords(tokens):
    """Remove common English stopwords."""
    return [t for t in tokens if t not in STOP_WORDS]


# %%
# Apply stopword removal
train_df["filtered_tokens"] = train_df["tokens"].apply(remove_stopwords)
test_df["filtered_tokens"] = test_df["tokens"].apply(remove_stopwords)


# %%
# Compare before and after
comparison = pd.DataFrame({
    "Before": train_df["tokens"].head(5),
    "After": train_df["filtered_tokens"].head(5)
})

comparison

# %% [markdown]
# # STEP 5: Lemmatization

# %%
# FUnction to Lemmatize Tokens
def lemmatize(tokens):
    """Reduce each token to its dictionary root form."""
    return [LEMMATIZER.lemmatize(t) for t in tokens]

# %%
# Apply lemmatization
train_df["lemmatized_tokens"] = train_df["filtered_tokens"].apply(lemmatize)
test_df["lemmatized_tokens"] = test_df["filtered_tokens"].apply(lemmatize)


# %%
# Compare before and after
comparison = pd.DataFrame({
    "Before": train_df["filtered_tokens"].head(5),
    "After": train_df["lemmatized_tokens"].head(5)
})

comparison

# %%
# Convert token lists back into sentences
train_df["processed_text"] = train_df["lemmatized_tokens"].apply(lambda words: " ".join(words))
test_df["processed_text"] = test_df["lemmatized_tokens"].apply(lambda words: " ".join(words))

# %%
train_df[["text", "clean_text", "category"]].head(10)

# %% [markdown]
# ## STEP 6: TF-IDF Vectorization

# %%
# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=20000, ngram_range=(1, 2))

# %%
# Learn vocabulary from training data and transform it
X_train = vectorizer.fit_transform(train_df["clean_text"])

# Transform test data using the same vocabulary
X_test = vectorizer.transform(test_df["clean_text"])

# %%
# Target labels
y_train = train_df["category"]
y_test = test_df["category"]

# %%
# Display information
print("Training Feature Matrix Shape :", X_train.shape)
print("Testing Feature Matrix Shape  :", X_test.shape)
print("Number of Features            :", len(vectorizer.get_feature_names_out()))

# %% [markdown]
# # STEP 7: Train-Test Split

# %%
print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples:  {X_test.shape[0]}")

# %% [markdown]
# # STEP 8: Train MOodel

# %%
# Initialize the Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train the model using the training data
model.fit(X_train, y_train)

print("Model training completed successfully!")

# %% [markdown]
# # STEP 9: Prediction

# %%
# Predict categories for the test dataset
y_pred = model.predict(X_test)


# %%
# Display some sample predictions
results = pd.DataFrame({
    "text": test_df["text"].values,
    "Actual": y_test.values,
    "Predicted": y_pred
})
results.head(10)

# %% [markdown]
# # STEP 10: Model Evaluation

# %%
# Calculate the accuracy
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc * 100:.2f}%\n")

# Display Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# %%
# Generate the confusion matrix
labels = sorted(y_test.unique())
cm = confusion_matrix(y_test, y_pred)

# Display the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Category")
plt.ylabel("Actual Category")
plt.show()

# %% [markdown]
# # Custom News Headline Prediction

# %%
def predict_headline(headline):
    """
    Predict the category of a custom news headline.
    """

    # Apply the same preprocessing used during training
    cleaned = clean_text(headline)
    tokens = tokenize(cleaned)
    filtered = remove_stopwords(tokens)
    lemmatized = lemmatize(filtered)
    processed_text = " ".join(lemmatized)

    # Convert text into TF-IDF features
    vector = vectorizer.transform([processed_text])

    # Predict category
    prediction = model.predict(vector)[0]

    return prediction

# %%
print("=" * 60)
print("Custom News Category Prediction")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    headline = input("\nEnter a news headline: ")

    if headline.lower() == "exit":
        print("\nThank you for using the News Classifier!")
        break

    predicted_category = predict_headline(headline)

    print(f"Predicted Category: {predicted_category}")

# %%



