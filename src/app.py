import streamlit as st
import openai

st.set_page_config(page_title="Wisher AI", page_icon="🧊", layout="wide")
#
if 'submit' not in st.session_state:
    st.session_state.submit = False

def on_generate_message():
    st.session_state.submit = True
    
def generate_message():
    with st.spinner("Generating message..."):
        openai.api_key = openai_key
        model = openai_model
        prompt = f"""I want you to write a {wish_category} message for "{wish_name}" 
        turning {wish_age} tomorrow.  Let it be {wish_tone}!"""
        result = openai.Completion.create(model=model,
                                          prompt=prompt,
                                          temperature=0.9,
                                          max_tokens=120)
        return result.choices[0].text
#
st.sidebar.title("Wisher AI")
st.sidebar.markdown("Personalized Wish Creator: Make Every Celebration Unforgettable!")
st.sidebar.caption("""Welcome to our Personalized Wish Creator, 
                    an innovative, user-friendly web application designed to 
                    create customized wishes for your loved ones! 
                    This easy-to-use tool allows you to input key information 
                    such as name, age, and specific occasions like birthdays, 
                    promotions, and much more.""")
st.sidebar.caption("Developed by Sundar Nalli")
st.sidebar.markdown("---")
st.sidebar.markdown("Built with OpenAI's GPT-3")
st.sidebar.caption("*Not optimized")
st.sidebar.caption("*May run out of OpenAI credits")
#
st.sidebar.markdown("---")
openai_key = st.sidebar.text_input("OpenAI API Key", "sk-<your-key>")
openai_model = st.sidebar.text_input("Model Name", "text-davinci-003")
#

st.title("Wisher AI")
st.markdown("**Personalized Wish Creator: Make Every Celebration Unforgettable!**")
st.markdown("""Welcome to our Personalized Wish Creator, 
                    an innovative, user-friendly web application designed to 
                    create customized wishes for your loved ones! 
                    This easy-to-use tool allows you to input key information 
                    such as name, age, and specific occasions like birthdays, 
                    promotions, and much more.""")

with st.container():
    st.divider()
    first_column, second_column = st.columns([0.3,0.7])
    with first_column:
        st.subheader("Inputs")
        wish_category = st.selectbox("Select a Category", ["Birthday"])
        wish_name = st.text_input("Name", "John Doe")
        wish_age = st.text_input("Age", "21")
        wish_tone = st.selectbox("Tone", ["Professional", "Casual", "Funny"])
        st.button("Generate Message", on_click=on_generate_message)
    with second_column:
        st.subheader("Generated Message")
        if st.session_state.submit:
            st.success(generate_message())