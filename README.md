# JUCE8 - Software Rendering Patch
A simple Python script that enforces software rendering for JUCE8-based applications (both as VSTs and standalone) by patching instructions.\
This can work as a temporary fix for issues such as black screen and crashes on Linux.

<img width="2555" height="1440" alt="JUCE8-SWAM" src="https://github.com/user-attachments/assets/31596af7-9792-491d-9b39-48651bc3ec7f" />
<img width="2513" height="1433" alt="JUCE8-SWAM-REAPER" src="https://github.com/user-attachments/assets/6e1abf75-ade3-499c-92b1-e72ce634d5a2" />

## Currently confirmed working software
- SWAM Instruments

> [!NOTE]
> Keep in mind that this is a hacky, unreliable solution and might not work for every application.

## Usage
```
python3 juce_patch.py -i *input file path* -o *output file path*
python3 juce_patch.py -i *input file path*
```

## References
Patches are based on [#804bf326fc62c0a3eb0603af874f76533de6db33](https://github.com/Pflugshaupt/JUCE/commit/804bf326fc62c0a3eb0603af874f76533de6db33)
