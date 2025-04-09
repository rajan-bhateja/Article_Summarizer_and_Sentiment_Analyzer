from google import genai

def summarize(text):
    # get the Gemini API Key: https://aistudio.google.com/app/apikey
    key = "your_gemini_api_key"
    client = genai.Client(api_key=key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Summarize the following text comprehensively in 5-10 points: \n\n{text}",
    )
    return response.text
