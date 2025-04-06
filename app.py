import streamlit as st
from spotifyRecommendation import recommend_songs,df

st.title("Music Recommendation System 🎵")
st.write("Select a song to get personalized recommendations.")

# Dropdown to select song
selected_song = st.selectbox("Choose a song", df["name"].unique())

if st.button("Get Recommendations"):
    recommendations = recommend_songs(selected_song, df)
    st.write(recommendations)

