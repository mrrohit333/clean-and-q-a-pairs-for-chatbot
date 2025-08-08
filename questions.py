import re

def generate_qa_pairs(text_path, output_path):
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split by line
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    qa_pairs = []

    current_question = None
    current_answer = []

    for line in lines:
        # Treat lines in ALL CAPS or ending in ':' as potential questions
        if (line.isupper() and len(line.split()) < 10) or line.endswith(":"):
            if current_question and current_answer:
                qa_pairs.append((current_question, " ".join(current_answer).strip()))
                current_answer = []
            current_question = line.rstrip(":")
        else:
            if current_question:
                current_answer.append(line)

    # Add the last pair
    if current_question and current_answer:
        qa_pairs.append((current_question, " ".join(current_answer).strip()))

    # Save as text file
    with open(output_path, "w", encoding="utf-8") as out:
        for i, (q, a) in enumerate(qa_pairs):
            out.write(f"### Question {i+1}:\n{q}\n")
            out.write(f"### Answer:\n{a}\n\n")

    print(f"{len(qa_pairs)} Q&A pairs saved to {output_path}")

# Run the function
generate_qa_pairs("cleaned_income_tax_law.txt", "qa_pairs.txt")
