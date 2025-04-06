from google import genai
from flask import Flask, jsonify
from flask_cors import CORS

def get_recipe(prompt):
    client = genai.Client(api_key="AIzaSyBfVTKu1aWMNdlsSyo1Ena_xE4eR8328ZM")
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[prompt +"detailed step-by-step recipe. starting from Step 1 Ingrediants and Step 2 Washing and Preparing. Always  directly starting from Step 1. provide the full recipe. Use maximun of 3 steps."]
    )

    return response.text

def clean_recipe(prompt):
    output = get_recipe(prompt).split("Step 1:")[1::]
    output[0] = "Step 1:" + output[0]
    return output

def clean_recipe_steps(prompt):

    recipe_text = clean_recipe(prompt)[0]

    steps = {}
    titles = []
    lines =  recipe_text.split("Step")
    subtext = []

    out = []

    for line in lines:
        line = line.strip()
        if line:
            clean_line = line.split("\n")
            if "1: Ingredients" in clean_line[0]:
                step_title = clean_line[0][:-2]
                titles.append(step_title)
                ind_step = []
                for seg in clean_line[1:-1]:
                    if seg:
                        clean_subtext = []
                        clean_subtext.append(seg[2:].strip()+'\n')
                        ind_step.append(clean_subtext)
                subtext.append(ind_step)
            else: 
                step_title = clean_line[0][:-2]
                titles.append(step_title)
                ind_step = []
                for seg in clean_line[1:-1]:
                    if seg:
                        clean_subtext = []
                        clean_subtext.append(seg+'\n')
                        ind_step.append(clean_subtext)
                subtext.append(ind_step)
    
                    
    for i in range(len(titles)):
        steps["Step " + titles[i]] = subtext[i]
        
                
    return steps


app = Flask(__name__)
cors = CORS(app, origins= '*')

@app.route("/api/users", methods=['GET'])
def users():
    return jsonify(
        {
            "users": clean_recipe_steps('Chicken')
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)








