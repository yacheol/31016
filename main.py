!pip install streamlit plotly

import plotly.express as px

# 각 증상별로 당뇨병 유무에 따라 평균 비율 계산
symptom_columns = df.columns[:-1]  # 마지막 컬럼(class) 제외
df_grouped = df.groupby("class")[symptom_columns].mean().T

# 시각화
fig = px.bar(df_grouped, barmode="group",
             labels={"value": "비율", "index": "증상"},
             title="당뇨병 유무에 따른 증상 발생 비율")
fig.show()
import plotly.figure_factory as ff

correlation = df[symptom_columns].corr()
fig = ff.create_annotated_heatmap(
    z=correlation.values,
    x=correlation.columns.tolist(),
    y=correlation.index.tolist(),
    colorscale='Viridis',
    showscale=True)
fig.update_layout(title="증상 간 상관관계 히트맵")
fig.show()
