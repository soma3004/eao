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
    st.session_state.time_difference = 0.0  # 5.00秒との差分初期化

# タイマー開始ボタン
if st.button("タイマー開始") and not st.session_state.timer_running:
    # タイマー開始時に経過時間をリセット
    st.session_state.start_time = time.time()  # 新たに開始時刻を記録
    st.session_state.elapsed_time = 0.0  # 経過時間をリセット
    st.session_state.timer_running = True
    st.session_state.time_difference = 0.0  # 差分をリセット

# タイマー停止ボタン
if st.button("タイマー停止") and st.session_state.timer_running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time  # 経過時間を保存
    st.session_state.timer_running = False

    # 経過時間と5.00秒との差を計算
    st.session_state.time_difference = round(st.session_state.elapsed_time - 5.00, 3)

# タイマーの表示
if st.session_state.timer_running:
    # タイマーが動いている間、経過時間を表示
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    st.write(f"経過時間: {st.session_state.elapsed_time:.2f}秒")

# タイマーが停止している場合
if not st.session_state.timer_running and st.session_state.elapsed_time > 0:
    st.write(f"最終経過時間: {st.session_state.elapsed_time:.2f}秒")
    # 経過時間と5.00秒との差分を表示（±差分のみ表示）
    st.write(f"5.00秒からの差: {st.session_state.time_difference:+.3f}秒")
