import google.generativeai as genai
import os
import apikey

###############################################
# ask gemini
def ask_gemini(prompt: str):
    """Generates text using the Gemini API."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

###############################################
# this module save the answer to avoid reask gemini
def ask_gemini_u(request: str) -> str:
    gemini_cache = None
    if request not in gemini_cache:
        response = model.generate_content(request)
        # todo: handle errors
        gemini_cache[request]=response.text
        # todo: save cache to file
    return gemini_cache[request]


###############################################

def main():
    print("----- generate_content ------")
    print("-- Start --")
    txt = "write hello word function in python"
    answer = ask_gemini(txt)
    print(answer)
    print("-- End --")


###############################################
if __name__ == "__main__":
    genai.configure(api_key=apikey.GEMINI_API_KEY)
    print("----- get model ------")
    model_name = "gemini-1.5-flash"  # Or "gemini-pro-vision" for multimodal.
    model = genai.GenerativeModel(model_name)

    print("----- main ------")
    main()
