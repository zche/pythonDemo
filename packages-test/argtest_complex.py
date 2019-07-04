import argparse
parser = argparse.ArgumentParser(description='parse imcoming text')
parser.add_argument('-e','--emulate',
                    type=str,
                    choices=['wit','luis','dialogflow'],
                    default='zhaoruifei',help='which service to emulate,default:None')
args = parser.parse_args()
print(args)
#print(args.echo)
print(parser.parse_args(['-e','luis']))