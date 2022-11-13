import openai

openai.api_key = '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'

def gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt= prompt + "\n",
        temperature=0.7,
        max_tokens=512,
        top_p=1.0,
        frequency_penalty=1.0,
        presence_penalty=0.0,
        echo=False,
        logit_bias={"50256": -100},
    )
    return response

complete = gpt("What are some examples of inequalities between sexes?:").choices[0].text

print(complete)