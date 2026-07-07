# -*- coding: utf-8 -*-
import streamlit as st

st.markdown(
    """
    <meta http-equiv="Content-Language" content="ru">
    <script>
        document.documentElement.lang = 'ru';
    </script>
""",
    unsafe_allow_html=True,
)

age = st.number_input("Возраст", min_value=1, max_value=120, value=25)
weight = st.number_input("Вес(кг)", min_value=1.0, value=65.0)
height = st.number_input("Рост(см)", min_value=1, value=215)
gender = st.radio("Пол", ("Мужской", "Женский"))
activity = st.selectbox("Уровень активности", ["Низкая", "Средняя", "Высокая"])
bmr = float()
if st.button("Расчитать"):
    if gender == "Мужской":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
multipliers = {"Низкая": 1.2, "Средняя": 1.55, "Высокая": 1.9}
calories = bmr + multipliers[activity]

protein = (calories * 0.3) / 4
fat = (calories * 0.3) / 9
carbs = (calories * 0.4) / 4

st.success(f"Твоя норма калорий: {calories}")
st.write(
    f"Твоя норма белков: {int(protein)}г | жиров: {int(fat)}г | углеводов: {int(carbs)}г"
)
