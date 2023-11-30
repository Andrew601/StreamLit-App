# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_probabilities(deck, num_decks):
    # All possible card values in blackjack, including 'A'
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    # Calculate probabilities for the remaining deck
    probabilities = [deck.count(value) / len(deck) * 100 for value in card_values]

    return card_values, probabilities

def calculate_busting_probability(deck, total):
    # Calculate the probability of busting on the next card
    busting_values = [value for value in deck if total + value > 21]

    busting_probability = len(busting_values) / len(deck) * 100

    return busting_probability

def main():
    st.title("Blackjack Probability Calculator")

    # Input for the number of decks
    num_decks_options = [1, 2, 3]
    num_decks = st.selectbox("Select the number of decks you're playing with:", num_decks_options)

    # Input for the first card
    first_card = st.slider("Select the value of your first card:", 2, 11)

    # Input for the second card
    second_card = st.slider("Select the value of your second card:", 2, 11)

    # Input for the number of cards dealt to other players
    num_other_cards_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num_cards_dealt = st.selectbox("Number of cards dealt to other players:", num_other_cards_options)

    # Create a deck based on the number of decks
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    deck = card_values * 4 * num_decks

    # Remove the user's cards from the deck
    deck.remove(first_card)
    deck.remove(second_card)

    # Input for other players' cards
    for i in range(num_cards_dealt):
        card_value = st.slider(f"Select the value of {i+1} card dealt to other players:", 2, 11, key=f"slider_{i}")
        deck.remove(card_value)

    # Calculate probabilities
    card_values, probabilities = calculate_probabilities(deck, num_decks)
    busting_probability = calculate_busting_probability(deck, first_card + second_card)

    # Display histogram
    st.subheader("Probability Distribution of Next Card Values:")
    fig, ax = plt.subplots()
    ax.bar(card_values, probabilities)
    ax.set_xlabel("Card Values")
    ax.set_ylabel("Probability (%)")
    st.pyplot(fig)

    # Display busting probability
    st.subheader("Busting Probability on Next Card:")
    st.write(f"The probability of busting on the next card is: {busting_probability:.2f}%")

if __name__ == "__main__":
    main()
