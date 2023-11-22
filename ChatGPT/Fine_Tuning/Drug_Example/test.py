import os 
import openai

def init_api():
    with open(".env") as env:
        for line in env:
            if "=" in line:
                key, value = line.strip().split("=")
                os.environ[key] = value

    openai.api_key = os.environ.get('OPENAI_API_KEY')


init_api()

# my fine tune model 
model = "ada:ft-learninggpt:drug-malady-data-2023-11-22-22-05-46"

drugs = [
    "What is 'A CN Gel(Topical) 20gmA CN Soap 75gm' used for?",  # Class 0
    "What is 'Addnok Tablet 20'S' used for?",  # Class 1
    "What is 'ABICET M Tablet 10's' used for?",  # Class 2
]

class_map = {
    0: "Acne",
    1: "Adhd",
    2: "Allergies",
}

for drug_name in drugs:
    prompt = "Drug: {}\nMalady:".format(drug_name)

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=1,
        max_tokens=1,
    )
    
    response = response.choices[0].text
    try: 
        print(drug_name + " is used for " + class_map[int(response)])
    except:
        print("I don't know what " + drug_name + " is used for.")
    print()