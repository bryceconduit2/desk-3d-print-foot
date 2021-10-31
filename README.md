# desk-3d-print-foot
Fully adjustable 3D printable spiral foot for desk.

![Alt text](/output/desk_foot.jpg?raw=true "Title")


Prerequisities: \
Open anaconda prompt. Anaconda/miniconda available from https://www.anaconda.com/.  \

Installation:
1) Create conda/miniconda environment and activate:\
conda create --name 3d \
conda activate 3d 
2) Install python\
conda install -c anaconda python=3.8
3) Clone/download github repositrary into desired folder.\
git clone https://github.com/bryceconduit2/desk-3d-print-foot.git
4) cd into directory\
cd desk-3d-print-foot
5) Install required python libraries:\
pip install -r requirements.txt. If problems are encountered here with installation of packages: - pip install pipreqs; pipreqs --force and repeat. You may need to install numpy-stl via pip install numpy-stl
6) Enter src directory\
cd src
7) Run python script\
python coaster3D.py. If "from stl import mesh" error encountered here do pip install numpy-stl.\
