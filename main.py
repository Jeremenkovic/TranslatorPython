import os
from google.cloud import translate_v2
from bs4 import BeautifulSoup

# Set your Google Cloud Translate API key here
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/nemanjajeremenkovic/Downloads/test-app-379617-5916865040e7.json"

# Initialize the translation client
translate_client = translate_v2.Client()

# Open the HTML file to be translated
with open("/Users/nemanjajeremenkovic/Desktop/project/www.classcentral.com/report/list-of-mooc-based-microcredentials/index.html", "r") as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Loop through all text nodes in the HTML file
for text_node in soup.find_all(string=True):
    if text_node.parent.name not in ['style', 'script', 'img', 'svg', 'ul']:
        # Split the text into smaller chunks
        text = text_node.string.strip()
        chunks = [text[i:i + 5000] for i in range(0, len(text), 5000)]

        # Translate each chunk and replace the text in the HTML file
        for chunk in chunks:
            translated_text = translate_client.translate(chunk, source_language="en", target_language="hi")[
                "translatedText"]
            new_element = soup.new_tag(text_node.parent.name)
            new_element.string = translated_text
            text_node.replace_with(new_element)

# Save the translated HTML file
with open("/Users/nemanjajeremenkovic/Desktop/translatedhtml/report/list-of-mooc-based-microcredentials/index.html", "w") as f:
    f.write(str(soup))

#stao si kod starting-this-month