# app.py

import streamlit as st
import time

# タイトル
st.title("インタラクティブタイマー")

# 初期状態
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
    st.session_state.elapsed_time = 0.0
    st.session_state.timer_running = False

# タイマー開始ボタン
if st.button("タイマー開始") and not st.session_state.timer_running:
    st.session_state.start_time = time.time() - st.session_state.elapsed_time  # 前回の停止時間から再開
    st.session_state.timer_running = True

# タイマー停止ボタン
if st.button("タイマー停止") and st.session_state.timer_running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time  # 経過時間を保存
    st.session_state.timer_running = False

# タイマーの表示
if st.session_state.timer_running:
    # タイマーが動いている間、経過時間を表示
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    st.write(f"経過時間: {st.session_state.elapsed_time:.2f}秒")

# タイマーが停止している場合
if not st.session_state.timer_running:
    st.write(f"最終経過時間: {st.session_state.elapsed_time:.2f}秒")
