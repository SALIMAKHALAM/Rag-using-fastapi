from transformers import pipeline

class Generator:
    def __init__(self, model_name="google/flan-t5-base"):
        self.pipe = pipeline("text2text-generation", model=model_name)

    def generate_answer(self, context, question):
        prompt = f"Answer the question based on the context:\n\nContext:\n{context}\n\nQuestion: {question}"
        result = self.pipe(prompt, max_new_tokens=256)[0]
        return result['generated_text']
