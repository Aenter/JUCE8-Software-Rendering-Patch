from shutil import copy
from glob import glob
from os.path import isdir
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, required=True, help="Input file path")
parser.add_argument("-o", "--output", type=str, required=False, help="Output file path")
parser.add_argument("-a", "--allow_overwrite", required=False, help="Automatically overwrite files without prompting a user", default=False, action="store_true")
args = parser.parse_args()

pattern_patch_pairs = [
    # ImagePixelData::Ptr NativeImageType::create (Image::PixelFormat format, int width, int height, bool clearImage) const
    (b"\x90\x48\x8B\x44\\\x24(.)\x48\x8B\x58.\x48\x85",
     b"\x90\x48\x8B\x44\x24\\1\x48\x33\xDB\x90\x48\x85"),
    # ComponentPeer* Component::createNewPeer (int styleFlags, void* parentHWND)
    (b"\x48\x89\x44\\\x24\x58\xC7\x44\\\x24\\\x28\x01\x00\x00\x00",
     b"\x48\x89\x44\x24\x58\xC7\x44\x24\x28\x00\x00\x00\x00"),
]

def patch_binary(input_path, output_path, allow_overwrite=False, fail_ok=False):
    # Read binary
    print(f"Reading file \"{input_path}\"...")
    exe_bytes = None
    with open(input_path, "rb") as executable:
        exe_bytes = executable.read()

    # Patch
    patch_counter = 0
    for pattern, patch in pattern_patch_pairs:
        print(f"Patching pattern from\n\"{pattern.hex(' ')}\"\nto\n\"{patch.hex(' ')}\"")
        match = re.search(pattern, exe_bytes)
        if not match:
            print("Pattern not found! Skipping...")
            continue
        exe_bytes = re.sub(pattern, patch, exe_bytes)
        patch_counter += 1
    if not patch_counter:
        no_match_message = "Could not find any matching pattern!"
        if not fail_ok:
            raise Exception(no_match_message)
        print(no_match_message)
        return
    print(f"Successfully applied {patch_counter}/{len(pattern_patch_pairs)} patches.")

    # Handle missing output path
    if not output_path:
        backup_path = f"{input_path}.bak"
        if not allow_overwrite:
            print(f"Output path was not provided. Original file is about to be overwritten and backed up as \"{backup_path}\"...")
            if input("Proceed? (y/n)") != "y":
                exit(0)
        output_path = input_path
        copy(input_path, backup_path)

    # Write patched file
    with open(output_path, "wb") as executable:
        executable.write(exe_bytes)
    print(f"The file has been patched and saved as \"{output_path}\"")

# Handle args
input_paths = glob(args.input, recursive=True)
output_path = args.output
if len(input_paths) > 1:
    print("Output path for multiple files is not supported!")
    output_path = None

# Process files
for path in glob(args.input, recursive=True):
    if isdir(path):
        continue
    patch_binary(path, output_path, args.allow_overwrite, True)