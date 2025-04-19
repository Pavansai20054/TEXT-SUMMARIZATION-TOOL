# 🏗️ ArticleSummarizer - Architecture Overview

This document provides a detailed explanation of the ArticleSummarizer project architecture, components, and how they interact.

## 🧩 System Components

### 1. Core Module (`CoreCut.py`) 🔍

This is the heart of the summarization engine that implements the TextRank algorithm:

```
CoreCut.py
└── summarize_text()
    ├── Initialize PlaintextParser
    ├── Create TextRankSummarizer instance
    └── Generate and return summary
```

**Key functions:**
- `summarize_text(text, sentence_count)`: Processes input text and returns a concise summary with the specified number of sentences.

**Dependencies:**
- Sumy library components (PlaintextParser, Tokenizer, TextRankSummarizer)

### 2. Application Runner (`main.py`) ⚙️

The entry point and orchestrator for the application:

```
main.py
├── load_article()
├── save_summary_md()
└── main execution block
    ├── Load article
    ├── Generate summary
    └── Save output
```

**Key functions:**
- `load_article(path)`: Reads input text from a file
- `save_summary_md(original, summary, output_path)`: Creates formatted markdown output
- Main execution block: Coordinates the workflow

**Dependencies:**
- NLTK for natural language processing
- CoreCut module for the summarization algorithm

## 🔄 Data Flow

```
                 ┌───────────┐
                 │input_text.txt│
                 └─────┬─────┘
                       │
                       ▼
┌───────────┐    ┌───────────┐
│  CoreCut.py │◄───┤   main.py   │
└─────┬─────┘    └─────┬─────┘
      │                │
      │                ▼
      │          ┌───────────┐
      └─────────►│output_text.md│
                 └───────────┘
```

1. 📄 The user places their article in `input_text.txt`
2. 🔍 `main.py` reads the article content
3. 🧠 `main.py` calls `CoreCut.py` to generate the summary
4. 💾 `main.py` formats and saves the results to `output_text.md`

## 🎯 Design Decisions

### 1. Modular Architecture 🧱

The project follows a modular design pattern:
- Core summarization logic is isolated in `CoreCut.py`
- Interface and I/O handling is managed by `main.py`

This separation makes the code more maintainable and allows the summarization logic to be reused in other applications.

### 2. TextRank Algorithm 🌟

The TextRank algorithm was chosen for its:
- ✅ Effectiveness with minimal training data
- 🌐 Language-agnostic approach
- 💪 Strong performance for extractive summarization
- 🧩 Implementation simplicity

### 3. Markdown Output Format 📝

The output uses Markdown format because:
- 👁️ It's human-readable
- 🔄 It can be easily converted to other formats
- 🌐 It works well with GitHub and other documentation systems
- 🏗️ It allows for structured presentation of both original text and summary

### 4. Error Handling 🛡️

Currently, basic error handling is implemented. Future versions could enhance:
- Input validation
- More robust file handling
- Better error messaging

## 🚀 Future Architectural Improvements

1. **Command Line Interface** 💻: Add proper CLI arguments for more flexibility
2. **Multiple Algorithm Support** 🧠: Plugin architecture to support different summarization algorithms
3. **Web API** 🌐: Develop a REST API wrapper
4. **Language Detection** 🔤: Automatic language identification for non-English texts
5. **Performance Optimization** ⚡: Caching and parallel processing for larger documents

## 📦 Dependencies Management

Dependencies are managed through `requirements.txt` to ensure consistent environments across installations.

## 🧪 Testing Strategy

Currently, testing is manual. Future improvements could include:
- ✅ Unit tests for core functions
- 🔄 Integration tests for the full workflow
- 📊 Performance benchmarks against standard datasets