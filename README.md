# Scrapy-on-Lagou

## 项目介绍

本项目是一个使用 Scrapy 爬取拉勾网招聘信息的示例。通过本项目，你可以了解到 Scrapy 的使用方法和爬取网站数据的基本流程。

## 代码逻辑分析

本项目的代码主要由以下几部分组成：

### 1. settings.py

在 `settings.py` 文件中，可以设置 Scrapy 的一些参数，包括爬虫的名称、网站的 URL、下载延迟、数据存储方式等等。其中，最重要的参数是 `ITEM_PIPELINES`，它定义了 Scrapy 的数据处理流程。在本项目中，我们使用了一个自定义的 `LagouPipeline` 类来处理爬取到的数据，将数据存储到 MySQL 数据库中。

### 2. items.py

`items.py` 定义了爬虫所要爬取的数据结构，它类似于一个数据库表的结构定义。在本项目中，定义了一个 `JobItem` 类来表示拉勾网招聘信息中的一个职位信息。这个类包括了职位名称、公司名称、职位要求等属性。

### 3. lagou_spider.py

`lagou_spider.py` 定义了一个 Scrapy 爬虫类，该类继承了 `scrapy.Spider` 类，并定义了爬虫的名称、起始 URL 和爬取的数据处理方法等。在本项目中，定义了一个名为 `LagouSpider` 的类来爬取拉勾网招聘信息。在 `parse` 方法中，首先从爬取到的网页中解析出每个职位信息的 URL，然后再对每个 URL 发起请求，爬取职位信息。最后，将职位信息存储到 MySQL 数据库中。

### 4. pipelines.py

`pipelines.py` 定义了数据处理的类。在本项目中，定义了一个名为 `LagouPipeline` 的类，它继承了 `scrapy.ItemPipeline` 类，并重写了其中的 `process_item` 方法。在 `process_item` 方法中，将爬取到的职位信息存储到 MySQL 数据库中。

### 5. main.py

`main.py` 是本项目的入口文件。在 `main` 函数中，我首先创建了一个 `CrawlerProcess` 对象，然后将 `LagouSpider` 添加到该对象中。最后，调用 `CrawlerProcess` 的 `start` 方法启动爬虫。

## 总结

通过本项目，了解了 Scrapy 爬虫的基本流程，并学会了如何使用 Scrapy 爬取拉勾网招聘信息。
