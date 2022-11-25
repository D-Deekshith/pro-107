import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv('data.csv')

student_df = df[df['student_id'] == 'TRL_987']

fig = px.scatter(
    x = student_df.groupby('level')['attempt'].mean(),
    color = student_df.groupby('level')['attempt'].mean(),
    y = ['level 1', 'level 2', 'level 3', 'level 4'],
    size = student_df.groupby('level')['attempt'].mean(),
)

fig.show()