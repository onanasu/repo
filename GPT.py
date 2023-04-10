import openai
import streamlit as st
from PIL import ImageFont

# Replace "YOUR_API_KEY" with your actual OpenAI API key
openai.api_key = "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"

st.title("訓練日誌　生成bot")

st.date_input('日付を選んでください', key='date_input')




col1, col2= st.columns(2)

with col1:
    author = st.text_input("作成者（フルネーム）",)
with col2:
    teacher = st.text_input("講師名（名字のみ）",)


col1, col2 = st.columns(2)

with col1:
    with st.expander("1限 欠席、遅刻、早退者"):
        absentee_1 = st.text_input("フルネームで入力してください", key="1")
    
    with st.expander("2限 欠席、遅刻、早退者"):
        absentee_2 = st.text_input("フルネームで入力してください", key="2")

    with st.expander("3限 欠席、遅刻、早退者"):
        absentee_3 = st.text_input("フルネームで入力してください", key="3")

with col2:
    with st.expander("4限 欠席、遅刻、早退者"):
        absentee_4 = st.text_input("フルネームで入力してください", key="4")

    with st.expander("5限 欠席、遅刻、早退者"):
        absentee_5 = st.text_input("フルネームで入力してください", key="5")

    with st.expander("1日欠席者"):
        absentee_6 = st.text_input("フルネームで入力してください", key="6")


    
categories = {
     '': {},  # 空の項目
'学科': {
'webプログラミング基礎': ['①', '②', '③', '④', '⑤', '⑥'],
'HTML/CSS基礎': ['①', '②', '③', '④', '⑤', '⑥'],
'JavaScript基礎': ['①', '②', '③', '④', '⑤', '⑥'],
},
'実技': {
'イラスト・ロゴ制作実習': ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧'],
'写真合成・修正加工実習': ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧'],
'ユーザーインターフェース制作実習': ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧'],
'WEBプログラミング実習': ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧'],
'JavaScriptプログラミング実習': ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧'],
'スマートフォンサイト制作実習': ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧'],
'CMS制作実習': ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧'],
'WEB総合制作実習': ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧'],
}
}

col1, col2, col3 = st.columns(3)

with col1:
    selected_category = st.selectbox("学科または実技を選択してください", list(categories.keys()))

with col2:
    if selected_category:
        selected_subcategory = st.selectbox("訓練内容を選択してください", list(categories[selected_category].keys()))
    else:
        selected_subcategory = None

with col3:
    if selected_subcategory:
        selected_small_category = st.selectbox("訓練回を選択してください", categories[selected_category][selected_subcategory])
    else:
        selected_small_category = None



import sys
sys.path.append('C:\\Users\\marim\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages')

import openai
import streamlit as st
from deepl import Translator

# DeepL APIキーの設定
deepl_api_key = "27d30d5e-b78f-6387-64ad-1e5fd7489726:fx"

# DeepL Translatorのインスタンス化
translator = Translator(deepl_api_key)


# Streamlitアプリの定義
st.title("感想文生成アプリ")

# ユーザー入力項目の取得
theme = st.text_input("テーマを入力してください：")
pn_slider = st.slider("ポジティブ／ネガティブの強弱を選択してください：", min_value=-10, max_value=10, value=0)

# APIリクエスト用のプロンプト作成
if pn_slider > 0:
    sentiment = "ポジティブ"
else:
    sentiment = "ネガティブ"
strength = abs(pn_slider)

prompt = f"{theme}に関する{sentiment}な感想を、中高生レベルの日本語でです・ます調で述べてください。強さ: {strength}。文章は自然に終わるようにしてください。"

# APIリクエストを送信し、レスポンスを取得
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,  # ここを変更
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].text.strip()

# ボタンをクリックしたときに感想文を生成
reflection_text = ""

if st.button("感想文を生成"):
    if theme:
        result = generate_text(prompt)
        
        # 英語の文章が生成された場合、DeepL APIを使用して日本語に翻訳
        if any(ord(c) < 128 for c in result):
            translated_result = translator.translate_text(result, target_lang="JA")
            st.write(translated_result.text)
        else:
            st.write(result)
        
        reflection_text = ""

import pandas as pd
from openpyxl import Workbook

# 日付の初期値を設定
date = ""

if st.button("エクセルファイルを生成"):
    # 日付が入力されているかを確認し、入力されている場合は変数に格納


    # 入力データをデータフレームに変換
    data = {
        "項目": [
            "日付", "作成者", "講師名", "1限 欠席、遅刻、早退者",
            "2限 欠席、遅刻、早退者", "3限 欠席、遅刻、早退者",
            "4限 欠席、遅刻、早退者", "5限 欠席、遅刻、早退者", "1日欠席者",
            "訓練内容: カテゴリ", "訓練内容: サブカテゴリ", "訓練内容: 訓練回", "感想文"
        ],
        "内容": [
            date,
            author,
            teacher,
            absentee_1,
            absentee_2,
            absentee_3,
            absentee_4,
            absentee_5,
            absentee_6,
            selected_category,
            selected_subcategory,
            selected_small_category,
            reflection_text
        ],
    }

    df = pd.DataFrame(data)

    # エクセルファイルを保存
    file_name = "training_log.xlsx"
    df.to_excel(file_name, engine="openpyxl", index=False)

    # ダウンロード用リンクを生成
    st.markdown(f"[{file_name}をダウンロード](training_log.xlsx)")

import pandas as pd

data = {
    '日付': [date],
    '作成者': [author],
    '講師名': [teacher],
    '1限 欠席、遅刻、早退者': [absentee_1],
    '2限 欠席、遅刻、早退者': [absentee_2],
    '3限 欠席、遅刻、早退者': [absentee_3],
    '4限 欠席、遅刻、早退者': [absentee_4],
    '5限 欠席、遅刻、早退者': [absentee_5],
    '1日欠席者': [absentee_6],
    '訓練内容': [selected_category],
    'サブカテゴリ': [selected_subcategory],
    '訓練回': [selected_small_category],
    '感想文': [reflection_text],
}

df = pd.DataFrame(data)

import datetime
import locale
from PIL import Image, ImageDraw, ImageFont
import streamlit as st

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

# 日本語フォントのパス
font_path = "C:/Users/marim/Desktop/python/Fonts/msgothic.ttc"

def update_image(date_str: str, author: str, teacher: str):
    if date_str is None:
        return None
    # ...

    # 画像を読み込む
    image = Image.open("C:/Users/marim/Desktop/python/訓練日誌.jpg")

    # 描画用のオブジェクトを生成
    draw = ImageDraw.Draw(image)

    # 日付を描画
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    week_day = {'Monday': '月曜日', 'Tuesday': '火曜日', 'Wednesday': '水曜日', 'Thursday': '木曜日', 'Friday': '金曜日', 'Saturday': '土曜日', 'Sunday': '日曜日'}.get(date.strftime('%A'), "")
    font_date = ImageFont.truetype(font_path, size=36)
    draw.text((475, 35), date_str, font=font_date, fill=(0, 0, 0))
    font_week = ImageFont.truetype(font_path, size=28)
    draw.text((755, 140), week_day, font=font_week, fill=(0, 0, 0))

    # 作成者、講師名を描画
    font_author = ImageFont.truetype(font_path, size=26)
    draw.text((952, 225), author, font=font_author, fill=(0, 0, 0))
    font_teacher = ImageFont.truetype(font_path, size=26)
    draw.text((612, 405), teacher, font=font_teacher, fill=(0, 0, 0))

    return image

# 入力フォームを表示
date_str = st.date_input('日付を選んでください', value=datetime.date.today(), key='my_date_input')
if date_str is None:
    date_str = datetime.date.today()


author = st.text_input("作成者（フルネーム）", key='author_input')
teacher = st.text_input("講師名（名字のみ）", key='teacher_input')
if st.button("更新"):
    image = update_image(date_str.strftime('%Y-%m-%d'), author, teacher)
    st.image(image, caption="訓練日誌")
