import six
import os
from google.cloud import translate_v2 as translate

# [PATH] should indicate the key file(Json file format), which is downloaded from Google cloud.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'[PATH]'

file = open("input_article.txt", "r",  encoding='UTF-8');
data = file.read()
# print(data)
file.close()

text = data
target_language = 'zh-CN'
# Korean: ko, Chinese Simplified: zh-CN, English: en, Japanese: Ja, Chinese Traditional: zh-TW
translate_client = translate.Client()

if isinstance(text, six.binary_type):
    text = text.decode("utf-8")

# Text can also be a sequence of strings, in which case this method
# will return a sequence of results for each text.
result = translate_client.translate(text, target_language, format_='text')

# print(u"Text: {}".format(result["input"]))
# print(u"Translation: {}".format(result["translatedText"]))
print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

file2 = open("output_article.txt", "w",  encoding='UTF-8');
file2.write(result["translatedText"])
file2.close()
