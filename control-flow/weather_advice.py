user_input = input("What's the weather like today? (sunny/rainy/cold): ")
if user_input == "sunny":
    recommendation = "Wear a t-shirt and sunglasses."
elif user_input == "rainy":
    recommendation = "Don't forget your umbrella and a raincoat."
elif user_input == "cold":
    recommendation = "Make sure to wear a warm coat and a scarf."
else:
    recommendation = "Sorry, I don't have recommendations for this weather."
print(recommendation)