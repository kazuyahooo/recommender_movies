# recommender_movies

### Setup (GPU)
```
conda create -n py38 python=3.8
conda activate py38
conda install pytorch torchvision cudatoolkit=11.1 -c pytorch -c conda-forge
conda install -c conda-forge jupyterlab
conda install -c conda-forge matplotlib
git clone https://github.com/CVxTz/recommender_transformer
cd recommender_transformer
pip install .
```

### References

Blog : https://towardsdatascience.com/build-your-own-movie-recommender-system-using-bert4rec-92e4e34938c5 
[Github CVxTz/recommender_transformer](https://github.com/CVxTz/recommender_transformer)
[BERT4Rec: Sequential Recommendation with Bidirectional
Encoder Representations from Transformer](https://arxiv.org/abs/1904.06690)
