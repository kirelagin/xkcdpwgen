#!/usr/bin/env python3


import sys
import argparse

from xkcdpwgen.generator import generate_


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate xkcd-style passphrase.')
    parser.add_argument('-n', '--words', help='number of words to generate', type=int, default=4)
    parser.add_argument('-m', '--min', help='minimum length of a word', type=int, default=4)
    parser.add_argument('-M', '--max', help='maximum length of a word', type=int, default=10)
    parser.add_argument('-v', '--verbose', help='be verbose', action='store_true')
    parser.add_argument('dictionary', help='path to a dictionary')
    args = parser.parse_args()

    with open(args.dictionary) as f:
        words, count = generate_(f, count=args.words, min_len=args.min, max_len=args.max)
        if args.verbose:
            print('# of words matched: {}.'.format(count))
        print('{}'.format(' '.join(words)))
