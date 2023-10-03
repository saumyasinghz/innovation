import praw
import pandas as pd

reddit = praw.Reddit(client_id='', client_secret='', user_agent='')

def extract_comments(comment, data, parent=None):
    data.append(('Reply', comment.body, parent))
    for reply in comment.replies:
        extract_comments(reply, data, comment.body)

data = []

# Fetch the submission using its URL
submission_url = "https://www.reddit.com/r/wallstreetbets/comments/125q6y2/credit_suisse_whistleblowers_say_swiss_bank_has/"
submission = reddit.submission(url=submission_url)
submission.comments.replace_more(limit=None)

# Extract main post content
data.append(('Main Post', submission.selftext, None))

# Extract comments and their replies
for comment in submission.comments:
    extract_comments(comment, data)

# Create a DataFrame from the data list
df = pd.DataFrame(data, columns=['Source', 'Content', 'Parent'])

# Save the DataFrame as a CSV file
df.to_csv('reddit_data_with_replies10.csv', index=False)
