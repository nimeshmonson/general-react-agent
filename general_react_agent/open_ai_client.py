from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_key):
        #api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
        self.client = OpenAI(api_key=api_key)
    def send_message(self, message, tools=None):
        return self.client.chat.completions.create(
            messages=message,
            model="gpt-4o",
            tools=tools
        )