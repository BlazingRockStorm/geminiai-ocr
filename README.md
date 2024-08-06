# Document OCR with Google Gemini


Fully in OpenAI

## Commands
```shell
python3 -m venv .
source ./bin/activate
```

run:
```shell
pip install -r requirements.txt
python app.py
```

## Conclusion

- Gemini 1.5 Flash: 50% correct
- Gemini 1.5 Pro: 100% correct, but sometimes this happened(This Pro version is something like free trial since it is the same key as the above Flash model, and my account didn't have any payment):
```log
Traceback (most recent call last):
  File "/Users/user/projects/geminiai-ocr/app.py", line 40, in <module>
    print(completion.text)
  File "/Users/user/projects/geminiai-ocr/lib/python3.10/site-packages/google/generativeai/types/generation_types.py", line 436, in text
    raise ValueError(
ValueError: Invalid operation: The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned. Please check the `candidate.safety_ratings` to determine if the response was blocked.
```

