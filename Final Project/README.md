# Lecture2RTF


## Description

**Lecture2RTF** is a Python code that retrieves lecture notes from the CS50’s Introduction to Programming with Python Harvard course website and converts them into RTF (Rich Text Format) files. This allows you to save the lecture content locally on your computer, enabling offline access and eliminating dependency on the CS50 website or internet connection. The RTF files can be modified or converted to PDF if needed, providing greater flexibility for personal use and sharing.

### Key Features

- **Section Extraction**: Offers flexibility to include specific sections or all sections of a lecture. Users can specify sections using a underscore-separated list, or simply request the entire lecture content.
- **RTF Formatting**: Generates RTF files with a professional layout. Each section is clearly labeled, and code snippets are highlighted for better readability. The document includes a table of contents and is formatted to include titles, paragraphs, and code blocks.
- **Error Handling**: Provides clear and user-friendly error messages for incorrect or missing command-line arguments. This ensures that users are informed about any issues with their input.

### Advantages

- **Offline Access**: Once downloaded, the RTF files can be accessed anytime without needing an internet connection, making it convenient for offline study and reference.
- **Modifiable Content**: The generated RTF files can be easily modified using any text editor that supports RTF, allowing users to add personal notes, annotations, or make adjustments.
- **Conversion to PDF**: The RTF files can be converted to PDF format if needed, offering greater flexibility for sharing or printing the lecture notes.

The script utilizes **Requests** for web scraping, **BeautifulSoup** for parsing HTML, and **Pygments** for code highlighting to produce well-organized and formatted lecture notes in RTF. This ensures that users receive a comprehensive and polished document that maintains the structure and readability of the original web content.

### Usage

To use the script, run it from the command line with the desired arguments:

```bash
python project.py [LectureNumber] [Sections]
```
Arguments:
- LectureNumber: The number of the lecture you want to retrieve. Use 'all' to retrieve all lectures.
- Sections: A hyphen-separated list of section titles to include (optional). If not provided, all sections will be included.

### Examples:
- Retrieve lecture 7:
```bash
python project.py 7
```
- Retrieve specific sections of lecture 7:
```bash
python project.py 7 "Regular Expressions_Extracting User Input"
```
- Retrieve all lectures:
```bash
python project.py all
```
