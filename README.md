# Danbooru-Tag-Selector

一个纯前端 Danbooru 标签浏览、筛选、随机抽取与候选收集工具。双击 HTML 文件即可使用，无需安装任何依赖。

## 界面预览

![](https://github.com/Fre2C/Danbooru-Tag-Selector/blob/main/preview/dada404291ae.png)
![](https://github.com/Fre2C/Danbooru-Tag-Selector/blob/main/preview/7a22e0d6a04c.png)

---

## 功能概览

### 数据加载
- 拖放或点击上传 **CSV** / **JSON** 文件
- **自动检测文件编码**（UTF-8 / GBK / GB18030 / Shift_JIS / Big5 等）
- JSON 支持嵌套对象数组结构

### 筛选与搜索
- **多条件筛选**：支持 `包含` / `等于` / `不等于` / `大于` / `小于` / `无内容` / `有内容` 七种运算符
- **行间 AND/OR 逻辑切换**：点击筛选行首的 `AND`/`OR` 按钮切换逻辑关系
- **输入防抖**：200ms 延迟触发过滤，减少无效计算
- **全局关键字搜索**：跨所有列模糊匹配
- **列值浏览面板**：快速选取列枚举值
- **筛选预设保存/加载**：一键保存常用筛选组合
- 筛选行支持添加、删除、禁用、折叠、全部禁用/启用

### 随机抽取
- 可指定抽取数量，支持 +/- 按钮和鼠标滚轮调节
- **空格键**触发快速抽取
- "避免重复"模式：已抽取过的标签不再出现
- 抽取结果可**拖拽**添加到候选列表
- 结果卡片支持下载 MD、查看原始数据

### 浏览器 / 表格视图
- 分页浏览（10 / 25 / 50 / 100 每页）
- **列排序**：点击表头升降序
- **列宽拖拽调整** + **列顺序拖拽重排**
- 列可见性控制
- **右键菜单**：添加到候选 / 按此值筛选
- 页码跳转

### 候选列表
- 从随机结果、浏览器视图、历史记录**拖拽添加**
- 拖拽排序
- 自定义标题列和附加信息列
- 三种复制格式：逗号 / 空格 / 换行分隔
- 面板宽度可拖拽调整

### 历史记录
- 自动记录抽取结果，**IndexedDB 持久化**
- 展开/折叠、导入/导出（JSON）
- 点击查看详情（含下载 MD、原始数据）
- 记录/去重开关

### 自定义模板
- **显示模板** / **保存模板**：用 `{{列名}}` 语法自定义 Markdown 渲染格式
- `{{列名:enc}}` 插入 URL 编码值

### 主题
- 深色/亮色主题
- 平滑过渡动画

### 设置导入/导出
- 导出内容：URL 模板、链接列、候选标题列、模板、筛选条件、列设置、面板宽度等
- 从 JSON 导入恢复配置

### 响应式
- 适配 1100px / 900px / 600px 三档断点
- 移动端筛选行纵向排列，按钮适配触摸

---

## 使用方法

1. 在浏览器中打开 `Danbooru-Tag-Selector.html`
2. 上传 CSV / JSON 数据文件（编码自动检测）
3. 使用筛选器 + 搜索缩小范围
4. 在「随机抽取」或「内容浏览」标签页中选取标签
5. 拖拽或右键添加到候选列表
6. 复制候选列表

---

## 数据集

- 本工具默认使用[SuzumiyaAkizuki](https://github.com/SuzumiyaAkizuki)的[DanbooruSearchOnline](https://github.com/SuzumiyaAkizuki/DanbooruSearchOnline)项目的[数据](https://github.com/SuzumiyaAkizuki/DanbooruSearchOnline/blob/main/origin_database/tags_enhanced.csv)
- 也可以通过data_tool文件夹中的脚本，对[DanbooruSearchEmbedding](https://huggingface.co/buckets/SAkizuki/DanbooruSearchEmbedding/tree/origin_database)中的tag_groups.json和tags_enhanced.csv文件进行合并后使用

---

## 路线图

- [x] 优化tag_groups的筛选及其他体验
- [x] 用比网页对话更正常一点的方式把文件规范地重构一下
- [ ] 完善 Tag 收藏功能（v1.0）

---

## 版本历史

### v0.7.0 — 2026.5.13
- 明暗主题配色修改
- 筛选条件新增 AND/OR 切换、输入防抖、预设保存/加载
- 新增「无内容」「有内容」操作符
- 全局搜索合并到筛选循环
- 浏览表格右键菜单支持「按此值筛选」
- 候选区域拖放时不再导致浏览区闪烁
- 自定义下拉组件替代原生 select（消除展开闪烁）
- 编码自动检测（无需手动选择）
- 响应式适配三档断点  

- 已知筛选条件的「选值」中，值的出现次数显示不正确

### v0.6.0 — 2026.5.10
- 第一个功能完善版本

---

## License

MIT