import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

# Define the list of players
players = ['snptkdn', 'job_hoiya', 'tottolu']

st.markdown("# Varorant Viewer")
st.markdown("この画面を一回見るたびに、ユーザーには$1294.6が課金されます。")

cont_multi_selected = st.sidebar.multiselect('表示するプレイヤー', players, default=players)

# Create a DataFrame with multiple columns
df = pd.DataFrame({
    'snptkdn': [1, 5, 2, 2, 3, 5, 3, 4, 5, 7],
    'job_hoiya': [2, 4, 1, 6, 3, 2, 4, 5, 6, 8],
    'tottolu': np.random.randint(1, 10, size=10),
    'date': pd.date_range('2022-01-01', periods=10, freq='D')
})

# Create a line chart with multiple lines
st.line_chart(df.set_index('date')[cont_multi_selected])

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