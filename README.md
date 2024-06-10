# Reddit Stories Metric Analysis

## Description

"Reddit Stories" is a project designed to collect, analyze, and predict patterns in Reddit stories quantitatively. The project leverages data science and machine learning techniques to provide insights and predictions based on user-generated content from Reddit.

### Motivation

This project aims to explore how user-generated content on social media platforms like Reddit can be analyzed to uncover patterns and predict future trends through story metrics. The focus is to see how, while stories are heavily qualitatively based, the metrics cause stories to succeed rather than the qualitative aspects.

### Problem Solved

This project addresses the problem of making sense of vast amounts of unstructured data from social media, helping to identify trends, understand the best metrics to optimize your stories, and how to optimize those specific metrics.

### Learning Outcomes

- Gained experience in data collection and cleaning.
- Improved skills in data analysis and visualization.
- Developed predictive models using machine learning.
- Learned to work with APIs and manage Docker containers.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

To get the development environment running, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/syedramim/Stories.git
2. Go into project file:
   ```bash
   cd Stories
3. Create Docker Container:
   ```bash
   docker build -t stories .

## Usage

### Running the application
1. Run Docker Container:
   ```bash
   docker run -p 8501:8501 stories
2. Use the running application at:
   ```bash
   http://localhost:8501/

### Notebooks:
- Open collection.ipynb to see the data collection process.
- Use eda.ipynb for exploratory data analysis. Alongside the process, A/B Testing was applied to determine what is the optimal range to handle a metric.
- predictive_analysis.ipynb contains the predictive modeling steps. XGBRegressor was used to create the model.

## Features
- Data Collection: Fetches data from Reddit using the Reddit PRAW API.
- Data Cleaning: Cleans and preprocesses the collected data using Pandas.
- Exploratory Data Analysis (EDA): Visualizes data to find patterns and insights using Matplotlib and Seaborn.
- Predictive Modeling: Builds models to predict sample stories based on data using sklearn to create a model using XGBRegressor to handle non-parametric data.
- A/B Testing: Includes results from A/B tests on user engagement metrics to determine optimal metric range alongside the metric impact on the success of a story.
