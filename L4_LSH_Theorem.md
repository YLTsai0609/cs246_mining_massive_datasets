# L4

<img src='./assets/lshtm_1.png'></img>

more hashing function, more accurate approx.

<img src='./assets/lshtm_2.png'></img>

X axis - similarity cut of the signature matrix.

Y axis - prob of sharing >=1 buckets

The figure is ideal situation.

The fp and fn discussion.

In general, we wanna reduce fn, becuase if fp is high, we can do filter after LSH procudure. but we cannot save fn if they just be discards.

<img src='./assets/lshtm_3.png'></img>

<img src='./assets/lshtm_4.png'></img>

# How Do We Make the S-curve?

<img src='./assets/lshtm_5.png'></img>

1. prob : element in a single row of $C_1, C_2$ are equal $=s$
2. prob : all rows in a band are equal $=s^{r}$
3. prob : some row in a band is not equal $=1-s^{r}$
4. prob : all bands are not equal $(1-s^{r})^{b}$
5. prob at least 1 band is equal = $1 - (1-s^{r})^{b}$ - $C_1, C_2$ Prob thatis a candidate pair

## Some example result

$k=50, s=0.6, r=5, b=10$

<img src='./assets/lshtm_6.png'></img>

we can easily move our s to .8, .9 to reduce the fp, but we will increase fn.


$k=50, s=0.6$, change $r, b$

<img src='./assets/lshtm_7.png'></img>

band = 1, rows per band = 1, basically hash once., we got straight line.

1. increase $r$, prob : sharing bucket are become harder.

2. $r=1$, increase $b$ : increase thr peob they sharing the bucket (because we hash them multiple times)

3. the 2 figure on the right hand : when we increse $r$
the curve shifting to 10.
(the more roes per band, the prob they sharing bucket is more strict.)
 
 
# Theory of LSH

<img src='./assets/lshtm_8.png'></img>

<img src='./assets/lshtm_9.png'></img>

Any func match following is distance measure

1. $d(x, y) \geq 0$
2. $d(x, y) = 0 ~ if ~ x=y$
3. $d(x, y) = d(y, x)$
4. $d(x, y) \neq d(x, z) + d(z, y)$ - triangle inequality.


1. jacarrd dist for set = 1 - jaccard similarity
2. cosine distance for vectors = angle between the vec
3. L2, L1, 

<img src='./assets/lshtm_10.png'></img>

1. hash fun : is any func that allows us to say whether two element are equal.

2. $h(x) = h(y)$ : h says $x$ and $y$ are equal.

3. A family of hash fun is any set of hash funcs fromwhich we can pick one at random efficiently

<img src='./assets/lshtm_11.png'></img>

<img src='./assets/lshtm_12.png'></img>

So we want our function match the property, and looks like the curve above.

And how do you think the middle part of function should be?

**ideally, our threshold will lie between $d_{1}, d_{2}$, of course, we want the value above the threshold, prob grows rapidly, on the other hand, prob  decrease**

<img src='./assets/lshtm_13.png'></img>

# Stats


0.5 hour - 20mins

0.75 hour - 15 mins
