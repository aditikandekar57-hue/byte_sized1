# import random module
import streamlit as st
import random

# 2 create subject
subjects =[
    "SRK",
    "Hits run",
    "Delhi ka laadka",
    "A Mumbai cat"
    "Prime minister Modi",
    "Auto driver"
]

actions =[
    "Launchers",
    "Dancers",
    "cancels",
    "orders",
    "eats",
    "declares war with",
    "celebrates",
]

places_or_things =[
    "at airport"
    "during match"
    "at railway"
    "at my house"
    "A cup of coffee"
    "Samosa"
]


while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things )

    headline = f"BREAKING NEWS:{subject}{action}{places_or_thing}"
    print("\n",headline)

    user_input = input("\n Do you want another headline? {yes/no}").strip().lower
    if user_input == "no":
        break

    print("\n Thanks for using this .have a good day")
    