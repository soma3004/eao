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
    st.session_state.success_message = None  # 成功メッセージの初期化

# タイマー開始ボタン
if st.button("タイマー開始") and not st.session_state.timer_running:
    # タイマー開始時に経過時間をリセット
    st.session_state.start_time = time.time()  # 新たに開始時刻を記録
    st.session_state.elapsed_time = 0.0  # 経過時間をリセット
    st.session_state.timer_running = True
    st.session_state.success_message = None  # 成功メッセージをリセット

# タイマー停止ボタン
if st.button("タイマー停止") and st.session_state.timer_running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time  # 経過時間を保存
    st.session_state.timer_running = False

    # 5秒ぴったりで停止できた場合、メッセージを表示
    if abs(st.session_state.elapsed_time - 5.0) < 0.05:
        st.session_state.success_message = "おめでとう！ 5秒ぴったりでタイマーを停止しました！"

# タイマーの表示
if st.session_state.timer_running:
    # タイマーが動いている間、経過時間を表示
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    st.write(f"経過時間: {st.session_state.elapsed_time:.2f}秒")

# タイマーが停止している場合
if not st.session_state.timer_running and st.session_state.elapsed_time > 0:
    st.write(f"最終経過時間: {st.session_state.elapsed_time:.2f}秒")
    # 5秒ぴったりの場合にメッセージを表示
    if st.session_state.success_message:
        st.success(st.session_state.success_message)

