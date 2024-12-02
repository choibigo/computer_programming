import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class llama3_8B:
    def __init__(self):
        model_name = "meta-llama/Meta-Llama-3-8B"
        # cache_dir = "input your cache directory"
        # model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)
        # tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model = self.model.to(self.device)
        

    def inference(self, user_input):
        prompt = f"""You are a professional translator specializing in English-to-Korean translations.
                Your job is to accurately and fluently translate any given English text into natural and grammatically correct Korean.
                Ensure that the meaning, tone, and nuances of the original text are preserved in the translation.
                English => Korean Examples:
                Interdisciplinarity: Is there room for It in undergraduate engineering education's futures? => 학제간 연구: 학부 공학 교육의 미래에 학제간 연구의 여지가 존재하는가.
                Today, let's observe the short agenda as shown on this slide. => 오늘은 이 슬라이드에 표시된 짧은 안건을 살펴보겠습니다.
                First, let's speak about our possible futures and how those are shaped by many agents of change. => 먼저, 가능성이 있는 미래와 그 미래가 다양한 변화의 주체에 의해 어떻게 형성되는지에 대해 이야기해 봅시다.
                {user_input} => """
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        inputs = {key: value.to(self.model.device) for key, value in inputs.items()}
        max_length = len(prompt)+50
        outputs = self.model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=max_length,
            num_beams=5,
            early_stopping=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        prediction = self.tokenizer.decode(outputs[0][len(inputs["input_ids"][0]):], skip_special_tokens=True)

        return prediction
