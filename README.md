# eng2hin-language-translator
# Training
This code defines a function translator that uses the transformers library to create a translation pipeline for English to Hindi translation.
The pipeline is created using a pre-trained translation model called Helsinki-NLP/opus-mt-en-hi. This model has been trained on a large corpus of English and Hindi text, and can be fine-tuned on specific domains or datasets for better performance.
The function first initializes the tokenizer and model for the translation pipeline using the AutoTokenizer and AutoModelForSeq2SeqLM classes respectively.
Next, it creates a pipeline object for translation using the pipeline method from transformers. The pipeline object takes in the previously defined tokenizer and model, and sets the task to translation.
Finally, the function returns the translated text in Hindi as well as the original input string. 
Overall, this code provides a simple and easy-to-use function for English to Hindi translation using pre-trained models from the transformers library.

# Webapp
a Flask web application that provides a simple user interface for translating English text to Hindi and uses html,css for frontend.
