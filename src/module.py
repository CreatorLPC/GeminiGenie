import google.generativeai as genai

def Genie(inputText):
    genai.configure(api_key="AIzaSyD8Kz_b-9MJoYW755ckVgxs-LW_nx9fZ6E")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content('rewrite this in the style of a cowboy ' + inputText)
    print(response.text)