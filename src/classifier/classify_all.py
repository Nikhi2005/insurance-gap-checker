import os
from unittest import result
from ollama import chat
import json

INPUT_FOLDER = "data/extracted_text"

results = []

def classify_document(document_text):

    prompt = f"""
You are an insurance document classifier.

Classify the document into ONE category only.

Rules:

Proposal Form:
Contains fields like:
Applicant Name,
Policy Type,
Sum Insured,
Annual Income

KYC Document:
Contains fields like:
PAN Number,
Aadhaar Number,
Address,
Nationality

Payment Receipt:
Contains fields like:
Transaction ID,
Amount Paid,
Payment Date,
Bank,
Status

Nominee Form:
Contains fields like:
Nominee Name,
Relationship,
Share Percentage

Document:

{document_text}

Return ONLY one of:

Proposal Form
KYC Document
Payment Receipt
Nominee Form
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

    result = response["message"]["content"]

    if "Proposal Form" in result:
        return "Proposal Form"

    elif "KYC Document" in result:
        return "KYC Document"

    elif "Payment Receipt" in result:
        return "Payment Receipt"

    elif "Nominee Form" in result:
        return "Nominee Form"

    else:
        return "Unknown"


for file_name in os.listdir(INPUT_FOLDER):

    if file_name.endswith(".txt"):

        file_path = os.path.join(INPUT_FOLDER, file_name)

        with open(file_path, "r", encoding="utf-8") as file:
            document_text = file.read()

        category = classify_document(document_text)

        results.append(
        {
            "file": file_name,
            "document_type": category
        }
        )

        print(f"{file_name} --> {category}")

        with open(
            "outputs/json/classification_results.json",
            "w",
            encoding="utf-8"
        ) as json_file:

            json.dump(
                results,
                json_file,
                indent=4
            )

        print("\nClassification results saved successfully.")