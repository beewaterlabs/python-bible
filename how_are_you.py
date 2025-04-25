#!/usr/bin/env python3

def main():
    # Ask the user how they are doing
    response = input("How are you doing today? ")
    
    # Respond based on the user's input
    if response.lower() in ['good', 'great', 'excellent', 'fine', 'well']:
        print("That's wonderful to hear! 😊")
    elif response.lower() in ['bad', 'terrible', 'awful', 'not good']:
        print("I'm sorry to hear that. I hope things get better soon! 💙")
    else:
        print("Thanks for sharing! I hope you have a great day! 🌟")

if __name__ == "__main__":
    main() 



    