from flask import Flask, render_template, request, jsonify
import openai

# Set up OpenAI API credentials
openai.api_key = 'Enter your open api key here'

# Initialize Flask application
app = Flask(__name__)

# Define function to interact with ChatGPT
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        temperature=0.6,
        n=1,
        stop=None,
        timeout=15,
    )
    return response.choices[0].text.strip()

# Define function to generate a healthy recipe based on given ingredients
def generate_recipe(ingredients):
    prompt = f"I have the following ingredients: {', '.join(ingredients)}. Please suggest a healthy recipe."
    recipe = chat_with_gpt(prompt)
    return recipe

# Define the main route for the web application
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve ingredients from the form
        ingredients = request.form.get('ingredients').split(',')

        # Generate recipe based on ingredients
        recipe = generate_recipe(ingredients)

        # Return the recipe as JSON response
        return jsonify({'recipe': recipe})
    
    # Render the index.html template for the initial page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(threaded=True)