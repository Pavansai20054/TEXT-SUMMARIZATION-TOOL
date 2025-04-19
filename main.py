import nltk
nltk.download('punkt')

from CoreCut import summarize_text

def load_article(path="input_text.txt"):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def save_summary_md(original, summary, output_path="output_text.md"):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("# 🧠 Article Summarizer Output\n\n")
        file.write("## 📄 **Original Article (First 500 characters)**\n")
        file.write("```text\n")
        file.write(original[:500] + "...\n")
        file.write("```\n\n")
        file.write("## ✨ **Summary**\n")
        file.write("```text\n")
        file.write(summary.strip() + "\n")
        file.write("```\n")

if __name__ == "__main__":
    article = load_article()
    summary = summarize_text(article, sentence_count=5)
    
    # ✅ Correct usage
    save_summary_md(article, summary)

    print("✅ Summary saved to `output_text.md`.")
