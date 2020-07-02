# -*- coding: utf-8 -*-

"""
Created on 2020-07-02 00:15  

@author: congyingxu
"""
import sys



def main():
    #hash file
    # corpus_content = read_TXTfile('../corpus/clean_corpus.txt')
    # corpus_content = corpus_content.replace(' ','\n')
    # write_TXTfile('embeddings/words100.lst',corpus_content)

    #hash file
    corpus_content = read_TXTfile('embeddings/model.vec')
    corpus_content_list = corpus_content.split('\n')[1:] # 去掉首行 82146 100

    hash_file_str = ''
    emb_file_str = ''
    for line in corpus_content_list:
        if len(line) <1:
            continue
        print(line)
        hash_file_str += line.split(' ')[0] + '\n'# 取每行第一个空格前的
        emb_file_str += line[ line.index(' ')+1 : ] + '\n'# 去每行第一个空格前的

    hash_file_str.strip('\n')
    emb_file_str.strip('\n')
    write_TXTfile('embeddings/words100.lst', hash_file_str)
    write_TXTfile('embeddings/embeddings100.txt', emb_file_str)



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