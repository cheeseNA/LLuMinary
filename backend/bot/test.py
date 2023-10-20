from gpt4all import GPT4All
model = GPT4All('gpt4all-13b-snoozy-q4_0.gguf')
output = model.generate("I am depressed, make me not depressed", max_tokens=200)
print(output)