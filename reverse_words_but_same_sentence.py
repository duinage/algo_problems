"""
Task:
Write an algorithm in a standard way that in linear time will transform the input sentence 
into a sentence in which the words are reversed but remain in their places. 
It is forbidden to use built-in functions, string to array conversion, etc.
"""


def reverse_words_but_same_sentence(string: str):
    s_new = ""
    s_temp = ""
    for i in string:
        if i == " ":
            s_new = s_new + s_temp +  " "
            s_temp = ''
        else:
            s_temp = i + s_temp
    else:
        s_new = s_new + s_temp
    return s_new


if __name__=="__main__":
    sentence = "this sentence will now become with the words inverted in the same places in linear time"
    result = reverse_words_but_same_sentence(sentence)
    print(result) # siht ecnetnes lliw won emoceb htiw eht sdrow detrevni ni eht emas secalp ni raenil emit