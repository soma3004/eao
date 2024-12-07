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
    st.session_state.target_time = 5.0  # デフォルトのターゲット時間を5秒に設定

# タイマー開始時間を選択するラジオボタン
target_time = st.radio("タイマーの目標時間を選択してください", [1.0, 5.0, 10.0], index=1)

# 目標時間の設定をセッション状態に保存
st.session_state.target_time = target_time

# 開始ボタンと停止ボタンの処理
start_button = st.button("タイマー開始")
stop_button = st.button("タイマー停止")

# タイマー開始ボタンが押された場合
if start_button and not st.session_state.timer_running:
    # 開始時の処理
    st.session_state.start_time = time.time()  # 新たに開始時刻を記録
    st.session_state.elapsed_time = 0.0  # 経過時間をリセット
    st.session_state.timer_running = True  # タイマーを開始
    st.session_state.time_difference = 0.0  # 差分をリセット

# タイマー停止ボタンが押された場合
if stop_button and st.session_state.timer_running:
    # 停止時の処理
    st.session_state.elapsed_time = time.time() - st.session_state.start_time  # 経過時間を保存
    st.session_state.timer_running = False  # タイマーを停止

    # 経過時間と目標時間との差を計算
    st.session_state.time_difference = round(st.session_state.elapsed_time - st.session_state.target_time, 3)

# タイマーが動いている間、経過時間を表示
if st.session_state.timer_running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    st.write(f"経過時間: {st.session_state.elapsed_time:.2f}秒")

# タイマーが停止している場合
if not st.session_state.timer_running and st.session_state.elapsed_time > 0:
    st.write(f"最終経過時間: {st.session_state.elapsed_time:.2f}秒")
    # 経過時間と目標時間との差分を表示（±差分のみ表示）
    st.write(f"目標時間{st.session_state.target_time}秒からの差: {st.session_state.time_difference:+.3f}秒")
