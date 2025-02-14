import torch
from torch import nn
from transformers import BertModel, BertPreTrainedModel, BertForMaskedLM
from transformers.modeling_outputs import MaskedLMOutput
from transformers import BertTokenizer, BertConfig

from pdb import set_trace as bp

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Load the configuration and set the type_vocab_size
config = BertConfig.from_pretrained("bert-base-uncased")
config.type_vocab_size = 2  # or however many token types you have

bp()

# Initialize the custom model
model = BertForMaskedLM.from_pretrained("bert-base-uncased", config=config)



# Example input
input_text = "Example input text for BERT model."
inputs = tokenizer(input_text, return_tensors="pt")

model.state_dict()

# Forward pass
outputs = model(input_ids=inputs["input_ids"],attention_mask=inputs["attention_mask"])

print(outputs.logits)