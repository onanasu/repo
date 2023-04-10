import openai
import streamlit as st
from deepl import Translator
import pandas as pd
from openpyxl import Workbook

# Replace "YOUR_API_KEY" with your actual OpenAI API key
openai.api_key = "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"

# DeepL APIキーの設定
deepl_api_key = "27d30d5e-b78f-6387-64ad-1e5fd7489726:fx"

# DeepL Translatorのインスタンス化
translator = Translator(deepl_api_key)

st.title("訓練日誌　生成bot")

st.date_input('日付を選んでください')



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
