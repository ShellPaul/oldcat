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
# 创建数据库配置文件
python -m oldcat.octuils.db_connection.py
vi oldcat/etc/oldcat_db.json

# 创建新闻数据库
python -m oldcat.models.news

# 运行新闻 Spider
python -m oldcat.spider_start

# 设置新闻 Spider 的定时任务
15 * * * * . /root/venv/oldcat/bin/activate; cd /root/workspace/oldcat; python -m oldcat.spider_start >log/oldcat.log 2>&1
```
