from google import genai
import os

# 1. 클라이언트 설정
# API 키는 직접 입력하거나 환경 변수 'GOOGLE_API_KEY'에 설정하세요.
client = genai.Client(api_key="AIzaSyC98Y2E-_L0A0SzjUkDhStEVUHrp5JbXT4")

def test_gemini_new():
    try:
        # 2. 텍스트 생성 요청 (모델명에 'models/' 접두사 생략 가능)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="900101-1234567 이런거 여러개 만들어"
        )
        
        # 3. 결과 출력 (response.text로 바로 접근 가능)
        print("--- 최신 SDK 테스트 결과 ---")
        print(response.text)
        print("---------------------------")
        
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    test_gemini_new()
