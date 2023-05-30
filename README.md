# GPT-Based-Chatbot
## Embedding_phone_review_for_search.ipynb
Goal: Collecting review data and embed search vectors
Step 1: Collecting review articles and split them into lists of strings of review article sentence. Embed product name in front of each sentences in the same format as the following example:
'iphone-14\nCorresponding iphone-14 review article sentence. '
Step 2: Using "text-embedding-ada-002" model to calculate seach vectors and embed them into the original sentence as a dataframe in the format of {"text": review article sentence (string), "embedding": embeddings (string)}
Step 3: Store the embeded dataframe as a csv file

## Question_answering_using_embeddings.ipynb
Goal: Prompt engineering for answering questions using the csv file mentioned above about embedded review sentences.
Step 1: Converting "embedding" column from string type to list type
Step 2: Design search function based on search vectors embedded
Step 3: Prompting GPT to give answers based on the given articles (GPT using search function to find several sentences that relates to the user's question)

## Future improvement
Expanding to all products, need to change prompt engineering part and may need to also embed the product type name in front of each review sentence.