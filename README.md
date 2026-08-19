# Corsican Language Tutor

A simple AI-powered command line language tutor for **Corsican (Corsu), English, and French**.

The program uses the **Groq API** with the `llama-3.3-70b-versatile` model to detect the language of a word or phrase, translate it, provide example sentences, and explain a short Corsican grammar or cultural note.

## Features

* Detects whether the input is in **Corsican, English, or French**
* Translates:

  * Corsican to English and French
  * English to Corsican
  * French to Corsican
* Generates example sentences
* Provides Corsican grammar tips or cultural notes
* Runs directly in the terminal
* Continues accepting new phrases until the user exits

## How It Works

The user enters a word or phrase in the terminal.

The program sends that input to the Groq API with instructions to:

1. Detect the language
2. Translate the phrase
3. Generate example sentences
4. Provide a grammar or cultural note

The AI response is then displayed directly in the terminal.

Example interaction:

```text
Corsican Language Tutor powered by Groq

Supports: English <-> Corsican | French <-> Corsican

Enter a word or phrase (or 'quit'): hello
```

The response follows this format:

```text
Language Detected:
Translation(s):
Example Sentences:
Grammar/Cultural Note:
```

## Tech Stack

* Python
* Groq API
* Llama 3.3 70B
* python-dotenv

## Installation

Clone the repository:

```bash
git clone https://github.com/MarieAnge04/Toccu-AI-chatbot-prototype.git
cd Toccu-AI-chatbot-prototype
```

Install the required packages:

```bash
pip install groq python-dotenv
```

## Environment Variables

Create a `.env` file in the root of the project:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The application loads the API key using `python-dotenv`:

```python
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
```

Do not upload your `.env` file or API key to GitHub.

Add this to your `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
```

## Running the Program

Run:

```bash
python main.py
```

Then enter any Corsican, English, or French word or phrase.

To exit, enter:

```text
quit
```

or:

```text
exit
```

## Example Use Cases

The tutor can be used to:

* Learn basic Corsican vocabulary
* Practice translations between Corsican, English, and French
* Explore example sentences
* Learn small grammar concepts
* Discover cultural context related to the Corsican language

## Project Purpose

This project explores how large language models can be used as interactive tools for language learning, particularly for less commonly supported languages such as Corsican.

The goal is to make Corsican practice more accessible by combining translation, examples, and cultural context in a simple conversational tool.

## Future Improvements

Possible future additions include:

* A web or mobile interface
* Vocabulary history
* Saved favorite words
* Pronunciation support
* Flashcards and quizzes
* Difficulty levels
* Conversation practice
* Persistent user progress
* More structured grammar lessons

## Disclaimer

AI-generated translations may not always be perfectly accurate, especially for regional vocabulary, dialect differences, or less common Corsican expressions. The tool is intended primarily for learning and experimentation.
