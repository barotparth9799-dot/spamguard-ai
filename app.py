import streamlit as st
from src.prediction.predict import predict_message
from src.database.history import get_history, save_detection

st.set_page_config(
    page_title="SpamGuard AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
    .main {
        padding-top: 1.5rem;
    }

    .brand {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 1.05rem;
        color: #64748b;
        margin-top: 0.2rem;
    }

    .status {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 20px;
        background: #dcfce7;
        color: #15803d;
        font-weight: 600;
        font-size: 0.85rem;
        margin-top: 0.5rem;
    }

    .section-title {
        font-size: 1.45rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }

    .info-card {
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        background: #f8fafc;
        margin-bottom: 1rem;
    }

    .result-card {
        padding: 1.4rem;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        background: #ffffff;
        margin-top: 1rem;
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)


# Header
header_col1, header_col2 = st.columns([4, 1])

with header_col1:
    st.markdown(
        '<div class="brand">🛡️ SPAMGUARD AI</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="subtitle">AI-Powered Spam Message & Email Detection</div>',
        unsafe_allow_html=True
    )

with header_col2:
    st.markdown(
        '<div class="status">● System Online</div>',
        unsafe_allow_html=True
    )

st.divider()


# Navigation
st.sidebar.markdown("## Navigation")
st.sidebar.caption("SpamGuard AI System")

page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Analyze Message", "History", "About"]
)


# Dashboard
if page == "Dashboard":

    st.markdown("## 📊 Dashboard")
    st.caption("Overview of SpamGuard AI detection activity")

    history = get_history()

    total = len(history)
    spam_count = sum(1 for row in history if row[4] == "spam")
    safe_count = total - spam_count

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Analyzed",
        total
    )

    col2.metric(
        "🚨 Spam Detected",
        spam_count
    )

    col3.metric(
        "✅ Safe Messages",
        safe_count
    )

    st.divider()

    st.markdown("### Detection Summary")

    if total == 0:
        st.info("No detections yet. Analyze a message to populate the dashboard.")

    else:
        chart_data = {
            "Safe": safe_count,
            "Spam": spam_count
        }

        st.bar_chart(chart_data)

        st.markdown("### Recent Detections")

        for row in history[:5]:

            prediction = row[4].upper()

            if row[4] == "spam":
                confidence = row[5]
            else:
                confidence = row[6]

            icon = "🚨" if row[4] == "spam" else "✅"

            st.write(
                f"{icon} **{prediction}** | "
                f"{row[1]} | {row[2]} | "
                f"Confidence: {confidence * 100:.2f}%"
            )


# Analyze Message
elif page == "Analyze Message":

    st.markdown("## 🔍 Analyze Message")
    st.caption("Use the AI model to classify an SMS or email.")

    st.markdown(
        '<div class="info-card">'
        '<b>How it works:</b> Your message is processed using '
        'TF-IDF feature extraction and a Logistic Regression classifier.'
        '</div>',
        unsafe_allow_html=True
    )

    message_type = st.radio(
        "Message Type",
        ["SMS", "Email"],
        horizontal=True
    )

    message = st.text_area(
        "Enter your message or email",
        height=220,
        placeholder="Paste the message you want SpamGuard AI to analyze..."
    )

    analyze = st.button(
        "🔎 Analyze Message",
        use_container_width=True
    )

    if analyze:

        if not message.strip():

            st.warning("Please enter a message first.")

        else:

            result = predict_message(message)

            prediction = result["prediction"]
            spam_probability = result["spam_probability"]
            safe_probability = result["safe_probability"]
            explanations = result["explanation"]

            save_detection(
                message_type,
                message,
                prediction,
                spam_probability,
                safe_probability,
                explanations
            )

            st.divider()

            if prediction == "spam":

                st.error("🚨 SPAM DETECTED")

            else:

                st.success("✅ NOT SPAM")

            st.markdown("### Detection Confidence")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Spam Probability",
                    f"{spam_probability * 100:.2f}%"
                )

            with col2:
                st.metric(
                    "Safe Probability",
                    f"{safe_probability * 100:.2f}%"
                )

            st.markdown("### Why was this message classified this way?")

            for reason in explanations:
                st.write(f"• {reason}")


# History
elif page == "History":

    st.markdown("## 🕘 Detection History")
    st.caption("Previous SMS and email analysis results")

    history = get_history()

    if not history:

        st.info("No messages have been analyzed yet.")

    else:

        for row in history:

            prediction = row[4].upper()

            if row[4] == "spam":
                confidence = row[5]
                icon = "🚨"
            else:
                confidence = row[6]
                icon = "✅"

            st.markdown(
                f"### {icon} {prediction}"
            )

            st.write(
                f"**Time:** {row[1]}  \n"
                f"**Type:** {row[2]}  \n"
                f"**Confidence:** {confidence * 100:.2f}%"
            )

            st.caption(row[3])

            st.write(
                f"**Explanation:** {row[7]}"
            )

            st.divider()


# About
elif page == "About":

    st.markdown("## ℹ️ About SpamGuard AI")

    st.write(
        "SpamGuard AI is an AI-powered system designed to detect "
        "spam SMS and email messages using machine learning."
    )

    st.markdown("### System Architecture")

    st.code(
        "USER\n"
        "  ↓\n"
        "WEB INTERFACE\n"
        "  ↓\n"
        "INPUT PROCESSING\n"
        "  ↓\n"
        "TEXT PREPROCESSING\n"
        "  ↓\n"
        "TF-IDF FEATURE EXTRACTION\n"
        "  ↓\n"
        "LOGISTIC REGRESSION\n"
        "  ↓\n"
        "PREDICTION + PROBABILITY\n"
        "  ↓\n"
        "EXPLANATION ENGINE\n"
        "  ↓\n"
        "SQLITE HISTORY + DASHBOARD"
    )

    st.markdown("### Technology Stack")

    st.write(
        "Python • Streamlit • Pandas • Scikit-learn • "
        "TF-IDF • Logistic Regression • SQLite"
    )

    st.markdown("### Dataset")

    st.write(
        "UCI SMS Spam Collection"
    )

    st.markdown("### Machine Learning Model")

    st.write(
        "Logistic Regression with TF-IDF feature extraction."
    )

    st.markdown("### Evaluation Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Accuracy", "98.45%")
        st.metric("Spam Precision", "93.89%")

    with col2:
        st.metric("Spam Recall", "93.89%")
        st.metric("Spam F1 Score", "93.89%")

    st.markdown("### Limitations")

    st.write(
        "The model is trained on the UCI SMS Spam Collection. "
        "It may not correctly classify every new, unusual, or "
        "previously unseen type of spam message."
    )


st.markdown(
    '<div class="footer">'
    'SpamGuard AI • AI-Powered Spam Detection System'
    '</div>',
    unsafe_allow_html=True
)