#!usr/bin/env python3
import argparse

def get_args():
  parser = argparse.ArgumentParser(description='Say hello')
  parser.add_argument("-n", "--name", default="World", help="name to greet")
  return parser.parse_args

def main():
  args = get_args
  name = args.name
  print("Hello " + name)

if __name__ == "__main__":
  main()
