# -*- coding: utf-8 -*-
"""
CET-6 45-Day Study Checklist Builder
Generates an interactive, beautiful HTML checklist application.
"""
import json
import datetime

def generate():
    start_date = datetime.date(2026, 10, 30)
    weekdays_cn = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

    # 45 days curated task data tailored for 429-score candidates
    tasks_schedule = [
        # Phase 1: Days 1-18
        {
            "day": 1,
            "vocab": "背诵 List 01 + List 02 (100词) · 开启「自动发音」跟读",
            "reading": "精做并精读 2021.06 仔细阅读 Passage 1 (画出主谓宾与长难句)",
            "listening": "盲听 2021.06 长对话 1 录音两遍，看原文对照连读弱读"
        },
        {
            "day": 2,
            "vocab": "背诵 List 03 + List 04 (100词) + 复习 Day 1 模糊生词",
            "reading": "精做并精读 2021.06 仔细阅读 Passage 2 (积累定位词与同义替换)",
            "listening": "盲听 2021.06 长对话 2 录音并尝试中文口头复述大意"
        },
        {
            "day": 3,
            "vocab": "背诵 List 05 + List 06 (100词) · 单词助手四选一自测20题",
            "reading": "精做 2021.12 仔细阅读 Passage 1 (运用「题文同序」技巧找段落)",
            "listening": "听力篇章 Passage 1 盲听练习，标注生词发音"
        },
        {
            "day": 4,
            "vocab": "背诵 List 07 + List 08 (100词) + 艾宾浩斯复盘 List 01-04 错词",
            "reading": "精做 2021.12 仔细阅读 Passage 2 (分析错题干扰项特征)",
            "listening": "盲听 2021.12 长对话 1，抓因果/转折信号词 (because, however)"
        },
        {
            "day": 5,
            "vocab": "背诵 List 09 + List 10 (100词) + 生词本加星巩固",
            "reading": "周末复盘：重读前4天仔细阅读的错题句与高频考点词",
            "listening": "写作破冰：背诵并默写 3 种引出社会现象的通用开头句"
        },
        {
            "day": 6,
            "vocab": "背诵 List 11 + List 12 (100词) · 注意动词固定搭配",
            "reading": "精做 2022.06 仔细阅读 Passage 1 (限时 12 分钟完成)",
            "listening": "盲听 2022.06 长对话 1 录音并跟读模仿语音语调"
        },
        {
            "day": 7,
            "vocab": "背诵 List 13 + List 14 (100词) + 单词遮挡模式速刷",
            "reading": "精做 2022.06 仔细阅读 Passage 2 (提炼每段首尾主题句)",
            "listening": "盲听 2022.06 长对话 2，练习在听到答案时做笔记简写"
        },
        {
            "day": 8,
            "vocab": "背诵 List 15 + List 16 (100词) + 艾宾浩斯复习前一周生词",
            "reading": "精做 2022.12 仔细阅读 Passage 1 (限时 12 分钟)",
            "listening": "听力篇章 2022.06 Passage 1 听写关键实词训练"
        },
        {
            "day": 9,
            "vocab": "背诵 List 17 + List 18 (100词) · 拼写自测 20 题",
            "reading": "精做 2022.12 仔细阅读 Passage 2 (梳理因果论证逻辑)",
            "listening": "盲听 2022.12 长对话 1，抓问答句中的核心回答点"
        },
        {
            "day": 10,
            "vocab": "背诵 List 19 + List 20 (100词) · 词汇量正式突破 1000 大关！",
            "reading": "精做 2023.03 仔细阅读 Passage 1 (严控时间 11 分钟)",
            "listening": "盲听 2022.12 长对话 2 两次，对照录音原文标出没听懂的短语"
        },
        {
            "day": 11,
            "vocab": "背诵 List 21 + List 22 (100词) + 清理生词本已掌握词汇",
            "reading": "翻译破冰：练习 1 篇传统文化主题短译（中国茶文化/传统节日）",
            "listening": "写作加练：积累并默写 3 个表达「积极作用」的高级短语"
        },
        {
            "day": 12,
            "vocab": "背诵 List 23 + List 24 (100词) · 听音辨义练习",
            "reading": "精做 2023.03 仔细阅读 Passage 2 (重点攻坚细节推断题)",
            "listening": "盲听 2023.03 长对话 1，练习听前预判选项核心主语"
        },
        {
            "day": 13,
            "vocab": "背诵 List 25 + List 26 (100词) + 强化四选一测试 30 题",
            "reading": "精做 2023.06 仔细阅读 Passage 1 (限时 11 分钟)",
            "listening": "盲听 2023.03 长对话 2，边听边在选项上打勾标记"
        },
        {
            "day": 14,
            "vocab": "背诵 List 27 + List 28 (100词) · 熟练区分常考近义词",
            "reading": "精做 2023.06 仔细阅读 Passage 2 (分析作者态度题词汇)",
            "listening": "盲听 2023.06 长对话 1 录音并排查连读失爆"
        },
        {
            "day": 15,
            "vocab": "背诵 List 29 + List 30 (100词) + 半月复盘：生词本大扫除",
            "reading": "整理仔细阅读已做真题中出现的 20 个高频同义替换词对",
            "listening": "盲听 2023.06 长对话 2，重点攻坚疑问句与转折句"
        },
        {
            "day": 16,
            "vocab": "背诵 List 31 + List 32 (100词) · 单词卡片评分复习",
            "reading": "精做 2023.12 仔细阅读 Passage 1 (两篇合并限时 24 分钟)",
            "listening": "盲听 2023.12 长对话 1，抓首尾句和场景词汇"
        },
        {
            "day": 17,
            "vocab": "背诵 List 33 + List 34 (100词) + 强化生词复习",
            "reading": "精做 2023.12 仔细阅读 Passage 2 (分析论证例证题的作用)",
            "listening": "盲听 2023.12 长对话 2，检验「视听一致」做题命中率"
        },
        {
            "day": 18,
            "vocab": "背诵 List 35 ~ 45 剩余冲刺词汇 · 🎉 2220 核心词第一轮全部通关！",
            "reading": "第一阶段成就总结：回顾已做的 12 篇仔细阅读错题本",
            "listening": "自我激励：第一阶段圆满结束，今晚犒劳一下自己，准备进入题型攻坚！"
        },

        # Phase 2: Days 19-32
        {
            "day": 19,
            "vocab": "遮中文模式刷 List 01-04 (200词) · 极速主动提取测试",
            "reading": "长篇匹配专项突破：精做 2021.06 长篇匹配 (先题干画2个核心词再扫读)",
            "listening": "听力长对话专项：连续听 3 套长对话，只抓题目定位词"
        },
        {
            "day": 20,
            "vocab": "遮中文模式刷 List 05-08 (200词) · 忘啦词进生词本",
            "reading": "精做 2021.12 长篇匹配 (严格控时 18 分钟以内完成)",
            "listening": "讲座听力 (Section C) 破冰：精听 1 篇讲座，抓第一句主题主旨"
        },
        {
            "day": 21,
            "vocab": "遮中文模式刷 List 09-12 (200词) + 四选一 30 题",
            "reading": "精做 2022.06 长篇匹配 (控时 16 分钟，争取对 8 题以上)",
            "listening": "写作专项：掌握主体论证段 3 种展开法（因果链、举例、正反对比）"
        },
        {
            "day": 22,
            "vocab": "遮中文模式刷 List 13-16 (200词) · 巩固重难点词汇",
            "reading": "精做 2022.12 长篇匹配 (总结同义替换模式：词性变换/近义归纳)",
            "listening": "讲座听力：精听 2021.12 Section C 第1篇，关注转折/建议信号词"
        },
        {
            "day": 23,
            "vocab": "遮中文模式刷 List 17-20 (200词) + 拼写强化默写",
            "reading": "仔细阅读综合提速：两篇合并限时 22 分钟实战训练",
            "listening": "翻译专项：练习科技创新主题翻译 1 篇（主谓宾拆解法）"
        },
        {
            "day": 24,
            "vocab": "遮中文模式刷 List 21-24 (200词) · 扫清模糊词",
            "reading": "精做 2023.03 长篇匹配 (限时 15 分钟，目标 9 题以上)",
            "listening": "听力整套演练：2023.03 听力整套不暂停限时播放，实测摸底得分"
        },
        {
            "day": 25,
            "vocab": "遮中文模式刷 List 25-28 (200词) + 专项四选一 50 题",
            "reading": "周末错题特训：把近 5 套长篇匹配中找错段落的题干重新定位一次",
            "listening": "分析听力错题：统计是「没听到」、「听到不认识」还是「选项掉坑」"
        },
        {
            "day": 26,
            "vocab": "遮中文模式刷 List 29-32 (200词) · 保持单词熟练度",
            "reading": "精做 2023.06 长篇匹配 (稳扎稳打，优先找数字、专有名词定位)",
            "listening": "写作专项：背诵并默写结尾段总结呼应与提出建议的黄金模板"
        },
        {
            "day": 27,
            "vocab": "遮中文模式刷 List 33-36 (200词) · 重点背诵高频名词",
            "reading": "选词填空破局策略：学习「先标词性再填空」，严格限制只花 7 分钟",
            "listening": "听力整套演练：2023.06 听力全套限时模拟，严格涂卡时间"
        },
        {
            "day": 28,
            "vocab": "遮中文模式刷 List 37-40 (200词) · 考点搭配巩固",
            "reading": "精做 2023.12 长篇匹配 (限时 15 分钟，力争全对)",
            "listening": "翻译通识积累：抄写并记忆 20 个中国传统文化常考词汇"
        },
        {
            "day": 29,
            "vocab": "遮中文模式刷 List 41-45 · 🎉 全库 2220 词第二轮复习大功告成！",
            "reading": "仔细阅读极限冲刺：2023.12 仔细阅读两篇限时 20 分钟完成",
            "listening": "听力演练：2023.12 听力全套限时实测，检验视听一致应用"
        },
        {
            "day": 30,
            "vocab": "集中攻坚生词本：把打了星标 (★) 的所有生词过两遍",
            "reading": "完整写作手写实战：拿出一张白纸，限时 25 分钟手写 1 篇真题大作文",
            "listening": "对照范文批改作文：检查有无第三人称单数、时态、单复数低级错误"
        },
        {
            "day": 31,
            "vocab": "HTML 助手四选一自测 40 题 · 维持词义敏锐直觉",
            "reading": "选词填空专项演练 1 套：严格限时 7 分钟，不会的果断选一个就走",
            "listening": "翻译手写实战：限时 25 分钟手写 1 篇社会发展类真题翻译"
        },
        {
            "day": 32,
            "vocab": "拼写听写默写测试 30 题 · 避免考场提笔忘字",
            "reading": "梳理个人《六级做题黄金顺序与时间表》，牢记先做长篇与仔细阅读！",
            "listening": "听力保温：盲听 1 套熟悉录音，重点体会出题句前后的语音语调停顿"
        },

        # Phase 3: Days 33-41
        {
            "day": 33,
            "vocab": "高频核心词速过 List 01-15 · 查漏补缺",
            "reading": "🔥 【全真模考 1】：2024.06 卷一，严格限时下午 15:00-17:25 全套实测！",
            "listening": "严格遵守考试纪律，不喝水不起身，完全模拟考场高压环境"
        },
        {
            "day": 34,
            "vocab": "录入模考 1 试卷中所有看不懂的生词到生词本",
            "reading": "深度复盘模考 1 阅读部分：逐题标记为什么错，分析是定位偏还是理解错",
            "listening": "深度复盘模考 1 听力部分：重听错题录音至少 3 遍，直到完全听懂"
        },
        {
            "day": 35,
            "vocab": "生词本专项特训：消灭 50 个顽固生词",
            "reading": "写作模板强化：默写 1 套自定专属议论文框架，固定开头与结尾",
            "listening": "翻译复盘：把模考 1 的翻译对照参考答案改写，学习简单句合并技巧"
        },
        {
            "day": 36,
            "vocab": "高频核心词速过 List 16-30 · 保持词感",
            "reading": "🔥 【全真模考 2】：2024.06 卷二，严格限时下午 15:00-17:25 全套模拟！",
            "listening": "检验做题顺序：作文(30m)→听力(30m)→长篇匹配(15m)→仔细阅读(22m)→翻译(23m)→选词填空(5m)"
        },
        {
            "day": 37,
            "vocab": "复盘模考 2 生词并用 HTML 助手测试",
            "reading": "深度复盘模考 2：核算总得分，对比底线目标（听力145+，阅读160+）",
            "listening": "精析听力 Section C：总结讲座听力常考题型（定义解释题、实验结果题）"
        },
        {
            "day": 38,
            "vocab": "高频核心词速过 List 31-45 · 消除死角",
            "reading": "翻译热词突击：熟记生态环保、高质量发展、文化遗产等 25 个热词",
            "listening": "写作金句背诵：熟记 5 个能立刻提升作文档次的连接副词与插入语"
        },
        {
            "day": 39,
            "vocab": "生词本快速循环翻阅 · 聚焦高频难词",
            "reading": "🔥 【全真模考 3 (终极决战)】：2024.12 最新真题，下午 15:00-17:25 严格实测！",
            "listening": "最后一次全真套卷大考，拿出最佳精神状态，争取总分冲破 450 分！"
        },
        {
            "day": 40,
            "vocab": "将模考 3 试卷生词彻底查清并记忆",
            "reading": "深度复盘模考 3：核对每个模块失分点，调整最后 5 天的抢分重心",
            "listening": "听力录音精琢：反复听这套真题中自己做对和做错的全部长对话"
        },
        {
            "day": 41,
            "vocab": "生词本集中清理：将已完全熟练掌握的生词移出生词本",
            "reading": "考前写作终极定型：把最顺手的 2 套模板默写在笔记本上，一字不差！",
            "listening": "翻译保命准则回顾：遇难词果断同义降级，宁写正确简单句，不写错病长句"
        },

        # Phase 4: Days 42-45
        {
            "day": 42,
            "vocab": "打开 HTML 单词助手中的「⭐ 生词错题本」，一键发起最后特训",
            "reading": "错题大巡礼：翻阅之前所有真题卷子的仔细阅读错题，复习定位技巧",
            "listening": "听力错题浏览：重温听力中常考的同义替换表达和转折陷阱"
        },
        {
            "day": 43,
            "vocab": "不再死记硬背新词，轻松翻看高频核心词，闭目回想作文框架结构与核心过渡词",
            "reading": "考场物资准备清单清点：身份证、准考证、2B铅笔、橡皮、黑色签字笔、收音机/耳机及备用电池；确认考场路线",
            "listening": "今晚 22:30 前准时上床睡觉，养精蓄锐，牢记答题顺序与各题型时间分配底线！"
        },
        {
            "day": 44,
            "vocab": "清晨热身：口头轻声朗读 1 篇作文模板与高级替换词，唤醒英语语感，禁止再刷难题",
            "reading": "12月12日 六级统考日！下午 14:40 前从容入场！长篇匹配圈定位词，仔细阅读稳准狠",
            "listening": "听力视听一致抢分！放平心态，429底子逆袭425+就在今天，落笔生花，六级必过！🏆"
        },
        {
            "day": 45,
            "vocab": "考后复盘与荣耀通关：回顾45天从429底子到胸有成竹的蜕变历程",
            "reading": "对答案估分与总结：记录自己在真题做题中的定位与时间管理得失",
            "listening": "听力与口语进阶：保持英语听音习惯，开启寒假进阶与未来学术深造新篇章！🎉"
        }
    ]

    # Combine with date info
    full_schedule = []
    for item in tasks_schedule:
        idx = item['day'] - 1
        d = start_date + datetime.timedelta(days=idx)
        phase_num = 1 if item['day'] <= 18 else (2 if item['day'] <= 32 else (3 if item['day'] <= 41 else 4))
        phase_names = {
            1: "阶段一 · 词汇筑基与真题破冰",
            2: "阶段二 · 题型击破与专项提分",
            3: "阶段三 · 真题套卷模考与写作翻译",
            4: "阶段四 · 错题清零与考前状态冲刺"
        }
        full_schedule.append({
            "day": item['day'],
            "date": f"{d.month}月{d.day}日",
            "weekday": weekdays_cn[d.weekday()],
            "isoDate": d.isoformat(),
            "phase": phase_num,
            "phaseName": phase_names[phase_num],
            "vocab": item['vocab'],
            "reading": item['reading'],
            "listening": item['listening']
        })

    json_data = json.dumps(full_schedule, ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CET-6 45天通关打卡清单 · 429逆袭425+专属计划</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%234f46e5'><path d='M9 11l3 3L22 4M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11'/></svg>">
  <style>
    :root {{
      --bg-app: #f8fafc;
      --bg-card: #ffffff;
      --bg-card-subtle: #f1f5f9;
      --bg-card-hover: #fcfdfe;
      --border: #e2e8f0;
      --border-focus: #6366f1;
      --text-main: #0f172a;
      --text-sub: #475569;
      --text-muted: #94a3b8;
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-subtle: #eef2ff;
      --success: #10b981;
      --success-subtle: #ecfdf5;
      --warning: #f59e0b;
      --warning-subtle: #fffbeb;
      --danger: #ef4444;
      --danger-subtle: #fef2f2;
      --phase1: #3b82f6;
      --phase2: #8b5cf6;
      --phase3: #f59e0b;
      --phase4: #10b981;
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-full: 9999px;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.03);
      --transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    [data-theme="dark"] {{
      --bg-app: #0b0f19;
      --bg-card: #161e2e;
      --bg-card-subtle: #1e293b;
      --bg-card-hover: #1c2638;
      --border: #273549;
      --border-focus: #818cf8;
      --text-main: #f8fafc;
      --text-sub: #cbd5e1;
      --text-muted: #64748b;
      --primary: #6366f1;
      --primary-hover: #818cf8;
      --primary-subtle: #1e1b4b;
      --success: #10b981;
      --success-subtle: #064e3b;
      --warning: #f59e0b;
      --warning-subtle: #451a03;
      --danger: #f43f5e;
      --danger-subtle: #4c0519;
      --phase1: #60a5fa;
      --phase2: #a78bfa;
      --phase3: #fbbf24;
      --phase4: #34d399;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
      background-color: var(--bg-app);
      color: var(--text-main);
      min-height: 100vh;
      line-height: 1.5;
      transition: background-color 0.25s ease, color 0.25s ease;
      padding-bottom: 60px;
    }}

    .container {{
      max-width: 980px;
      margin: 0 auto;
      padding: 16px 20px;
    }}

    /* Header */
    header.header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 0 20px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 20px;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .brand-box {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .logo-badge {{
      background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
      color: #fff;
      font-weight: 800;
      font-size: 13px;
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
    }}

    .title-main {{
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.3px;
    }}

    .title-sub {{
      font-size: 12px;
      color: var(--text-muted);
      margin-left: 6px;
      font-weight: 500;
    }}

    .header-actions {{
      display: flex;
      gap: 10px;
      align-items: center;
    }}

    .btn {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-sub);
      padding: 8px 14px;
      border-radius: var(--radius-md);
      cursor: pointer;
      font-size: 13px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition);
      text-decoration: none;
    }}

    .btn:hover {{
      background: var(--bg-card-subtle);
      color: var(--text-main);
      border-color: var(--border-focus);
    }}

    .btn-primary {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }}
    .btn-primary:hover {{
      background: var(--primary-hover);
      color: #ffffff;
    }}

    /* Global Stats Card */
    .dashboard-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }}

    .stats-row {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 18px;
    }}

    .stat-item {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .stat-title {{
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .stat-number {{
      font-size: 26px;
      font-weight: 800;
      letter-spacing: -0.5px;
    }}

    .stat-number small {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      margin-left: 2px;
    }}

    .progress-bar-wrap {{
      margin-top: 10px;
    }}

    .progress-label-row {{
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 6px;
    }}

    .progress-track {{
      height: 10px;
      background: var(--bg-card-subtle);
      border-radius: var(--radius-full);
      overflow: hidden;
      display: flex;
    }}

    .progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, #4f46e5, #10b981);
      transition: width 0.4s ease;
      border-radius: var(--radius-full);
    }}

    /* Filter Tabs */
    .filter-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }}

    .phase-tabs {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 4px;
    }}

    .phase-tab-btn {{
      padding: 7px 14px;
      border-radius: var(--radius-full);
      border: 1px solid var(--border);
      background: var(--bg-card);
      font-size: 13px;
      font-weight: 600;
      color: var(--text-sub);
      cursor: pointer;
      white-space: nowrap;
      transition: var(--transition);
    }}

    .phase-tab-btn:hover {{
      color: var(--text-main);
      background: var(--bg-card-subtle);
    }}

    .phase-tab-btn.active {{
      background: var(--primary);
      border-color: var(--primary);
      color: #fff;
      box-shadow: 0 2px 8px rgba(99, 102, 241, 0.25);
    }}

    /* Day Card */
    .day-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px 22px;
      margin-bottom: 16px;
      box-shadow: var(--shadow-sm);
      transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
      position: relative;
    }}

    .day-card:hover {{
      border-color: var(--border-focus);
    }}

    .day-card.today {{
      border: 2px solid var(--primary);
      box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15);
    }}

    .day-card.day-completed {{
      border-color: var(--success);
      background: linear-gradient(to right, rgba(16, 185, 129, 0.03), transparent);
    }}

    .day-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .day-info {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .day-badge {{
      font-size: 16px;
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.3px;
    }}

    .date-tag {{
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .phase-tag {{
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      color: #fff;
    }}
    .phase-tag.p1 {{ background: var(--phase1); }}
    .phase-tag.p2 {{ background: var(--phase2); }}
    .phase-tag.p3 {{ background: var(--phase3); }}
    .phase-tag.p4 {{ background: var(--phase4); }}

    .today-pill {{
      background: var(--danger);
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      animation: pulse 1s infinite alternate;
    }}

    @keyframes pulse {{
      0% {{ transform: scale(0.95); opacity: 0.9; }}
      100% {{ transform: scale(1.05); opacity: 1; }}
    }}

    .day-status-pill {{
      font-size: 12px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: var(--radius-full);
      background: var(--bg-card-subtle);
      color: var(--text-muted);
    }}
    .day-completed .day-status-pill {{
      background: var(--success-subtle);
      color: var(--success);
    }}

    /* Tasks List */
    .task-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .task-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 8px 10px;
      border-radius: var(--radius-md);
      transition: background 0.15s ease;
      cursor: pointer;
    }}

    .task-item:hover {{
      background: var(--bg-card-subtle);
    }}

    .task-checkbox {{
      width: 18px;
      height: 18px;
      accent-color: var(--success);
      margin-top: 2px;
      cursor: pointer;
      flex-shrink: 0;
    }}

    .task-content {{
      flex: 1;
      font-size: 14px;
      color: var(--text-main);
      line-height: 1.5;
    }}

    .task-type-badge {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: 4px;
      margin-right: 6px;
      color: #fff;
    }}
    .type-vocab {{ background: #3b82f6; }}
    .type-reading {{ background: #10b981; }}
    .type-listen {{ background: #f59e0b; }}

    .task-item.checked .task-content {{
      color: var(--text-muted);
      text-decoration: line-through;
    }}

    /* Notes section in day card */
    .note-btn {{
      font-size: 12px;
      color: var(--text-muted);
      background: none;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 4px 0;
      margin-top: 8px;
    }}
    .note-btn:hover {{
      color: var(--primary);
    }}

    .note-textarea {{
      width: 100%;
      min-height: 60px;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: var(--bg-card-subtle);
      color: var(--text-main);
      padding: 8px 12px;
      font-size: 13px;
      font-family: inherit;
      outline: none;
      margin-top: 6px;
      display: none;
      resize: vertical;
    }}
    .note-textarea.active {{
      display: block;
    }}

    /* Cheatsheet Modal */
    .modal-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(4px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 100;
      padding: 20px;
    }}
    .modal-overlay.active {{
      display: flex;
    }}

    .modal-body {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      max-width: 680px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 28px;
      box-shadow: var(--shadow-lg);
    }}

    .modal-title-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
    }}

    .guide-box {{
      background: var(--bg-card-subtle);
      border-left: 4px solid var(--primary);
      padding: 12px 16px;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      margin-bottom: 16px;
      font-size: 14px;
      line-height: 1.6;
    }}

    /* Responsive */
    @media (max-width: 768px) {{
      .stats-row {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .day-card {{
        padding: 16px 14px;
      }}
    }}
  </style>
</head>
<body>

  <div class="container">
    <!-- Header -->
    <header class="header">
      <div class="brand-box">
        <span class="logo-badge">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 11l3 3L22 4M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
          CET-6
        </span>
        <div>
          <span class="title-main">六级 45 天通关打卡清单</span>
          <span class="title-sub">429分逆袭425+ · 每日任务与考场急救指南</span>
        </div>
      </div>

      <div class="header-actions">
        <!-- Link to Word App -->
        <a href="index.html" class="btn" title="打开背单词助手">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
          🔤 单词背诵
        </a>
        <a href="cet6_reading_platform.html" class="btn btn-primary" title="打开六级真题阅读研习平台">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
          📖 阅读真题研习
        </a>

        <!-- Cheatsheet Button -->
        <button id="guideBtn" class="btn" title="查看考场做题技巧与急救包">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          429保过急救包
        </button>

        <!-- Theme Toggle -->
        <button id="themeToggleBtn" class="btn" title="切换深色/浅色模式">
          <span id="themeIcon">🌙</span>
        </button>
      </div>
    </header>

    <!-- Global Progress Dashboard -->
    <section class="dashboard-card">
      <div class="stats-row">
        <div class="stat-item">
          <span class="stat-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            考前倒计时
          </span>
          <span class="stat-number" id="countdownVal" style="color: var(--danger);">45<small>天</small></span>
        </div>

        <div class="stat-item">
          <span class="stat-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            已通关天数
          </span>
          <span class="stat-number" id="completedDaysVal" style="color: var(--success);">0<small>/ 45 天</small></span>
        </div>

        <div class="stat-item">
          <span class="stat-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            总任务完成数
          </span>
          <span class="stat-number" id="completedTasksVal" style="color: var(--primary);">0<small>/ 135 项</small></span>
        </div>

        <div class="stat-item">
          <span class="stat-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            打卡毅力值
          </span>
          <span class="stat-number" id="streakVal">0<small>🔥 连击</small></span>
        </div>
      </div>

      <div class="progress-bar-wrap">
        <div class="progress-label-row">
          <span>总通关进度</span>
          <span id="progressPctText" style="color: var(--primary);">0%</span>
        </div>
        <div class="progress-track">
          <div id="progressFill" class="progress-fill" style="width: 0%;"></div>
        </div>
      </div>
    </section>

    <!-- Filter & Action Bar -->
    <div class="filter-bar">
      <div class="phase-tabs">
        <button class="phase-tab-btn active" data-phase="all">全部 45 天</button>
        <button class="phase-tab-btn" data-phase="1">阶段一 · 词汇破冰 (D1-18)</button>
        <button class="phase-tab-btn" data-phase="2">阶段二 · 题型击破 (D19-32)</button>
        <button class="phase-tab-btn" data-phase="3">阶段三 · 套卷模考 (D33-41)</button>
        <button class="phase-tab-btn" data-phase="4">阶段四 · 状态冲刺 (D42-45)</button>
      </div>

      <div style="display: flex; gap: 8px;">
        <button id="jumpTodayBtn" class="btn" style="padding: 6px 12px; font-size: 12px;">🎯 跳转到今日</button>
        <button id="exportPlanBtn" class="btn" style="padding: 6px 12px; font-size: 12px;">💾 备份打卡记录</button>
        <input type="file" id="importFileInput" accept=".json" style="display: none;">
      </div>
    </div>

    <!-- Day Cards Container -->
    <main id="daysContainer">
      <!-- Injected by JavaScript -->
    </main>
  </div>

  <!-- Cheatsheet & Rescue Modal -->
  <div class="modal-overlay" id="guideModal">
    <div class="modal-body">
      <div class="modal-title-row">
        <h3 style="font-size: 18px; font-weight: 800;">🚨 429分考场急救指南与保分秘籍</h3>
        <button id="closeGuideBtn" class="btn" style="padding: 4px 8px;">✕</button>
      </div>

      <div class="guide-box">
        <strong style="color: var(--primary);">⏱️ 考场做题时间分配黄金表（严格执行）：</strong><br>
        1. <strong>15:00 - 15:30 (作文 30分钟)</strong>：前5分钟构思列框架，18分钟套用模板写完，最后2分钟检查单三、时态。<br>
        2. <strong>15:30 - 16:10 (听力 30分钟 + 收答题卡一 10分钟)</strong>：听到什么选什么（视听一致），坚决不纠结错过题。<br>
        3. <strong>16:10 - 16:25 (长篇信息匹配 15分钟)</strong>：先题后文，画出大写、数字定位词，对8个以上拿满大分！<br>
        4. <strong>16:25 - 16:50 (两篇仔细阅读 25分钟)</strong>：每题 14.2 分，全卷最贵分值！根据题文同序找准定位句。<br>
        5. <strong>16:50 - 17:15 (翻译 25分钟)</strong>：主谓宾先行，拆分长句，难词同义降级。<br>
        6. <strong>17:15 - 17:25 (选词填空 10分钟)</strong>：分值最低(每题3.55分)，按词性快速蒙选，切忌前置浪费时间！
      </div>

      <div class="guide-box" style="border-left-color: var(--success);">
        <strong style="color: var(--success);">🎧 听力 3 大保命黄金法则：</strong><br>
        • <strong>视听一致原则</strong>：听到哪个选项词汇重合度最高就选哪个，尤其是长对话和短文前两篇。<br>
        • <strong>信号词必出题</strong>：听到 <code>however, but, in fact, unfortunately, what really matters</code> 之后必有答案！<br>
        • <strong>首尾提炼主旨</strong>：第一句和最后两句往往对应主旨态度题。
      </div>

      <div class="guide-box" style="border-left-color: var(--warning);">
        <strong style="color: var(--warning);">📖 阅读 3 大避坑技巧：</strong><br>
        • <strong>题文同序</strong>：第 1 题在 1-2 段，第 2 题在 2-3 段，绝不跳段找。<br>
        • <strong>绝对词排除</strong>：选项带有 <code>always, completely, entirely, must</code> 90% 是错误干扰项；带有 <code>may, can, some, not necessarily</code> 往往是正确答案。<br>
        • <strong>同义替换是王道</strong>：原文的动词/形容词被换成同义词或解释性句子的，必是正确选项。
      </div>

      <div class="guide-box" style="border-left-color: var(--danger);">
        <strong style="color: var(--danger);">✍️ 翻译避坑与同义降级：</strong><br>
        • “蓬勃发展” 不会写 <code>thrive</code>？降级写 <code>develop rapidly</code>！<br>
        • “不可磨灭的贡献” 不会写 <code>indelible</code>？降级写 <code>great contribution</code>！<br>
        • 确保<strong>主干语法无误</strong>，老师给分绝不会低！
      </div>
    </div>
  </div>

  <!-- Application Logic & Embedded 45-Day Data -->
  <script>
    const SCHEDULE = {json_data};
    const STORAGE_KEY = 'cet6_45day_checklist_state_v2';

    function getLocalTodayStr() {{
      const d = new Date();
      const year = d.getFullYear();
      const month = String(d.getMonth() + 1).padStart(2, '0');
      const day = String(d.getDate()).padStart(2, '0');
      return `${{year}}-${{month}}-${{day}}`;
    }}

    // State: checks[day_taskKey] = bool, notes[day] = string
    let checkState = {{
      checks: {{
        '1_vocab': true,
        '1_reading': true,
        '1_listening': true
      }},
      notes: {{}},
      theme: 'light'
    }};

    function loadState() {{
      try {{
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {{
          const parsed = JSON.parse(saved);
          if (parsed.checks) checkState.checks = parsed.checks;
          if (parsed.notes) checkState.notes = parsed.notes;
          if (parsed.theme) checkState.theme = parsed.theme;
        }} else {{
          // Default Day 1 as completed because yesterday (10-30) was Day 1 of serious study!
          checkState.checks = {{
            '1_vocab': true,
            '1_reading': true,
            '1_listening': true
          }};
          saveState();
        }}
      }} catch (e) {{
        console.warn('Load checklist err:', e);
      }}
    }}

    function saveState() {{
      try {{
        localStorage.setItem(STORAGE_KEY, JSON.stringify(checkState));
      }} catch (e) {{
        console.warn('Save checklist err:', e);
      }}
      updateDashboard();
    }}

    // Check if a specific task is checked
    function isTaskChecked(day, type) {{
      return !!checkState.checks[`${{day}}_${{type}}`];
    }}

    function setTaskChecked(day, type, checked) {{
      checkState.checks[`${{day}}_${{type}}`] = checked;
      saveState();
    }}

    // Update Top Dashboard stats
    function updateDashboard() {{
      let completedTasks = 0;
      let completedDays = 0;

      SCHEDULE.forEach(item => {{
        const c1 = isTaskChecked(item.day, 'vocab');
        const c2 = isTaskChecked(item.day, 'reading');
        const c3 = isTaskChecked(item.day, 'listening');

        if (c1) completedTasks++;
        if (c2) completedTasks++;
        if (c3) completedTasks++;

        if (c1 && c2 && c3) completedDays++;
      }});

      const totalTasks = SCHEDULE.length * 3; // 135
      const pct = Math.round((completedTasks / totalTasks) * 100);

      document.getElementById('completedTasksVal').innerHTML = `${{completedTasks}}<small>/ ${{totalTasks}} 项</small>`;
      document.getElementById('completedDaysVal').innerHTML = `${{completedDays}}<small>/ 45 天</small>`;
      document.getElementById('progressPctText').textContent = pct + '%';
      document.getElementById('progressFill').style.width = pct + '%';

      // Streak calculation
      document.getElementById('streakVal').innerHTML = `${{completedDays}}<small>🔥 连击</small>`;

      // Countdown to Exam (2026-12-12)
      const examDate = new Date(2026, 11, 12);
      const now = new Date();
      const todayStart = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      const diffTime = examDate - todayStart;
      const diffDays = Math.max(0, Math.round(diffTime / (1000 * 60 * 60 * 24)));
      document.getElementById('countdownVal').innerHTML = `${{diffDays}}<small>天</small>`;
    }}

    // Render cards
    function renderDays(filterPhase = 'all') {{
      const container = document.getElementById('daysContainer');
      container.innerHTML = '';

      const todayStr = getLocalTodayStr();

      SCHEDULE.forEach(item => {{
        if (filterPhase !== 'all' && String(item.phase) !== String(filterPhase)) {{
          return;
        }}

        const isToday = (item.isoDate === todayStr);
        const cVocab = isTaskChecked(item.day, 'vocab');
        const cReading = isTaskChecked(item.day, 'reading');
        const cListening = isTaskChecked(item.day, 'listening');
        const isDayDone = (cVocab && cReading && cListening);

        const card = document.createElement('article');
        card.className = `day-card ${{isToday ? 'today' : ''}} ${{isDayDone ? 'day-completed' : ''}}`;
        card.id = `dayCard-${{item.day}}`;

        const noteText = checkState.notes[item.day] || '';

        card.innerHTML = `
          <div class="day-header">
            <div class="day-info">
              <span class="day-badge">Day ${{item.day.toString().padStart(2, '0')}}</span>
              <span class="date-tag">${{item.date}} (${{item.weekday}})</span>
              <span class="phase-tag p${{item.phase}}">${{item.phaseName}}</span>
              ${{isToday ? '<span class="today-pill">TODAY</span>' : ''}}
            </div>
            <span class="day-status-pill">${{isDayDone ? '✓ 已打卡' : '未完成'}}</span>
          </div>

          <div class="task-list">
            <div class="task-item ${{cVocab ? 'checked' : ''}}" onclick="toggleCheck(${{item.day}}, 'vocab', this)">
              <input type="checkbox" class="task-checkbox" ${{cVocab ? 'checked' : ''}} onclick="event.stopPropagation(); toggleCheck(${{item.day}}, 'vocab', this.parentElement)">
              <div class="task-content">
                <span class="task-type-badge type-vocab">词汇</span>
                ${{item.vocab}}
              </div>
            </div>

            <div class="task-item ${{cReading ? 'checked' : ''}}" onclick="toggleCheck(${{item.day}}, 'reading', this)">
              <input type="checkbox" class="task-checkbox" ${{cReading ? 'checked' : ''}} onclick="event.stopPropagation(); toggleCheck(${{item.day}}, 'reading', this.parentElement)">
              <div class="task-content">
                <span class="task-type-badge type-reading">阅读/综合</span>
                ${{item.reading}}
              </div>
            </div>

            <div class="task-item ${{cListening ? 'checked' : ''}}" onclick="toggleCheck(${{item.day}}, 'listening', this)">
              <input type="checkbox" class="task-checkbox" ${{cListening ? 'checked' : ''}} onclick="event.stopPropagation(); toggleCheck(${{item.day}}, 'listening', this.parentElement)">
              <div class="task-content">
                <span class="task-type-badge type-listen">听力/技巧</span>
                ${{item.listening}}
              </div>
            </div>
          </div>

          <div>
            <button class="note-btn" onclick="toggleNoteField(${{item.day}})">
              ✏️ ${{noteText ? '查看/编辑今日心得' : '添加今日学习笔记...'}}
            </button>
            <textarea id="noteInput-${{item.day}}" class="note-textarea ${{noteText ? 'active' : ''}}" placeholder="记录今天错题感受、生词或鼓励自己的一句话..." onchange="saveNote(${{item.day}}, this.value)">${{noteText}}</textarea>
          </div>
        `;

        container.appendChild(card);
      }});
    }}

    function toggleCheck(day, type, rowEl) {{
      const cb = rowEl.querySelector('.task-checkbox');
      const newState = !cb.checked;
      cb.checked = newState;
      if (newState) {{
        rowEl.classList.add('checked');
      }} else {{
        rowEl.classList.remove('checked');
      }}

      setTaskChecked(day, type, newState);

      // Check if day is all done
      const c1 = isTaskChecked(day, 'vocab');
      const c2 = isTaskChecked(day, 'reading');
      const c3 = isTaskChecked(day, 'listening');
      const card = document.getElementById(`dayCard-${{day}}`);
      if (card) {{
        const statusPill = card.querySelector('.day-status-pill');
        if (c1 && c2 && c3) {{
          card.classList.add('day-completed');
          if (statusPill) statusPill.textContent = '✓ 已打卡';
        }} else {{
          card.classList.remove('day-completed');
          if (statusPill) statusPill.textContent = '未完成';
        }}
      }}
    }}

    function toggleNoteField(day) {{
      const ta = document.getElementById(`noteInput-${{day}}`);
      if (ta) {{
        ta.classList.toggle('active');
        if (ta.classList.contains('active')) ta.focus();
      }}
    }}

    function saveNote(day, text) {{
      checkState.notes[day] = text;
      saveState();
    }}

    // Export & Backup
    function exportBackup() {{
      const dataStr = JSON.stringify({{
        version: 1,
        exportTime: new Date().toISOString(),
        state: checkState
      }}, null, 2);

      const blob = new Blob([dataStr], {{ type: 'application/json;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `CET6_45天打卡记录_${{getLocalTodayStr()}}.json`;
      a.click();
      URL.revokeObjectURL(url);
    }}

    // Init
    document.addEventListener('DOMContentLoaded', () => {{
      loadState();

      // Theme init
      if (checkState.theme === 'dark') {{
        document.documentElement.setAttribute('data-theme', 'dark');
        document.getElementById('themeIcon').textContent = '☀️';
      }}

      document.getElementById('themeToggleBtn').onclick = () => {{
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        if (isDark) {{
          document.documentElement.removeAttribute('data-theme');
          checkState.theme = 'light';
          document.getElementById('themeIcon').textContent = '🌙';
        }} else {{
          document.documentElement.setAttribute('data-theme', 'dark');
          checkState.theme = 'dark';
          document.getElementById('themeIcon').textContent = '☀️';
        }}
        saveState();
      }};

      renderDays('all');
      updateDashboard();

      // Filter tabs
      document.querySelectorAll('.phase-tab-btn').forEach(btn => {{
        btn.onclick = () => {{
          document.querySelectorAll('.phase-tab-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          renderDays(btn.dataset.phase);
        }};
      }});

      // Jump to today
      document.getElementById('jumpTodayBtn').onclick = () => {{
        const todayStr = getLocalTodayStr();
        const todayItem = SCHEDULE.find(item => item.isoDate === todayStr) || SCHEDULE[0];
        const targetCard = document.getElementById(`dayCard-${{todayItem.day}}`);
        if (targetCard) {{
          targetCard.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        }}
      }};

      // Guide Modal
      const modal = document.getElementById('guideModal');
      document.getElementById('guideBtn').onclick = () => modal.classList.add('active');
      document.getElementById('closeGuideBtn').onclick = () => modal.classList.remove('active');
      modal.onclick = (e) => {{
        if (e.target === modal) modal.classList.remove('active');
      }};

      document.getElementById('exportPlanBtn').onclick = exportBackup;
    }});
  </script>
</body>
</html>
'''

    with open('六级45天通关打卡清单.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated 六级45天通关打卡清单.html successfully')

if __name__ == '__main__':
    generate()
