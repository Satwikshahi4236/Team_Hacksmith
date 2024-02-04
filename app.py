from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__, template_folder='templates')

# Set your OpenAI API key
openai.api_key = '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'

@app.route("/")
def index():
    return render_template("template.html")

@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.form.get("message")

    # Use OpenAI API to get a response
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    # Return the response message as JSON
    response = {
        "message": completion.choices[0].message.content
    }
    return response

if __name__ == '__main__':
    app.run()