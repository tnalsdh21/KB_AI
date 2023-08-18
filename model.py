import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel, PeftConfig

peft_model_id = "hyos0415/kb_ad"
config = PeftConfig.from_pretrained(peft_model_id)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

# torch.save(model.state_dict(), 'model.pth')  # 학습된 모델의 매개변수(state_dict)만 저장하는 방법
# model.load_state_dict(torch.load('model.pth')) # 원래 모델과 일치하는지 확인


#  매개변수(state_dict) 불러와서 pre-trained 모델에 재적용
model2 = AutoModelForCausalLM.from_pretrained(config.base_model_name_or_path, quantization_config=bnb_config, device_map={"":0})
model2 = PeftModel.from_pretrained(model2, peft_model_id)
tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
model2.load_state_dict(torch.load('model.pth'))
model2.eval()


# 위에 모델만 받아와서 여기에서 살짝 학습시켜야한답니다,,,

# def gen(x):
#   q = f"### 질문: {x}\n\n### 답변:"
#   # print(q)
#   gened = model2.generate(
#     **tokenizer(
#       q,
#       return_tensors='pt',
#       return_token_type_ids=False
#     ).to('cuda'),
#     max_new_tokens=512,
#     early_stopping=True,
#     do_sample=True,
#     eos_token_id=2,
#   )
  # print(tokenizer.decode(gened[0]))
#   return tokenizer.decode(gened[0])