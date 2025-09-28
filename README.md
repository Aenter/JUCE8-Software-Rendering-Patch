# JUCE8 - Software Rendering Patch
A simple Python script that forces software rendering for JUCE8-based applications (both as VSTs and standalone) by patching instructions.\
This can work as a temporary fix for issues such as black screen and crashes on Linux.

<img width="2555" height="1440" alt="JUCE8-SWAM" src="https://github.com/user-attachments/assets/31596af7-9792-491d-9b39-48651bc3ec7f" />
<img width="2513" height="1433" alt="JUCE8-SWAM-REAPER" src="https://github.com/user-attachments/assets/6e1abf75-ade3-499c-92b1-e72ce634d5a2" />

### What works
- **Audio Modeling SWAM Instruments 3.10.0** - All instruments (including VariFlute), Ambiente, Software Center
### What doesn't work
- **Divisimate v2.0.6** - at first window renders fine, but after a brief moment it turns black
- **Sonible learn:bundle** - loading any VST results in stack overflow and crash
> [!NOTE]
> Keep in mind that this is a hacky, unreliable solution and might not work for every application.

## How to use
### Arguments
- **-i**: Can be either file path or glob pattern.
- **-o**: Output path for patched file. Works only for single file.
- **-a**: Automatically overwrite files without asking user for confirmation.
### Examples
```
python3 juce_patch.py -i "/home/mekuu/.wine/drive_c/Program Files/Audio Modeling/SWAM Cello/SWAM Cello 3.exe" -o "/home/mekuu/.wine/drive_c/Program Files/Audio Modeling/SWAM Cello/SWAM Cello 3 Patched.exe"
python3 juce_patch.py -i "/home/mekuu/.wine/drive_c/Program Files/Audio Modeling/SWAM Cello/SWAM Cello 3.exe"
python3 juce_patch.py -i "/home/mekuu/.wine/drive_c/Program Files/Common Files/VST3/SWAM/**/*.vst3" -a
```

## References
Patches are based on [#804bf326fc62c0a3eb0603af874f76533de6db33](https://github.com/Pflugshaupt/JUCE/commit/804bf326fc62c0a3eb0603af874f76533de6db33)
