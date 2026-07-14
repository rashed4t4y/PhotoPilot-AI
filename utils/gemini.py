from google import genai
from dotenv import load_dotenv
from PIL import Image
import os

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")

# ==========================================
# Gemini Client
# ==========================================

client = genai.Client(api_key=API_KEY)

# ==========================================
# Generate Caption & Description
# ==========================================

def generate_content(uploaded_image):

    image = Image.open(uploaded_image)

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=[
            image,

            """
You are a professional photography assistant.

Analyze the uploaded image carefully.

Generate TWO outputs.

Caption:
- Maximum 20 words
- Professional
- Catchy
- Natural
- No hashtags
- No emojis

Description:
- Between 80 and 120 words.
- Describe the subject.
- Mention lighting.
- Mention colors.
- Mention background.
- Mention mood.
- Mention photography composition.
- Write naturally like a professional photographer.
- No hashtags.
- No emojis.

Return ONLY in this exact format.

Caption:
Your caption here

Description:
Your description here
"""
        ]
    )

    result = response.text.strip()

    caption = ""
    description = ""

    if "Description:" in result:

        parts = result.split("Description:")

        caption = parts[0].replace("Caption:", "").strip()

        description = parts[1].strip()

    else:

        caption = result

    return caption, description