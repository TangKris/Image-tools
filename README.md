# 图片处理工具 v2.1

一个功能强大的图片处理工具，支持图片识别、转换、优化等多种操作。

## 项目简介
该工具旨在为用户提供一个简单易用的界面，用于处理各种图片相关任务，包括但不限于文字识别、图片格式转换、图片优化等。它特别适合需要快速处理大量图片的用户，如设计师、开发者和普通办公人员。

## 功能特性
### 图片识别
- 支持从图片或 PDF 文件中提取文字。
- 支持发票自动识别，快速提取发票关键信息（如发票号码、开票日期等）。
- 提供多种优化选项，提升识别准确率。

### 图片转换
- 支持将 PDF 转换为图片（PNG、JPG、TIFF）。
- 支持将图片转换为 PDF。
- 支持将 TXT 文件转换为 PDF。
- 支持合并多张图片为一个 PDF 文件。

### 图片优化
- 提供多种优化选项，包括去噪、锐化、亮度调整、对比度调整等。
- 支持实时预览优化效果。

### 其他功能
- 支持多语言界面（简体中文、英语）。
- 提供详细的更新日志和版本信息。
- 支持检查更新功能，方便用户获取最新版本。

## 使用方法
### 使用界面操作
- **图片识别**：选择图片或 PDF 文件，设置优化选项，点击“开始识别”。
- **图片转换**：选择转换类型，添加文件，点击“开始转换”。
- **图片优化**：选择图片，调整优化参数，点击“保存结果”。
- **设置**：调整语言、主题、CPU 使用率阈值等设置。

## 更新日志
### v2.1
- 新增多方面识别优化设置。
- 提升初始化速度。
- 增强发票识别用户体验。

### v2.0
- 大幅度美化 UI，提升用户体验。
- 提升加载速度。
- 新增风格切换功能。
- 支持兼容 Win7/10/11、MacOS、Linux 系统。

### v1.9
- 大幅度提升程序启动速度。
- 完善发票记录功能。
- 修复语言翻译缺陷。

### v1.8
- 修复已知 bug，删除部分组件。
- 新增发票记录功能，支持清除记录。
- 支持永久保存语言。

### v1.7
- 修复已知 bug。
- 完善语言切换功能。
- 新增图片编辑功能，实现图片缩放、裁剪功能。
- 添加确认修改按钮。

### v1.6
- 修复已知 bug。
- 新增语言切换功能。
- 大幅优化性能。

### v1.5
- 优化图片功能增强，实时预览修改结果和数值。
- 新增“检查更新”功能，快捷更新新版本。
- 更新日志、选项卡优化。

### v1.4
- 程序窗口图标换新。
- 完善“关于”显示内容。
- 新增“优化图片”选项卡，支持调节锐化、对比度、亮度等参数。

### v1.3
- 新增发票自动识别功能。
- 快速获取发票键值（发票号码等），实现初步判断真伪。
- 识别图片支持图片实时预览。

### v1.2
- 新增一键复制功能。
- 新增一键清空文本功能。
- 新增“转换与合并”功能，支持 PDF 转多种图片、多张图片转 PDF、TXT 转 PDF、PDF 合并等功能。
- 程序图标换新。

### v1.1
- 实现 PaddleOCR 识别。
- 新增创建 Excel 并写入指定单元格功能。
- 无需用户手动安装 OCR 库。

### v1.0
- 实现基础 PaddleOCR 识别功能。
- 新增创建 Excel 写入功能。

## 项目结构
Image-tools/
├── Image-tools_v2.1.py  # 主程序文件
├── models/              # 模型文件
├── paddleocr/           # PaddleOCR 相关文件
├── t1.ico               # 程序图标
├── pyinstaller.txt      # PyInstaller 配置文件
└── pyinstaller.txt   # 安装依赖库
└── README.md            # 项目说明文档

## 依赖项
- Python 3.10+
- PaddleOCR
- OpenCV
- PyMuPDF
- ttkbootstrap
- reportlab
- openpyxl
- requests

## 贡献指南
欢迎贡献代码！请遵循以下步骤：
1. **Fork** 本仓库到你的 GitHub 账户。
2. 创建一个新的分支：\`git checkout -b feature/your-feature-name\`。
3. 提交你的更改：\`git commit -m "Add some feature"\`。
4. 推送到你的分支：\`git push origin feature/your-feature-name\`。
5. 提交一个 Pull Request。

## 许可证
本项目采用 [MIT License](LICENSE) 许可证。

## 联系方式
开发者：TangKris (小汤)  
邮箱：[3398458131@qq.com]  
GitHub：[https://github.com/TangKris](https://github.com/TangKris)
