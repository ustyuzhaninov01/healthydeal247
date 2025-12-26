import streamlit as st
import pandas as pd
import plotly.express as px

def get_data_from_csv(file):
    df = pd.read_csv(file)
    return df

def main():
    # Add a file uploader button
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = get_data_from_csv(uploaded_file)

        # Replace empty values in "extra_state" with values from "state" column
        df["extra_state"].fillna(df["extra_state"], inplace=True)

        # Update values in "extra_state" column when it is "uncalled"
        df.loc[df["extra_state"] == "uncalled", "extra_state"] = df.loc[df["extra_state"] == "uncalled", "extra_state"]

        # Update values in "extra_state" column when it is "recalled"
        df.loc[df["extra_state"] == "recalled", "extra_state"] = df.loc[df["extra_state"] == "recalled", "extra_state"]

        # Replace values in "state_comment" column with new values
        df["state_comment"] = df["state_comment"].replace({
            '(Языковой барьер)': 'The language barrier',
            '(Доставка не возможна( адрес или срок не корректны ))': 'Delivery is not possible (address or date is not correct)',
            '(Отказ третьего лица, возраст до 18)': 'Third party waiver, age under 18',
            '(Бросил трубку и не отвечает при перезвоне)': 'Hung up and doesnt answer when I call back',
            '(Заказано у конкурентов)': 'Ordered from competitors'
        })

        # Pie Chart for Tokens by sales
        fig_pie_chart1 = px.pie(
            df,
            names="state",
            title="<b>(Pie Chart 1)</b>",
            template="plotly_white",
        )
        fig_pie_chart1.update_traces(textinfo="percent+label")
        st.plotly_chart(fig_pie_chart1, use_container_width=True)

        # Display DataFrame below the chart
        st.write("Dataframe:")
        st.dataframe(df)


from streamlit.components.v1 import html

button = """
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="ustyuzhanix" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
"""

html(button, height=70, width=220)

st.markdown(
    """
    <style>
        iframe[width="220"] {
            position: fixed;
            bottom: 60px;
            right: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


if __name__ == "__main__":
    main()

