import spacy

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Function to get the response from the chatbot


def get_response(query):
    # Process the user query
    doc = nlp(query)

    # Extract important information from the user query (e.g., named entities)
    named_entities = [ent.text for ent in doc.ents]

    # Example: Detecting greetings and responding accordingly
    greetings = ["hello", "hi", "hey", "howdy"]
    if any(greet in query.lower() for greet in greetings):
        return "Hello! How can I assist you today?"

    # Example: Handling 'who' questions
    if "who" in query.lower() and "is" in query.lower():
        # Replace 'who is' with an empty string to get the subject of the question
        subject = query.lower().replace("who is", "").strip()
        if subject:
            # Custom logic for specific topics
            if subject == "python":
                return "Python is a popular programming language known for its simplicity and versatility."
            elif subject == "ai":
                return "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that can perform tasks that typically require human intelligence."
            elif subject == "elon musk":
                return "Elon Musk is a visionary entrepreneur and CEO of companies like SpaceX and Tesla, known for his ambitious goals in space exploration and sustainable energy."

    # Example: Handling 'what' questions
    if "what" in query.lower() and "is" in query.lower():
        # Replace 'what is' with an empty string to get the subject of the question
        subject = query.lower().replace("what is", "").strip()
        if subject:
            # Custom logic for speci
