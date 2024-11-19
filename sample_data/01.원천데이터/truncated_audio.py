import wave

def trim_wav(input_file, output_file, start_time, end_time):
    # .wav 파일 열기
    with wave.open(input_file, 'rb') as wav:
        params = wav.getparams()
        framerate = wav.getframerate()
        n_channels = wav.getnchannels()
        sampwidth = wav.getsampwidth()
        
        # 시작 및 종료 프레임 계산
        start_frame = int(start_time * framerate)
        end_frame = int(end_time * framerate)
        num_frames = end_frame - start_frame

        # 프레임 포인터를 시작 위치로 이동
        wav.setpos(start_frame)
        
        # 필요한 프레임 읽기
        frames = wav.readframes(num_frames)

    # 잘라낸 데이터를 새 파일에 저장
    with wave.open(output_file, 'wb') as out_wav:
        out_wav.setnchannels(n_channels)
        out_wav.setsampwidth(sampwidth)
        out_wav.setframerate(framerate)
        out_wav.writeframes(frames)

# 사용 예시
trim_wav(r'D:\workspace\difficult\class\3기_2024_2\컴퓨터프로그래밍\computer_programming\speech_recognition\Sample\01.원천데이터\E_EA_10001.wav',
         'truncated_audio.wav',
         start_time=5.0,
         end_time=60.0)
