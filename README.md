Cloc Pie
==========

This software generates pie chart based on [cloc](https://github.com/AlDanial/cloc) output. The code defines which [langauge you are](http://miniim.blogspot.com/2016/02/line-of-code.html). To get to know yourself there are following steps,

- Install [cloc](https://github.com/AlDanial/cloc).
- get the code statistics of each project.
- Create summary of all the statistics.
```
$(CLOC) --sum-reports --out summary.txt *.txt
```
- Use clock pie to render pie chart.
```
pie.py summary.txt.lang
```

It is also possible to get the pie chart from csv file.
```
pie.py info.csv
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

File | files | blank | comment | code 
--- | --- | --- | --- | --- 
libsync.txt                      | 241 | 8649 | 9998 | 56467 
aroop.txt                        | 256 | 3561 | 2506 | 22042 
miniim.txt                        | 88 | 1757 | 3824 | 8572 
shotodol.txt                     | 134 | 574 | 867 | 6564 
roopkotha.txt                     | 66 | 737 | 990 | 4903 
opp_factory.txt                   | 23 | 517 | 308 | 3875 
roopkotha_vela.txt                | 56 | 302 | 638 | 2689 
hciplus.txt                       | 29 | 207 | 141 | 2089 
barrel.txt                        | 47 | 270 | 135 | 1864 
shotodol_net.txt                  | 20 | 115 | 161 | 1454 
shotodol_web.txt                  | 20 | 116 | 189 | 1151 
shotodol_db.txt                   | 12 | 74 | 122 | 689 
shotodol_script.txt                | 8 | 34 | 39 | 354 
shotodol_media.txt                 | 2 | 12 | 20 | 100 
SUM:                            | 1002 | 16925 | 19938 | 112813 

By the way it is possible to add `--md` argument to `cloc` to generate markdown files.

Enjoy !
