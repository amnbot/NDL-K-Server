import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

import json
from pathlib import Path



class GroupsRecommender:
    
    # Initialize with 
    def __init__(self, user_gender_input, user_group_input):
        self.user_gender_input = user_gender_input
        self.user_group_input = user_group_input


        # Load data
        data_path = ""
        path = Path(__file__)
        data_path = path.parent.parent.parent
        # Store data
        self.df = pd.read_json(data_path.as_uri().removeprefix('file:///') + f'/data/groups/all_{user_gender_input}_groups.json')
        # Swap rows and columns
        self.df = self.df.T

        # Create a column to hold the combined string
        self.df['important_features'] = self.get_important_features(self.df)
        self.df['group_id'] = self.provide_id_to_rows(self.df)

        self.compute_cosine_similarity()

    # Create a function to combine the values of the important columns into a single string
    def get_important_features(self,data):
        important_features = []
        for i in range(0, data.shape[0]):
            important_features.append(data['Company'][i] +  ' ' + data['Active'][i] + ' ' + str(data['Views'][i]).replace('.', ''))

        return important_features

    # Create a function to provide an id to every group
    def provide_id_to_rows(self,data):
        group_id = []
        for i in range(0, data.shape[0]):
            group_id.append(i)
        return group_id

    def compute_cosine_similarity(self):


        # Convert the text to a matrix of token counts
        cm = CountVectorizer().fit_transform(self.df['important_features'])

        # Get the cosine similarity matrix from the count matrix
        self.cs = cosine_similarity(cm)
        

    def compute_top_k_similar_groups(self, k=10, print_recommendations=False):

        # Print the cosine similarity matrix
        # print(cs)

        # Get the name of the group that the user likes
        group_name = self.user_group_input

        # Find the group's id
        id_group = self.df[self.df.Name == group_name]['group_id'].values[0]

        # Create a list of enumerations for the similarity score [(group_id, similarity score), (...)]
        scores = list(enumerate(self.cs[id_group]))

        # Sort the list
        self.sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
        self.sorted_scores = self.sorted_scores[1:]

        if print_recommendations:
            # Print the sorted scores
            # print(sorted_scores)

            # Create a loop to print the first 10 similar groups
            print(f'The {k} most recommended groups to', group_name, 'are:\n')
            j = 1
            for item in self.sorted_scores:
                if self.df[self.df.group_id == item[0]]['Active'].values[0] == 'Yes':
                    name_group = self.df[self.df.group_id == item[0]]['Name'].values[0]
                    print(j, name_group)
                    j = j + 1
                if j >= k:
                    break


if __name__ == '__main__':
    gr = GroupsRecommender('boy', 'ENHYPEN')
    gr.compute_top_k_similar_groups(20, True)