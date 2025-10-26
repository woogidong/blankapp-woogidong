from typing import List
import streamlit as st
import matplotlib.pyplot as plt

def plot_performance_chart(incorrect_answers: List[str], correct_answers: List[str]):
    labels = ['Correct', 'Incorrect']
    sizes = [len(correct_answers), len(incorrect_answers)]
    colors = ['#4CAF50', '#F44336']
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.pyplot(fig)

def plot_topic_performance(topic_data: dict):
    topics = list(topic_data.keys())
    scores = [topic_data[topic]['score'] for topic in topics]
    
    fig, ax = plt.subplots()
    ax.barh(topics, scores, color='skyblue')
    ax.set_xlabel('Score')
    ax.set_title('Performance by Topic')
    
    st.pyplot(fig)