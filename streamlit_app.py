# app.py

import streamlit as st
import time

# タイトル
st.title("5秒タイマー")

# タイマー開始ボタン
if st.button('タイマー開始'):
    # タイマーのカウントダウン
    start_time = time.time()  # タイマー開始時の時刻を取得
    timer_running = True

    # 空のコンテナを作成してタイマーを表示
    timer_display = st.empty()

    while timer_running:
        elapsed_time = time.time() - start_time  # 経過時間を計算
        # 小数第2位まで表示
        timer_display.text(f"経過時間: {elapsed_time:.2f}秒")

        # 5秒に到達したら停止
        if elapsed_time >= 5:
            timer_display.text(f"タイマー終了: {elapsed_time:.2f}秒")
            timer_running = False

        # 0.1秒待機してから再度表示を更新
        time.sleep(0.1)
