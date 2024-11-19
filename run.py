import os
import speech_recognition
import utils
import translation

if __name__ == '__main__':
    
    wav_path = os.path.join(os.getcwd(), 'sample_data', '01.원천데이터', 'truncated_audio.wav')
    
    sr_model = speech_recognition.whisper_large_v3_turbo_model(device='cuda')
    sr_result = sr_model.inference(wav_path)

    print(f'\n {sr_result}')

    english_gt_path = os.path.join(os.getcwd(), 'sample_data', '01.원천데이터', 'truncated_audio_gt.txt')
    with open(english_gt_path, "r", encoding="utf-8") as file:
        english_gt = file.read()

    sr_bleu_score = utils.calculate_bleu_score([english_gt], sr_result)
    print(f'\n sr_bleu_score: {sr_bleu_score}')

    # TO DO
    # trans_model = translation. ....
