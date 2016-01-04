# coding:utf-8
#!/usr/bin/python
import sys
import codecs

def character_4tagging(input_file, output_file):
    input = codecs.open(input_file, "r", 'utf-8')
    output = codecs.open(output_file, 'w', 'utf-8')

    for line in input.readlines():
        word_list = line.strip().split()
        for word in word_list:
            if len(word) == 1:
                output.write(word + "\tS\n")
            else:
                output.write(word[0] + "\tB\n")
                for w in word[1:len(word) - 1]:
                    output.write(w + "\tM\n")
                output.write(word[-1] + "\tE\n")
        output.write("\n")
    input.close()
    output.flush()
    output.close()
    
if __name__ == "__main__":
    input_file = "E:\workspace\crf++\data\SEG_train.txt"
    output_file = "result.txt"
    character_4tagging(input_file, output_file)
    print "end!"
