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

# ボタンのラベルを決める
if st.session_state.timer_running:
    button_label = "タイマー停止"
else:
    button_label = "タイマー開始"

# タイマー開始・停止ボタン
if st.button(button_label):
    if st.session_state.timer_running:
        # 停止時の処理
        st.session_state.elapsed_time = time.time() - st.session_state.start_time  # 経過時間を保存
        st.session_state.timer_running = False

        # 経過時間と5.00秒との差を計算
        st.session_state.time_difference = round(st.session_state.elapsed_time - 5.00, 3)
    else:
        # 開始時の処理
        st.session_state.start_time = time.time()  # 新たに開始時刻を記録
        st.session_state.elapsed_time = 0.0  # 経過時間をリセット
        st.session_state.timer_running = True
        st.session_state.time_difference = 0.0  # 差分をリセット

# タイマーが動いている場合
if st.session_state.timer_running:
    # タイマーが動いている間、経過時間を表示
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    minutes = int(st.session_state.elapsed_time // 60)
    seconds = int(st.session_state.elapsed_time % 60)
    milliseconds = int((st.session_state.elapsed_time - int(st.session_state.elapsed_time)) * 1000)
    st.write(f"経過時間: {minutes:02}:{seconds:02}.{milliseconds:03}")

# タイマーが停止している場合
if not st.session_state.timer_running and st.session_state.elapsed_time > 0:
    minutes = int(st.session_state.elapsed_time // 60)
    seconds = int(st.session_state.elapsed_time % 60)
    milliseconds = int((st.session_state.elapsed_time - int(st.session_state.elapsed_time)) * 1000)
    st.write(f"最終経過時間: {minutes:02}:{seconds:02}.{milliseconds:03}")
    # 経過時間と5.00秒との差分を表示（±差分のみ表示）
    st.write(f"5.00秒からの差: {st.session_state.time_difference:+.3f}秒")
