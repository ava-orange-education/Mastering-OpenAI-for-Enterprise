from openai import OpenAI
client = OpenAI()

#upload dataset
response = client.File.create(
    file=open("data.jsonl"),
    purpose='fine-tune'
)
file_id = response["id"]

#start finetuning
response = client.FineTune.create(
    training_file=file_id,
    model="gpt-3.5-turbo"
)
fine_tune_id = response["id"]

# Evaluate
completion = client.chat.completions.create(
  model="fine-tuned-model-id",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)
print(completion.choices[0].message)

