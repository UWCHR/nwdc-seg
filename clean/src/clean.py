#
# :date: 2020-01-15
# :author: PN
# :copyright: GPL v2 or later
#
# nwdc/clean/src/clean.py
#
#
import pandas as pd
import argparse
import sys
import yaml
if sys.version_info[0] < 3:
    raise "Must be using Python 3"


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--facilities", required=True)
    parser.add_argument("--cleanrules", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    return parser.parse_args()


if __name__ == "__main__":

    args = _get_args()

    read_csv_opts = {'sep': '|',
                     'quotechar': '"',
                     'compression': 'gzip',
                     'encoding': 'utf-8'}

    df = pd.read_csv(args.input, **read_csv_opts)

    print(f'Cleaning {args.input}')

    with open(args.cleanrules, 'r') as yamlfile:
        cleanrules = yaml.load(yamlfile)

    if args.output == 'output/pogo.csv.gz':
        redacted = cleanrules['pogo_drop']
        df = df.drop(redacted, axis=1)

    if args.output == 'output/uwchr.csv.gz':
        redacted = cleanrules['uwchr_drop']
        df = df.drop(redacted, axis=1)

    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.strip()
    for key in cleanrules['all_cols'].keys():
        df.columns = df.columns.str.replace(key, cleanrules['all_cols'][key])

    placement_types = cleanrules['placement_types']
    df['placement_reason_type'] = df['placement_reason'].replace(placement_types)

    facil = pd.read_csv(args.facilities)
    facil_detloc = dict(zip(facil['facility'], facil['detloc']))

    df['detloc'] = df['facility'].replace(facil_detloc)
    df = df.rename(cleanrules['rename'], axis=1)

    write_csv_opts = {'sep': '|',
                      'quotechar': '"',
                      'compression': 'gzip',
                      'encoding': 'utf-8',
                      'index': False}

    df.to_csv(args.output, **write_csv_opts)
    print(df.columns)
    print(f'Wrote {len(df)} records to {args.output}')
    print()

# END.
