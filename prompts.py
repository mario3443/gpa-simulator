import openai
import os
from dotenv import load_dotenv

#從.env檔案讀取API金鑰
load_dotenv()
api_key = os.getenv("chatgpt_apikey")

client = openai.OpenAI(api_key=api_key)

def format_coursefor_prompt(course):
    line = []
    for course in course:
        line.append(f"{course['name']}（{course['credit']} 學分，等第：{course['grade']}）")
    return "\n".join(line)

#叫gpt回答
def generate_gpt_advise(courses):
    course_text = format_coursefor_prompt(courses)
    prompt = f"""以下是我目前的修課資料：

{course_text}

請你幫我分析目前的課程與 GPA 表現，有哪些課程如果等第拉高會讓 GPA 明顯上升？有什麼建議給我？請用條列式回覆。
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一個大學生的學習顧問，擅長幫忙分析課程與 GPA 表現。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"gpt發生錯誤:{str(e)}"