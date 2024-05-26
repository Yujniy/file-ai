import streamlit as st

def load_api_key(provider):
    return st.session_state.get(f"{provider}_api_key", "")

def save_api_key(provider, api_key):
    if f"{provider}_api_key" not in st.session_state:
        st.session_state[f"{provider}_api_key"] = api_key

def main():
    st.title("Конфигурация боковой панели")

    st.sidebar.title("Настройки")
    provider = st.sidebar.selectbox("Поставщик", ["Free", "Nvidia", "Groq"], index=0)

    api_key = None
    if provider in ["Nvidia", "Groq"]:
        if f"{provider}_api_key" not in st.session_state:
            st.session_state[f"{provider}_api_key"] = load_api_key(provider)
        api_key = st.sidebar.text_input(f"API ключ для {provider}", type="password", value=st.session_state[f"{provider}_api_key"], key=f"{provider}_api_key")
        save_api_key(provider, api_key)

    if provider == "Nvidia":
        st.sidebar.subheader("Информация о модели")
        st.sidebar.write("Model ID: meta/llama3-70b-instruct")
        st.sidebar.write("Developer: Meta")
        st.sidebar.write("Context Window: 8,192 tokens")

        with st.sidebar.expander("Настройки модели"):
            temperature = st.slider("Температура", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
            top_p = st.slider("Top-p", min_value=0.0, max_value=1.0, value=1.0, step=0.1)
            max_tokens = st.number_input("Максимальное количество токенов", min_value=1, max_value=1024, value=1024, step=1)
    elif provider == "Groq":
        model = st.sidebar.selectbox("Модель", ["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768", "gemma-7b"])

        st.sidebar.subheader("Информация о модели")
        if model == "llama3-8b-8192":
            st.sidebar.write("Model ID: llama3-8b-8192")
            st.sidebar.write("Developer: Meta")
            st.sidebar.write("Context Window: 8,192 tokens")
        elif model == "llama3-70b-8192":
            st.sidebar.write("Model ID: llama3-70b-8192")
            st.sidebar.write("Developer: Meta")
            st.sidebar.write("Context Window: 8,192 tokens")
        elif model == "mixtral-8x7b-32768":
            st.sidebar.write("Model ID: mixtral-8x7b-32768")
            st.sidebar.write("Developer: Mistral")
            st.sidebar.write("Context Window: 32,768 tokens")
        elif model == "gemma-7b":
            st.sidebar.write("Model ID: gemma-7b")
            st.sidebar.write("Developer: Anthropic")

    # Эта часть просто демонстрирует настройки боковой панели без основной логики приложения
    st.write("Настройки боковой панели загружены. Добавьте сюда основную логику вашего приложения.")

if __name__ == "__main__":
    main()
