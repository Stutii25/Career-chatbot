import google.generativeai as genai

genai.configure(api_key="AIzaSyBwg_uKsoint-XzUFeITq7u-hkxOhBP5vI")

# Get generator
models_gen = genai.list_models()

# Convert to list and print
models_list = list(models_gen)
for m in models_list:
    print(m)
