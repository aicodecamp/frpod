

align sentence boundry in transcripe:

https://github.com/openai/whisper/discussions/1243

https://github.com/openai/whisper/discussions/314


```
whisper testeur.mp3 --model large --language French  --word_timestamps True  --prepend_punctuations '' --append_punctuations ''


--prepend_punctuations '' --append_punctuations ''

--word_timestamps True


```

copy first 22 seconds of mp3 file

```
ffmpeg -ss 00:00:00 -i testeur.mp3 -t 22 -c copy -map 0 out.mp3
```