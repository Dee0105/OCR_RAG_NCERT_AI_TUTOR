import ollama


def extract_text_from_image(image_path):

    response = ollama.chat(
        model="moondream",
        messages=[
            {
                "role": "user",
                "content": "Extract all text from this image.",
                "images": [image_path]
            }
        ]
    )

    extracted_text = response["message"]["content"]

    return extracted_text