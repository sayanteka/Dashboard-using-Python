import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
#from streamlit_extras.metric_cards import style_metric_cards
import pandas as pd
import plotly.graph_objs as go
import os
import random
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(page_title="StreamlitDashboard", page_icon=":bar_chart:",layout="wide")
# st.title(" :bar_chart: Car Price Prediction Summary")
# st.markdown("<style>#title{text-align:center;}</style>", unsafe_allow_html=True)
# st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)
st.markdown("<h1 id='title'> Car Price Prediction Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<style>#title{text-align:center;}</style>", unsafe_allow_html=True)
st.markdown("<style>div.block-container{padding-top:2rem;text-align:center;}</style>", unsafe_allow_html=True)
fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding = "ISO-8859-1")
else:

    df = pd.read_csv("Car Predictions Output csv.csv", encoding = "ISO-8859-1")

col1, col2, col3, col4 = st.columns((4),gap="medium")
engine_type = df['enginetype'].unique().tolist()
cylinder_number=df['cylindernumber'].unique().tolist()
fuel_type=df['fueltype'].unique().tolist()
phase_type=df['Phase'].unique().tolist()
with col1:
     Engine_Type = st.multiselect('Filter Engine Type:',
                                      engine_type,placeholder='All')
     
     if not Engine_Type :
        Engine_Type=engine_type
     
with col2:
     Cylinder_Number=st.multiselect('Filter Cylinder Type:',
                                       cylinder_number,placeholder='All')
     if not Cylinder_Number :
        Cylinder_Number=cylinder_number
with col3:
     Fuel_Type=st.multiselect('Filter Fuel Type:',
                                       fuel_type,placeholder='All')
     if not Fuel_Type:
        Fuel_Type=fuel_type

with col4:
     Phase_Type=st.multiselect('Filter Phase Type:',
                                       phase_type,placeholder='All')
     if not Phase_Type:
        Phase_Type=phase_type
    
new_df = (df['enginetype'].isin(Engine_Type) & df['cylindernumber'].isin(Cylinder_Number) & df['fueltype'].isin(Fuel_Type) & df['Phase'].isin(Phase_Type))
filtered_df = df[new_df]
st.markdown("  ")
col4,col5=st.columns((2),gap="medium")
with col4:
     grouped_df = filtered_df.groupby('carbody')['car_ID'].count().reset_index()
     new_title = '<p style="font-family:Times New Roman; color:Black; font-size:33px;font-weight:bold;">Count of cars vs car body</p>'
     st.markdown(new_title, unsafe_allow_html=True)
     #st.header("Count of cars by car body")
     fig = px.bar(
        grouped_df,
        x='carbody',
        y="car_ID",
        text_auto=".2s",
        height=520,
        color_discrete_sequence=['#38B39B'])
     fig.update_traces(
        textfont_size=20, textangle=0, textposition="outside", cliponaxis=False
    )
     fig.update_layout(xaxis=dict(categoryorder='total descending'))
     fig.update_xaxes(showgrid=False)
     fig.update_yaxes(showgrid=False)
     fig.update_layout(
     margin=dict(l=15, r=15, t=15, b=15)) #used to move the graphs close to title.

     st.plotly_chart(fig, use_container_width=True)


with col5:
     
    col6, col7 = st.columns(2)
    with col6:
        val=filtered_df['car_ID'].count()
        fig = go.Figure()

        fig.add_trace(
        go.Indicator(
            value=val,
            gauge={"axis": {"visible": False}},
            number={
                "prefix": "",
                "suffix": "",
                "font.size": 28,
            },
            title={
                "text": "Number of cars",
                "font": {"size": 24}}))

        if True:
           fig.add_trace(
            go.Scatter(
                y=random.sample(range(0, 101), 30),
                hoverinfo="skip",
                fill="tozeroy",
                fillcolor="rgba(255, 43, 43, 0.2)",
                line={
                    "color": "rgba(255, 43, 43, 0.2)"}))

        fig.update_xaxes(visible=False, fixedrange=True)
        fig.update_yaxes(visible=False, fixedrange=True)
        fig.update_layout(margin=dict(t=30, b=0),
            showlegend=False,
            plot_bgcolor="white",
            height=100)
        st.plotly_chart(fig, use_container_width=True)

        grouped_df = filtered_df.groupby('carbody')['price'].mean().reset_index()
        new_title = '<p style="font-family:Times New Roman; color:Black; font-size:27px;font-weight:bold;">Average price vs car body</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        #st.header("Average price per car body")
        fig = px.bar(
        grouped_df,
        x="carbody",
        y="price",
        text_auto=".2s",
        color_discrete_sequence=["rgba(255, 43, 43, 0.2)"],
        height=400,
    )
        fig.update_traces(
        textfont_size=20, textangle=0, textposition="outside", cliponaxis=False
    )
        fig.update_layout(xaxis=dict(categoryorder='total descending'))
        fig.update_layout(
        margin=dict(l=15, r=15, t=15, b=15))
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)

        st.plotly_chart(fig, use_container_width=True)

    with col7:
        avg_price = filtered_df['price'].mean()

        fig = go.Figure()

        fig.add_trace(
        go.Indicator(
            value=avg_price,
            gauge={"axis": {"visible": False}},
            number={
                "prefix": "$",
                "suffix": "",
                "font.size": 28,
            },
            title={
                "text": "Average price of cars",
                "font": {"size": 24}}))

        if True:
           fig.add_trace(
            go.Scatter(
                y=random.sample(range(0, 101), 30),
                hoverinfo="skip",
                fill="tozeroy",
                fillcolor="rgba(0, 104, 201, 0.2)",
                line={
                    "color": "rgba(0, 104, 201, 0.2)"}))

        fig.update_xaxes(visible=False, fixedrange=True)
        fig.update_yaxes(visible=False, fixedrange=True)
        fig.update_layout(margin=dict(t=30, b=0),
            showlegend=False,
            plot_bgcolor="white",
            height=100)
        st.plotly_chart(fig, use_container_width=True)   
        grouped_df = filtered_df.groupby('Phase')['car_ID'].count().reset_index()
        new_title = '<p style="font-family:Times New Roman; color:Black; font-size:27px;font-weight:bold;">Number of cars vs phase</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        #st.header("Number of cars per phase")
        fig = px.bar(
        grouped_df,
        y="car_ID",
        x="Phase",
        text_auto=".2s",
        height=400,
        color_discrete_sequence=["rgba(0, 104, 201, 0.2)"],
        orientation='v')

        fig.update_traces(
        textfont_size=20, textangle=0, textposition="outside", cliponaxis=False)
        fig.update_layout(xaxis=dict(categoryorder='total descending'))
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        # fig.update_xaxes(showgrid=False,showline=True, linewidth=1, linecolor='black', mirror=True)#adds border to the graph
        # fig.update_yaxes(showgrid=False,showline=True, linewidth=1, linecolor='black', mirror=True)
        fig.update_layout(
        margin=dict(l=15, r=15, t=15, b=15))
        st.plotly_chart(fig, use_container_width=True)
    
col8,col9=st.columns(2)
with col8:
    new_title = '<p style="font-family:Times New Roman; color:Black; font-size:33px;font-weight:bold;">Engine size vs price</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    #st.header("Engine size vs Price")
    fig = px.scatter(filtered_df, x="price", y="enginesize",
	         color="cylindernumber",
                 hover_name="cylindernumber", log_x=True, size_max=60,height=400)
    fig.update_layout(
        margin=dict(l=15, r=15, t=15, b=15))
    st.plotly_chart(fig, use_container_width=True)

with col9:
    new_title = '<p style="font-family:Times New Roman; color:Black; font-size:33px;font-weight:bold;">Actual price Vs predicted price</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    fig = go.Figure()

    fig = go.Figure(data=[
    go.Bar(name='Actual Price', x=filtered_df['CarName'], y=filtered_df['price'],orientation='v'),
    go.Bar(name='Predicted Price', x=filtered_df['CarName'], y=filtered_df['Price Predictions'],orientation='v')])
    fig.update_layout(barmode='group')
    fig.update_traces(width=0.2)
    fig.update_layout(height=400,bargap=0.1,
    bargroupgap=0.1)
    fig.update_layout(
        margin=dict(l=15, r=15, t=15, b=15))
    st.plotly_chart(fig, use_container_width=True)
new_title = '<p style="font-family:Times New Roman; color:Black; font-size:33px;font-weight:bold;">Dataset</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.dataframe(filtered_df)
