import streamlit as st

st.title('Whiskey Machine')

st.header('1. with 표기법 사용 예시')
st.subheader('위스키 머신')

with st.form('whiskey_form'):
    st.subheader('**위스키 주문하기**')
    
    # 입력 위젯
    whiskey_type_val = st.selectbox('위스키 종류', ['싱글 몰트', '블렌디드', '버번', '아이리시', '라이'])
    whiskey_age_val = st.slider('숙성 연수 (년)', 3, 30, 12)
    serving_type_val = st.selectbox('서빙 형식', ['온더락', '스트레이트', '마티니', '하이볼', '콜린스'])
    ice_val = st.checkbox('얼음 추가')
    garnish_val = st.text_input('장식', '레몬 조각을 추가하려면 입력하세요.')
    submitted = st.form_submit_button('제출')

if submitted:
    st.markdown(f'''
    주문하신 내용:
    - 위스키 종류 : '{whiskey_type_val}'
    - 숙성 연수 : '{whiskey_age_val}년'
    - 서빙 형식 : '{serving_type_val}'
    - 얼음 추가 : '{ice_val}'
    - 장식 : '{garnish_val if garnish_val else "없음"}'
    ''')
else:
    st.write('주문하세요!')
