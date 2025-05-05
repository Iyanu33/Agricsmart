import random

def predict_soil(image_path):
    soil_types = ["Loamy Soil", "Clay Soil", "Sandy Soil", "Silty Soil", "Peaty Soil", "Chalky Soil"]
    return random.choice(soil_types)

SOIL_CROP_MAPPING = {
    "Loamy Soil": ["Wheat", "Sugarcane", "Cotton", "Pulses"],
    "Clay Soil": ["Rice", "Broccoli", "Cabbage"],
    "Sandy Soil": ["Watermelon", "Peanuts", "Potatoes"],
    "Silty Soil": ["Rice", "Maize", "Sugar Beet"],
    "Peaty Soil": ["Vegetables", "Salad crops"],
    "Chalky Soil": ["Barley", "Clover", "Spinach"],
}

def get_crops_for_soil(soil_type):
    return SOIL_CROP_MAPPING.get(soil_type, [])
