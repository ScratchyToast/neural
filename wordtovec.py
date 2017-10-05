def wordToNum(text):
    tmp = []
    for i in range(255):
        if i < len(text):
           tmp.append(ord(text[i]))
        else:
            tmp.append(0)
    return tmp

def arrNumToWord(nums):
    text = ''
    for i in nums:
        if i>255:
            continue
        text += chr(int(round(i)))
    return text
