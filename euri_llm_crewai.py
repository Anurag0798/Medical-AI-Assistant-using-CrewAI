import requests
from crewai.llm import BaseLLM

class EuriLLM(BaseLLM):
    def __init__(self, model="gpt-4.1-nano"):
        super().__init__(model=model)

    def call(self, prompt: str, **kwargs) -> str:
        print("\nEURI Prompt:\n", prompt[:500])  # preview prompt

        try:
            response = requests.post(
                "https://api.euron.one/api/v1/euri/alpha/chat/completions",
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                },
                headers={
                    "Authorization": "Bearer Your-Euri-API-key",
                    "Content-Type": "application/json"
                }
            )

            print("Response status:", response.status_code)
            print("Response content:", response.text[:300])

            if response.status_code != 200:
                raise Exception(f"EURI API Error: {response.status_code} - {response.text}")

            return response.json()["choices"][0]["message"]["content"]

        except Exception as e:
            raise Exception(f"[EuriLLM Error] {str(e)}")