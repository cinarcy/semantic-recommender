import streamlit as st
import requests

st.set_page_config(page_title="Semantic Recommender", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #f7fafd;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0066cc;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📚 Semantic Article Recommender</div>", unsafe_allow_html=True)
st.write("Discover similar articles using semantic search powered by sentence embeddings and FAISS.")

# Sidebar with examples
with st.sidebar:
    st.header("🔍 Try a sample query")
    if st.button("Learn Python"):
        st.session_state.query = "how to learn Python"
    if st.button("Better sleep"):
        st.session_state.query = "how to sleep better"
    if st.button("Remote work tools"):
        st.session_state.query = "tools for remote work"
    if st.button("Investing"):
        st.session_state.query = "investing for beginners"
    if st.button("Travel cheap"):
        st.session_state.query = "how to travel Europe on a budget"

# Input box
query = st.text_input("Enter your query", value=st.session_state.get("query", ""), placeholder="e.g. how to learn Python")
k = st.slider("Number of recommendations", min_value=1, max_value=10, value=5)

# Query results
if st.button("Get Recommendations") and query:
    with st.spinner("Searching..."):
        try:
            response = requests.get("http://localhost:8000/recommend", params={"q": query, "k": k})
            data = response.json()
            st.subheader("🔎 Results:")
            category_icon = {
                "technology": "💻",
                "health": "🧠",
                "finance": "💰",
                "education": "📚",
                "travel": "✈️"
            }
            for result in data["results"]:
                icon = category_icon.get(result["category"], "📄")
                text_color = "black"
                st.markdown(f"<p style='color:{text_color}; font-weight:600'>{icon} {result['title']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color:{text_color}'>{result['description']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color:{text_color}; font-style: italic'>Category: {result['category']}</p>", unsafe_allow_html=True)
                st.markdown("---")
        except Exception as e:
            st.error(f"Error: {e}")