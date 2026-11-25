#!/bin/bash
set -e


export PATH="$HOME/.local/bin:$PATH" && 
python3.13 -m PyInstaller --clean --noconfirm --onedir --collect-all PyQt5 --collect-all PIL --debug all --distpath kdEngineLinuxBuild -n kdEngine main.py &&

# deletes kdEngine.spec file after building
rm kdEngine.spec &&

# deletes the build folder after building 
rm -rf build &&

# copies the 'assets' folder
echo "The 'assets' folder is being copied..." &&
cp -r assets kdEngineLinuxBuild/kdEngine/ &&
echo "Done." &&

# copies the 'kdengine' modules folder after building too
echo "The 'kdengine' folder is being copied..." &&
cp -r kdengine kdEngineLinuxBuild/kdEngine/ &&
echo "Done."

# launching the game
echo "Launching the game..."
cd kdEngineLinuxBuild/kdEngine/
chmod +X kdEngine
./kdEngine
