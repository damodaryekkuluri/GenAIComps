from fastapi import FastAPI
from classifier_pi import ClassificationPIDetection

app = FastAPI()
classifier = ClassificationPIDetection()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/detect_injection")
def detect_injection(input_prompt: str = None):
    res = classifier.detect_injection(input_prompt)
    return {"Result": res}