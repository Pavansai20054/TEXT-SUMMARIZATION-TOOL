from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize_text(text, sentence_count=5):
    """
    Summarizes the given text using TextRank algorithm.

    Args:
        text (str): The input article text.
        sentence_count (int): Number of sentences for the summary.

    Returns:
        str: A summarized version of the article.
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)
