
import streamlit as st
import openai
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def enhance_prompt(role, context, task):
    """
    Enhance a prompt based on user input role, context, and task.
    Returns an improved prompt that includes formatting instructions and clarification of assumptions.
    """
    enhancement_prompt = f"""
    I need to create an enhanced prompt based on the following inputs:
    
    ROLE: {role}
    CONTEXT: {context}
    TASK: {task}
    
    Please create a comprehensive prompt that:
    1. Clearly defines the role and relevant expertise
    2. Provides necessary context and background information
    3. Specifies the task in detail with clear objectives
    4. Includes specific instructions for formatting the response
    5. Explicitly asks to clarify assumptions before responding
    
    Return ONLY the enhanced prompt without any explanations or additional text.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # You can use "gpt-3.5-turbo" for a more cost-effective option
            messages=[
                {"role": "system", "content": "You are an expert prompt engineer who creates effective prompts for AI assistants."},
                {"role": "user", "content": enhancement_prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Prompt Enhancer", page_icon="✨", layout="wide")

st.title("AI Prompt Enhancer")
st.subheader("Create better prompts for AI assistants")

st.markdown("""
This app helps you create enhanced prompts for AI systems like ChatGPT.
Fill in the details below to generate a comprehensive prompt.
""")

with st.form("prompt_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        role = st.text_area("Role", placeholder="Example: Financial Advisor, Python Expert, Marketing Specialist", height=100)
    
    with col2:
        context = st.text_area("Context", placeholder="Example: Planning retirement, Building a web app, Creating an ad campaign", height=100)
    
    task = st.text_area("Task", placeholder="Example: Create a retirement plan for a 45-year-old, Build a weather app, Design an Instagram campaign", height=150)
    
    submit_button = st.form_submit_button("Enhance Prompt")

if submit_button and role and context and task:
    with st.spinner("Enhancing your prompt..."):
        enhanced_prompt = enhance_prompt(role, context, task)
    
    st.success("Prompt enhanced successfully!")
    
    st.subheader("Enhanced Prompt")
    st.text_area("Copy this prompt to use with AI assistants:", enhanced_prompt, height=300)
    
    # Add a copy button
    st.markdown("""
    <style>
    .stButton button {
        width: 100%;
    }
    </style>""", unsafe_allow_html=True)
    
    if st.button("Copy to Clipboard"):
        st.write("Copied to clipboard! (Note: This only works when running locally)")
        st.code(f"""
        # Add this to your JavaScript in a local Streamlit app:
        # navigator.clipboard.writeText(`{enhanced_prompt}`);
        """)
elif submit_button:
    st.warning("Please fill in all fields to enhance your prompt.")

# Information section
with st.expander("How to Use This App"):
    st.markdown("""
    ### Instructions:
    
    1. **Role**: Define who the AI assistant should act as (e.g., "Expert Python Developer").
    2. **Context**: Provide background information relevant to your request.
    3. **Task**: Clearly state what you want the AI to do for you.
    4. Click "Enhance Prompt" to generate an improved prompt.
    5. Copy the enhanced prompt and use it with ChatGPT or other AI assistants.
    
    ### Tips for Better Results:
    
    - Be specific about the role and expertise needed
    - Include relevant details in the context
    - Make your task clear and actionable
    - The enhanced prompt will include formatting instructions and ask the AI to clarify assumptions
    """)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit and OpenAI")

# Add instructions for setting up the API key
with st.expander("Setup Instructions"):
    st.markdown("""
    ### Setting Up Your OpenAI API Key:
    
    1. Create a `.env` file in the same directory as this script
    2. Add the following line to the file:
       ```
       OPENAI_API_KEY=your_api_key_here
       ```
    3. Replace `your_api_key_here` with your actual OpenAI API key
    4. Install required packages:
       ```
       pip install streamlit openai python-dotenv
       ```
    5. Run the app with:
       ```
       streamlit run app.py
       ```
    """)
def enhance_prompt(role, context, task):
    """
    Enhance a prompt based on user input role, context, and task.
    Returns an improved prompt that includes formatting instructions and clarification of assumptions.
    """
    enhancement_prompt = f"""
    I need to create an enhanced prompt based on the following inputs:
    
    ROLE: {role}
    CONTEXT: {context}
    TASK: {task}
    
    Please create a comprehensive prompt that:
    1. Clearly defines the role and relevant expertise
    2. Provides necessary context and background information
    3. Specifies the task in detail with clear objectives
    4. Includes specific instructions for formatting the response
    5. Explicitly asks to clarify assumptions before responding
    
    Return ONLY the enhanced prompt without any explanations or additional text.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can use "gpt-3.5-turbo" for a more cost-effective option
            messages=[
                {"role": "system", "content": "You are an expert prompt engineer who creates effective prompts for AI assistants."},
                {"role": "user", "content": enhancement_prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Prompt Enhancer", page_icon="✨", layout="wide")

st.title("AI Prompt Enhancer")
st.subheader("Create better prompts for AI assistants")

st.markdown("""
This app helps you create enhanced prompts for AI systems like ChatGPT.
Fill in the details below to generate a comprehensive prompt.
""")

with st.form("prompt_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        role = st.text_area("Role", placeholder="Example: Financial Advisor, Python Expert, Marketing Specialist", height=100)
    
    with col2:
        context = st.text_area("Context", placeholder="Example: Planning retirement, Building a web app, Creating an ad campaign", height=100)
    
    task = st.text_area("Task", placeholder="Example: Create a retirement plan for a 45-year-old, Build a weather app, Design an Instagram campaign", height=150)
    
    submit_button = st.form_submit_button("Enhance Prompt")

if submit_button and role and context and task:
    with st.spinner("Enhancing your prompt..."):
        enhanced_prompt = enhance_prompt(role, context, task)
    
    st.success("Prompt enhanced successfully!")
    
    st.subheader("Enhanced Prompt")
    st.text_area("Copy this prompt to use with AI assistants:", enhanced_prompt, height=300)
    
    # Add a copy button
    st.markdown("""
    <style>
    .stButton button {
        width: 100%;
    }
    </style>""", unsafe_allow_html=True)
    
    if st.button("Copy to Clipboard"):
        st.write("Copied to clipboard! (Note: This only works when running locally)")
        st.code(f"""
        # Add this to your JavaScript in a local Streamlit app:
        # navigator.clipboard.writeText(`{enhanced_prompt}`);
        """)
elif submit_button:
    st.warning("Please fill in all fields to enhance your prompt.")

# Information section
with st.expander("How to Use This App"):
    st.markdown("""
    ### Instructions:
    
    1. **Role**: Define who the AI assistant should act as (e.g., "Expert Python Developer").
    2. **Context**: Provide background information relevant to your request.
    3. **Task**: Clearly state what you want the AI to do for you.
    4. Click "Enhance Prompt" to generate an improved prompt.
    5. Copy the enhanced prompt and use it with ChatGPT or other AI assistants.
    
    ### Tips for Better Results:
    
    - Be specific about the role and expertise needed
    - Include relevant details in the context
    - Make your task clear and actionable
    - The enhanced prompt will include formatting instructions and ask the AI to clarify assumptions
    """)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit and OpenAI")

# Add instructions for setting up the API key
with st.expander("Setup Instructions"):
    st.markdown("""
    ### Setting Up Your OpenAI API Key:
    
    1. Create a `.env` file in the same directory as this script
    2. Add the following line to the file:
       ```
       OPENAI_API_KEY=your_api_key_here
       ```
    3. Replace `your_api_key_here` with your actual OpenAI API key
    4. Install required packages:
       ```
       pip install streamlit openai python-dotenv
       ```
    5. Run the app with:
       ```
       streamlit run app.py
       ```
    """)
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to enhance the prompt
def enhance_prompt(role, context, task):
    enhanced_prompt = (
        f"You are a {role}. Given the following context: {context}, your task is: {task}.\n\n"
        "Please enhance this prompt to be more structured and useful.\n"
        "The response must include:\n"
        "1. A clear and concise problem statement.\n"
        "2. A well-structured format for the answer.\n"
        "3. A request to clarify any assumptions before responding."
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can change to "gpt-3.5-turbo" if needed
            messages=[{"role": "system", "content": "You are an AI assistant that helps refine prompts."},
                      {"role": "user", "content": enhanced_prompt}],
            temperature=0.7,
            max_tokens=300
        )
        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("AI Prompt Enhancer")

st.write("Enter your Role, Context, and Task, and get a refined prompt!")

role = st.text_input("Enter Your Role", placeholder="e.g., Data Scientist")
context = st.text_area("Enter Context", placeholder="e.g., Working on analyzing customer behavior")
task = st.text_area("Enter Task", placeholder="e.g., Write a Python script to cluster customers")

if st.button("Enhance Prompt"):
    if role and context and task:
        enhanced_text = enhance_prompt(role, context, task)
        st.subheader("Enhanced Prompt:")
        st.write(enhanced_text)
    else:
        st.error("Please fill in all fields.")

