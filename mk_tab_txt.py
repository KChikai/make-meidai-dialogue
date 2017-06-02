# -*- coding: utf-8 -*-


def make_pairs():
    with open('pair_corpus.txt', 'w', encoding='utf-8') as f:
        input_lines = open('./input.txt', 'r', encoding='utf-8').read().split('\n')
        output_lines = open('./output.txt', 'r', encoding='utf-8').read().split('\n')
        for index, input_text in enumerate(input_lines):
            f.write(input_text + '\t' + output_lines[index] + '\n')


def check():
    import re
    pattern = "(.+?)(\t)(.+?)(\n|\r\n)"
    r = re.compile(pattern)
    for line in open('pair_corpus.txt', 'r', encoding='utf-8'):
        m = r.search(line)
        if m is not None:
            post = [word for word in m.group(1).split(' ')]
            cmnt = [word for word in m.group(3).split(' ')]
            print(post)
            print(cmnt)
            break


if __name__ == '__main__':
    make_pairs()
    check()
