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

# Problem for today's lecture

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

Convert document into a set.

<img src='./assets/lsh_8.png'></img>

<img src='./assets/lsh_9.png'></img>

<img src='./assets/lsh_10.png'></img>

<img src='./assets/lsh_11.png'></img>

Jaccard similiarity --> Interection over Union(same as detection task)

similarity basically means the same as distances.

## From Sets to Boolean Matrices

<img src='./assets/lsh_12.png'></img>

actually a document(column), shilingling sparse matrix.

Q : how to tune/determine the k-shilingling
    * A1 : words are not random, your k should be small them the words(?)

When you build such a matrix. you can calculate the jaccard similarity between each column, it's fine.

<img src='./assets/lsh_13.png'></img>

notice the warning, these methods can produce flase negtive, even false positive.

# Min-Hashing

<img src='./assets/lsh_14.png'></img>

Convert Large sets to short signatures, while perserving similarity.

<img src='./assets/lsh_15.png'></img>

<img src='./assets/lsh_16.png'></img>

If sim($C_{1}$, $C_{2}$) is high, then with high prob $h(C_{1})$ = $h(C_{C2})$

If sim($C_{1}$, $C_{2}$) is low, then with high prob $h(C_{1})$ != $h({C_{2}})$

<img src='./assets/lsh_17.png'></img>

Interesting thing : we need a custom collision to match our algorithm!

<img src='./assets/lsh_18.png'></img>

Jaccard similarity <---> Min-Hashing

the hash function depedends on your similarity function!.

We'll talk more about the hashing function for cosine / euclidean distance.

<img src='./assets/lsh_19.png'></img>

## example

<img src='./assets/lsh_20.png'></img>

<img src='./assets/lsh_21.png'></img>

create a permutation $\pi$(just a shulffing)

<img src='./assets/lsh_23.png'></img>

we wanna create a signature matrix $M$

<img src='./assets/lsh_22.png'></img>

we look at our permutation column matrix.

we look at the value $1$, it's match the 2nd, 4th document. So the Signature matrix $M$ values become $1$

Same idea, we got value $2$ for document 1 and document 3.

Then we build another permutation, do the same thing!

you will get $[2,1, 4, 1]$ for signature matrix.

<img src='./assets/lsh_24.png'></img>

So that we can build a sigmature matrix $M$ for rows x columns = number of permutation(hash functions) x number of documentation.

## Why the similarity preserve? - The Min-Hash Poperty.
### One way to look this
Choose a random permutation $\pi$

Claim $Pr[h_{\pi}(C_{1}) = h_{\pi}C(_{2})] = sim(C_{1}, C_{2})$

Why?

**Let** $X$ be a doc(set of shingles), $z \in X$ is a shingle.

**Then** $Pr[\pi(z)] = min(\pi(X))] = \frac{1}{|X|}$

the prob that particular shingle is the first shingle = $\frac{1}{X}$, because our permutation is random basically.

<img src='./assets/lsh_25.png'></img>

### Here is another way

<img src='./assets/lsh_26.png'></img>

Consider another way, there is four type of comparison.

$a$ = # rows of type A

$b$ = # rows of type B

$c$ =  # rows of type C

$d$ =  # rows of type D

Jaccard similarity $sim(C_1, C_2) = \frac{a}{a+b+c}$

Claim :  $Pr[h(C_{1}) = h(C_{2})] = sim(C_1, C_2)$

If you look up the two docuemnt column(shingle), both of them is equal to 1. it's a type A-row

TODO, 39:22

https://www.youtube.com/watch?v=dRWO3il-jjA&list=PLoCMsyE1cvdVnCgHk43vRy7PVTVWJ6WVR&index=4

# Stats

1 hour - 20mins

1 hour - 20 mins