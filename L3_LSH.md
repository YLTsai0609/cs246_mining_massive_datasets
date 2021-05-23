# Locality Sensitive Hashing

<img src='./assets/lsh_1.png'></img>

LHS could be the basis for the recommendation system.

e.g. Image search

<img src='./assets/lsh_2.png'></img>

Pintrest : 4B images

user eanna search the similar images of query.

<img src='./assets/lsh_3.png'></img>

Collect billions of images

determine the feature representation of each image.

Given a query Q, find nearest neighbors FAST.

Other Applications

<img src='./assets/lsh_4.png'></img>

1. Google - Pages with simiar words
2. Shopee - similar products
3. Pintrest - similar pictures
4. ...

# Problem for todat's lecture

<img src='./assets/lsh_5.png'></img>


1. LSH is really a family of related techniques.
2. In general, one throws items into buckets using serveral different **hash functions**

examine - 檢查
upside - 優勢
downside - 劣勢

3. You only examine only those pairs of itmes that share a bucket for at lease one of these hasgings.(we don't need to check all of he itmes, you know it right?)
   1. (Upside) If you design the hash function correctly, only a small fraction of pairs are ever examined.
   2. (DOwnside) There are false negtives - pairs of similar items that never even got considered.


# Naive approach

<img src='./assets/lsh_6.png'></img>

# LSH

<img src='./assets/lsh_7.png'></img>

# Shingling

<img src='./assets/lsh_8.png'></img>

<img src='./assets/lsh_9.png'></img>

<img src='./assets/lsh_10.png'></img>

<img src='./assets/lsh_11.png'></img>

Jaccard similiarity --> Interection over Union(same as detection task)

similarity basically means the same as distances.

## From Sets to Boolean Matrices

<img src='./assets/lsh_12.png'></img>

TODO : https://www.youtube.com/watch?v=dRWO3il-jjA&list=PLoCMsyE1cvdVnCgHk43vRy7PVTVWJ6WVR&index=3

20:21