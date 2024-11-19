import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import soundfile as sf 
import numpy as np

class whisper_large_v3_turbo_model:
    def __init__(self, device):
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        model_id = "openai/whisper-large-v3-turbo"
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id, torch_dtype=self.torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        model.to(self.device)
        processor = AutoProcessor.from_pretrained(model_id)


        # Create the pipeline
        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            torch_dtype=self.torch_dtype,
            device=device,
        )

    def inference(self, wav_path):
        audio_data, sample_rate = sf.read(wav_path)

        if len(audio_data.shape) > 1:
            audio_data = np.mean(audio_data, axis=1)

        input_audio = {"array": audio_data, "sampling_rate": sample_rate}
        result = self.pipe(input_audio, return_timestamps=True)
        return result['text'] 

