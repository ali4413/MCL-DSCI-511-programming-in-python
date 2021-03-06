---
type: slides
---

# Slicing Only Columns using df.loc\[\]

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

What happens now if we wanted all the rows of the dataframe but only the
columns `calories` to `fiber`?

We would simply use `:` to indicate from “end” to “end” for rows.

``` python
df.loc[:, 'calories':'fiber']
```

```out
                           calories  protein  fat  sodium  fiber
name                                                            
100% Bran                        70        4    1     130   10.0
100% Natural Bran               120        3    5      15    2.0
All-Bran                         70        4    1     260    9.0
All-Bran with Extra Fiber        50        4    0     140   14.0
Almond Delight                  110        2    2     200    1.0
...                             ...      ...  ...     ...    ...
Triples                         110        2    1     250    0.0
Trix                            110        1    1     140    0.0
Wheat Chex                      100        3    1     230    3.0
Wheaties                        100        3    1     200    3.0
Wheaties Honey Gold             110        2    1     200    1.0

[77 rows x 5 columns]
```

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

## So Far

`loc` is used to slice columns and rows by **label** and within an
interval. We always specify **row** indexing first, then **columns**.

``` python
df.loc['row name start':'row name end', 'column name start':'column name end']
```

  - If we aren’t slicing any columns, we can simply say `df.loc[ 'row
    name start': 'row name end']` since columns specification follow
    rows.
  - However, the reverse is not true. If we want all the rows with only
    specific columns, we specify rows first and therefore we would need
    to make it clear with `df.loc[ : , 'column name start' : 'column
    name end']`.
  - We can read `:` as **“to”**
  - If the indices are labeled with numbers, we do not need “quotations”
    when calling them.

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>

---

# Let’s apply what we learned\!

Notes: Script here.

<html>

<audio controls >

<source src="placeholder_audio.mp3" />

</audio>

</html>
