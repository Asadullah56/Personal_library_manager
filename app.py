import streamlit as st
import json 

# load & save library data.
def load_library():
    try:
        with open("Library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_library(library):
    with open("Library.json", "w") as file:
        json.dump(library, file, indent=4)

# initial library
library = load_library()

st.title("Personal Library Manager")
menu = st.sidebar.radio("Select an Option", ["View Library", "Add Book", "Remove Book", "Search Book", "Save and Exit"])

if menu == "View Library":    
    st.sidebar.title("Your Library")
    if library:
        st.table(library)
    else:
        st.write("No Book in your Library. Add Some Books")

# Add Books
elif menu == "Add Book":
    st.sidebar.title("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=2022, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as Read")
    
    if st.button("Add Book"):
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
        save_library(library)
        st.success("Book added successfully!")
        st.rerun()

# Remove Book
elif menu == "Remove Book":
    st.sidebar.title("Remove a Book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("Select a Book to remove", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library(library)
            st.success("Book Removed Successfully")
            st.rerun()
    else:
        st.warning("No Book in Your Library. Add Some Book")

# Search Book
elif menu == "Search Book":
    st.sidebar.title("Search a Book")
    search_term = st.text_input("Enter Title or Author Name")

    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No book found!")

# Save and Exit
elif menu == "Save and Exit":
    save_library(library)
    st.success("Library Saved Successfully!")
