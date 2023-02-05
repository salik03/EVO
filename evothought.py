responses = {}

input_text = input("You: ")

if input_text in responses:
    print("Evo: ", responses[input_text])
else:
    response = input("Evo: What would be a good response when someone says \"" + input_text + "\"? ")
    responses[input_text] = response

while True:
    input_text = input("You: ")
    if input_text in responses:
        print("Evo: ", responses[input_text])
    else:
        response = input("Evo: What would be a good response when someone says \"" + input_text + "\"? ")
        responses[input_text] = response
