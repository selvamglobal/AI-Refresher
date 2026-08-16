model = 'gpt-4'
tokens = 1000
score = 1.2345

print(f"model used   : {model}")
print(f"tokens used. : {tokens}")
print(f"score        : {score}")
print(f"score rounded: {(round(score))}")

if tokens > 500:
    print(f"tokens used is greater than 500, {tokens} tokens used.")
elif tokens >  100:
    print(f"tokens used is equal to 500, {tokens} tokens used.")
else:
    print(f"tokens used is less than 100, {tokens} tokens used.")

prompts = [
    "Write a poem about the sea.",
    "Explain the theory of relativity in simple terms.",
    "What are the benefits of meditation?",
    "Describe the process of photosynthesis.",
    "What is the history of the internet?"]
for prompt in prompts:
    print(f"Prompt: {prompt}")
    