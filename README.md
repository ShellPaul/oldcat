Old Cat
=======

More Traffic, More information

问题1：一个新闻网站会有流量吗？
----------------
**策略1.**
- 在 360 搜索首页获取热点新闻标题
- 在今日头条搜索新闻
- 爬取新闻内容到数据库  


启动命令
----
```python
# 创建新闻数据库
python -m oldcat.models.news

# 运行新闻 Spider
python -m oldcat.spider_start
```
