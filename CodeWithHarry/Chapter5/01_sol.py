
# dictionary for synonyms 
synonyms = {
    "happy": ["joyful", "content", "cheerful", "delighted", "pleased"],
    "sad": ["unhappy", "sorrowful", "depressed", "downcast", "melancholy"],
    "fast": ["quick", "speedy", "swift", "rapid", "brisk"],
    "slow": ["sluggish", "lethargic", "unhurried", "lagging", "dull"],
    "smart": ["intelligent", "clever", "bright", "brainy", "wise"],
    "big": ["large", "huge", "massive", "enormous", "gigantic"],
    "small": ["tiny", "little", "miniature", "petite", "compact"],
    "easy": ["simple", "effortless", "straightforward", "clear", "uncomplicated"],
    "hard": ["difficult", "challenging", "tough", "tricky", "demanding"],
    "beautiful": ["pretty", "lovely", "gorgeous", "stunning", "attractive"]
}


word = input("enter the word for synonyms : ")
print(synonyms[word])