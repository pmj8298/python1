# 구글 Gemini AI
from google import genai
from dotenv import load_dotenv
import os

#.env 파일 로드
load_dotenv()

gemini_key = os.getenv('GEMINI_KEY')

def aiai(text):
    client = genai.Client(api_key=gemini_key)
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=text
        + '내용이 길면 문단으로 끊어서 알려줘. 단 친절하게 알려줘.'
    )
    answer = response.text
    # print(response.text)
    print(answer)
    return answer

if __name__=='__main__':
   aiai('gpt에 대해 설명해')