# Markdown Viewer

A modern, interactive markdown viewer built with Streamlit that provides a rich reading experience with search functionality and a hierarchical table of contents.

## Features

- **File Upload**: Upload and view markdown files (.md, .markdown, .txt)
- **Search Functionality**: Real-time search with highlighted results
- **Table of Contents**: Automatic generation of hierarchical navigation from markdown headings
- **Responsive Layout**: Wide layout optimized for reading
- **Anchor Links**: Clickable navigation between sections
- **Syntax Highlighting**: Search terms are highlighted in the content

## Installation

1. **Clone or download the project files**
   ```bash
   # If you have the files locally, navigate to the project directory
   cd /path/to/markdown-viewer
   ```

2. **Install Streamlit** (if not already installed)
   ```bash
   pip install streamlit
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   The application will automatically open in your default browser at `http://localhost:8501`

## Usage

1. **Upload a Markdown File**
   - Use the file uploader in the sidebar to select a markdown file
   - Supported formats: `.md`, `.markdown`, `.txt`

2. **Navigate the Content**
   - Use the table of contents in the sidebar to jump to specific sections
   - Click on any heading link to navigate directly to that section

3. **Search the Content**
   - Use the search box in the sidebar to find specific text
   - Search results are highlighted in yellow
   - Search is case-insensitive

4. **View the Content**
   - The main content area displays your markdown file with proper formatting
   - Headings are automatically converted to anchor links
   - The layout is optimized for reading with a wide format

## File Structure

```
web/
├── app.py              # Main Streamlit application
├── index.html          # (Not used in current version)
├── example.chm         # Example file
├── vendor/             # Vendor dependencies
│   ├── archmage-0.4.2.1-py3-none-any.whl
│   ├── pychm-0.8.6+pyodide-cp312-cp312-pyodide_2024_0_wasm32.whl
│   └── sgmllib3k-1.0.0-py3-none-any.whl
└── README.md           # This file
```

## How It Works

### Markdown Parsing
The application parses markdown files and:
- Extracts headings to create a table of contents
- Converts markdown to HTML for display
- Generates URL-friendly anchor slugs for navigation

### Search Implementation
- Real-time search with case-insensitive matching
- Search terms are wrapped in `<mark>` tags for highlighting
- Works across the entire document content

### Table of Contents
- Automatically generated from markdown headings
- Hierarchical structure based on heading levels (#, ##, ###, etc.)
- Collapsible sections using HTML `<details>` and `<summary>` tags
- Clickable links that scroll to the corresponding section

## Requirements

- Python 3.7+
- Streamlit
- No additional dependencies required

## Browser Compatibility

The application works best in modern browsers that support:
- HTML5 features
- CSS3 styling
- JavaScript for Streamlit functionality

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.

## License

This project is open source and available under the MIT License. 