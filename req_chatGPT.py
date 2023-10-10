"""
こちらが本来のリクエスト用プログラム

import openai
def request_chatGPT(入力情報):
    openai.organization = "Organization IDをここに入れる"
    openai.api_key = "API keyをここに入れる"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "ChatGPTの役割を指定する"},
            {"role": "user", "content": "リクエスト本文"},
            {"role": "assistant", "content": "補足説明を記載（使わなくてもOK）"},
        ],
    )

    print(response['choices'][0]['message']['content'])
"""

# 今はとりあえず動いている風にみせているだけ
def request_chatGPT(request_list):
    # メール確認画面から受け取った情報を API に埋め込んで投げる
    print("req_chatGPT : receive ", request_list['role_system'])
    
    return "これが ChatGPT の答えや！"