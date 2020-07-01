# -*- coding: utf-8 -*-

"""
Created on 2020-07-02 00:15  

@author: congyingxu
"""
import sys



def main():
    corpus_content = read_TXTfile('../corpus/clean_corpus.txt')
    corpus_content = corpus_content.replace(' ','\n')
    write_TXTfile('embeddings/words300.lst',corpus_content)

def read_TXTfile(path):
    with open(path,'r') as f :
        content = f.read()
        return content

def write_TXTfile(path,content):
    with open(path,'w') as f :
        # f.write(str(content, encoding = "utf-8"))
        f.write(content)

if __name__ == '__main__':
    main()