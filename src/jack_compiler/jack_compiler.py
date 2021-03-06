#!/usr/bin/env python

import sys
import glob
from os import path
from compilation_engine import CompilationEngine
from jack_tokenizer import JackTokenizer
from symbol_table import SymbolTable
from vm_writer import VMWriter

def analyze(src_jack_file, output):
    print(src_jack_file)
    tokenizer = JackTokenizer(src_jack_file)
    compilation_engine = CompilationEngine(tokenizer)
    compilation_engine.analysis(output)


def compile(src_jack_file, output):
    print(src_jack_file)
    tokenizer = JackTokenizer(src_jack_file)
    symbol_table = SymbolTable()
    vm_writer = VMWriter(output)
    compilation_engine = CompilationEngine(tokenizer, symbol_table, vm_writer)
    compilation_engine.compile()


if __name__ == '__main__':
    input = sys.argv[1]

    if path.isfile(input):
        src_jack_files = [input]
    else:
        src_jack_files = glob.glob(path.join(input, '*.jack'))

    for src_jack_file in src_jack_files:
        #output = sys.stdout
        if len(sys.argv) == 3 and sys.argv[2] == '-a':
            output = open(path.splitext(src_jack_file)[0] + ".xml", 'w')
            analyze(src_jack_file, output)
        else:
            output = open(path.splitext(src_jack_file)[0] + ".vm", 'w')
            compile(src_jack_file, output)
        output.close()
