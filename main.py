import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
from clean_functions import info

def preprocess_input(title, story):
    # takes strings title and story and returns back a df that is the sample data matching model expectations
    title_params = {key: value for key, value in info(title, True).items() if type(value) != str}
    story_params = {key: value for key, value in info(story, False).items() if type(value) != str}
    user_data = pd.DataFrame({**title_params, **story_params}, index=[0])
    return user_data

def main():
    st.title("Story Upvote Expectations")

    title = st.text_input("Enter the title:")
    story = st.text_area("Enter the story:", height=200)
    loaded_model = load('stories_model.joblib')
    
    note = st.text("NOTE: For MOST accurate results, input a complete title and story. \nInaccurate results will occur with very short stories.")
    
    if st.button("Submit"):
        # Process input data and inputs it into model and returns prediction
        user_data = preprocess_input(title, story)
        log_predictions = loaded_model.predict(user_data)
        predictions = np.expm1(log_predictions)
        st.write("### Expected Upvotes:", int(predictions[0]))

if __name__ == '__main__':
    main()



