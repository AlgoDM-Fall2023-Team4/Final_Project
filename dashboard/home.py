import streamlit as st
import requests
import pandas as pd

PREFIX = "http://0.0.0.0:8080"

def home(token: str):
    if "main_dashboard_dict" not in st.session_state:
        st.session_state['main_dashboard_dict'] = None

    if "more_dashboard_dict" not in st.session_state:
        st.session_state['more_dashboard_dict'] = None

    if "selected_image" not in st.session_state:
        st.session_state['selected_image'] = None


    st.title("Art Recommendation Homepage")

    df = pd.read_csv('imagesinfo.csv')

    df['filename_numeric'] = df['filename'].str.replace('.jpg', '').astype(int)
    df = df.sort_values(by="filename_numeric")

    df = df.head(5001)

    df_cleaned = df.dropna(subset=["genre"])

    genre_list = df_cleaned["genre"].drop_duplicates().tolist()

    user_data = {
        "token": token
    }
    response = requests.post(f"{PREFIX}/user", json=user_data)
    user = response.json()
    st.header("Your Recommended Artworks:")

    res = requests.get(f"{PREFIX}/top_categories/{user['email']}")
    categories = res.json()
    # st.write(categories)

    if not st.session_state['main_dashboard_dict']:
        main_dashboard_dict = {}

        for genre in categories:
            df_filtered = df_cleaned[df_cleaned['genre'] == genre]
            df_sampled = df_filtered.sample(3)
            main_dashboard_dict[genre] = df_sampled['filename'].tolist()
        for i, j in main_dashboard_dict.items():
            st.subheader(i)
            with st.container():
                images = []
                for k in j:
                    image_path = f"/Users/pranitha/Desktop/AlgoDM/FinalProject/images/data/{k}"
                    images.append(image_path)

                k = 0
                for col in st.columns(3):
                    col.image(images[k])
                    button_clicked = col.button("Show", key=images[k])
                    if button_clicked:
                        st.session_state.selected_image = images[k]
                    k += 1
        st.session_state['main_dashboard_dict'] = main_dashboard_dict
    else:
        for i,j in st.session_state.main_dashboard_dict.items():
            st.subheader(i)
            with st.container():
                images = []
                for k in j:
                    image_path = f"/Users/pranitha/Desktop/AlgoDM/FinalProject/images/data/{k}"
                    images.append(image_path)

                k = 0
                for col in st.columns(3):
                    col.image(images[k])
                    button_clicked = col.button("Show", key = images[k])
                    if button_clicked:
                        st.session_state.selected_image = images[k]

                    k += 1

    st.header("More Artworks:")
    more_genre_list = [element for element in genre_list if element not in categories]

    if not st.session_state['more_dashboard_dict']:
        more_dashboard_dict = {}
        index = 0
        for genre in more_genre_list:
            if index == 3:
                break
            df_filtered = df_cleaned[df_cleaned['genre'] == genre]
            df_sampled = df_filtered.sample(1)
            more_dashboard_dict[genre] = df_sampled['filename'].tolist()
            index += 1

        with st.container():
            cols = st.columns(3)
            for col, images in zip(cols, more_dashboard_dict.values()):
                image_path = f"/Users/pranitha/Desktop/AlgoDM/FinalProject/images/data/{images[0]}"
                col.image(image_path)
                button_clicked = col.button("Show", key=image_path)
                if button_clicked:
                    st.session_state.selected_image = image_path
        st.session_state['more_dashboard_dict'] = more_dashboard_dict
    else:
        with st.container():
            cols = st.columns(3)
            for col, images in zip(cols, st.session_state.more_dashboard_dict.values()):
                image_path = f"/Users/pranitha/Desktop/AlgoDM/FinalProject/images/data/{images[0]}"
                col.image(image_path)
                button_clicked = col.button("Show", key=image_path)
                if button_clicked:
                    st.session_state.selected_image = image_path

    if st.session_state.selected_image:
        st.session_state.go_to_display_image = True
        st.experimental_rerun()


if __name__ == '__main__':
    home()
