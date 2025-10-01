import spacy
nlp = spacy.load("zh_core_web_trf")

with open("medium示例.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
for text in lines:
    print(text.strip())  
doc = nlp(text)
print([token.text for token in doc])
for ent in doc.ents:
    print(ent.text, ent.label_)

# from spacy.tokens import Token

# # Add the property
# Token.set_extension("is_fruit", getter=lambda token: token.text in ("apple", "banana", "cherry"))

# # Process some text
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("I have an apple.")

# # Check the custom attribute
# print([(token.text, token._.is_fruit) for token in doc])