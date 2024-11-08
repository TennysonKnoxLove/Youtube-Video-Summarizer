from openai import OpenAI

# Takes The SpeechToText Output & Organizes It In Bullet Points, Briefly & Concisely Summarizing The Video.
def summarizer(text):
     try:
        api_key = 'ENTER YOUR API KEY HERE!' # <- Enter Your Own API Key for ChatGPT
        if not api_key:
            raise ValueError("API Key not found. Please set the 'OPENAI_API_KEY' environment variable.")
        client = OpenAI(api_key=api_key)
        prompt = f"Summarize this text. Refer to it as a Video. Don't give any extra content, only return the answer to the question and nothing else. Try to make sense of the passage if there are misspelled words or things that do not make sense before answering. Return bullet points highlighting the key topics in the text. THE TEXT: { text }"
        response = client.chat.completions.create(model="gpt-4", messages=[{"role": "assistant", "content": prompt}])
        print("\n")
        print(response.choices[0].message.content) 
        print("\n")
     except Exception as e:
        print(f"An error has occurred while attempting to summarize: {e}")
        print("\n")