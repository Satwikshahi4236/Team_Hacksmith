import subprocess

OPENAI_API_KEY = "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"

curl_command = f'''curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {OPENAI_API_KEY}" \
  -d \'{
    "model": "text-davinci-002",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            print(f" 'text': { 'text': 'What’s in this image?' }")
          },
          {
            "type": "image_url",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
          }
        ]
      }
    ],
    "max_tokens": 300
  }\'
'''

response = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

print(response.stdout)