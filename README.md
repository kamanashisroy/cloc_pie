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

And that will generate a nice `pie.svg` file.

Again, it is also possible to convert the cloc summary table into markdown table.
```
markdown.py summary.txt.lang summary_lang.md
markdown.py summary.txt.file summary_file.md
```
Enjoy !
