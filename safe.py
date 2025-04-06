from google import genai
from flask import Flask, jsonify
from flask_cors import CORS

def get_safe(prompt):
    client = genai.Client(api_key="AIzaSyBfVTKu1aWMNdlsSyo1Ena_xE4eR8328ZM")
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[prompt +"detailed step-by-step things to be aware of regarding food safey. Use maximun of 3 steps."]
    )

    return response.text

if __name__ == "__main__":
    app.run(debug=True, port=1010)
