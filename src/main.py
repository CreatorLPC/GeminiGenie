# AIzaSyD8Kz_b-9MJoYW755ckVgxs-LW_nx9fZ6E api key

import google.generativeai as genai

genai.configure(api_key="AIzaSyD8Kz_b-9MJoYW755ckVgxs-LW_nx9fZ6E")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)