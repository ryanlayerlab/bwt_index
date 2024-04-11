import gzip


def read_fasta(file):
    if file.endswith('.gz'):
        with gzip.open(file, 'rt') as f:
            data = f.read().split('>')
            data = [x for x in data if x != '']
            data = [x.split('\n') for x in data]
            data = [[x[0], ''.join(x[1:]).upper()] for x in data]
        return data
    else:
        with open(file, 'r') as f:
            data = f.read().split('>')
            data = [x for x in data if x != '']
            data = [x.split('\n') for x in data]
            data = [[x[0], ''.join(x[1:]).upper()] for x in data]
        return data
