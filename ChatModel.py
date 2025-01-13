from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

class ChatModel:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-3.5-turbo"
        self.system_message = {
            "role": "system",
            "content": (
                "You are a music recommendation chatbot. Based on this, the system recommended the following songs: {recommendations}\n\n"
                "Your task is to:\n"
                "1. Present these recommendations in a conversational and friendly tone.\n"
                "2. Provide brief descriptions of these songs, if possible.\n"
            )
        }


    def get_response(self, user_message):
        messages = [
            self.system_message,
            {
                "role": "user",
                "content": user_message
            }
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            # 단순히 content를 반환하고 프롬프트에 출력
            result = response.choices[0].message.content
            print(result)  # 결과값을 프롬프트에 출력
            return result
        except Exception as e:
            return f"죄송합니다. 오류가 발생했습니다: {str(e)}"