import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

plt.style.use('ggplot')
play = pd.read_csv('women_player.csv')
df = pd.read_csv('women_t20.csv')

def player_detail():
    st.title('Player performance')
    df1 = pd.DataFrame(lis)
    test = df[(df.batter.isin(df1[0]))|(df.bowler.isin(df1[0]))]
    # sector investment Analysis
    col1, col2 = st.columns(2)
    with col1:
        sec = test[(test.batter.isin(df1[0]))&(test.over.between(over[0],over[1]))].groupby('batter')['total_run'].sum().sort_values(ascending=False)
        st.subheader('Total Run')
        #fig = plt.figure(figsize=(12, 3))
        fig, ax = plt.subplots()
        ax.bar(sec.index, sec.values)
        plt.xticks(rotation=90)
        st.pyplot(fig)


    with col2:
        data = test[(test.batter.isin(df1[0]))&(test.over.between(over[0],over[1]))].groupby('batter')['total_run'].mean().sort_values(ascending=False)
        Data = pd.DataFrame(data)
        Data['total_run'] = Data['total_run'] * 100
        st.subheader('Strike rate')
        st.dataframe(Data)

    col3, col4 = st.columns(2)

    with col3:
        ct = test[test.bowler.isin(df1[0])].groupby('bowler')['total_run'].count().sort_values(ascending=False)
        st.subheader('Total Boll Count')
        fig1, ax1 = plt.subplots()
        ax1.bar(ct.index, ct.values)
        plt.xticks(rotation=90)
        st.pyplot(fig1)

    with col4:
        data1 = test[(test.bowler.isin(df1[0]))&(test.over.between(over[0],over[1]))].groupby('bowler')['total_run'].mean().sort_values(ascending=False)
        Data1 = pd.DataFrame(data1)
        Data1['total_run'] = Data1['total_run'] * 100
        st.subheader('Bowler Strike rate')
        st.dataframe(Data1)





st.sidebar.title('Select Player')

lis=[]
option1 = st.sidebar.selectbox('Pick Your Choice',play['player'].unique())
option2 = st.sidebar.selectbox('2',play['player'].unique())
option3 = st.sidebar.selectbox('3',play['player'].unique())
option4 = st.sidebar.selectbox('4',play['player'].unique())
option5 = st.sidebar.selectbox('5',play['player'].unique())
option6 = st.sidebar.selectbox('6',play['player'].unique())
option7 = st.sidebar.selectbox('7',play['player'].unique())
option8 = st.sidebar.selectbox('8',play['player'].unique())
option9 = st.sidebar.selectbox('9',play['player'].unique())
option10 = st.sidebar.selectbox('10',play['player'].unique())
option11 = st.sidebar.selectbox('11',play['player'].unique())
option12 = st.sidebar.selectbox('12',play['player'].unique())
option13 = st.sidebar.selectbox('13',play['player'].unique())
option14 = st.sidebar.selectbox('14',play['player'].unique())
option15 = st.sidebar.selectbox('15',play['player'].unique())
option16 = st.sidebar.selectbox('16',play['player'].unique())
option17 = st.sidebar.selectbox('17',play['player'].unique())
option18 = st.sidebar.selectbox('18',play['player'].unique())
option19 = st.sidebar.selectbox('19',play['player'].unique())
option20 = st.sidebar.selectbox('20',play['player'].unique())
option21 = st.sidebar.selectbox('21',play['player'].unique())
option22 = st.sidebar.selectbox('22',play['player'].unique())

option23 = st.sidebar.selectbox('select over',['0,19','0,6','14,19'])

if option23 == '0,19':
    over = 0,19

elif option23 == '0,6':
    over = 0,6

elif option23 == '14,19':
    over = 14,19

btn1=st.sidebar.button('Add Player')
#btn2=st.sidebar.button('Show Player')

if btn1:
    if option1:
        lis.append(option1)
        lis.append(option2)
        lis.append(option3)
        lis.append(option4)
        lis.append(option5)
        lis.append(option6)
        lis.append(option7)
        lis.append(option8)
        lis.append(option9)
        lis.append(option10)
        lis.append(option11)
        lis.append(option12)
        lis.append(option13)
        lis.append(option14)
        lis.append(option15)
        lis.append(option16)
        lis.append(option17)
        lis.append(option18)
        lis.append(option19)
        lis.append(option20)
        lis.append(option21)
        lis.append(option22)
        st.success("Item added!")
        st.write(lis)
        player_detail()
    else:
        st.warning("Please enter a valid item.")