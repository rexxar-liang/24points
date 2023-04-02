# 24points
24 Points game written in Python with pygame, 24 points  is a popular game in primary schools. 

# New Feature will be added
1. Add new Release for Windows
2. Add docs, such as design, proposal, etc

# convert to exe
1. Install pyinstaller

    pip install pyinstaller
2. download source code 

    git clone https://github.com/rexxar-liang/24points.git

    cd 24points
3. generate exe by pyinstaller, the exe file will be in ./dist

    pyinstaller.exe -F -w -i res/images/24points.ico 24points.py

    or

    pyinstaller.exe 24points.spec
4. move 24points.exe

   cp dist/24points.exe .
5. run 24points
