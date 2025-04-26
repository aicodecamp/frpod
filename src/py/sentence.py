import json
from pprint import pprint 
from dataclasses import dataclass
import pysrt


@dataclass
class Sentence:
    index_start : int =None
    index_end: int =None
    time_start: float =None
    time_end: float =None
    text: str = None
   


# ajust the srt to start new line at sentense boundary

def offset_whitespace(s):
    # Calculates the number of leading whitespace characters in a string.
    return(len(s) - len(s.lstrip()))

def load_whisper_json(file):
    # Loads and processes Whisper JSON output to extract text and timing information.
    doc_timing = {}
    doc_text = ""
    js = open(file)
    jsdata = json.load(js)

    # segments is lines in srt
    for s in jsdata["segments"]:
        # words - has : word, start, end
        for word_timed in s["words"]:
            # print(word_timed['start'], word_timed['end'], word_timed['word'])
            word = word_timed['word']
            if len(doc_text) == 0:
                word = word.lstrip() # remove any leading whitespace from first word in Whisper
                start_index = 0
            doc_text += word 
            start_index = len(doc_text) - len(word) + offset_whitespace(word) # align the timing index with the spaCy token index
            doc_timing[start_index] = (word_timed['start'], word_timed['end'], word_timed['word'])
    return doc_text, doc_timing



def get_sentence_boundary(doc_text:str, doc_timing: dict):

    # Identifies sentence boundaries in text based on timing information.
    sentence = Sentence()
    sentences = []
    index_max = max(doc_timing.keys())
    for index in sorted(doc_timing.keys()):
        token = doc_timing[index]
        start =  token[0]
        end = token[1]
        word: str = token[2]

        # sentence end
        if (len(word.strip()) == 1 and word.strip() in '?.!,') or (index >=index_max) :
            sentence.index_end = index + len(word)
            sentence.time_end = end
            sentence.text = doc_text[sentence.index_start: sentence.index_end]

            sentences.append(sentence)
            # save sentence, and reset
            sentence = Sentence()
        else:
            if sentence.time_start ==None:
                sentence.time_start = start
            if sentence.index_start == None:
                sentence.index_start = index

    return sentences




if __name__ == '__main__':
    json_file = 'build/test/out.json'
    srt_file = 'build/test/out.srt'    
    srt_new = 'build/test/out-new.srt'

    testeur_json = "build/fr-qa/testeur.json"
    testeur_srt = "build/fr-qa/testeur.srt"
    testeur_new = "build/fr-qa/testeur-new.srt"


    s = Sentence()
    pprint(s)

    

    doc_text, doc_timing = load_whisper_json(testeur_json)
    sentenses = get_sentence_boundary(doc_text, doc_timing)

    print( doc_text)
    pprint(doc_timing)
    pprint(sentenses)

    subs = pysrt.open( testeur_srt)

    for index in range(len(subs) , len(sentenses),  -1):
        del subs[index-1]

    for index, sentence   in enumerate(sentenses):
        subs[index].start.seconds =sentence.time_start
        subs[index].end.seconds = sentence.time_end
        subs[index].text = sentence.text

    subs.save(testeur_new)

