import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os
import PIL.Image

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
image_path = "./content/invoice_template_002.png"

json_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "address": {
      "type": "string",
    },
    "name": {
      "type": "string",
    },
    "post_code": {
      "type": "string",
    },
  },
  "required": ["address", "name", "post_code"]
}

img = PIL.Image.open(image_path)

model = genai.GenerativeModel('gemini-1.5-pro-latest')

completion = model.generate_content(["""\

この画像に表示されている内容について回答してください。
請求先の住所(address), 氏名(name), 郵便番号(post_code)を教えて下さい。

""",
img]
)

print(completion.text)
