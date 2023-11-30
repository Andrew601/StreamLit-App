# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_probabilities(first_card, second_card, num_decks):
    # All possible card values in blackjack, including 'A'
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'A']

    # Create a deck based on the number of decks
    deck = card_values * 4 * num_decks

    # Remove the first two cards from the deck
    deck.remove(first_card)
    deck.remove(second_card)

    # Calculate probabilities for the next card
    probabilities = [deck.count(value) / len(deck) * 100 for value in card_values]

    return card_values, probabilities

def calculate_busting_probability(first_card, second_card, num_decks):
    card_values, _ = calculate_probabilities(first_card, second_card, num_decks)

    # Calculate the probability of busting on the next card
    total = first_card + second_card
    
    # Initialize an empty list for busting values
    busting_values = []

    for value in card_values:
        # Check if the value is 11 (ace) and whether using it as 11 busts the total
        if value == 11 and total + value > 21:
            busting_values.append(1)  # Consider using the ace as 1
        elif total + value > 21:
            busting_values.append(value)

    # If using Ace as 1 avoids busting, add it to the busting values
    if 11 in card_values and total + 1 <= 21:
        busting_values.append(1)

    busting_probability = len(busting_values) / len(card_values) * 100

    return busting_probability


def main():
    st.title("Blackjack Probability Calculator")

    # Input for the first card
    first_card = st.slider("Select the value of the first card:", 1, 11, key="first_card")

    # Input for the second card
    second_card = st.slider("Select the value of the second card:", 1, 11, key="second_card")

    # Input for the number of decks
    num_decks_options = [1, 2, 3, 4]
    num_decks = st.selectbox("Select the number of decks:", num_decks_options)

    # Calculate probabilities
    card_values, probabilities = calculate_probabilities(first_card, second_card, num_decks)
    busting_probability = calculate_busting_probability(first_card, second_card, num_decks)

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
