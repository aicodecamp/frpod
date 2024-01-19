import ctranslate2
import transformers

translator = ctranslate2.Translator("data/models/mt5-base")
tokenizer = transformers.AutoTokenizer.from_pretrained("google/mt5-base", use_fast=False)

input_text = "translate English to German: The house is wonderful."
input_tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(input_text))

results = translator.translate_batch([input_tokens], target_prefix=[['fr']])

output_tokens = results[0].hypotheses[0]
output_text = tokenizer.decode(tokenizer.convert_tokens_to_ids(output_tokens))

print(output_text)