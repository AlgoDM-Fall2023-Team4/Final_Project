import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel



def main():
    # Replace 'your_file.csv' with the actual path to your CSV file
    file_path = 'cleaned_dataset.csv'

    # Load the CSV file into a DataFrame
    dataset = pd.read_csv(file_path)

    # Concatenate relevant text features for TF-IDF
    dataset['text_features'] = dataset['Category'] + ' ' + dataset['Artist'] + ' ' + dataset['Title']

    # Create TF-IDF matrix
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset['text_features'])

    # Compute similarity using linear kernel (cosine similarity)
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Streamlit app
    st.title('Image Recommendations Based on Artist')

    # Allow the user to select an artist
    selected_artist = st.selectbox('Select an Artist', dataset['Artist'].unique())

    # Get the index of the selected artist
    artist_index = dataset.index[dataset['Artist'] == selected_artist].tolist()[0]

    # Function to get recommendations based on artist index
    def get_recommendations(artist_index, cosine_similarities):
        similar_images_indices = cosine_similarities[artist_index].argsort()[:-6:-1]

        # Display top 5 recommended images
        recommended_images = dataset.iloc[similar_images_indices][['Image URL', 'Artist', 'Painting Info URL', 'Title']]
        return recommended_images

    # Display the artist name
    selected_artist_row = dataset.iloc[artist_index]
    #st.image(selected_artist_row['Artist Info URL'], caption=selected_artist_row['Artist'], use_column_width=True)

    # Get and display recommendations when the user selects an artist
    if st.button('Get Recommendations'):
        recommendations = get_recommendations(artist_index, cosine_similarities)
        st.write('Top 5 Recommended Images:')
        for index, row in recommendations.iterrows():
            # Display image
            st.image(row['Image URL'], caption=row['Title'], use_column_width=True)

            # Add a hyperlink to open 'Painting Info URL' in a new tab
            button_key = f"button_open_info_{row['Artist']}_{index}"
            st.markdown(f'<a href="{row["Painting Info URL"]}" target="_blank">Open Painting Info for {row["Artist"]}</a>', unsafe_allow_html=True)

