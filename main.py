import streamlit as st
import pandas as pd
import plotly.express as px

# One way to switch from a white background to a black background (with reversed colors)
# is to go into the Settings on the Streamlit webpage in which this program is running and
# change "Appearance" to dark.

st.title(":blue[In Search of Happiness]")

df = pd.read_csv("happy.csv")

columns = df.columns

options = [option.title().replace("_", " ").replace("Gdp", "GDP") for option in columns[1:]]  # ignore "country" column

x_choice = st.selectbox(":green[Select the data for the X-axis]", options=options)
y_choice = st.selectbox(":green[Select the data for the Y-axis]", options=options)

# color = st.color_picker("Pick A Color", "#00f900")  # Green
# st.write("The current color is", color)

st.subheader(f"{x_choice} :violet[and] {y_choice}")

# The streamlit scatter chart is visually less appealing than the plotly express scatter chart. Column
#   titles appear in lowercase and there is too much empty space on the left and right sides of the graph.
# st.scatter_chart(df, x=x_choice.lower().replace(" ", "_"), y=y_choice.lower().replace(" ", "_"))

x_column_name = x_choice.lower().replace(" ", "_")
y_column_name = y_choice.lower().replace(" ", "_")

x_values = df[x_column_name]
y_values = df[y_column_name]

figure = px.scatter(df, x=x_values, y=y_values,
                    hover_name="country", color='country',
                    labels={x_column_name: x_choice, y_column_name: y_choice})

st.plotly_chart(figure)
