import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
from calc_pay import calc_pay, Rank, format_pay

# Define the list of players
players = ['snptkdn', 'job_hoiya', 'tottolu']

st.markdown("# ValorantViewer")

view = st.selectbox(
    'どの情報を表示しますか？',
    ('成績', '給与')
)
cont_multi_selected = st.multiselect('表示するプレイヤー', players, default=players)


if view == '成績':
    # Create a DataFrame with multiple columns
    df = pd.DataFrame({
        'snptkdn': [1, 5, 2, 2, 3, 5, 3, 4, 5, 7],
        'job_hoiya': [2, 4, 1, 6, 3, 2, 4, 5, 6, 8],
        'tottolu': np.random.randint(1, 10, size=10),
        'date': pd.date_range('2022-01-01', periods=10, freq='D')
    })

    # Create a line chart with multiple lines
    st.markdown("## Player Score")
    st.line_chart(df.set_index('date')[cont_multi_selected])

    st.markdown("## Radar Chart")
    df = pd.DataFrame({
        'snptkdn': [1, 5, 2, 2, 3],
        'job_hoiya': [2, 4, 1, 6, 3],
        'tottolu': [2, 4, 1, 6, 3],
        'category': ['kills', 'deaths', 'assists', 'headshots', 'accuracy']
    })

    # Melt the DataFrame to long format
    df_melt = df.melt(id_vars=['category'], var_name='player', value_name='score')

    # Filter the DataFrame to selected players
    df_melt = df_melt[df_melt['player'].isin(cont_multi_selected)]

    # Create a radar chart with multiple lines
    fig = px.line_polar(df_melt, r='score', theta='category', line_close=True, color='player')
    st.plotly_chart(fig, use_container_width=True)
elif view == '給与':
    st.markdown("## 今月の給与（暫定）")

    snptkdn = [10000, 40, 23]
    job_hoiya = [20000, 43, 21]
    tottolu = [5000, 42, 25]
    average_match = (snptkdn[1] + job_hoiya[1] + tottolu[1])/3

    st.dataframe(pd.DataFrame({
        'player': players,
        '能力給': [snptkdn[0], job_hoiya[0], tottolu[0]],
        'PM': [snptkdn[1], job_hoiya[1], tottolu[1]],
        'WM': [snptkdn[2], job_hoiya[2], tottolu[2]],
        'AM': average_match,
        '支給給与': [
            format_pay(calc_pay(Rank.SILVER1, snptkdn[1], snptkdn[2], average_match)),
            format_pay(calc_pay(Rank.GOLD1, job_hoiya[1], job_hoiya[2], average_match)),
            format_pay(calc_pay(Rank.BRONZE1, tottolu[1], tottolu[2], average_match))
        ]
    }), hide_index=True)

    st.markdown("## 給与計算概要")
    st.markdown("給与項目の算定は以下とする。")
    st.markdown("```能力給 × WM x (PM/AM)^2 - 能力給 x (GM - PM)```")
    st.markdown("能力給: 以下等級テーブルに基づくベース給与")
    st.markdown("プレイヤーマッチ数(PM): 当月における各プレイヤーが参加したマッチ数")
    st.markdown("勝利マッチ数(WM): PMのうち、勝利したマッチ数")
    st.markdown("標準マッチ数(AM): 当月における標準的なマッチ数(全プレイヤーのPMの平均値とする")
    st.markdown("ゴールマッチ数(GM): 当月における義務消化マッチ数。(月あたり60マッチとする)")


    ranks = ['Iron1-3', 'Bronze1', 'Bronze2', 'Bronze3', 'Silver1', 'Silver2', 'Silver3', 'Gold1', 'Gold2', 'Gold3', 'Diamond1']
    skill_based_pay = [500, 5000, 6000, 7000, 10000, 12500, 15000, 20000, 30000, 40000, 50000]

    st.markdown("## 等級テーブル")
    st.markdown("以下の等級テーブルに基づき、能力給を算定する。")
    st.dataframe(pd.DataFrame({
        'Rank': ranks,
        '能力給': skill_based_pay,
    }).T, hide_index=True)
