import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="Versioned Notes", layout="centered")
st.title("📝 Versioned Notes App")

# Create a new note
st.header("Create a New Note")
with st.form("note_form"):
    title = st.text_input("Title")
    content = st.text_area("Content")
    tag = st.text_input("Tag (optional)")
    submitted = st.form_submit_button("Create Note")

    if submitted and title and content:
        res = requests.post(f"{BASE_URL}/notes/", json={
            "title": title,
            "content": content,
            "tag": tag
        })
        if res.status_code == 200:
            st.success("Note created successfully!")
        else:
            st.error("Failed to create note.")

# List all notes
st.header("📋 All Notes (All Versions)")
res = requests.get(f"{BASE_URL}/notes/")
if res.status_code == 200:
    notes = res.json()
    for note in notes:
        with st.expander(f"{note['title']} (v{note['version']})"):
            st.markdown(f"**Tag:** {note['tag'] or 'None'}")
            st.markdown(f"**Timestamp:** {note['timestamp']}")
            st.markdown("**Content:**")
            st.code(note['content'])
else:
    st.error("Failed to load notes.")

# View all versions of a note
st.header("🔍 View Versions of a Note")
selected_title = st.text_input("Enter the note title to view all versions:")

if selected_title:
    res = requests.get(f"{BASE_URL}/notes/{selected_title}")
    if res.status_code == 200:
        versions = res.json()
        if not versions:
            st.warning("No versions found for this title.")
        for v in versions:
            with st.expander(f"Version {v['version']}"):
                st.markdown(f"**Tag:** {v['tag'] or 'None'}")
                st.markdown(f"**Timestamp:** {v['timestamp']}")
                st.code(v['content'])
    else:
        st.error("Could not retrieve versions.")
