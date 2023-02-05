import numpy as np
import random
from textblob import TextBlob

class EVO_Model:
    def __init__(self):
        self.weights = np.zeros(50)
        self.environment = ["Eat","Drink","Sleep","Walk","Run","Jump","Dance","Sing","Read","Write","Listen","Speak","Watch","Play","Swim","Ride","Drive",    "Cook",    "Clean",    "Shop",    "Work",    "Study",    "Pray",    "Meditate",    "Exercise",    "Paint",    "Draw",    "Cook",    "Bake",    "Garden",    "Travel",    "Explore",    "Relax",    "Socialize",    "Volunteer",    "Help",    "Donate",    "Invest",    "Save",    "Spend",    "Earn",    "Manage",    "Organize",    "Decorate",    "Create",    "Innovate",    "Research",    "Analyze",    "Plan",    "Execute"]
        
    def predict(self, inputs):
        sentiment = TextBlob(inputs).sentiment.polarity
        return sentiment
    
    def one_hot_encode(self, inputs):
        encoded = np.zeros(len(self.environment))
        encoded[self.environment.index(inputs)] = 1
        return encoded
    
    def train(self, input_text, response, learning_rate=0.1):
        sentiment_input = TextBlob(input_text).sentiment.polarity
        sentiment_response = TextBlob(response).sentiment.polarity
        similarity = sentiment_input - sentiment_response
        encoded = self.one_hot_encode(input_text)
        errors = similarity
        self.weights += errors * learning_rate * encoded
        
    def evolve(self):
        while True:
            inputs = random.choice(self.environment)
            action = self.predict(inputs)
            print(f"EVO performed action: {inputs}")
            feedback = input("Did EVO perform the right action? (yes/no): ")
            if feedback == "yes":
                targets = action + 1
                self.train(inputs, targets)
            else:
                targets = action - 1
                self.train(inputs, targets)
            print(f"weights: {self.weights}")

evo = EVO_Model()
evo.evolve()
