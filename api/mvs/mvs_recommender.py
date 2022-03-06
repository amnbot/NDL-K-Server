import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

import json
from pathlib import Path



class MvsRecommender:
    
    # Initialize with 
    def __init__(self, user_gender_input, user_mv_input):
        self.user_gender_input = user_gender_input
        self.user_mv_input = user_mv_input


        # Load data
        data_path = ""
        path = Path(__file__)
        data_path = path.parent.parent.parent
        print(data_path)
        # Store data
        self.df = pd.read_json(data_path.as_uri().removeprefix('file:///') + f'/data/mvs/{user_gender_input}_mvs.json')
        # Swap rows and columns
        self.df = self.df.T

        # Create a column to hold the combined string
        self.df['important_features'] = self.get_important_features(self.df)
        self.df['mv_id'] = self.provide_id_to_rows(self.df)

        self.compute_cosine_similarity()

    # Create a function to combine the values of the important columns into a single string
    def get_important_features(self,data):
        important_features = []
        for i in range(0, data.shape[0]):
            important_features.append(data['Release Date'][i] + ' ' + data['Artist'][i] + ' ' + data['Release Type'][i])

        return important_features

    # Create a function to provide an id to every mv
    def provide_id_to_rows(self,data):
        mv_id = []
        for i in range(0, data.shape[0]):
            mv_id.append(i)
        return mv_id

    def compute_cosine_similarity(self):


        # Convert the text to a matrix of token counts
        cm = CountVectorizer().fit_transform(self.df['important_features'])

        # Get the cosine similarity matrix from the count matrix
        self.cs = cosine_similarity(cm)
        

    def compute_top_k_similar_mvs(self, k=10, print_recommendations=False):

        # Print the cosine similarity matrix
        # print(cs)

        # Get the name of the mv that the user likes
        mv_name = self.user_mv_input

        # Find the mv's id
        id_mv = self.df[self.df['Song Name'] == mv_name]['mv_id'].values[0]

        # Create a list of enumerations for the similarity score [(mv_id, similarity score), (...)]
        scores = list(enumerate(self.cs[id_mv]))

        # Sort the list
        self.sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
        self.sorted_scores = self.sorted_scores[1:]

        top_k_mvs = []

        # Print the sorted scores
        # print(sorted_scores)

        # Create a loop to print the first 10 similar MVs
        if print_recommendations:
            print(f'The {k} most recommended MVs to', mv_name, 'are:\n')
        j = 1
        for item in self.sorted_scores:
            name_mv, artist = self.df[self.df.mv_id == item[0]]['Song Name'].values[0], self.df[self.df.mv_id == item[0]]['Artist'].values[0]
            if print_recommendations:
                print(j, name_mv, artist)
            top_k_mvs.append({'Artist': artist, 'Song Name': name_mv, 'Video': self.df[self.df.mv_id == item[0]]['Video'].values[0]})
            j = j + 1
            if j >= k:
                break
    
        return top_k_mvs


if __name__ == '__main__':
    gr = MvsRecommender('gg', 'Feel Special')
    k_mvs = gr.compute_top_k_similar_mvs(20)

    print(k_mvs)