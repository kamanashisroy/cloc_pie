Cloc Pie
==========

This software generates pie chart based on [cloc](https://github.com/AlDanial/cloc) output. The code defines which [langauge you are](http://miniim.blogspot.com/2016/02/line-of-code.html). To get to know yourself there are following steps,

1. install [cloc](https://github.com/AlDanial/cloc).
2. get the code statistics of each project.
3. Create summary of all the statistics.
```
$(CLOC) --sum-reports --out summary.txt *.txt
```
4. Use clock pie to render pie chart.
```
pie.py summary.txt.lang
```

Here is my pie.

![pie](https://cloud.githubusercontent.com/assets/973414/12768766/aa70e5a8-c9d7-11e5-9e18-069bd961a3c8.jpg)

And that will generate a nice `pie.svg` file.

Again, it is also possible to convert the cloc summary table into markdown table.
```
markdown.py summary.txt.lang summary_lang.md
markdown.py summary.txt.file summary_file.md
```

Here is my sample language table.

Language | files | blank | comment | code |
-- | -- | -- | -- | -- |
C                               | 127 | 8070 | 7770 | 58476 |
Vala                            | 424 | 3483 | 3279 | 27305 |
C/C++ Header                    | 171 | 1662 | 3710 | 6752 |
Java                             | 30 | 830 | 2867 | 3868 |
Vala Header                      | 19 | 283 | 245 | 3387 |
C++                              | 16 | 448 | 589 | 2959 |
PHP                              | 46 | 272 | 173 | 1907 |
CSS                              | 19 | 372 | 138 | 1789 |
XHTML                            | 26 | 325 | 62 | 1463 |
JavaScript                       | 13 | 238 | 727 | 1438 |
make                             | 66 | 571 | 50 | 1423 |
Lua                              | 25 | 198 | 110 | 1252 |
Bourne Shell                      | 7 | 51 | 93 | 221 |
Ant                               | 2 | 22 | 28 | 155 |
m4                                | 2 | 28 | 17 | 110 |
Perl                              | 1 | 32 | 36 | 107 |
Assembly                          | 2 | 14 | 41 | 84 |
HTML                              | 2 | 6 | 0 | 41 |
XML                               | 1 | 0 | 3 | 27 |
Bourne Again Shell                | 1 | 9 | 0 | 24 |
NAnt script                       | 1 | 9 | 0 | 23 |
DOS Batch                         | 1 | 2 | 0 | 2 |
SUM:                           | 1002 | 16925 | 19938 | 112813 |



Enjoy !
