from ollama import chat

# Read one extracted text file
with open("data/extracted_text/proposal_A.txt", "r", encoding="utf-8") as file:
    document_text = file.read()

prompt = f"""
You are an insurance document classifier.

Classify the document into ONLY one category:

1. Proposal Form
2. KYC Document
3. Payment Receipt
4. Nominee Form

Document:

{document_text}

Return only the category name.
"""

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])