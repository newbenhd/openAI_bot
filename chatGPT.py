import openai


class ChatGTP:
    def __init__(self, api_key: str, model: str = "text-davinci-003"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def ask(self, text: str):
        response = openai.Completion.create(model=self.model, prompt=text, temperature=0.7, max_tokens=1000)
        text = ''
        for choice in response.choices:
            text += choice.text.lstrip()
        return text
