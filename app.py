import re
import streamlit as st
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(page_title="Markdown Viewer", layout="wide")

# ---- Top bar -------------------------------------------------------------
# Sidebar controls (file uploader & search)
with st.sidebar:
    uploaded_file = st.file_uploader(
        "Open markdown file",
        type=["md", "markdown", "txt"],
        label_visibility="collapsed",
    )
    search_query = st.text_input(
        "Search", placeholder="Search", label_visibility="collapsed"
    )
    st.markdown("---")

# -------------------------------------------------------------------------
# Helper utilities


def slugify(text: str) -> str:
    """Convert heading text to a URL-friendly anchor slug."""
    slug = re.sub(r"[^a-zA-Z0-9\-\s]", "", text).strip().lower()
    slug = re.sub(r"\s+", "-", slug)
    return slug or "heading"


def parse_markdown(md: str):
    """Return (headings, html) where headings is a list of dicts with keys
    title, level, anchor."""
    headings = []
    html_lines = []
    for line in md.splitlines():
        m = re.match(r"^(#+)\s+(.*)", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            anchor = slugify(title)
            headings.append({"title": title, "level": level, "anchor": anchor})
            html_lines.append(f'<h{level} id="{anchor}">{title}</h{level}>')
        else:
            html_lines.append(line)
    return headings, "\n".join(html_lines)


def highlight_html(html_text: str, query: str) -> str:
    """Wrap all case-insensitive occurrences of `query` in <mark> tags."""
    if not query:
        return html_text
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    return pattern.sub(lambda m: f"<mark>{m.group(0)}</mark>", html_text)


# -------------------------------------------------------------------------
# Main UI logic
if uploaded_file is None:
    st.info("Upload a markdown file to get started.")
    st.stop()

markdown_text = uploaded_file.read().decode("utf-8")
headings, html_content = parse_markdown(markdown_text)
html_content = highlight_html(html_content, search_query)

# Sidebar – hierarchical collapsible table of contents rendered as HTML lists


def build_tree(headings_list):
    """Convert flat headings list to hierarchical tree using heading levels."""
    root = {"level": 0, "children": []}
    stack = [root]
    for h in headings_list:
        while stack and h["level"] <= stack[-1]["level"]:
            stack.pop()
        parent = stack[-1]
        node = {**h, "children": []}
        parent["children"].append(node)
        stack.append(node)
    return root["children"]


def build_toc_html(nodes, indent=0):
    """Recursively build HTML for the TOC using <details>/<summary>."""
    html_fragments = []
    indent += 10
    for node in nodes:
        if node["children"]:
            html_fragments.append(
                f"<details style='margin-left:{indent}px;'>"
                f"<summary><a href='#{node['anchor']}'>{node['title']}</a></summary>"
            )
            html_fragments.append(build_toc_html(node["children"], indent))
            html_fragments.append("</details>")
        else:
            link = (
                f"<div style='margin-left:{indent}px;'>"
                f"<a href='#{node['anchor']}'>{node['title']}</a>"
                f"</div>"
            )
            html_fragments.append(link)
    return "\n".join(html_fragments)


if headings:
    st.sidebar.header("Table of Contents")
    toc_tree = build_tree(headings)
    st.sidebar.markdown(build_toc_html(toc_tree), unsafe_allow_html=True)

# Content pane (right side)
content_container = st.container()
with content_container:
    st.markdown(html_content, unsafe_allow_html=True)
