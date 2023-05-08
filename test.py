import pandas as pd
from transformers import GPT2Tokenizer, GPT2ForSequenceClassification

# absolute path
file_path = 'C:/Users/HP/Desktop/innovation project/data.csv'
df = pd.read_csv(file_path)


# Load the pre-trained model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2ForSequenceClassification.from_pretrained("gpt2")

def predict_sentiment(text):
    # Encode the text
    encoded_text = tokenizer.encode(text, return_tensors="pt")
    # Predict the sentiment
    sentiment = model(encoded_text)[0]
    # Decode the sentiment
    return sentiment.argmax().item()

# Test the model
text = "I love this product!"
list=[]
for x in df['Sentence']:
    sentiment = predict_sentiment(x)
    print("Sentiment: ",sentiment) # 1 for positive, 0 for negative
    # list.append(sentiment)  