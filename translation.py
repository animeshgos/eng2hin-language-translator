from transformers import pipeline

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def translator(inp_str):
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")

    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hi")

    translator = pipeline("translation", model=model, tokenizer=tokenizer)

    res = translator(inp_str)

    return res[0]["translation_text"], inp_str
