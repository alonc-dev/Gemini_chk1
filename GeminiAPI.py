import google.generativeai as genai
import os
import apikey

###############################################
def generate_text(model_name, prompt):
    """Generates text using the Gemini API."""
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

###############################################
def ask_gemini(request: str) -> str:
    gemini_cache = None
    if request not in gemini_cache:
        response = model.generate_content(request)
        # todo: handle errors
        gemini_cache[request]=response.text
        # todo: save cache to file
    return gemini_cache[request]


###############################################
def genai_setup():
    print("setup")

###############################################
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


###############################################
def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Args:     numbers: A list of numbers.
    Returns:  The average of the numbers in the list, or None if the list is empty.
    """
    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    print(f' Average={average}')
    return average


###############################################

def main():
    print("----- generate_content ------")
    print("-- Start --")
    print_hi('PyCharm')
    genai_setup()
    print("-- End --")


###############################################
if __name__ == "__main__":
    genai.configure(api_key=apikey.GEMINI_API_KEY)
    print("----- get model ------")
    model_name = "gemini-1.5-flash"  # Or "gemini-pro-vision" for multimodal.
    model = genai.GenerativeModel(model_name)
    response = model.generate_content('Write in Java a "Hello World" console application.')
    print(response.text)

    print("----- main ------")
    main()
