# Post conda init
conda create -n llava python=3.10 -y
conda activate llava
conda install ipython -y
pip install -e .