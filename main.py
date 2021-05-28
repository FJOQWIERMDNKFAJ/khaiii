from khaiii import KhaiiiApi


def parse(s):
    api = KhaiiiApi()
    gen = api.analyze(s)
    for word in gen:
        if hasattr(word, 'morphs'):
            morphs = word.morphs
            for morph in morphs:
                yield [morph.lex, morph.tag]


if __name__ == '__main__':
    import sys
    data = ' '.join(sys.argv[1:])
    output = set()
    target_tags = ['NNG', 'NNP']
    for lex, tag in parse(data):
        if tag in target_tags:
            output.add(lex)
    print(output)




