import pandas as pd
from sklearn.model_selection import train_test_split
import os

#URL to dataset
url = "https://raw.githubusercontent.com/avi350751/my-datasets/main/student_performance.csv"

#Read the dataset
df = pd.read_csv(url)

#Split the data into train and test set
train, test = train_test_split(df, test_size=0.2, random_state=42)

#Save the splits
train.to_csv('data/raw/train.csv', index=False)
test.to_csv('data/raw/test.csv', index=False)