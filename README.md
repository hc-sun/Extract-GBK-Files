# A script extracts files to properly display GBK encoded file names. 
## 解压文件名中带有GBK编码中文字符的文件。

In Unicode encoded operating systems, GBK encoded Chinese characters cannot be displayed properly, especially when extracting compressed zip/rar files.

Example:
```bash
python extract.py -f test.zip
```