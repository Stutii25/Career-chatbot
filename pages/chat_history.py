import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "career_chatbot.db"

def get_chat_history(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT message, is_user, timestamp FROM chat_history WHERE user_id=? ORDER BY id ASC",
        (user_id,),
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

# ✅ Do NOT call st.set_page_config() here (only allowed in app.py)
st.title("📜 Chat History")

# Check login
if "user" not in st.session_state or not st.session_state.user:
    st.warning("⚠️ Please log in from the main app (CareerBot) to see your chat history.")
else:
    user = st.session_state.user
    st.subheader(f"Welcome back, {user['username']} 👋")

    history = get_chat_history(user["id"])
    if history:
        df = pd.DataFrame(history, columns=["Message", "Is User", "Time"])
        df["Speaker"] = df["Is User"].map({1: "User", 0: "Bot"})
        
        # Reorder columns for readability
        df = df[["Speaker", "Message", "Time"]]
        
        # Show chat history table
        st.dataframe(df, use_container_width=True)

        # Download option
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download Chat History",
            data=csv,
            file_name="chat_history.csv",
            mime="text/csv",
        )

        # Clear history option
        if st.button("🗑️ Clear History"):
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM chat_history WHERE user_id=?", (user["id"],))
            conn.commit()
            conn.close()
            st.success("✅ Chat history cleared!")
            st.rerun()
    else:
        st.info("ℹ️ No chat history found yet.")
