import ollama 

client = ollama.Client()

model = "gandroid"

def brain(text):
    prompt = text

    response = client.generate(model=model, prompt=prompt)

    # print("Response:")
    # print(response.response)
    responseText = response.response

    return responseText