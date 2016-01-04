#coding:utf-8
import codecs
import sys

# import CRFPP
def crf_sefmenter(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    reader = input_data.read()
    for line in reader.split('\n'):
        if len(line) == 0:
            output_data.write('\n')
            continue
        wordList = line.split('\t')
        
        word = wordList[0]
        tag = wordList[1]
        print word
        
        if tag == 'B':
            output_data.write(word)
        elif tag == 'M':
            output_data.write(word)
        elif tag == 'E':
            output_data.write(word + ' ')
        else:
            output_data.write(word + ' ')
              
if __name__ == '__main__':
    input_file = "result.txt"
    output_file = "rest.txt" 
    crf_sefmenter(input_file, output_file)
