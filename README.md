# Danbooru-Tag-Selector

## 界面预览

![](https://github.com/Fre2C/Danbooru-Tag-Selector/blob/main/preview/801fd5294d4a.png)  
![](https://github.com/Fre2C/Danbooru-Tag-Selector/blob/main/preview/af83592faab7.png)

## 功能概览

### 数据加载

- 支持 **CSV** 和 **JSON** 两种格式的文件导入（拖拽或点击上传）
- 内置多种编码选项：UTF-8、GBK、GB2312、GB18030、Big5、Shift_JIS、EUC-KR、ISO-8859-1、Windows-1252
- 自动检测文件格式，JSON 支持对象数组嵌套结构

### 筛选与搜索

- **多条件过滤器**：支持"包含"、"等于"、"不等于"、"大于"、"小于"五种运算符
- 可按列筛选，支持添加/删除/禁用/折叠筛选行
- **全局关键字搜索**：跨所有列进行模糊匹配
- 列值浏览面板：当枚举值过多（>500）时给予警告提示
- 一键全部禁用/启用所有筛选条件

### 随机抽取

- 可指定抽取数量，支持 +/- 按钮调节和鼠标滚轮
- **空格键快捷键**触发随机抽取
- 支持"避免重复"模式：历史记录中的标签将被排除
- 抽取结果可批量添加到候选列表、下载为 Markdown 或复制到剪贴板

### 浏览器 / 表格视图

- 分页浏览全部数据，支持 10 / 25 / 50 / 100 每页
- **列排序**：点击表头按升序/降序排列，支持数值和文本排序
- **列宽拖拽调整**：拖动表头边缘自适应调整列宽
- **列拖拽排序**：拖动表头重新排列列顺序
- **列可见性控制**：自由显示/隐藏指定列
- 支持页码跳转和分页导航

### 候选列表

- 从随机结果、浏览器视图、历史记录中**拖拽添加**标签到候选列表
- 候选列表支持**拖拽排序**
- 自定义候选列表的标题列和附加信息列
- 支持三种复制格式：逗号分隔、空格分隔、换行分隔
- 候选面板宽度可拖拽调整（范围 180px–600px）
- 已加入候选的标签在各视图中有高亮标识

### 历史记录

- 自动记录每次抽取结果，**使用 IndexedDB 持久化存储**（上限 2000 条）
- 支持展开/折叠历史列表，可自定义显示的附加列
- 历史记录支持**导入/导出**（JSON 格式，导入上限 5000 条）
- 可从历史记录直接查看详情或添加到候选列表
- 可单独删除或清空全部历史记录
- 提供"是否记录历史"和"避免重复"开关

### 自定义模板

- **显示模板**：自定义随机结果卡片的 Markdown 渲染格式
- **保存模板**：自定义下载 Markdown 文件的格式
- 使用 `{{列名}}` 插入列值，`{{列名:enc}}` 插入 URL 编码值
- 点击列名芯片快速插入模板变量

### URL 与链接

- 可自定义 Wiki URL 模板（默认 `https://danbooru.donmai.us/wiki_pages/{value}`）
- 可指定用于生成链接的列
- 浏览器视图和候选列表中的标签名可直接跳转到对应 Wiki 页面

### 主题与外观

- **深色 / 浅色**双主题切换，带平滑过渡动画

### 设置导入/导出

- 可将所有设置（URL 模板、列选择、模板内容、筛选器状态、列顺序/宽度/可见性、候选面板宽度等）导出为 JSON
- 支持从 JSON 文件导入设置，实现跨设备/跨浏览器配置同步

## 使用方法

1. 直接在浏览器中打开 `Danbooru-Selector.html` 文件
2. 上传 CSV 或 JSON 格式的数据文件（可提前选择编码）
3. 使用筛选器和搜索栏缩小数据范围
4. 通过"随机抽取"或"浏览"标签页选取标签
5. 将选中的标签添加到候选列表
6. 复制或导出候选列表

## 数据集

- 本工具默认使用[SuzumiyaAkizuki](https://github.com/SuzumiyaAkizuki)的[DanbooruSearchOnline](https://github.com/SuzumiyaAkizuki/DanbooruSearchOnline)项目的[数据](https://github.com/SuzumiyaAkizuki/DanbooruSearchOnline/blob/main/origin_database/tags_enhanced.csv)
- 可以通过data_tool文件夹中的脚本，对[DanbooruSearchEmbedding](https://huggingface.co/buckets/SAkizuki/DanbooruSearchEmbedding/tree/origin_database)中的tag_groups.json和tags_enhanced.csv文件进行合并后在当前版本中使用

## 路线图

- [ ] 优化tag_groups的筛选及其他体验
- [ ] 用比网页对话更正常一点的方式把文件规范地重构一下
- [ ] 增加完善的标签收藏功能（更新至1.0.0）

## 版本历史

### v0.6.0
2026.5.10
第一个功能完善版本
