import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
 
tokenizer = AutoTokenizer.from_pretrained("ProtectAI/deberta-v3-base-prompt-injection")
model = AutoModelForSequenceClassification.from_pretrained("ProtectAI/deberta-v3-base-prompt-injection")
 
class ClassificationPIDetection:
    def _init_(self) -> None:
        pass
 
    def _get_classification_output(self, text):
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits
        predicted_class_id = logits.argmax().item()
        return predicted_class_id
 
 
    def detect_injection(self, user_input: str) -> bool:
        injection_label = self._get_classification_output(user_input)
        if injection_label == 1:
            return True
        return False