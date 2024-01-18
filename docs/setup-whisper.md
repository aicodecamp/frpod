# setup openai-whiser on windows with GPU support

# use python 3.10

    # install miniconda for python 3.10: https://repo.anaconda.com/miniconda/Miniconda3-py310_23.11.0-2-Windows-x86_64.exe
    C:\ProgramData\miniconda3 ; C:\ProgramData\miniconda3\scripts

C:\Users\jason.JIGJOG\.conda\envs\whisper
conda create -n whisper

- conda init
- -conda activate whisper
  conda deactivate
- conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia ffmpeg

-
