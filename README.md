# Scrapy-on-Lagou

这个GitHub仓库是一个使用Scrapy框架从拉勾网爬取数据的项目。以下是该项目的代码逻辑的概览：

首先，lagou文件夹包含了Scrapy项目的一些配置信息和必要的文件，如settings.py和middlewares.py。其中middlewares.py文件包含了一些自定义的中间件，用于处理请求和响应。

接下来，在spiders文件夹中，有两个爬虫文件，分别是lagou.py和lagou_jobs.py。这些文件定义了从拉勾网爬取数据的方式和规则。其中，lagou.py爬取公司的信息，lagou_jobs.py爬取职位的信息。
爬虫文件中定义了一些回调函数，用于处理从拉勾网返回的响应。这些函数包括parse、parse_company和parse_job，它们分别用于处理公司、职位和页面信息。

在items.py文件中定义了需要爬取的数据的结构和字段。

最后，在pipelines.py文件中定义了数据的处理和存储方式。其中，LagouPipeline类定义了数据如何被处理和存储，包括去重、数据清洗和存储到CSV文件中。
总的来说，通过使用Scrapy框架和自定义的中间件、回调函数和管道，可以方便地从拉勾网爬取数据并进行处理和存储。
