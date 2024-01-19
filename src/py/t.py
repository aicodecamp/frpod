import ctranslate2
translator = ctranslate2.Translator("data/models/nllb-200-600M")
results = translator.translate_batch([["你好", "世界", "!"]])
target = results[0].hypotheses[0][1:]

print(tokenizer.decode(tokenizer.convert_tokens_to_ids(target)))
