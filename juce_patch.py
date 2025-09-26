from shutil import copy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, required=True, help="Input file path")
parser.add_argument("-o", "--output", type=str, required=False, help="Output file path")
args = parser.parse_args()

pattern_patch_pairs = [
    # ImagePixelData::Ptr NativeImageType::create (Image::PixelFormat format, int width, int height, bool clearImage) const
    (b"\x90\x48\x8B\x44\x24\x40\x48\x8B\x58\x38\x48\x85",
     b"\x90\x48\x8B\x44\x24\x40\x48\x33\xDB\x90\x48\x85"),
    # ComponentPeer* Component::createNewPeer (int styleFlags, void* parentHWND)
    (b"\x48\x89\x44\x24\x58\xc7\x44\x24\x28\x01\x00\x00\x00",
     b"\x48\x89\x44\x24\x58\xc7\x44\x24\x28\x00\x00\x00\x00"),
]

input_path = args.input
output_path = args.output

# Read binary
exe_bytes = None
with open(input_path, "rb") as executable:
    exe_bytes = executable.read()

# Patch
for pattern, patch in pattern_patch_pairs:
    print(f"Patching pattern from\n\"{pattern}\"\nto\n\"{patch}\"...")
    if pattern not in exe_bytes:
        raise Exception("Pattern not found!")
    exe_bytes = exe_bytes.replace(pattern, patch)
print(f"Finished patching.")

# Handle missing output path
if not output_path:
    backup_path = f"{input_path}.bak"
    print(f"Output path was not provided. Original file is about to be overriden and backed up as \"{backup_path}\"...")
    if input("Proceed? (y/n)") != "y":
        exit(0)
    output_path = input_path
    copy(input_path, backup_path)

# Write patched file
with open(output_path, "wb") as executable:
    executable.write(exe_bytes)
print(f"The file has been patched and saved as \"{output_path}\"")
input("Press any key to exit.")
