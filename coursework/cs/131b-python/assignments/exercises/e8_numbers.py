'''
e8_numbers.py
jl-ccsf
07/26/2026
CS-131B, Prof. Ibrahim
Reads a file containing text, writes lines to an output file, and numbers lines.
'''

def main():

    # Opens/closes input file to read/write
    in_file = input("Enter input file name: ")
    contents = in_file.open(f"{in_file}", "rw")
    in_file.close()

    # Opens/closes output to read/write
    out_file = input("Enter output file name: ")
    out_file.open()
    # Numbers lines
    num = 0
    for line in in_file:
        line = in_file.readlines()
        num += 1
        out_file.write(f"/* {num} */" + f"{line}")
    out_file.close()

main()

'''
SAMPLE RUN: INPUT FILE

Mary had a little lamb,
Whose fleece was white as snow.
And everywhere that Mary went,
The lamb was sure to go!

SAMPLE RUN: OUTPUT FILE

/* 1 */ Mary had a little lamb,
/* 2 */ Whose fleece was white as snow.
/* 3 */ And everywhere that Mary went,
/* 4 */ The lamb was sure to go!
'''
