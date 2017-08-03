#NYU Depth v2 Dataset
##Description
The *NYU-Depth V2* dataset is from http://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html.
It is proposed in *Indoor Segmentation and Support Inference from RGBD Images, ECCV 2012*. [PDF](http://cs.nyu.edu/~silberman/papers/indoor_seg_support.pdf), [Bib](http://cs.nyu.edu/~silberman/bib/indoor_seg_support.bib)

The `nyu_depth_v2_labeled.mat` file (~2.8 GB) features:
- 1449 pairs of RGB and depth images
- 640 x 480 pixels

In our experiments, this dataset is partitioned into three sets:
- the first 1350 pairs as the training set
- the following 50 pairs as the validation set
- the last 49 pairs as the test set.

Note that hazy images will be generated according to the *Atmospheric Scattering Model* in other phases.

##Download
[nyu_depth_v2_labeled.mat](http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/nyu_depth_v2_labeled.mat)

You can run `wget -c http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/nyu_depth_v2_labeled.mat` or `python download_nyu_depth_v2.py`. 
