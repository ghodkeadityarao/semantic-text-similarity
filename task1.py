import numpy as np
import pandas as pd
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

# Load the spaCy model
nlp = spacy.load("en_core_web_lg")

# Function to preprocess text
def preprocess_text(text):
    doc = nlp(text)
    # Remove stop words and punctuation
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

# Function to compute similarity score
def compute_similarity(text1, text2):
    # Preprocess the texts
    processed_text1 = preprocess_text(text1)
    processed_text2 = preprocess_text(text2)
    
    # Compute word embeddings for each token in the processed text
    embeddings_text1 = np.array([token.vector for token in nlp(processed_text1)])
    embeddings_text2 = np.array([token.vector for token in nlp(processed_text2)])
    
    # Aggregate embeddings to get paragraph vectors (averaging)
    paragraph_vector_text1 = np.mean(embeddings_text1, axis=0)
    paragraph_vector_text2 = np.mean(embeddings_text2, axis=0)
    
    # Compute cosine similarity between paragraph vectors
    similarity_score = cosine_similarity([paragraph_vector_text1], [paragraph_vector_text2])[0][0]
    similarity_score = round(np.float64(similarity_score), 2)
    return similarity_score

'''
# Apply the compute_similarity function to each pair of text paragraphs 
# in the dataset and save the similarity scores to a new column in the DataFrame.

df = pd.read_csv("DataNeuron_Text_Similarity.csv") 

similarity_scores = []
for index, row in tqdm(df.iterrows()):
    text1 = row['text1']
    text2 = row['text2']
    similarity_score = compute_similarity(text1, text2)
    similarity_scores.append(similarity_score)

df['similarity_score'] = similarity_scores
print(df)
df.to_csv("updated.csv")

'''
