# coding:utf-8
#!/usr/bin/python
import sys
import codecs

def seg(input_file, output_file):
    input = codecs.open(input_file, "r", 'utf-8')
    output = codecs.open(output_file, 'w', 'utf-8')
    for line in input.readlines():
        word_list = line.strip().split()
        for word in word_list:
            for w in word:
                output.write(w + "\tB\n")
                output.flush()
    output.close()
    input.close()
    
if __name__ == "__main__":
    input_file = "E:\workspace\crf++\data\SEG_test.txt"
    output_file = "E:\workspace\crf++\\result\SEG_test.utf-8"
    seg(input_file, output_file)
    print "end!"