import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.image('images/imagetop.jpg')
st.title('The Best Company')
st.write('At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.')
st.header('Our team')

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data.csv', sep=',')

with col1:
    for index, row in df[:4].iterrows():
        st.header(row['first name'].capitalize() + ' ' + row['last name'].capitalize())
        st.write(row['role'])
        st.image('images/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(row['first name'].capitalize() + ' ' + row['last name'].capitalize())
        st.write(row['role'])
        st.image('images/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row['first name'].capitalize() + ' ' + row['last name'].capitalize())
        st.write(row['role'])
        st.image('images/' + row['image'])