# SerpentSorterAI

## Overview
SerpentSorterAI is a Python-based tool designed for preprocessing large volumes of text data from diverse sources like video transcripts, blog articles, legal documents, and PDFs. It aims to clean, deduplicate, and prepare this data for training AI chatbots, focusing on customer service and assistant roles.

## Features
- **Text Normalization**: Converts text to a uniform format.
- **Tokenization**: Splits text into words/sentences.
- **Stemming/Lemmatization**: Standardizes word forms.
- **Stop Word Removal**: Eliminates common words.
- **Spell Checking**: Corrects typos and misspellings.
- **Deduplication**: Removes duplicate content.
- **PDF Text Extraction**: Processes text from PDF files.
- **Custom Cleaning Rules**: Handles unique data inconsistencies.

## Prerequisites
- Python 3.8 or later
- Pip (Python package installer)
- Basic knowledge of Python and command line operations

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SerpentSorterAI.git
   ```
## Navigate to the SerpentSorterAI directory:
```
cd SerpentSorterAI
```
## Install required packages:
```
pip install -r requirements.txt

```
## Usage
# Place your text data files in the designated input folder.
# Run the main script to start processing:
```
python main.py
```
# Processed data will be saved in the output folder.

## Tools Used

- **NLTK**: For foundational text processing tasks.
- **SpaCy**: Advanced NLP operations and performance.
- **TextBlob**: Basic text processing and sentiment analysis.
- **PyMuPDF**: Handling and extracting text from PDFs.
- **Regular Expressions**: Pattern matching and data cleaning.

## Techniques Employed

- **Normalization and Tokenization**: Standardizes and breaks down text.
- **Stemming/Lemmatization and Stop Word Removal**: Reduces words to their root forms and removes unnecessary words.
- **Spell Checking and Deduplication**: Corrects errors and removes redundancies.
- **Custom Cleaning Rules**: Tailored for specific data types like legal documents.

## Contributing

Contributions to SerpentSorterAI are welcome! Please read `CONTRIBUTING.md` for guidelines on how to contribute.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- AI community for continuous support and inspiration.
- Contributors who have helped shape this project.

## Contact

For questions or support, please contact [jay@mobilelegalsolutions.com](mailto:jay@mobilelegalsolutions.com).

## Authors

- Your Name - Initial work - [jay-alexander-elliot](https://github.com/Jay-Alexander-Elliot)

## FAQ

- **Q: Can I use SerpentSorterAI for other types of text data?**
  - **A:** Yes, while it's optimized for chatbot training data, it can be adapted for other text processing tasks.

## Changelog

For a detailed changelog, see the `CHANGELOG.md` file.

## Future Improvements

- Incorporating machine learning for more sophisticated text analysis.
- Expanding compatibility with more data formats.








