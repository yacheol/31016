import plotly.express as px

# 주요 증상 리스트
symptoms = ['Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness', 'Polyphagia',
            'Genital thrush', 'visual blurring', 'Itching', 'Irritability',
            'delayed healing', 'partial paresis', 'muscle stiffness', 'Alopecia', 'Obesity']

# 증상별로 당뇨(class=1)와 비당뇨(class=0) 비율 계산
symptom_stats = df.groupby("class")[symptoms].mean().T.reset_index()
symptom_stats.columns = ["Symptom", "No Diabetes", "Diabetes"]

# Plotly로 시각화
fig = px.bar(symptom_stats, x="Symptom", y=["No Diabetes", "Diabetes"],
             barmode="group", title="증상별 당뇨 유무에 따른 비율",
             labels={"value": "비율", "Symptom": "증상", "variable": "당뇨 여부"})

fig.update_layout(xaxis_tickangle=-45)
fig.show()
