# CET-6 大学英语六级全流程全真备考研习套件 🎓

<div align="center">

**大学英语六级历年真题研习平台 · 听力 / 阅读 / 词汇全套离线自适应学习系统**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)]()
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)]()
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)]()

</div>

---

## 🌟 核心平台一览

本仓库包含一套完整的大学英语六级（CET-6）全真备考平台，所有 HTML 页面均为**纯前端单页应用（SPA）**，双击即可直接在浏览器中打开，**完全离线可用，无需配置复杂服务器环境**。

### 1. 🎧 六级听力真题全真研习平台 (`cet6_listening_platform.html`)
> 副本文件：`六级听力真题研习平台.html`

- **27 套官方全真试题全覆盖（2019 – 2025 年）**：
  - 收录 2019 年 6 月至 2025 年 6 月共计 27 套真题、675 道原题，包含 Section A 长对话、Section B 听力篇章、Section C 讲座/讲话。
- **27 套官方原版高清完整音频**：
  - 音频文件统一存放于 `audio/` 目录，单套时长约 27~28 分钟。
- **边听边看 · 听读双分栏交互**：
  - **左侧原文**：逐段对齐中英双语听力原文，每句均配备 `▶ 播放此处` 时间戳按钮，点击即可直接跳转至音频对应秒数开播！
  - **随音滚动（Auto-Scroll）**：播放时实时侦测音频进度，正在朗读的段落自动高亮并平滑居中滚动。
  - **双向考点穿梭**：题目一键定位原文出处句子；原文高亮线索标签（如 `Q1 答案出处`）一键联动聚焦右侧对应题目。
- **官方 710 分制听力加权折算**：
  - 精确遵循全国大学英语四六级考试委员会官方加权模型：Section A（8题×7.1分）、Section B（7题×7.1分）、**Section C（10题×14.2分 · 双倍权重）**，总分 248.5 分。
  - 自动输出学情诊断与战力评级，支持「错题专项强化重练」。
- **内嵌 13,796 词离线英汉字典**：
  - 点击原文或选项中任意单词，即可呼出音标、词义与 Web Speech API 真人发音。
- **专业听力控制台**：
  - AB 循环精听（Set A / Set B 反复磨耳朵）、0.75x~1.5x 倍速调节、分段秒级跳转、全键盘快捷键（Space 播放/暂停，J/L 快退快进）。

---

### 2. 📖 六级阅读真题全真研习平台 (`cet6_reading_platform.html`)
- **历年真题深度特训**：
  - 全面覆盖 Section A 选词填空、Section B 长篇匹配、Section C 仔细阅读。
- **左右分屏阅读器**：
  - 双屏分栏、纯阅读模式、纯做题模式自由切换。
  - 选词填空自动回填清除与词性角标、仔细阅读段落定位金光动效。
- **全文逐段中英双语解析与生词高亮**。

---

### 3. 🔤 六级核心词汇背诵助手 (`index.html` / `词汇背诵.html`)
- **2220 / 3996 词核心大词库**：
  - 基于艾宾浩斯遗忘曲线的每日抽词与智能复习提醒。
  - 拼写测试与选义测试挑战，生词本与已斩词库管理。

---

## 📂 目录结构说明

```plaintext
├── audio/                          # 2019-2025年 27套官方六级听力原版真题音频 (mp3)
│   ├── cet6_2019_06_1.mp3
│   ├── cet6_2024_12_1.mp3
│   └── ...
├── cet6_listening_platform.html    # 六级听力全真研习平台 (边听边看双分栏)
├── 六级听力真题研习平台.html       # 听力平台中文快捷副本
├── cet6_reading_platform.html      # 六级阅读全真研习平台
├── index.html                      # 六级核心词汇背诵助手
├── comprehensive_cet6_dict.json    # 13,796词核心英汉字典数据
├── cet6_listening_transcripts.json # 27套听力真题中英双语结构化原文
├── build_listening_platform.py     # 听力平台生成与构建脚本
├── build_enhanced_platform.py      # 阅读平台生成与构建脚本
└── README.md                       # 项目说明文档
```

---

## 🚀 快速使用

1. **直接打开**：
   - 听力练习：双击 `cet6_listening_platform.html` 或 `六级听力真题研习平台.html`。
   - 阅读练习：双击 `cet6_reading_platform.html`。
   - 单词复习：双击 `index.html`。
2. **无需安装任何环境**，在 Chrome、Edge、Firefox、Safari 等现代浏览器中即可完美运行。

---

## 📄 开源许可

本项目遵循 [MIT License](LICENSE) 开源许可协议。
