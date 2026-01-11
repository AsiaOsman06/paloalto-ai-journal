from src.analyzer import analyze_text
from src.storage import save_entry, load_entries

def add_entry(text: str):
    analysis = analyze_text(text)
    entry = {"text": text, "analysis": analysis}
    save_entry(entry)
    return {"message": "Entry saved", "analysis": analysis}

def get_summary():
    entries = load_entries()
    if not entries:
        return {"summary": "No entries yet"}

    sentiments = [e["analysis"]["sentiment"] for e in entries]
    avg = round(sum(sentiments) / len(sentiments), 2)

    return {
        "total_entries": len(entries),
        "average_sentiment": avg,
        "reflection": "You tend to feel more balanced when journaling consistently."
    }
