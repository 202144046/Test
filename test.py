from openai import OpenAI

client = OpenAI(
    base_url='http://172.16.32.101:11434/v1',
    api_key='ollama', # 실제로는 체크하지 않지만 필수 입력 항목
)

response = client.chat.completions.create(
    model="llama3.2", # 현재 올려두신 모델명 900101-1234567
    messages=[
        {"role": "system", "content": "도움이 되는 비서입니다."},
        {"role": "user", "content": "Ollama와 OpenAI API의 차이점이 뭐야?"}
    ]
)

print(response.choices[0].message.content)
