# spider
这是最基本的基于Python实现的爬虫，输入一个入口地址后，会爬取该地址网页中的以www开头的地址，并将这些地址的页面内容下载下来，依次保存。

注意：
1、对于不能访问的坏链接，将会忽略。
2、只能爬取入口地址的链接，不再向更深处爬取。
3、会自动给页面编ID，并跳过已爬取的页面

