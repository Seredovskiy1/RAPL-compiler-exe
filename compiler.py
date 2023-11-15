# compiler.py

from languageAPI import riskuap_builder, InvalidArgvLength
import argparse

def compile_files(files):
    try:
        builder_: riskuap_builder = riskuap_builder(files, [], False)
        print(builder_.start_language_builder())
    except SyntaxError as e:
        print(f"Warning: SyntaxError in the file {files}. Compilation will continue. Error details: {e}")
    except AttributeError as e:
        print(f"Error: {e}. Compilation failed. Please check if the provided file is valid.")

def main():
    parser = argparse.ArgumentParser(description='Compiler script.')
    parser.add_argument('-normal', dest='file_path', help='Path to the file to compile')

    args = parser.parse_args()

    if args.file_path:
        compile_files(args.file_path)
    else:
        print("Error: Please provide a file path using the '-normal' option.")

if __name__ == "__main__":
    main()
