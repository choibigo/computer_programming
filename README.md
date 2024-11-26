Repository for computer programming class (2024-2)

# Folder structure
```
|
├─ speech_recognition
|  ├─ init.py # speech_recognition api setting
|  ├─ ...
├─ translation
|  ├─ init.py # translation api setting
|  ├─ ... 
| run.py # to do - running speech_recognition, translation
```

# Setup
```

conda create -n cp_env python=3.10 -y
conda activate cp_env

pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu124
# pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu121 (혁준, 승완)
# pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu118 (영재)

git clone https://github.com/choibigo/computer_programming.git
cd computer_programming

pip install -r requirements.txt
# pip install accelerate>=0.26.0 

python run.py
```

# Role
### Speech Recognition
- 유혁준
- 최대원

### Translation
- 류승완
- 전영재

# Schedule

| Check | Data | Content | Presenter |
|----------|----------|----------|----------|
| - | 11월 16일 | Paper review | 미정 |
| - | 12월 03일 | Weekly progression | 미정 |
| - | 12월 10일 | Weekly progression | 미정 |
| - | 12월 17일 | Final presentation | 미정 |
| - | 12월 24일 | Personal report | 미정 |


![logo](https://www.hanyang.ac.kr/documents/20182/0/initial3.png/4054db65-27de-4fff-80fb-15a05561b317?t=1472537582993)
