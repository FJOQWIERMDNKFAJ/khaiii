import json

from khaiii import KhaiiiApi


target_tags = ['NNG', 'NNP']


def parse(s):
    api = KhaiiiApi()
    gen = api.analyze(s)
    for word in gen:
        if hasattr(word, 'morphs'):
            morphs = word.morphs
            for morph in morphs:
                yield [morph.lex, morph.tag]


def collect(inp):
    output = set()
    for lex, tag in parse(inp):
        if tag in target_tags:
            output.add(lex)
    return output


def lambda_handler(event, context):
    if event['isBase64Encoded']:
        import base64
        body = json.loads(base64.b64decode(event['body']).decode())
    else:
        body = json.loads(event['body'])
    try:
        inp = body['text']
        out = collect(inp)  # set[str]
        o = {
            'statusCode': 200,
            'body': json.dumps({'nn': list(out)}),
            'isBase64Encoded': False,
        }
        return o
    except:
        o = {
            'statusCode': 400,
            #'body': json.dumps(event),
            'body': {'detail': 'bad request'},
            'isBase64Encoded': False,
        }
        return o

