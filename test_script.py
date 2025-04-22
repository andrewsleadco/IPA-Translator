import eng_to_ipa as ipa

sentence = "This is a fuckign test sentence and it lives inside this script."
result = ipa.convert(sentence, retrieve_all=False, stress_marks=False)

print(result)
