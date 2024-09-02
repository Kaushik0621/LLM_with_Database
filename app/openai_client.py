# import os
# from dotenv import load_dotenv
# import openai

# # Load environment variables from the .env file
# load_dotenv()

# # Access the API key from the environment variables
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def get_meaning_from_openai(word: str) -> str:
#     prompt = f"What is the meaning of the word '{word}'?"

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=50
#     )
#     return response['choices'][0]['message']['content'].strip()
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# # Load environment variables from the .env file
# load_dotenv()

# # Configure the API key from environment variables
# genai.configure(api_key=os.getenv("API_KEY"))

# def get_meaning_from_openai(word: str) -> str:
#     prompt = (
#         f"What is the meaning of the word '{word}'? "
#         "Write it in a single sentence. "
#         "The number of words in the answer should not exceed 20."
#     )

#     # Generate content using the Gemini model
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     response = model.generate_content(prompt)

#     # Extract and return the generated content
#     return response.text.strip()

# # Example usage
# if __name__ == "__main__":
#     word_meaning = get_meaning_from_openai("example")
#     print(word_meaning)

# import os
# from dotenv import load_dotenv
# import openai
# from openai.error import RateLimitError

# # Load environment variables from the .env file
# load_dotenv()

# # Access the API key from the environment variables
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def get_meaning_from_openai(word: str) -> str:
#     prompt = f"What is the meaning of the word '{word}'?"

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}],
#             max_tokens=50
#         )
#         return response['choices'][0]['message']['content'].strip()

#     except RateLimitError:
#         return "Error: Rate limit exceeded. Please try again later."

#     except Exception as e:
#         return f"An error occurred: {str(e)}"
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the API key from environment variables
genai.configure(api_key=os.getenv("API_KEY"))

def get_meaning_from_gemai(word: str) -> str:
    prompt = (
        f"What is the meaning of the word '{word}'? "
        "Write it in a single sentence. "
        "The number of words in the answer should not exceed 20."
    )

    # Generate content using the Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    # Extract and return the generated content
    return response.text.strip()
