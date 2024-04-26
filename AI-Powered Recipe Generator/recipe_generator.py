import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample database of recipes
recipes = {
    "Spaghetti Carbonara": {
        "ingredients": "pasta, eggs, bacon, parmesan cheese, black pepper",
        "source_link": "https://www.example.com/spaghetti-carbonara",
        "preferences": ["non-vegetarian"],
        "instructions": "1. Cook pasta according to package instructions.\n2. In a separate bowl, whisk together eggs, grated parmesan cheese, and black pepper.\n3. In a skillet, cook bacon until crispy, then remove from heat.\n4. Toss cooked pasta with the bacon and bacon fat.\n5. Add the egg mixture to the pasta, tossing quickly to avoid scrambling the eggs. The heat from the pasta will cook the eggs and create a creamy sauce. Serve immediately.",
    },
    "Chicken Stir-Fry": {
        "ingredients": "chicken, broccoli, carrots, soy sauce, garlic, ginger",
        "source_link": "https://www.example.com/chicken-stir-fry",
        "preferences": ["non-vegetarian"],
        "instructions": "1. Heat oil in a wok or large skillet over high heat.\n2. Add chopped chicken and cook until browned and cooked through.\n3. Add minced garlic and grated ginger, stir for a minute.\n4. Add chopped vegetables (broccoli, carrots) and stir-fry until tender-crisp.\n5. Pour in soy sauce and toss everything together. Serve hot.",
    },
    "Caprese Salad": {
        "ingredients": "tomatoes, mozzarella cheese, basil, olive oil, balsamic vinegar",
        "source_link": "https://www.example.com/caprese-salad",
        "preferences": ["vegetarian"],
        "instructions": "1. Slice tomatoes and mozzarella cheese.\n2. Arrange tomato and mozzarella slices on a plate, alternating them.\n3. Drizzle with olive oil and balsamic vinegar.\n4. Sprinkle fresh basil leaves over the top. Serve as a refreshing salad.",
    },
    "Chocolate Brownies": {
        "ingredients": "chocolate, butter, sugar, eggs, flour, vanilla extract",
        "source_link": "https://www.example.com/chocolate-brownies",
        "preferences": ["vegetarian"],
        "instructions": "1. Preheat oven to 350°F (175°C). Grease a baking pan.\n2. In a microwave-safe bowl, melt chocolate and butter together.\n3. Stir in sugar, eggs, flour, and vanilla extract until well combined.\n4. Pour the batter into the prepared pan.\n5. Bake for about 25 minutes or until a toothpick inserted in the center comes out with moist crumbs. Let it
