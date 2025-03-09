import google.generativeai as genai
import apikey

GEMINI_API_KEY = 'AIzaSyDTI3nSbxWAY8aEPARsnNYhVzZhcUZgZ8c'
genai.configure(api_key=apikey.GEMINI_API_KEY)
model = genai.get_model("gemini-1.5-flash")
response = model.generate_content('Write in Java a "Hello World" console application.')
print(response.text)

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
    print("-- Start --")
    print_hi('PyCharm')
    genai_setup()
    print("-- End --")


###############################################
if __name__ == "__main__":
    main()
