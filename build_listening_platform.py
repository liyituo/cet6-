# -*- coding: utf-8 -*-
"""
Enhanced Builder for CET-6 Listening Master Platform with Synchronized Transcripts
(大学英语六级历年听力真题全真研习平台 · 听读分栏 · 边听边看 · 2019-2025 全套27套原版真题音频与双语原文)
"""

import json
import os
import re
import sys

def load_data():
    lq_path = 'temp_astrbot/listening_questions_v3.json'
    if not os.path.exists(lq_path):
        raise FileNotFoundError(f"Cannot find {lq_path}")
    
    with open(lq_path, 'r', encoding='utf-8') as f:
        raw_lq = json.load(f)

    durations = {}
    if os.path.exists('audio_durations.json'):
        with open('audio_durations.json', 'r', encoding='utf-8') as f:
            durations = json.load(f)

    dict_map = {}
    if os.path.exists('comprehensive_cet6_dict.json'):
        with open('comprehensive_cet6_dict.json', 'r', encoding='utf-8') as f:
            dict_map = json.load(f)
        print(f"Loaded dictionary: {len(dict_map)} words")

    transcripts_db = {}
    if os.path.exists('cet6_listening_transcripts.json'):
        with open('cet6_listening_transcripts.json', 'r', encoding='utf-8') as f:
            transcripts_db = json.load(f)
        print(f"Loaded transcripts: {len(transcripts_db)} exams")

    exams = []
    
    # Process all 27 sets
    for k in sorted(raw_lq.keys()):
        val = raw_lq[k]
        meta = val.get('meta') or {}
        year = meta.get('year') or k.split('_')[0]
        month = meta.get('month') or k.split('_')[1]
        set_num = meta.get('set_num') or k.split('_')[2]
        
        mp3_file = meta.get('mp3_file') or f"cet6_{year}_{month}_{set_num}.mp3"
        duration_sec = durations.get(mp3_file, 1660.0)
        dur_mins = int(duration_sec // 60)
        dur_secs = int(duration_sec % 60)
        duration_label = f"{dur_mins:02d}:{dur_secs:02d}"

        m_int = int(month)
        title = f"{year}年{m_int:02d}月 六级听力真题 (第{set_num}套)"

        answers = val.get('answers', {})

        sections_data = val.get('sections', {})
        sec_a_raw = sections_data.get('A', {}).get('questions', [])
        sec_b_raw = sections_data.get('B', {}).get('questions', [])
        sec_c_raw = sections_data.get('C', {}).get('questions', [])

        total_q = len(sec_a_raw) + len(sec_b_raw) + len(sec_c_raw)
        if total_q == 0:
            total_q = 25

        exam_obj = {
            "id": k,
            "year": year,
            "month": month,
            "set_num": set_num,
            "title": title,
            "mp3_file": mp3_file,
            "duration_sec": duration_sec,
            "duration_label": duration_label,
            "audio_sources": [
                f"./audio/{mp3_file}",
                f"./CET-6听力/{mp3_file}",
                f"./temp_astrbot/CET-6听力/{mp3_file}"
            ],
            "total_questions": total_q,
            "answers": answers,
            "transcripts": transcripts_db.get(k, {"parts": []}),
            "sections": {
                "A": {
                    "key": "A",
                    "title": "Section A: 长对话 (Long Conversations)",
                    "weight_label": "共8题 (Q1-Q8) · 每题7.1分 · 共56.8分",
                    "direction": "In this section, you will hear two long conversations. At the end of each conversation, you will hear four questions. Both the conversation and the questions will be spoken only once.",
                    "groups": [
                        {
                            "name": "Conversation 1 (长对话一)",
                            "range": "Q1 - Q4",
                            "start_q": 1,
                            "end_q": 4,
                            "questions": sec_a_raw[0:4]
                        },
                        {
                            "name": "Conversation 2 (长对话二)",
                            "range": "Q5 - Q8",
                            "start_q": 5,
                            "end_q": 8,
                            "questions": sec_a_raw[4:8]
                        }
                    ]
                },
                "B": {
                    "key": "B",
                    "title": "Section B: 听力篇章 (Passages)",
                    "weight_label": "共7题 (Q9-Q15) · 每题7.1分 · 共49.7分",
                    "direction": "In this section, you will hear two passages. At the end of each passage, you will hear three or four questions. Both the passage and the questions will be spoken only once.",
                    "groups": [
                        {
                            "name": "Passage 1 (短文理解一)",
                            "range": "Q9 - Q11",
                            "start_q": 9,
                            "end_q": 11,
                            "questions": sec_b_raw[0:3]
                        },
                        {
                            "name": "Passage 2 (短文理解二)",
                            "range": "Q12 - Q15",
                            "start_q": 12,
                            "end_q": 15,
                            "questions": sec_b_raw[3:7]
                        }
                    ]
                },
                "C": {
                    "key": "C",
                    "title": "Section C: 讲座/讲话 (Recordings & Lectures)",
                    "weight_label": "共10题 (Q16-Q25) · 每题14.2分 (双倍权重！核心得分区) · 共142.0分",
                    "direction": "In this section, you will hear three recordings of lectures or talks. At the end of each recording, you will hear three or four questions. Both the recording and the questions will be spoken only once.",
                    "groups": [
                        {
                            "name": "Recording 1 (讲座讲话一)",
                            "range": "Q16 - Q18",
                            "start_q": 16,
                            "end_q": 18,
                            "questions": sec_c_raw[0:3]
                        },
                        {
                            "name": "Recording 2 (讲座讲话二)",
                            "range": "Q19 - Q21",
                            "start_q": 19,
                            "end_q": 21,
                            "questions": sec_c_raw[3:6]
                        },
                        {
                            "name": "Recording 3 (讲座讲话三)",
                            "range": "Q22 - Q25",
                            "start_q": 22,
                            "end_q": 25,
                            "questions": sec_c_raw[6:10]
                        }
                    ]
                }
            }
        }
        exams.append(exam_obj)

    print(f"Processed {len(exams)} exams successfully. Total questions: {sum(e['total_questions'] for e in exams)}")
    return exams, dict_map

def generate_platform_html(exams, dict_map):
    exams_json = json.dumps(exams, ensure_ascii=False).replace('</script>', '<\\/script>')
    dict_json = json.dumps(dict_map, ensure_ascii=False).replace('</script>', '<\\/script>')

    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CET-6 英语六级历年听力真题全真研习平台 (2019-2025 全套27套原版真题音频与双语原文)</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%234f46e5'><path d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 14.5c-2.49 0-4.5-2.01-4.5-4.5S9.51 7.5 12 7.5s4.5 2.01 4.5 4.5-2.01 4.5-4.5 4.5zm0-5.5c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1z'/></svg>">
  <style>
    /* ==========================================================================
       CSS Variables & Themes
       ========================================================================== */
    :root {{
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-subtle: #eef2ff;
      --primary-border: #c7d2fe;
      --bg-body: #f8fafc;
      --bg-surface: #ffffff;
      --bg-subtle: #f1f5f9;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border-color: #e2e8f0;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --card-shadow-hover: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
      --success: #10b981;
      --success-subtle: #ecfdf5;
      --success-border: #a7f3d0;
      --danger: #ef4444;
      --danger-subtle: #fef2f2;
      --danger-border: #fecaca;
      --warning: #f59e0b;
      --warning-subtle: #fffbeb;
      --warning-border: #fde68a;
      --header-height: 64px;
    }}

    [data-theme="dark"] {{
      --primary: #6366f1;
      --primary-hover: #818cf8;
      --primary-subtle: #1e1b4b;
      --primary-border: #3730a3;
      --bg-body: #090d16;
      --bg-surface: #111827;
      --bg-subtle: #1f2937;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --border-color: #374151;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
      --card-shadow-hover: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
      --success: #34d399;
      --success-subtle: #064e3b;
      --success-border: #059669;
      --danger: #f87171;
      --danger-subtle: #7f1d1d;
      --danger-border: #dc2626;
      --warning: #fbbf24;
      --warning-subtle: #78350f;
      --warning-border: #d97706;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background: var(--bg-body);
      color: var(--text-main);
      line-height: 1.6;
      transition: background-color 0.2s, color 0.2s;
      min-height: 100vh;
      overflow-x: hidden;
    }}

    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: var(--bg-body);
    }}
    ::-webkit-scrollbar-thumb {{
      background: var(--border-color);
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: var(--text-muted);
    }}

    .container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 20px;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 8px 16px;
      font-size: 0.88rem;
      font-weight: 600;
      border-radius: 8px;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
      outline: none;
      white-space: nowrap;
    }}
    .btn:active {{
      transform: scale(0.98);
    }}
    .btn-primary {{
      background: var(--primary);
      color: white;
      box-shadow: 0 2px 4px rgba(79, 70, 229, 0.2);
    }}
    .btn-primary:hover {{
      background: var(--primary-hover);
    }}
    .btn-secondary {{
      background: var(--bg-subtle);
      color: var(--text-main);
      border-color: var(--border-color);
    }}
    .btn-secondary:hover {{
      background: var(--border-color);
    }}
    .btn-outline {{
      background: transparent;
      border-color: var(--border-color);
      color: var(--text-main);
    }}
    .btn-outline:hover {{
      border-color: var(--primary);
      color: var(--primary);
      background: var(--primary-subtle);
    }}
    .btn-sm {{
      padding: 5px 10px;
      font-size: 0.8rem;
      border-radius: 6px;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 8px;
      font-size: 0.75rem;
      font-weight: 600;
      border-radius: 9999px;
      white-space: nowrap;
    }}
    .badge-primary {{
      background: var(--primary-subtle);
      color: var(--primary);
      border: 1px solid var(--primary-border);
    }}
    .badge-success {{
      background: var(--success-subtle);
      color: var(--success);
      border: 1px solid var(--success-border);
    }}
    .badge-warning {{
      background: var(--warning-subtle);
      color: var(--warning);
      border: 1px solid var(--warning-border);
    }}
    .badge-danger {{
      background: var(--danger-subtle);
      color: var(--danger);
      border: 1px solid var(--danger-border);
    }}

    /* ==========================================================================
       Header
       ========================================================================== */
    .app-header {{
      position: sticky;
      top: 0;
      z-index: 50;
      height: var(--header-height);
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      backdrop-filter: blur(12px);
      display: flex;
      align-items: center;
      transition: all 0.2s;
    }}
    .header-content {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
    }}
    .brand-area {{
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
    }}
    .brand-logo {{
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 1.25rem;
      box-shadow: 0 4px 10px rgba(79, 70, 229, 0.3);
    }}
    .brand-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .layout-switch-group {{
      display: flex;
      background: var(--bg-subtle);
      border-radius: 10px;
      padding: 3px;
      border: 1px solid var(--border-color);
    }}
    .layout-btn {{
      padding: 5px 12px;
      font-size: 0.82rem;
      font-weight: 600;
      border-radius: 7px;
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
    }}
    .layout-btn.active {{
      background: var(--bg-surface);
      color: var(--primary);
      box-shadow: 0 2px 5px rgba(0,0,0,0.06);
    }}

    .timer-widget {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 5px 12px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
    }}
    .timer-widget.warning {{
      background: var(--danger-subtle);
      border-color: var(--danger-border);
      color: var(--danger);
      animation: pulse 1s infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.6; }}
    }}

    /* ==========================================================================
       Sticky Audio Player Bar
       ========================================================================== */
    .sticky-player-bar {{
      position: sticky;
      top: var(--header-height);
      z-index: 40;
      background: var(--bg-surface);
      border-bottom: 2px solid var(--border-color);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
      padding: 10px 0;
      transition: all 0.2s ease;
    }}
    .player-container {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .player-top-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .player-track-info {{
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 220px;
    }}
    .player-disc-icon {{
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
      flex-shrink: 0;
      box-shadow: 0 2px 6px rgba(16, 185, 129, 0.3);
    }}
    .player-disc-icon.spinning {{
      animation: spin 3s linear infinite;
    }}
    @keyframes spin {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}
    .player-title-box {{
      display: flex;
      flex-direction: column;
    }}
    .player-exam-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--text-main);
      max-width: 280px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .player-sub-status {{
      font-size: 0.75rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .player-transport {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .btn-circle {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      cursor: pointer;
      font-size: 0.85rem;
      transition: all 0.15s;
    }}
    .btn-circle:hover {{
      background: var(--primary-subtle);
      border-color: var(--primary);
      color: var(--primary);
    }}
    .btn-play-pause {{
      width: 44px;
      height: 44px;
      background: var(--primary);
      color: white;
      border: none;
      box-shadow: 0 4px 10px rgba(79, 70, 229, 0.3);
      font-size: 1.1rem;
    }}
    .btn-play-pause:hover {{
      background: var(--primary-hover);
      transform: scale(1.05);
    }}

    .player-progress-row {{
      display: flex;
      align-items: center;
      gap: 12px;
      width: 100%;
    }}
    .time-badge {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-muted);
      min-width: 50px;
      text-align: center;
    }}
    .progress-bar-wrap {{
      position: relative;
      flex: 1;
      height: 8px;
      background: var(--bg-subtle);
      border-radius: 4px;
      cursor: pointer;
      user-select: none;
    }}
    .progress-bar-fill {{
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      background: linear-gradient(90deg, #4f46e5 0%, #818cf8 100%);
      border-radius: 4px;
      pointer-events: none;
      width: 0%;
      transition: width 0.1s linear;
    }}
    .progress-loop-range {{
      position: absolute;
      top: 0;
      height: 100%;
      background: rgba(245, 158, 11, 0.45);
      border-left: 2px solid var(--warning);
      border-right: 2px solid var(--warning);
      display: none;
      pointer-events: none;
      z-index: 2;
    }}

    .section-jumpers {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .player-tools {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .speed-select {{
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 5px 8px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      outline: none;
    }}
    .ab-loop-btn {{
      padding: 4px 8px;
      font-size: 0.78rem;
      border-radius: 6px;
      font-weight: 600;
    }}
    .ab-loop-btn.active {{
      background: var(--warning);
      color: white;
      border-color: var(--warning);
    }}

    /* ==========================================================================
       Exam Hub View
       ========================================================================== */
    .exam-hub-view {{
      padding: 30px 0 60px 0;
    }}
    .hub-hero {{
      background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%);
      border-radius: 18px;
      color: white;
      padding: 36px 40px;
      margin-bottom: 30px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.3);
    }}
    .hub-hero::after {{
      content: "🎧";
      position: absolute;
      right: 30px;
      bottom: -20px;
      font-size: 130px;
      opacity: 0.12;
      pointer-events: none;
    }}
    .hub-hero h1 {{
      font-size: 1.85rem;
      font-weight: 800;
      margin-bottom: 10px;
      letter-spacing: -0.02em;
    }}
    .hub-hero p {{
      font-size: 0.96rem;
      opacity: 0.9;
      max-width: 780px;
      line-height: 1.6;
    }}
    .hub-stats-row {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      margin-top: 25px;
    }}
    .hub-stat-card {{
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 12px;
      padding: 14px 18px;
    }}
    .hub-stat-label {{
      font-size: 0.8rem;
      opacity: 0.85;
      margin-bottom: 4px;
    }}
    .hub-stat-val {{
      font-size: 1.5rem;
      font-weight: 800;
      font-family: ui-monospace, SFMono-Regular, monospace;
    }}

    .hub-filter-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }}
    .hub-tabs {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}
    .hub-tab-btn {{
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s;
    }}
    .hub-tab-btn:hover {{
      border-color: var(--primary);
      color: var(--primary);
    }}
    .hub-tab-btn.active {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}
    .hub-search-box {{
      position: relative;
      min-width: 240px;
    }}
    .hub-search-input {{
      width: 100%;
      padding: 8px 14px 8px 36px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      color: var(--text-main);
      font-size: 0.88rem;
      outline: none;
      transition: border-color 0.15s;
    }}
    .hub-search-input:focus {{
      border-color: var(--primary);
    }}
    .hub-search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 0.85rem;
    }}

    .exams-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 20px;
    }}
    .exam-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 20px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
      position: relative;
    }}
    .exam-card:hover {{
      box-shadow: var(--card-shadow-hover);
      border-color: var(--primary-border);
      transform: translateY(-2px);
    }}
    .exam-card-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 12px;
    }}
    .exam-card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.4;
    }}
    .exam-card-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 14px;
    }}
    .exam-card-stats {{
      background: var(--bg-subtle);
      border-radius: 8px;
      padding: 10px 14px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .exam-card-stat-item {{
      display: flex;
      flex-direction: column;
    }}
    .exam-card-stat-lbl {{
      font-size: 0.72rem;
      color: var(--text-muted);
    }}
    .exam-card-stat-val {{
      font-size: 0.95rem;
      font-weight: 700;
      font-family: ui-monospace, SFMono-Regular, monospace;
    }}
    .exam-card-actions {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}

    /* ==========================================================================
       Workspace: Dual-Pane (Split-Screen) Architecture
       ========================================================================== */
    .workspace-view {{
      display: none;
      padding: 16px 0 80px 0;
    }}
    .workspace-top-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
      flex-wrap: wrap;
      gap: 12px;
      background: var(--bg-surface);
      padding: 12px 20px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
    }}

    /* Split Panes Wrapper */
    .split-layout-wrapper {{
      display: flex;
      width: 100%;
      gap: 0;
      min-height: calc(100vh - 230px);
      position: relative;
    }}

    /* Left Pane: Transcript Reader */
    .pane-transcript {{
      flex: 1 1 50%;
      min-width: 320px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--card-shadow);
      max-height: calc(100vh - 230px);
      overflow: hidden;
    }}
    .pane-transcript-header {{
      padding: 14px 20px;
      border-bottom: 1px solid var(--border-color);
      background: var(--bg-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .pane-transcript-body {{
      padding: 20px;
      overflow-y: auto;
      flex: 1;
      scroll-behavior: smooth;
    }}

    /* Center Resizer */
    .split-resizer {{
      width: 12px;
      cursor: col-resize;
      background: transparent;
      display: flex;
      align-items: center;
      justify-content: center;
      user-select: none;
      z-index: 20;
    }}
    .split-resizer::after {{
      content: "";
      width: 4px;
      height: 36px;
      background: var(--border-color);
      border-radius: 2px;
      transition: background 0.15s;
    }}
    .split-resizer:hover::after, .split-resizer.resizing::after {{
      background: var(--primary);
      width: 5px;
    }}

    /* Right Pane: Questions & Console */
    .pane-questions {{
      flex: 1 1 50%;
      min-width: 320px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--card-shadow);
      max-height: calc(100vh - 230px);
      overflow: hidden;
    }}
    .pane-questions-header {{
      padding: 14px 20px;
      border-bottom: 1px solid var(--border-color);
      background: var(--bg-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .pane-questions-body {{
      padding: 20px;
      overflow-y: auto;
      flex: 1;
      scroll-behavior: smooth;
    }}

    /* Layout Mode Variations */
    .split-layout-wrapper.transcript-only .pane-questions {{
      display: none !important;
    }}
    .split-layout-wrapper.transcript-only .split-resizer {{
      display: none !important;
    }}
    .split-layout-wrapper.transcript-only .pane-transcript {{
      flex: 1 1 100% !important;
      max-width: 100% !important;
    }}

    .split-layout-wrapper.console-only .pane-transcript {{
      display: none !important;
    }}
    .split-layout-wrapper.console-only .split-resizer {{
      display: none !important;
    }}
    .split-layout-wrapper.console-only .pane-questions {{
      flex: 1 1 100% !important;
      max-width: 100% !important;
    }}

    /* ==========================================================================
       Transcript Cards & Paragraphs
       ========================================================================== */
    .transcript-part-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 18px 20px;
      margin-bottom: 22px;
      transition: all 0.2s ease;
    }}
    .part-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 10px;
      margin-bottom: 14px;
    }}
    .part-title {{
      font-weight: 800;
      font-size: 1.05rem;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .part-topic-pill {{
      font-size: 0.78rem;
      padding: 2px 8px;
      background: var(--primary-subtle);
      color: var(--primary);
      border-radius: 4px;
      font-weight: 600;
    }}

    /* Transcript Paragraph */
    .transcript-paragraph {{
      padding: 12px 14px;
      border-radius: 8px;
      margin-bottom: 12px;
      border-left: 3px solid transparent;
      background: var(--bg-subtle);
      transition: all 0.2s ease;
      position: relative;
    }}
    .transcript-paragraph:hover {{
      background: var(--primary-subtle);
    }}
    .transcript-paragraph.active-playing {{
      background: rgba(79, 70, 229, 0.1) !important;
      border-left-color: var(--primary) !important;
      box-shadow: 0 0 0 1px var(--primary-border);
    }}
    .paragraph-top-line {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }}
    .spk-badge {{
      font-weight: 800;
      font-size: 0.8rem;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .spk-play-btn {{
      padding: 2px 7px;
      font-size: 0.75rem;
      border-radius: 6px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      color: var(--text-main);
    }}
    .spk-play-btn:hover {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}
    .p-en-text {{
      font-size: 0.95rem;
      line-height: 1.65;
      color: var(--text-main);
      margin-bottom: 6px;
    }}
    .p-zh-text {{
      font-size: 0.85rem;
      line-height: 1.55;
      color: var(--text-muted);
      border-top: 1px dashed var(--border-color);
      padding-top: 6px;
    }}

    /* Evidence Highlighting in Transcript */
    .evidence-highlight {{
      background: #fef08a;
      color: #854d0e;
      padding: 2px 4px;
      border-radius: 4px;
      font-weight: 600;
      cursor: pointer;
      border-bottom: 2px solid #ca8a04;
      transition: background 0.15s;
    }}
    [data-theme="dark"] .evidence-highlight {{
      background: #854d0e;
      color: #fef08a;
      border-bottom-color: #fde047;
    }}
    .evidence-tag {{
      display: inline-flex;
      align-items: center;
      gap: 3px;
      padding: 1px 6px;
      background: #eab308;
      color: black;
      font-size: 0.72rem;
      font-weight: 800;
      border-radius: 4px;
      margin-left: 6px;
      cursor: pointer;
    }}

    /* Spoken Questions Block */
    .spoken-questions-drawer {{
      margin-top: 12px;
      border-top: 1px solid var(--border-color);
      padding-top: 10px;
    }}
    .spoken-q-item {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 8px 12px;
      margin-bottom: 6px;
      font-size: 0.82rem;
    }}

    /* ==========================================================================
       Questions Component
       ========================================================================== */
    .question-block {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 16px 18px;
      margin-bottom: 18px;
      transition: all 0.2s ease;
      scroll-margin-top: 100px;
    }}
    .question-block:hover {{
      border-color: var(--primary-border);
    }}
    .question-block.focused {{
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
    }}
    .question-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }}
    .q-number-pill {{
      font-size: 0.92rem;
      font-weight: 800;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .q-actions {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .btn-flag {{
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.78rem;
      cursor: pointer;
    }}
    .btn-flag.flagged {{
      background: var(--warning-subtle);
      border-color: var(--warning);
      color: var(--warning);
    }}

    .options-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
      margin-bottom: 12px;
    }}
    .option-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 10px 14px;
      border-radius: 8px;
      border: 1.5px solid var(--border-color);
      background: var(--bg-surface);
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
    }}
    .option-item:hover {{
      background: var(--primary-subtle);
      border-color: var(--primary-border);
    }}
    .option-item.selected {{
      background: var(--primary-subtle);
      border-color: var(--primary);
    }}
    .option-item.correct {{
      background: var(--success-subtle) !important;
      border-color: var(--success) !important;
      color: var(--success) !important;
      font-weight: 600;
    }}
    .option-item.wrong {{
      background: var(--danger-subtle) !important;
      border-color: var(--danger) !important;
      color: var(--danger) !important;
      text-decoration: line-through;
    }}
    .opt-letter {{
      font-weight: 800;
      color: var(--primary);
      min-width: 24px;
      height: 24px;
      border-radius: 6px;
      background: var(--bg-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
    }}
    .option-item.selected .opt-letter {{
      background: var(--primary);
      color: white;
    }}
    .opt-text {{
      font-size: 0.92rem;
      line-height: 1.5;
      color: var(--text-main);
      flex: 1;
    }}
    .dict-word {{
      cursor: pointer;
      border-bottom: 1px dotted rgba(79, 70, 229, 0.4);
      padding: 0 1px;
      border-radius: 2px;
      transition: background 0.1s;
    }}
    .dict-word:hover {{
      background: rgba(79, 70, 229, 0.15);
      color: var(--primary);
    }}

    .scratchpad-wrap {{
      margin-top: 10px;
      border-top: 1px dashed var(--border-color);
      padding-top: 10px;
      display: none;
    }}
    .scratchpad-textarea {{
      width: 100%;
      height: 60px;
      padding: 8px 12px;
      font-size: 0.85rem;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background: var(--bg-subtle);
      color: var(--text-main);
      outline: none;
      resize: vertical;
    }}

    .study-analysis-box {{
      margin-top: 12px;
      padding: 10px 14px;
      border-radius: 8px;
      background: var(--bg-subtle);
      border-left: 4px solid var(--primary);
      font-size: 0.85rem;
      display: none;
    }}
    .study-analysis-box.visible {{
      display: block;
    }}

    /* ==========================================================================
       Floating Answer Sheet Drawer
       ========================================================================== */
    .floating-sheet-toggle {{
      position: fixed;
      right: 20px;
      bottom: 30px;
      z-index: 60;
      background: var(--primary);
      color: white;
      border: none;
      padding: 12px 20px;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 0.9rem;
      box-shadow: 0 10px 20px -3px rgba(79, 70, 229, 0.4);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .floating-sheet-toggle:hover {{
      transform: translateY(-2px);
      box-shadow: 0 14px 25px -4px rgba(79, 70, 229, 0.5);
    }}

    .sheet-drawer {{
      position: fixed;
      right: -360px;
      top: 0;
      bottom: 0;
      width: 340px;
      background: var(--bg-surface);
      border-left: 1px solid var(--border-color);
      z-index: 70;
      box-shadow: -5px 0 25px rgba(0, 0, 0, 0.15);
      transition: right 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }}
    .sheet-drawer.open {{
      right: 0;
    }}
    .sheet-drawer-header {{
      padding: 20px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .sheet-drawer-title {{
      font-size: 1.1rem;
      font-weight: 700;
    }}
    .sheet-drawer-body {{
      padding: 20px;
      overflow-y: auto;
      flex: 1;
    }}
    .sheet-progress-summary {{
      margin-bottom: 16px;
      font-size: 0.88rem;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
    }}
    .sheet-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 10px;
      margin-bottom: 24px;
    }}
    .sheet-cell {{
      aspect-ratio: 1;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-subtle);
      color: var(--text-muted);
      font-weight: 700;
      font-size: 0.88rem;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      transition: all 0.15s;
    }}
    .sheet-cell:hover {{
      border-color: var(--primary);
      color: var(--primary);
    }}
    .sheet-cell.answered {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}
    .sheet-cell.flagged::after {{
      content: "★";
      position: absolute;
      top: 1px;
      right: 3px;
      font-size: 0.65rem;
      color: var(--warning);
    }}
    .sheet-cell.correct {{
      background: var(--success) !important;
      color: white !important;
      border-color: var(--success) !important;
    }}
    .sheet-cell.wrong {{
      background: var(--danger) !important;
      color: white !important;
      border-color: var(--danger) !important;
    }}
    .sheet-drawer-footer {{
      padding: 16px 20px;
      border-top: 1px solid var(--border-color);
      background: var(--bg-surface);
    }}

    /* ==========================================================================
       Modals
       ========================================================================== */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(4px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-backdrop.open {{
      display: flex;
    }}
    .modal-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      max-width: 650px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
      padding: 28px;
      position: relative;
    }}
    .modal-close-btn {{
      position: absolute;
      top: 18px;
      right: 18px;
      background: transparent;
      border: none;
      font-size: 1.2rem;
      color: var(--text-muted);
      cursor: pointer;
    }}

    .scorecard-hero {{
      text-align: center;
      padding: 20px 0;
      border-bottom: 1px solid var(--border-color);
      margin-bottom: 20px;
    }}
    .score-big-num {{
      font-size: 3.5rem;
      font-weight: 900;
      color: var(--primary);
      line-height: 1;
      font-family: ui-monospace, SFMono-Regular, monospace;
    }}
    .score-scaled-pill {{
      display: inline-block;
      margin-top: 10px;
      padding: 6px 16px;
      background: var(--primary-subtle);
      border: 1px solid var(--primary-border);
      border-radius: 9999px;
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--primary);
    }}
    .score-rating {{
      margin-top: 8px;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
    }}
    .score-breakdown-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 20px;
    }}
    .score-breakdown-card {{
      background: var(--bg-subtle);
      border-radius: 10px;
      padding: 12px;
      text-align: center;
    }}
    .score-bd-title {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-bottom: 4px;
    }}
    .score-bd-score {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--text-main);
    }}

    .dict-popover {{
      position: fixed;
      z-index: 120;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 14px 18px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
      width: 320px;
      display: none;
    }}
    .dict-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }}
    .dict-word-text {{
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--primary);
    }}
    .dict-phonetic {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-family: ui-monospace, SFMono-Regular, monospace;
    }}
    .dict-trans {{
      font-size: 0.9rem;
      line-height: 1.5;
      color: var(--text-main);
      margin-bottom: 10px;
    }}

    @media (max-width: 900px) {{
      .split-layout-wrapper {{
        flex-direction: column;
      }}
      .split-resizer {{
        display: none;
      }}
      .pane-transcript, .pane-questions {{
        max-height: none;
        flex: 1 1 100%;
      }}
    }}
  </style>
</head>
<body>

  <!-- Audio Player Element (Global) -->
  <audio id="globalAudioPlayer" preload="metadata"></audio>

  <!-- ==========================================================================
       Header
       ========================================================================== -->
  <header class="app-header">
    <div class="container header-content">
      <div class="brand-area" onclick="showHubView()">
        <div class="brand-logo">🎧</div>
        <div>
          <div class="brand-title">
            CET-6 英语六级历年听力真题全真研习平台
            <span class="badge badge-primary">2019-2025 全套27套原版音频与双语原文</span>
          </div>
        </div>
      </div>

      <div class="header-actions">
        <!-- Layout Switcher (Split vs Transcript vs Console) -->
        <div class="layout-switch-group" id="headerLayoutSwitcher" style="display: none;">
          <button class="layout-btn active" id="btnLayoutSplit" onclick="setLayout('split')" title="听读分栏：左看真题原文，右边做题对照">
            🎧 听读分栏
          </button>
          <button class="layout-btn" id="btnLayoutTranscript" onclick="setLayout('transcript-only')" title="沉浸式纯原文精读与跟读">
            📖 纯原文
          </button>
          <button class="layout-btn" id="btnLayoutConsole" onclick="setLayout('console-only')" title="纯考卷做题模考">
            📝 纯做题
          </button>
        </div>

        <!-- Word Lookup Toggle -->
        <button class="btn btn-sm btn-outline" id="btnWordLookupToggle" onclick="toggleWordLookupMode()" title="点词查义开关">
          🔍 点词查义: <span id="wordLookupStatus" style="font-weight: 700; color: var(--primary);">开启</span>
        </button>

        <!-- Mode Switcher (Exam vs Study) -->
        <div class="mode-switch-group">
          <button class="mode-btn active" id="btnModeExam" onclick="switchMode('exam')" title="全真模考模式：30分钟考场倒计时">
            ⏱️ 模考
          </button>
          <button class="mode-btn" id="btnModeStudy" onclick="switchMode('study')" title="精听研习模式：即时反馈答案">
            🔍 精听
          </button>
        </div>

        <!-- Timer -->
        <div class="timer-widget" id="examTimerWidget" style="display: none;">
          <span id="timerIcon">⏳</span>
          <span id="timerDisplay">30:00</span>
          <button class="btn btn-sm btn-outline" id="btnTimerToggle" onclick="toggleTimer()" style="padding: 2px 6px;">暂停</button>
        </div>

        <button class="btn btn-outline btn-sm" onclick="openStrategiesModal()" title="六级听力战法技巧">
          💡 秘籍
        </button>

        <button class="btn btn-outline btn-sm" onclick="openShortcutsModal()" title="快捷键指南">
          ⌨️ 快捷键
        </button>

        <button class="btn btn-outline btn-sm" onclick="toggleTheme()" title="切换明亮/深色模式">
          🌓
        </button>

        <button class="btn btn-primary btn-sm" id="btnHeaderHub" onclick="showHubView()" style="display: none;">
          📋 返回大厅
        </button>
      </div>
    </div>
  </header>

  <!-- ==========================================================================
       Sticky Audio Player Bar
       ========================================================================== -->
  <div class="sticky-player-bar" id="stickyPlayerBar" style="display: none;">
    <div class="container player-container">
      <div class="player-top-row">
        <!-- Track Title -->
        <div class="player-track-info">
          <div class="player-disc-icon" id="discIcon">🎵</div>
          <div class="player-title-box">
            <div class="player-exam-title" id="playerTrackTitle">未选择试卷</div>
            <div class="player-sub-status">
              <span id="audioSourceStatus">就绪</span>
              <span>·</span>
              <span id="audioCurrentSectionLabel">Section A</span>
            </div>
          </div>
        </div>

        <!-- Transport Controls -->
        <div class="player-transport">
          <button class="btn-circle" onclick="seekRelative(-15)" title="快退15秒">⏪ 15s</button>
          <button class="btn-circle" onclick="seekRelative(-5)" title="快退5秒 (左箭头 / J)">◀ 5s</button>
          <button class="btn-circle btn-play-pause" id="btnPlayPause" onclick="togglePlayPause()" title="播放/暂停 (空格 / K)">▶</button>
          <button class="btn-circle" onclick="seekRelative(5)" title="快进5秒 (右箭头 / L)">5s ▶</button>
          <button class="btn-circle" onclick="seekRelative(15)" title="快进15秒">15s ⏩</button>
        </div>

        <!-- Section Jumpers -->
        <div class="section-jumpers">
          <button class="btn btn-sm btn-outline" onclick="jumpToSection('A')" title="快速跳转至长对话">📍 Sec A</button>
          <button class="btn btn-sm btn-outline" onclick="jumpToSection('B')" title="快速跳转至短文理解 (~08:00)">📍 Sec B</button>
          <button class="btn btn-sm btn-outline" onclick="jumpToSection('C')" title="快速跳转至讲座讲话 (~15:00)">📍 Sec C</button>
        </div>

        <!-- Tools: Speed, AB Loop, Audio Loader -->
        <div class="player-tools">
          <select class="speed-select" id="speedSelect" onchange="changePlaybackRate(this.value)">
            <option value="0.75">0.75x</option>
            <option value="0.85">0.85x</option>
            <option value="1.0" selected>1.0x 原速</option>
            <option value="1.15">1.15x 提速</option>
            <option value="1.25">1.25x 冲刺</option>
            <option value="1.5">1.5x 飞速</option>
          </select>

          <button class="btn btn-sm btn-outline ab-loop-btn" id="btnSetA" onclick="setLoopPointA()" title="设置A点">设A点</button>
          <button class="btn btn-sm btn-outline ab-loop-btn" id="btnSetB" onclick="setLoopPointB()" title="设置B点">设B点</button>
          <button class="btn btn-sm btn-outline" id="btnClearAB" onclick="clearLoopAB()" style="display: none;" title="取消AB循环">✕ 取消</button>

          <label class="btn btn-sm btn-outline" style="cursor: pointer;" title="若浏览器限制本地音频自动读取，可手动选取本套音频或拖拽至此">
            📂 导入音频
            <input type="file" id="localAudioFileInput" accept="audio/*" style="display: none;" onchange="handleManualAudioFile(event)">
          </label>
        </div>
      </div>

      <!-- Scrubber Row -->
      <div class="player-progress-row">
        <span class="time-badge" id="timeCurrent">00:00</span>
        <div class="progress-bar-wrap" id="progressBarWrap" onclick="seekProgressBar(event)">
          <div class="progress-bar-fill" id="progressBarFill"></div>
          <div class="progress-loop-range" id="progressLoopRange"></div>
        </div>
        <span class="time-badge" id="timeDuration">27:30</span>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       View 1: Exam Hub
       ========================================================================== -->
  <main class="container exam-hub-view" id="examHubView">
    <div class="hub-hero">
      <h1>CET-6 英语六级历年真题听力全真研习平台</h1>
      <p>
        收录 2019 年至 2025 年全部 27 套官方六级听力真题，包含 675 道原题、官方原版高清录音及<strong>逐题对齐中英双语听力原文</strong>。
        全新支持【🎧 边听边看听读分栏】、【🎬 随音滚动高亮】、【💡 考点线索溯源定位】、【AB循环反复精听】与【点词即查英汉字典】。
      </p>

      <div class="hub-stats-row">
        <div class="hub-stat-card">
          <div class="hub-stat-label">总真题套数</div>
          <div class="hub-stat-val">27 套</div>
        </div>
        <div class="hub-stat-card">
          <div class="hub-stat-label">已练套数</div>
          <div class="hub-stat-val" id="statCompletedSets">0 / 27</div>
        </div>
        <div class="hub-stat-card">
          <div class="hub-stat-label">累计做题量</div>
          <div class="hub-stat-val" id="statAnsweredQuestions">0 / 675</div>
        </div>
        <div class="hub-stat-card">
          <div class="hub-stat-label">平均正确率</div>
          <div class="hub-stat-val" id="statAvgAccuracy">0.0%</div>
        </div>
        <div class="hub-stat-card">
          <div class="hub-stat-label">平均折算分 (710分制)</div>
          <div class="hub-stat-val" id="statAvgScaledScore">0.0 / 248.5</div>
        </div>
      </div>
    </div>

    <!-- Filters & Search -->
    <div class="hub-filter-bar">
      <div class="hub-tabs">
        <button class="hub-tab-btn active" onclick="filterExams('all', this)">全部真题 (27)</button>
        <button class="hub-tab-btn" onclick="filterExams('2024-2025', this)">2024-2025 最新 (6)</button>
        <button class="hub-tab-btn" onclick="filterExams('2022-2023', this)">2022-2023 经典 (9)</button>
        <button class="hub-tab-btn" onclick="filterExams('2019-2021', this)">2019-2021 特训 (12)</button>
        <button class="hub-tab-btn" onclick="filterExams('done', this)">已完成</button>
        <button class="hub-tab-btn" onclick="filterExams('undone', this)">未完成</button>
      </div>

      <div style="display: flex; gap: 10px; align-items: center;">
        <div class="hub-search-box">
          <span class="hub-search-icon">🔍</span>
          <input type="text" class="hub-search-input" id="hubSearchInput" placeholder="搜索年份/月份 (如 2024, 12月)..." oninput="searchExams(this.value)">
        </div>
        <button class="btn btn-primary" onclick="startRandomExam()">🎲 随机抽一套真题</button>
      </div>
    </div>

    <!-- Exams Grid -->
    <div class="exams-grid" id="examsGrid">
      <!-- Injected by JS -->
    </div>
  </main>

  <!-- ==========================================================================
       View 2: Workspace View (Dual-Pane Split Screen / 边听边看)
       ========================================================================== -->
  <main class="container workspace-view" id="workspaceView">
    <!-- Workspace Top Banner -->
    <div class="workspace-top-bar">
      <div>
        <h2 id="workspaceExamTitle" style="font-size: 1.25rem; font-weight: 800; color: var(--text-main);">2024年12月 六级听力真题 (第1套)</h2>
        <div style="font-size: 0.85rem; color: var(--text-muted); display: flex; gap: 10px; align-items: center;">
          <span>🎧 录音时长: <strong id="workspaceDuration">27:46</strong></span>
          <span>·</span>
          <span>共 25 题 · 满分 248.5 分</span>
          <span>·</span>
          <span class="badge badge-primary" id="currentModeBadge">全真模考模式</span>
        </div>
      </div>
      <div style="display: flex; gap: 8px; align-items: center;">
        <button class="btn btn-outline btn-sm" onclick="resetCurrentExam()">🔄 重做本套</button>
        <button class="btn btn-primary btn-sm" onclick="openAnswerSheet()">📑 答题卡 (<span id="answeredPillCount">0</span>/25)</button>
      </div>
    </div>

    <!-- Split Panes Wrapper -->
    <div class="split-layout-wrapper" id="splitLayoutWrapper">
      <!-- ================= Left Pane: Transcript Reader ================= -->
      <section class="pane-transcript" id="paneTranscript">
        <div class="pane-transcript-header">
          <div style="font-weight: 800; font-size: 0.95rem; color: var(--text-main); display: flex; align-items: center; gap: 6px;">
            <span>📜 听力真题原文研习</span>
            <span class="badge badge-primary">边听边看</span>
          </div>

          <div style="display: flex; align-items: center; gap: 6px;">
            <!-- Language Mode Selector -->
            <button class="btn btn-sm btn-outline" id="btnLangBilingual" onclick="setTranscriptLanguage('bilingual')">中英双语</button>
            <button class="btn btn-sm btn-outline" id="btnLangEnOnly" onclick="setTranscriptLanguage('en')">仅英文</button>
            <button class="btn btn-sm btn-outline" id="btnLangZhOnly" onclick="setTranscriptLanguage('zh')">仅中文</button>
            
            <!-- Auto-scroll Toggle -->
            <button class="btn btn-sm btn-outline" id="btnAutoScroll" onclick="toggleAutoScroll()" title="自动随音频滚动至当前朗读段落">
              🎬 随音滚动: <span id="autoScrollStatus" style="font-weight: 700; color: var(--primary);">开启</span>
            </button>
          </div>
        </div>

        <div class="pane-transcript-body" id="paneTranscriptBody">
          <!-- Injected by JS -->
        </div>
      </section>

      <!-- ================= Center Resizer ================= -->
      <div class="split-resizer" id="splitResizer"></div>

      <!-- ================= Right Pane: Questions & Console ================= -->
      <section class="pane-questions" id="paneQuestions">
        <div class="pane-questions-header">
          <div style="font-weight: 800; font-size: 0.95rem; color: var(--text-main); display: flex; align-items: center; gap: 6px;">
            <span>📝 试题作答区</span>
            <span class="badge badge-primary">Q1 - Q25</span>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <button class="btn btn-sm btn-outline" onclick="scrollToQuestion(1)">跳转 Q1</button>
            <button class="btn btn-sm btn-outline" onclick="scrollToQuestion(9)">跳转 Q9 (Sec B)</button>
            <button class="btn btn-sm btn-outline" onclick="scrollToQuestion(16)">跳转 Q16 (Sec C)</button>
          </div>
        </div>

        <div class="pane-questions-body" id="paneQuestionsBody">
          <!-- Injected by JS -->
        </div>
      </section>
    </div>
  </main>

  <!-- ==========================================================================
       Floating Answer Sheet Drawer Toggle
       ========================================================================== -->
  <button class="floating-sheet-toggle" id="floatingSheetToggle" onclick="toggleAnswerSheetDrawer()" style="display: none;">
    📑 答题卡 (<span id="floatingAnsweredCount">0</span>/25)
  </button>

  <!-- ==========================================================================
       Sliding Answer Sheet Drawer
       ========================================================================== -->
  <aside class="sheet-drawer" id="sheetDrawer">
    <div class="sheet-drawer-header">
      <div class="sheet-drawer-title">答题卡 (Answer Sheet)</div>
      <button class="btn-circle" onclick="toggleAnswerSheetDrawer()">✕</button>
    </div>
    <div class="sheet-drawer-body">
      <div class="sheet-progress-summary">
        <span>已作答: <strong id="sheetDrawerAnsweredCount">0</strong> / 25 题</span>
        <span id="sheetDrawerAccuracyLabel"></span>
      </div>

      <div class="sheet-grid" id="sheetGrid">
        <!-- 25 Cells generated by JS -->
      </div>

      <div style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 15px;">
        💡 提示：点击题号可平滑滚动至对应题目；黄色星标表示标记存疑题目。
      </div>
    </div>
    <div class="sheet-drawer-footer">
      <button class="btn btn-primary" style="width: 100%; padding: 12px;" onclick="confirmSubmitExam()">
        交卷并查看学情诊断报告
      </button>
    </div>
  </aside>

  <!-- ==========================================================================
       Scorecard Modal
       ========================================================================== -->
  <div class="modal-backdrop" id="scorecardModal">
    <div class="modal-card">
      <button class="modal-close-btn" onclick="closeModal('scorecardModal')">✕</button>

      <div class="scorecard-hero">
        <div style="font-size: 0.95rem; font-weight: 700; color: var(--text-muted); margin-bottom: 8px;" id="modalExamTitle">
          2024年12月 六级听力真题
        </div>
        <div class="score-big-num" id="modalRawScore">22 <span style="font-size: 1.8rem; color: var(--text-muted); font-weight: 600;">/ 25</span></div>
        <div class="score-scaled-pill" id="modalScaledScore">折算分: 220.1 / 248.5 分</div>
        <div class="score-rating" id="modalRatingText">👑 六级听力卓越 · 冲刺600+</div>
      </div>

      <div class="score-breakdown-grid">
        <div class="score-breakdown-card">
          <div class="score-bd-title">Section A 长对话</div>
          <div class="score-bd-score" id="modalSecAScore">7 / 8</div>
          <div style="font-size: 0.72rem; color: var(--text-muted);" id="modalSecAScaled">49.7 / 56.8分</div>
        </div>
        <div class="score-breakdown-card">
          <div class="score-bd-title">Section B 听力篇章</div>
          <div class="score-bd-score" id="modalSecBScore">6 / 7</div>
          <div style="font-size: 0.72rem; color: var(--text-muted);" id="modalSecBScaled">42.6 / 49.7分</div>
        </div>
        <div class="score-breakdown-card">
          <div class="score-bd-title">Section C 讲座讲话 (双倍)</div>
          <div class="score-bd-score" id="modalSecCScore">9 / 10</div>
          <div style="font-size: 0.72rem; color: var(--text-muted);" id="modalSecCScaled">127.8 / 142.0分</div>
        </div>
      </div>

      <div style="background: var(--bg-subtle); border-radius: 10px; padding: 14px 18px; margin-bottom: 20px;">
        <div style="font-weight: 700; font-size: 0.9rem; margin-bottom: 6px; color: var(--text-main);">
          🎯 智能学情诊断与复习建议:
        </div>
        <div style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;" id="modalDiagnosticAdvice">
          分析生成中...
        </div>
      </div>

      <div style="display: flex; gap: 8px; margin-bottom: 14px;">
        <button class="btn btn-sm btn-primary" id="btnFilterAll" onclick="filterModalQuestions('all')">全部题目 (25)</button>
        <button class="btn btn-sm btn-outline" id="btnFilterWrong" onclick="filterModalQuestions('wrong')">仅看错题</button>
        <button class="btn btn-sm btn-outline" id="btnFilterFlagged" onclick="filterModalQuestions('flagged')">仅看标记题</button>
      </div>

      <div id="modalQuestionsTable" style="max-height: 200px; overflow-y: auto; border: 1px solid var(--border-color); border-radius: 8px; padding: 10px; margin-bottom: 20px;">
        <!-- Injected by JS -->
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
        <button class="btn btn-secondary" onclick="retryMistakes()">🔄 错题专项强化</button>
        <button class="btn btn-primary" onclick="switchToStudyAndCloseModal()">🔍 进入精听解析模式</button>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       Strategies & Traps Modal
       ========================================================================== -->
  <div class="modal-backdrop" id="strategiesModal">
    <div class="modal-card">
      <button class="modal-close-btn" onclick="closeModal('strategiesModal')">✕</button>
      <h3 style="font-size: 1.3rem; font-weight: 800; margin-bottom: 16px;">💡 大学英语六级听力核心战法与通关秘籍</h3>
      
      <div style="font-size: 0.9rem; line-height: 1.7; color: var(--text-main); display: flex; flex-direction: column; gap: 14px;">
        <div style="background: var(--bg-subtle); padding: 14px; border-radius: 10px; border-left: 4px solid var(--primary);">
          <strong>1. 预读选项三步法（听前定乾坤）</strong><br>
          • <strong>划主干</strong>：迅速圈画每个选项的名词、动词及核心修饰语。<br>
          • <strong>纵向对比</strong>：寻找4个选项的共同点（锁定对话话题）与差异点（锁定出题切入角度）。<br>
          • <strong>预判提问</strong>：动作建议类通常问下一步行动；观点态度类通常问对某事的看法；原因结果类通常问产生问题的主因。
        </div>

        <div style="background: var(--bg-subtle); padding: 14px; border-radius: 10px; border-left: 4px solid var(--success);">
          <strong>2. 视听一致与同义替换原则</strong><br>
          • <strong>Section A (长对话)</strong>：视听一致率高达 70%！听到什么选什么，特别留意转折词 <em>but, however, actually</em> 后的关键信息。<br>
          • <strong>Section B (篇章) & Section C (讲座)</strong>：侧重<strong>同义替换</strong>与首尾总结！例如听力原文为 <em>"cut down expenses"</em>，选项替换为 <em>"reduce costs"</em>。
        </div>

        <div style="background: var(--bg-subtle); padding: 14px; border-radius: 10px; border-left: 4px solid var(--warning);">
          <strong>3. Section C 双倍分值破解心法（冲分核武器！）</strong><br>
          • 六级听力 Section C 每题占 <strong>14.2分</strong>（前两部分每题仅 7.1分），错两道相当于错别人四道！<br>
          • 讲座开篇 30 秒必交代核心主题与学术背景；文中出现数字例证后，<strong>必有转折总结句</strong>，此处 90% 出题！
        </div>

        <div style="background: var(--bg-subtle); padding: 14px; border-radius: 10px; border-left: 4px solid var(--danger);">
          <strong>4. 考场走神应急策略</strong><br>
          • 六级听力仅播放一次！若某一题走神错过，<strong>切忌纠缠回忆</strong>，果断依据选项常识排除并标记星号，立刻全身心投入下一题的预读！
        </div>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       Shortcuts Modal
       ========================================================================== -->
  <div class="modal-backdrop" id="shortcutsModal">
    <div class="modal-card" style="max-width: 480px;">
      <button class="modal-close-btn" onclick="closeModal('shortcutsModal')">✕</button>
      <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 16px;">⌨️ 全键盘快捷键指南</h3>
      <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem;">
        <tr style="border-bottom: 1px solid var(--border-color);">
          <th style="text-align: left; padding: 8px 0; color: var(--text-muted);">按键</th>
          <th style="text-align: left; padding: 8px 0; color: var(--text-muted);">操作功能</th>
        </tr>
        <tr><td style="padding: 8px 0;"><kbd>Space</kbd> 或 <kbd>K</kbd></td><td>播放 / 暂停音频</td></tr>
        <tr><td style="padding: 8px 0;"><kbd>←</kbd> 或 <kbd>J</kbd></td><td>快退 5 秒</td></tr>
        <tr><td style="padding: 8px 0;"><kbd>→</kbd> 或 <kbd>L</kbd></td><td>快进 5 秒</td></tr>
        <tr><td style="padding: 8px 0;"><kbd>Shift + ←</kbd></td><td>快退 15 秒</td></tr>
        <tr><td style="padding: 8px 0;"><kbd>Shift + →</kbd></td><td>快进 15 秒</td></tr>
        <tr><td style="padding: 8px 0;"><kbd>[</kbd> / <kbd>]</kbd></td><td>降低 / 增加播放倍速</td></tr>
        <tr><td style="padding: 8px 0;"><kbd>A</kbd> / <kbd>B</kbd> / <kbd>C</kbd> / <kbd>D</kbd></td><td>为当前聚焦题目选择对应选项</td></tr>
        <tr><td style="padding: 8px 0;"><kbd>F</kbd></td><td>标记 / 取消存疑 (★)</td></tr>
        <tr><td style="padding: 8px 0;"><kbd>?</kbd></td><td>打开本快捷键指南</td></tr>
      </table>
    </div>
  </div>

  <!-- ==========================================================================
       Dictionary Popover
       ========================================================================== -->
  <div class="dict-popover" id="dictPopover" onclick="event.stopPropagation()">
    <div class="dict-header">
      <div>
        <div class="dict-word-text" id="dictWordText">word</div>
        <div class="dict-phonetic" id="dictPhonetic">/wɜːd/</div>
      </div>
      <div style="display: flex; gap: 4px;">
        <button class="btn btn-sm btn-outline" onclick="speakCurrentWord()" title="发音">🔊</button>
        <button class="btn btn-sm btn-outline" onclick="closeDictPopover()">✕</button>
      </div>
    </div>
    <div class="dict-trans" id="dictTrans">释义加载中...</div>
    <div style="font-size: 0.75rem; color: var(--text-muted);" id="dictRootHint"></div>
  </div>

  <!-- ==========================================================================
       Application JavaScript Logic
       ========================================================================== -->
  <script>
    const EXAMS_DATA = {exams_json};
    const DICT_DATA = {dict_json};

    let currentExam = null;
    let currentMode = 'exam'; // 'exam' | 'study'
    let currentLayout = 'split'; // 'split' | 'transcript-only' | 'console-only'
    let transcriptLang = 'bilingual'; // 'bilingual' | 'en' | 'zh'
    let isAutoScroll = true;
    let isWordLookupEnabled = true;

    let currentFilter = 'all';
    let focusedQuestionNum = 1;
    let timerInterval = null;
    let timerSeconds = 1800; // 30 minutes
    let isTimerRunning = false;
    let loopA = null;
    let loopB = null;

    const audio = document.getElementById('globalAudioPlayer');
    const examHubView = document.getElementById('examHubView');
    const workspaceView = document.getElementById('workspaceView');
    const stickyPlayerBar = document.getElementById('stickyPlayerBar');
    const discIcon = document.getElementById('discIcon');
    const btnPlayPause = document.getElementById('btnPlayPause');
    const progressBarFill = document.getElementById('progressBarFill');
    const progressLoopRange = document.getElementById('progressLoopRange');
    const timeCurrent = document.getElementById('timeCurrent');
    const timeDuration = document.getElementById('timeDuration');
    const floatingSheetToggle = document.getElementById('floatingSheetToggle');
    const sheetDrawer = document.getElementById('sheetDrawer');

    window.addEventListener('DOMContentLoaded', () => {{
      initTheme();
      renderHubExams();
      updateHubStats();
      initAudioListeners();
      initKeyboardListeners();
      initClickOutsideListeners();
      initDragDropAudio();
      initSplitResizer();
    }});

    function initTheme() {{
      const savedTheme = localStorage.getItem('cet6_listen_theme') || 'light';
      document.documentElement.setAttribute('data-theme', savedTheme);
    }}

    function toggleTheme() {{
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('cet6_listen_theme', next);
    }}

    function toggleWordLookupMode() {{
      isWordLookupEnabled = !isWordLookupEnabled;
      const statusEl = document.getElementById('wordLookupStatus');
      statusEl.textContent = isWordLookupEnabled ? '开启' : '关闭';
      statusEl.style.color = isWordLookupEnabled ? 'var(--primary)' : 'var(--text-muted)';
      renderQuestions();
      renderTranscripts();
    }}

    // ==========================================================================
    // Layout Management (Split vs Transcript vs Console)
    // ==========================================================================
    function setLayout(mode) {{
      currentLayout = mode;
      const wrapper = document.getElementById('splitLayoutWrapper');
      wrapper.className = 'split-layout-wrapper ' + (mode === 'split' ? '' : mode);

      document.getElementById('btnLayoutSplit').className = mode === 'split' ? 'layout-btn active' : 'layout-btn';
      document.getElementById('btnLayoutTranscript').className = mode === 'transcript-only' ? 'layout-btn active' : 'layout-btn';
      document.getElementById('btnLayoutConsole').className = mode === 'console-only' ? 'layout-btn active' : 'layout-btn';
    }}

    function initSplitResizer() {{
      const resizer = document.getElementById('splitResizer');
      const leftPane = document.getElementById('paneTranscript');
      const rightPane = document.getElementById('paneQuestions');
      let isResizing = false;

      resizer.addEventListener('mousedown', (e) => {{
        isResizing = true;
        resizer.classList.add('resizing');
        document.body.style.cursor = 'col-resize';
      }});

      window.addEventListener('mousemove', (e) => {{
        if (!isResizing) return;
        const containerRect = document.getElementById('splitLayoutWrapper').getBoundingClientRect();
        const offset = e.clientX - containerRect.left;
        const totalWidth = containerRect.width;
        const pct = Math.max(20, Math.min(80, (offset / totalWidth) * 100));

        leftPane.style.flex = `0 0 ${{pct}}%`;
        rightPane.style.flex = `0 0 ${{100 - pct}}%`;
      }});

      window.addEventListener('mouseup', () => {{
        if (isResizing) {{
          isResizing = false;
          resizer.classList.remove('resizing');
          document.body.style.cursor = 'default';
        }}
      }});
    }}

    function setTranscriptLanguage(lang) {{
      transcriptLang = lang;
      document.getElementById('btnLangBilingual').className = lang === 'bilingual' ? 'btn btn-sm btn-primary' : 'btn btn-sm btn-outline';
      document.getElementById('btnLangEnOnly').className = lang === 'en' ? 'btn btn-sm btn-primary' : 'btn btn-sm btn-outline';
      document.getElementById('btnLangZhOnly').className = lang === 'zh' ? 'btn btn-sm btn-primary' : 'btn btn-sm btn-outline';
      renderTranscripts();
    }}

    function toggleAutoScroll() {{
      isAutoScroll = !isAutoScroll;
      const statusEl = document.getElementById('autoScrollStatus');
      statusEl.textContent = isAutoScroll ? '开启' : '关闭';
      statusEl.style.color = isAutoScroll ? 'var(--primary)' : 'var(--text-muted)';
    }}

    // ==========================================================================
    // Hub View Logic
    // ==========================================================================
    function showHubView() {{
      workspaceView.style.display = 'none';
      stickyPlayerBar.style.display = 'none';
      floatingSheetToggle.style.display = 'none';
      document.getElementById('examTimerWidget').style.display = 'none';
      document.getElementById('btnHeaderHub').style.display = 'none';
      document.getElementById('headerLayoutSwitcher').style.display = 'none';
      examHubView.style.display = 'block';

      if (!audio.paused) {{
        audio.pause();
      }}
      stopTimer();
      renderHubExams();
      updateHubStats();
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function renderHubExams(searchQuery = '') {{
      const grid = document.getElementById('examsGrid');
      grid.innerHTML = '';

      const query = searchQuery.trim().toLowerCase();

      EXAMS_DATA.forEach(ex => {{
        if (currentFilter === '2024-2025' && !(ex.year === '2024' || ex.year === '2025')) return;
        if (currentFilter === '2022-2023' && !(ex.year === '2022' || ex.year === '2023')) return;
        if (currentFilter === '2019-2021' && !(ex.year === '2019' || ex.year === '2020' || ex.year === '2021')) return;

        const record = getExamRecord(ex.id);
        const isDone = record && record.submitted;

        if (currentFilter === 'done' && !isDone) return;
        if (currentFilter === 'undone' && isDone) return;

        if (query) {{
          const matchTitle = ex.title.toLowerCase().includes(query);
          const matchYear = ex.year.includes(query);
          const matchMonth = ex.month.includes(query);
          if (!matchTitle && !matchYear && !matchMonth) return;
        }}

        const card = document.createElement('div');
        card.className = 'exam-card';

        let scoreLabel = '未作答';
        let scaledLabel = '0.0 / 248.5分';
        let badgeStatus = '<span class="badge badge-primary">真题原卷</span>';

        if (isDone) {{
          scoreLabel = `${{record.rawScore}} / 25 题`;
          scaledLabel = `${{record.scaledScore.toFixed(1)}} / 248.5分`;
          badgeStatus = record.scaledScore >= 180 ? 
            '<span class="badge badge-success">已通过 · 优秀</span>' : 
            '<span class="badge badge-warning">已作答</span>';
        }}

        card.innerHTML = `
          <div>
            <div class="exam-card-header">
              <div class="exam-card-title">${{ex.title}}</div>
              ${{badgeStatus}}
            </div>
            <div class="exam-card-tags">
              <span class="badge badge-primary">🎧 ${{ex.duration_label}}</span>
              <span class="badge badge-primary">25题完整版</span>
              <span class="badge badge-primary">双语原文全对照</span>
            </div>
            <div class="exam-card-stats">
              <div class="exam-card-stat-item">
                <span class="exam-card-stat-lbl">历史得分</span>
                <span class="exam-card-stat-val">${{scoreLabel}}</span>
              </div>
              <div class="exam-card-stat-item">
                <span class="exam-card-stat-lbl">710分制折算</span>
                <span class="exam-card-stat-val" style="color: var(--primary);">${{scaledLabel}}</span>
              </div>
            </div>
          </div>
          <div class="exam-card-actions">
            <button class="btn btn-primary" onclick="openExam('${{ex.id}}', 'exam')">⏱️ 边听边做</button>
            <button class="btn btn-secondary" onclick="openExam('${{ex.id}}', 'study')">📖 双语精听</button>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    function filterExams(type, el) {{
      currentFilter = type;
      document.querySelectorAll('.hub-tab-btn').forEach(b => b.classList.remove('active'));
      if (el) el.classList.add('active');
      renderHubExams(document.getElementById('hubSearchInput').value);
    }}

    function searchExams(val) {{
      renderHubExams(val);
    }}

    function startRandomExam() {{
      const randIdx = Math.floor(Math.random() * EXAMS_DATA.length);
      openExam(EXAMS_DATA[randIdx].id, 'exam');
    }}

    function updateHubStats() {{
      let completedCount = 0;
      let totalAnswered = 0;
      let totalRawSum = 0;
      let totalScaledSum = 0;

      EXAMS_DATA.forEach(ex => {{
        const rec = getExamRecord(ex.id);
        if (rec && rec.submitted) {{
          completedCount++;
          totalAnswered += 25;
          totalRawSum += rec.rawScore;
          totalScaledSum += rec.scaledScore;
        }} else if (rec && rec.answers) {{
          totalAnswered += Object.keys(rec.answers).length;
        }}
      }});

      document.getElementById('statCompletedSets').textContent = `${{completedCount}} / ${{EXAMS_DATA.length}}`;
      document.getElementById('statAnsweredQuestions').textContent = `${{totalAnswered}} / 675`;

      if (completedCount > 0) {{
        const avgAcc = ((totalRawSum / (completedCount * 25)) * 100).toFixed(1);
        const avgScaled = (totalScaledSum / completedCount).toFixed(1);
        document.getElementById('statAvgAccuracy').textContent = `${{avgAcc}}%`;
        document.getElementById('statAvgScaledScore').textContent = `${{avgScaled}} / 248.5`;
      }} else {{
        document.getElementById('statAvgAccuracy').textContent = '0.0%';
        document.getElementById('statAvgScaledScore').textContent = '0.0 / 248.5';
      }}
    }}

    // ==========================================================================
    // Workspace & Answering Logic
    // ==========================================================================
    function openExam(examId, mode = 'exam') {{
      currentExam = EXAMS_DATA.find(e => e.id === examId);
      if (!currentExam) return;

      currentMode = mode;

      examHubView.style.display = 'none';
      workspaceView.style.display = 'block';
      stickyPlayerBar.style.display = 'block';
      floatingSheetToggle.style.display = 'flex';
      document.getElementById('btnHeaderHub').style.display = 'inline-flex';
      document.getElementById('headerLayoutSwitcher').style.display = 'flex';

      document.getElementById('workspaceExamTitle').textContent = currentExam.title;
      document.getElementById('workspaceDuration').textContent = currentExam.duration_label;
      document.getElementById('playerTrackTitle').textContent = currentExam.title;

      updateModeUI();
      renderQuestions();
      renderTranscripts();
      setupAudioForCurrentExam();

      if (currentMode === 'exam') {{
        startTimer();
      }} else {{
        stopTimer();
      }}

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function updateModeUI() {{
      const btnExam = document.getElementById('btnModeExam');
      const btnStudy = document.getElementById('btnModeStudy');
      const modeBadge = document.getElementById('currentModeBadge');
      const timerWidget = document.getElementById('examTimerWidget');

      if (currentMode === 'exam') {{
        btnExam.classList.add('active');
        btnStudy.classList.remove('active');
        modeBadge.textContent = '全真模考模式';
        modeBadge.className = 'badge badge-primary';
        timerWidget.style.display = 'flex';
      }} else {{
        btnStudy.classList.add('active');
        btnExam.classList.remove('active');
        modeBadge.textContent = '精听研习模式 (答案解析即时显示)';
        modeBadge.className = 'badge badge-warning';
        timerWidget.style.display = 'none';
      }}
    }}

    function switchMode(newMode) {{
      if (currentMode === newMode) return;
      currentMode = newMode;
      updateModeUI();
      renderQuestions();
      renderTranscripts();
    }}

    // ==========================================================================
    // Render Transcripts (Left Pane)
    // ==========================================================================
    function renderTranscripts() {{
      const container = document.getElementById('paneTranscriptBody');
      container.innerHTML = '';

      if (!currentExam || !currentExam.transcripts || !currentExam.transcripts.parts) {{
        container.innerHTML = '<div style="color: var(--text-muted); padding: 20px;">暂无本套真题的结构化原文。</div>';
        return;
      }}

      const parts = currentExam.transcripts.parts;

      parts.forEach((part, partIdx) => {{
        const card = document.createElement('div');
        card.className = 'transcript-part-card';
        card.id = `transcript_part_${{part.part_id}}`;

        let html = `
          <div class="part-header">
            <div>
              <div class="part-title">
                <span>${{part.title}}</span>
                <span class="part-topic-pill">${{part.topic || '话题研习'}}</span>
              </div>
            </div>
            <button class="btn btn-sm btn-outline" onclick="seekAudioTime(${{part.start_time}})" title="从此部分开头播放">
              ▶ ${{part.start_time_str || '00:00'}}
            </button>
          </div>
        `;

        // Render Paragraphs
        part.paragraphs.forEach((p, pIdx) => {{
          const isEvid = p.evidence_q !== undefined;
          const evidQ = p.evidence_q;

          let enText = p.en;
          if (isWordLookupEnabled) {{
            enText = wrapWordsForDict(enText);
          }}

          let zhText = p.zh || '';

          // If evidence, wrap with marker
          let evidBadge = '';
          if (isEvid) {{
            evidBadge = `<span class="evidence-tag" onclick="scrollToQuestion(${{evidQ}})" title="点击直达试题 Q${{evidQ}}">Q${{evidQ}} 答案出处</span>`;
          }}

          html += `
            <div class="transcript-paragraph" id="t_para_${{partIdx}}_${{pIdx}}" data-time="${{p.time}}">
              <div class="paragraph-top-line">
                <div class="spk-badge">
                  <span>${{p.speaker}}</span>
                  ${{evidBadge}}
                </div>
                <button class="spk-play-btn" onclick="seekAudioTime(${{p.time}})" title="播放此句">
                  ▶ ${{p.time_str || '00:00'}}
                </button>
              </div>
              ${{transcriptLang !== 'zh' ? `<div class="p-en-text">${{enText}}</div>` : ''}}
              ${{transcriptLang !== 'en' ? `<div class="p-zh-text">${{zhText}}</div>` : ''}}
            </div>
          `;
        }});

        // Render Spoken Questions
        if (part.questions_audio && part.questions_audio.length > 0) {{
          html += `<div class="spoken-questions-drawer">`;
          html += `<div style="font-size: 0.82rem; font-weight: 700; color: var(--text-muted); margin-bottom: 6px;">🎧 录音提问句速查:</div>`;
          part.questions_audio.forEach(q => {{
            html += `
              <div class="spoken-q-item">
                <strong>Q${{q.q_num}}:</strong> ${{q.stem}}
                <div style="color: var(--text-muted); font-size: 0.78rem;">${{q.stem_zh || ''}}</div>
              </div>
            `;
          }});
          html += `</div>`;
        }}

        card.innerHTML = html;
        container.appendChild(card);
      }});
    }}

    function seekAudioTime(sec) {{
      audio.currentTime = sec;
      if (audio.paused) audio.play();
    }}

    function scrollToTranscriptEvidence(qNum) {{
      setLayout('split');
      const allParas = document.querySelectorAll('.transcript-paragraph');
      for (const p of allParas) {{
        if (p.innerHTML.includes(`Q${{qNum}} 答案出处`)) {{
          p.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
          p.classList.add('active-playing');
          setTimeout(() => {{
            p.classList.remove('active-playing');
          }}, 2500);
          return;
        }}
      }}
    }}

    // ==========================================================================
    // Audio Player Engine
    // ==========================================================================
    function setupAudioForCurrentExam() {{
      if (!currentExam) return;
      clearLoopAB();

      const sources = currentExam.audio_sources;
      let sourceIdx = 0;

      function tryNextSource() {{
        if (sourceIdx < sources.length) {{
          audio.src = sources[sourceIdx];
          sourceIdx++;
        }} else {{
          document.getElementById('audioSourceStatus').textContent = '⚠️ 需导入音频';
          document.getElementById('audioSourceStatus').style.color = 'var(--danger)';
        }}
      }}

      audio.onerror = () => {{
        tryNextSource();
      }};

      audio.oncanplay = () => {{
        document.getElementById('audioSourceStatus').textContent = '音频就绪';
        document.getElementById('audioSourceStatus').style.color = 'var(--success)';
      }};

      tryNextSource();
    }}

    function initAudioListeners() {{
      audio.addEventListener('play', () => {{
        discIcon.classList.add('spinning');
        btnPlayPause.textContent = '⏸';
      }});

      audio.addEventListener('pause', () => {{
        discIcon.classList.remove('spinning');
        btnPlayPause.textContent = '▶';
      }});

      audio.addEventListener('timeupdate', () => {{
        if (!audio.duration) return;

        timeCurrent.textContent = formatTime(audio.currentTime);
        timeDuration.textContent = formatTime(audio.duration);

        const pct = (audio.currentTime / audio.duration) * 100;
        progressBarFill.style.width = `${{pct}}%`;

        if (loopA !== null && loopB !== null && loopB > loopA) {{
          if (audio.currentTime >= loopB || audio.currentTime < loopA) {{
            audio.currentTime = loopA;
          }}
        }}

        updateCurrentSectionBadge(audio.currentTime);
        syncTranscriptActiveParagraph(audio.currentTime);
      }});
    }}

    function syncTranscriptActiveParagraph(currTime) {{
      const paras = document.querySelectorAll('.transcript-paragraph');
      let activePara = null;

      paras.forEach(p => {{
        const pTime = parseFloat(p.dataset.time || 0);
        if (currTime >= pTime) {{
          activePara = p;
        }}
      }});

      paras.forEach(p => p.classList.remove('active-playing'));

      if (activePara) {{
        activePara.classList.add('active-playing');
        if (isAutoScroll && !isUserScrollingTranscript) {{
          activePara.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
        }}
      }}
    }}

    let isUserScrollingTranscript = false;
    let scrollTimeout = null;
    document.addEventListener('DOMContentLoaded', () => {{
      const pane = document.getElementById('paneTranscriptBody');
      if (pane) {{
        pane.addEventListener('wheel', () => {{
          isUserScrollingTranscript = true;
          if (scrollTimeout) clearTimeout(scrollTimeout);
          scrollTimeout = setTimeout(() => {{
            isUserScrollingTranscript = false;
          }}, 2000);
        }});
      }}
    }});

    function formatTime(seconds) {{
      if (isNaN(seconds)) return '00:00';
      const m = Math.floor(seconds / 60);
      const s = Math.floor(seconds % 60);
      return `${{m.toString().padStart(2, '0')}}:${{s.toString().padStart(2, '0')}}`;
    }}

    function updateCurrentSectionBadge(currTime) {{
      const badge = document.getElementById('audioCurrentSectionLabel');
      if (currTime < 480) {{
        badge.textContent = 'Section A (长对话)';
      }} else if (currTime < 900) {{
        badge.textContent = 'Section B (篇章理解)';
      }} else {{
        badge.textContent = 'Section C (讲座讲话)';
      }}
    }}

    function togglePlayPause() {{
      if (audio.paused) {{
        audio.play().catch(e => {{
          console.warn('Playback error or blocked:', e);
        }});
      }} else {{
        audio.pause();
      }}
    }}

    function seekRelative(deltaSeconds) {{
      audio.currentTime = Math.max(0, Math.min(audio.duration || 1800, audio.currentTime + deltaSeconds));
    }}

    function seekProgressBar(e) {{
      const rect = e.currentTarget.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const pct = Math.max(0, Math.min(1, clickX / rect.width));
      if (audio.duration) {{
        audio.currentTime = pct * audio.duration;
      }}
    }}

    function changePlaybackRate(rate) {{
      audio.playbackRate = parseFloat(rate);
    }}

    function jumpToSection(secKey) {{
      if (secKey === 'A') {{
        audio.currentTime = 0;
      }} else if (secKey === 'B') {{
        audio.currentTime = 480;
      }} else if (secKey === 'C') {{
        audio.currentTime = 900;
      }}
      if (audio.paused) audio.play();
    }}

    function setLoopPointA() {{
      loopA = audio.currentTime;
      document.getElementById('btnSetA').classList.add('active');
      document.getElementById('btnSetA').textContent = `A: ${{formatTime(loopA)}}`;
      updateLoopRangeBar();
    }}

    function setLoopPointB() {{
      if (loopA === null) {{
        loopA = Math.max(0, audio.currentTime - 10);
        document.getElementById('btnSetA').classList.add('active');
        document.getElementById('btnSetA').textContent = `A: ${{formatTime(loopA)}}`;
      }}
      loopB = audio.currentTime;
      if (loopB <= loopA) loopB = loopA + 5;
      document.getElementById('btnSetB').classList.add('active');
      document.getElementById('btnSetB').textContent = `B: ${{formatTime(loopB)}}`;
      document.getElementById('btnClearAB').style.display = 'inline-flex';
      updateLoopRangeBar();
      audio.currentTime = loopA;
    }}

    function clearLoopAB() {{
      loopA = null;
      loopB = null;
      const btnA = document.getElementById('btnSetA');
      const btnB = document.getElementById('btnSetB');
      btnA.classList.remove('active');
      btnA.textContent = '设A点';
      btnB.classList.remove('active');
      btnB.textContent = '设B点';
      document.getElementById('btnClearAB').style.display = 'none';
      progressLoopRange.style.display = 'none';
    }}

    function updateLoopRangeBar() {{
      if (!audio.duration || loopA === null) return;
      const startPct = (loopA / audio.duration) * 100;
      progressLoopRange.style.left = `${{startPct}}%`;
      if (loopB !== null) {{
        const endPct = (loopB / audio.duration) * 100;
        progressLoopRange.style.width = `${{endPct - startPct}}%`;
        progressLoopRange.style.display = 'block';
      }}
    }}

    function handleManualAudioFile(e) {{
      const file = e.target.files[0];
      if (!file) return;
      loadAudioFileDirect(file);
    }}

    function loadAudioFileDirect(file) {{
      const objectUrl = URL.createObjectURL(file);
      audio.src = objectUrl;
      audio.play().catch(e => console.warn(e));
      document.getElementById('audioSourceStatus').textContent = '✅ 本地音频已载入';
      document.getElementById('audioSourceStatus').style.color = 'var(--success)';
    }}

    function initDragDropAudio() {{
      window.addEventListener('dragover', (e) => e.preventDefault());
      window.addEventListener('drop', (e) => {{
        e.preventDefault();
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {{
          const file = e.dataTransfer.files[0];
          if (file.name.endsWith('.mp3') || file.type.startsWith('audio/')) {{
            loadAudioFileDirect(file);
          }}
        }}
      }});
    }}

    // ==========================================================================
    // Render Questions (Right Pane)
    // ==========================================================================
    function renderQuestions() {{
      if (!currentExam) return;

      const container = document.getElementById('paneQuestionsBody');
      container.innerHTML = '';

      const record = getExamRecord(currentExam.id) || {{ answers: {{}}, flags: {{}}, notes: {{}}, submitted: false }};
      const isPostExamOrStudy = record.submitted || currentMode === 'study';

      const secOrder = ['A', 'B', 'C'];

      secOrder.forEach(secKey => {{
        const sec = currentExam.sections[secKey];
        if (!sec) return;

        const secWrapper = document.createElement('div');
        secWrapper.id = `section_block_${{secKey}}`;
        secWrapper.style.marginBottom = '24px';

        secWrapper.innerHTML = `
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--text-main);">${{sec.title}}</h4>
            <span class="badge badge-primary">${{sec.weight_label}}</span>
          </div>
        `;

        sec.groups.forEach(grp => {{
          const grpCard = document.createElement('div');
          grpCard.style.marginBottom = '20px';

          let grpHtml = `
            <div style="font-weight: 700; font-size: 0.95rem; margin-bottom: 10px; color: var(--text-muted); display: flex; justify-content: space-between;">
              <span>📖 ${{grp.name}}</span>
              <span class="badge badge-primary">${{grp.range}}</span>
            </div>
          `;

          grp.questions.forEach(q => {{
            const qNum = q.q_num;
            const userChoice = record.answers[qNum] || '';
            const isFlagged = record.flags[qNum] || false;
            const officialAns = currentExam.answers[qNum] || '';
            const userNote = record.notes[qNum] || '';

            const isDoubleWeight = qNum >= 16;
            const weightPill = isDoubleWeight ? 
              '<span class="badge badge-danger">双倍权重 14.2分</span>' : 
              '<span class="badge badge-primary">单选 7.1分</span>';

            grpHtml += `
              <div class="question-block" id="question_item_${{qNum}}" onclick="setFocusedQuestion(${{qNum}})">
                <div class="question-top">
                  <div class="q-number-pill">
                    <span>Q${{qNum}}</span>
                    ${{weightPill}}
                  </div>
                  <div class="q-actions">
                    <button class="btn btn-sm btn-outline" onclick="scrollToTranscriptEvidence(${{qNum}})" title="在左侧原文中高亮定位本题答案出处">
                      📜 原文线索
                    </button>
                    <button class="btn-flag ${{isFlagged ? 'flagged' : ''}}" id="flagBtn_${{qNum}}" onclick="toggleFlag(${{qNum}}, event)">
                      ${{isFlagged ? '★ 存疑' : '☆ 标记'}}
                    </button>
                    <button class="btn btn-sm btn-outline" onclick="speakQuestionOptions(${{qNum}}, event)" title="朗读本题选项">
                      🔊 朗读
                    </button>
                    <button class="btn btn-sm btn-outline" onclick="toggleScratchpad(${{qNum}}, event)" title="速记笔记">
                      📝 笔记
                    </button>
                  </div>
                </div>

                <div class="options-grid" id="options_grid_${{qNum}}">
            `;

            ['A', 'B', 'C', 'D'].forEach(letter => {{
              const optRawText = q.options[letter] || '';
              const optWrappedText = isWordLookupEnabled ? wrapWordsForDict(optRawText) : optRawText;

              let optionClasses = 'option-item';
              if (userChoice === letter) {{
                optionClasses += ' selected';
              }}

              if (isPostExamOrStudy) {{
                if (letter === officialAns) {{
                  optionClasses += ' correct';
                }} else if (userChoice === letter && userChoice !== officialAns) {{
                  optionClasses += ' wrong';
                }}
              }}

              grpHtml += `
                <div class="${{optionClasses}}" id="opt_${{qNum}}_${{letter}}" onclick="selectOption(${{qNum}}, '${{letter}}')">
                  <div class="opt-letter">${{letter}}</div>
                  <div class="opt-text">${{optWrappedText}}</div>
                </div>
              `;
            }});

            grpHtml += `</div>`;

            // Scratchpad
            grpHtml += `
              <div class="scratchpad-wrap" id="scratchpad_${{qNum}}">
                <textarea class="scratchpad-textarea" placeholder="在此速记听力核心词、问句或做题笔记..." oninput="saveNote(${{qNum}}, this.value)">${{userNote}}</textarea>
              </div>
            `;

            // Study Analysis Box
            const isCorrect = userChoice === officialAns;
            const statusTag = isCorrect ? '✅ 回答正确' : '❌ 作答错误';
            const statusColor = isCorrect ? 'var(--success)' : 'var(--danger)';
            const analysisVisible = isPostExamOrStudy ? 'visible' : '';

            grpHtml += `
              <div class="study-analysis-box ${{analysisVisible}}" id="analysis_box_${{qNum}}">
                <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                  <strong>官方标准答案: <span style="color: var(--success); font-size: 1.05rem;" id="analysis_ans_${{qNum}}">${{officialAns}}</span></strong>
                  <span style="color: ${{statusColor}}; font-weight: 700;" id="analysis_status_${{qNum}}">${{statusTag}} (你的选择: ${{userChoice || '未作答'}})</span>
                </div>
                <div style="color: var(--text-muted); font-size: 0.85rem;">
                  💡 研习点拨：点击上方【📜 原文线索】可在左侧查看对应段落原文及中英翻译。
                </div>
              </div>
            `;

            grpHtml += `</div>`;
          }});

          grpCard.innerHTML = grpHtml;
          secWrapper.appendChild(grpCard);
        }});

        container.appendChild(secWrapper);
      }});

      updateAnswerSheetStatus();
    }}

    function wrapWordsForDict(text) {{
      return text.replace(/[A-Za-z]+/g, match => {{
        return `<span class="dict-word" onclick="handleWordClick('${{match}}', event)">${{match}}</span>`;
      }});
    }}

    function setFocusedQuestion(qNum) {{
      focusedQuestionNum = qNum;
      document.querySelectorAll('.question-block').forEach(b => b.classList.remove('focused'));
      const target = document.getElementById(`question_item_${{qNum}}`);
      if (target) target.classList.add('focused');
    }}

    function selectOption(qNum, letter) {{
      if (!currentExam) return;
      const record = getOrCreateExamRecord(currentExam.id);
      record.answers[qNum] = letter;
      saveExamRecord(currentExam.id, record);

      setFocusedQuestion(qNum);

      const officialAns = currentExam.answers[qNum] || '';
      const isPostExamOrStudy = record.submitted || currentMode === 'study';

      ['A', 'B', 'C', 'D'].forEach(l => {{
        const el = document.getElementById(`opt_${{qNum}}_${{l}}`);
        if (!el) return;
        el.className = 'option-item';

        if (letter === l) {{
          el.classList.add('selected');
        }}

        if (isPostExamOrStudy) {{
          if (l === officialAns) {{
            el.classList.add('correct');
          }} else if (letter === l && letter !== officialAns) {{
            el.classList.add('wrong');
          }}
        }}
      }});

      const analysisBox = document.getElementById(`analysis_box_${{qNum}}`);
      if (analysisBox && isPostExamOrStudy) {{
        analysisBox.classList.add('visible');
        const statusEl = document.getElementById(`analysis_status_${{qNum}}`);
        if (statusEl) {{
          const isCorrect = letter === officialAns;
          statusEl.textContent = `${{isCorrect ? '✅ 回答正确' : '❌ 作答错误'}} (你的选择: ${{letter}})`;
          statusEl.style.color = isCorrect ? 'var(--success)' : 'var(--danger)';
        }}
      }}

      updateAnswerSheetStatus();
    }}

    function toggleFlag(qNum, event) {{
      if (event) event.stopPropagation();
      const record = getOrCreateExamRecord(currentExam.id);
      record.flags[qNum] = !record.flags[qNum];
      saveExamRecord(currentExam.id, record);

      const btn = document.getElementById(`flagBtn_${{qNum}}`);
      if (btn) {{
        if (record.flags[qNum]) {{
          btn.className = 'btn-flag flagged';
          btn.textContent = '★ 存疑';
        }} else {{
          btn.className = 'btn-flag';
          btn.textContent = '☆ 标记';
        }}
      }}
      updateAnswerSheetStatus();
    }}

    function toggleScratchpad(qNum, event) {{
      if (event) event.stopPropagation();
      const sp = document.getElementById(`scratchpad_${{qNum}}`);
      if (sp) {{
        sp.style.display = sp.style.display === 'block' ? 'none' : 'block';
      }}
    }}

    function saveNote(qNum, val) {{
      const record = getOrCreateExamRecord(currentExam.id);
      record.notes[qNum] = val;
      saveExamRecord(currentExam.id, record);
    }}

    // ==========================================================================
    // Answer Sheet Drawer Logic
    // ==========================================================================
    function toggleAnswerSheetDrawer() {{
      sheetDrawer.classList.toggle('open');
      updateAnswerSheetStatus();
    }}

    function openAnswerSheet() {{
      sheetDrawer.classList.add('open');
      updateAnswerSheetStatus();
    }}

    function updateAnswerSheetStatus() {{
      if (!currentExam) return;

      const record = getExamRecord(currentExam.id) || {{ answers: {{}}, flags: {{}}, submitted: false }};
      const total = currentExam.total_questions;
      let answeredCount = 0;

      const grid = document.getElementById('sheetGrid');
      grid.innerHTML = '';

      const isPostExamOrStudy = record.submitted || currentMode === 'study';

      for (let i = 1; i <= total; i++) {{
        const btn = document.createElement('div');
        btn.className = 'sheet-cell';
        btn.textContent = i;

        const ans = record.answers[i];
        const isFlag = record.flags[i];
        const official = currentExam.answers[i];

        if (ans) {{
          answeredCount++;
          btn.classList.add('answered');
        }}

        if (isFlag) {{
          btn.classList.add('flagged');
        }}

        if (isPostExamOrStudy) {{
          if (ans === official) {{
            btn.classList.add('correct');
          }} else if (ans) {{
            btn.classList.add('wrong');
          }}
        }}

        btn.onclick = () => {{
          scrollToQuestion(i);
        }};

        grid.appendChild(btn);
      }}

      document.getElementById('answeredPillCount').textContent = answeredCount;
      document.getElementById('floatingAnsweredCount').textContent = answeredCount;
      document.getElementById('sheetDrawerAnsweredCount').textContent = answeredCount;
    }}

    function scrollToQuestion(qNum) {{
      setLayout('split');
      const target = document.getElementById(`question_item_${{qNum}}`);
      if (target) {{
        target.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        setFocusedQuestion(qNum);
      }}
      if (window.innerWidth < 768) {{
        sheetDrawer.classList.remove('open');
      }}
    }}

    // ==========================================================================
    // Exam Submission & Grading
    // ==========================================================================
    function confirmSubmitExam() {{
      if (!currentExam) return;
      const record = getOrCreateExamRecord(currentExam.id);
      const answeredCount = Object.keys(record.answers).length;
      const unAnsCount = 25 - answeredCount;

      if (unAnsCount > 0) {{
        if (!confirm(`您还有 ${{unAnsCount}} 道题未作答，确定现在交卷吗？`)) {{
          return;
        }}
      }}

      submitExamGrade();
    }}

    function submitExamGrade() {{
      if (!currentExam) return;
      const record = getOrCreateExamRecord(currentExam.id);
      record.submitted = true;

      let rawScore = 0;
      let secAScore = 0;
      let secBScore = 0;
      let secCScore = 0;

      for (let i = 1; i <= 25; i++) {{
        const user = record.answers[i];
        const correct = currentExam.answers[i];
        if (user === correct) {{
          rawScore++;
          if (i <= 8) secAScore++;
          else if (i <= 15) secBScore++;
          else secCScore++;
        }}
      }}

      // CET-6 Standard Scaled Score
      const scaledScore = (secAScore * 7.1) + (secBScore * 7.1) + (secCScore * 14.2);

      record.rawScore = rawScore;
      record.scaledScore = scaledScore;
      record.secAScore = secAScore;
      record.secBScore = secBScore;
      record.secCScore = secCScore;

      saveExamRecord(currentExam.id, record);

      stopTimer();
      renderQuestions();
      renderTranscripts();
      updateAnswerSheetStatus();
      sheetDrawer.classList.remove('open');

      showScorecardModal(record);
    }}

    function showScorecardModal(record) {{
      document.getElementById('modalExamTitle').textContent = currentExam.title;
      document.getElementById('modalRawScore').innerHTML = `${{record.rawScore}} <span style="font-size: 1.8rem; color: var(--text-muted); font-weight: 600;">/ 25</span>`;
      document.getElementById('modalScaledScore').textContent = `折算分: ${{record.scaledScore.toFixed(1)}} / 248.5 分`;

      let rating = '💡 听力亟需提分 · 需专项强化';
      if (record.scaledScore >= 200) {{
        rating = '👑 听力王者 · 冲刺六级600+卓越水平';
      }} else if (record.scaledScore >= 170) {{
        rating = '🌟 听力良好 · 稳过六级优势科目';
      }} else if (record.scaledScore >= 149) {{
        rating = '🎯 听力达标 · 达到六级及格线水平';
      }}
      document.getElementById('modalRatingText').textContent = rating;

      document.getElementById('modalSecAScore').textContent = `${{record.secAScore}} / 8`;
      document.getElementById('modalSecAScaled').textContent = `${{(record.secAScore * 7.1).toFixed(1)}} / 56.8分`;

      document.getElementById('modalSecBScore').textContent = `${{record.secBScore}} / 7`;
      document.getElementById('modalSecBScaled').textContent = `${{(record.secBScore * 7.1).toFixed(1)}} / 49.7分`;

      document.getElementById('modalSecCScore').textContent = `${{record.secCScore}} / 10`;
      document.getElementById('modalSecCScaled').textContent = `${{(record.secCScore * 14.2).toFixed(1)}} / 142.0分`;

      let advice = '';
      if (record.secCScore < 6) {{
        advice += '⚠️ <strong>重点补强 Section C 讲座/讲话</strong>：六级听力 Section C 每题占 14.2分（双倍分值），占听力总分近 60%！请开启左侧【双语原文】对照 AB 循环精听。<br>';
      }}
      if (record.secAScore >= 7) {{
        advice += '✨ <strong>长对话表现卓越</strong>：对话场景转折词（but, actually）捕捉精准，请继续保持。<br>';
      }} else {{
        advice += '📌 <strong>长对话建议预读提速</strong>：预读时圈画首尾句动词，紧跟男女声问答转折。<br>';
      }}
      document.getElementById('modalDiagnosticAdvice').innerHTML = advice;

      renderModalQuestionsTable('all');
      openModal('scorecardModal');
    }}

    function renderModalQuestionsTable(filter = 'all') {{
      const tableWrap = document.getElementById('modalQuestionsTable');
      const record = getExamRecord(currentExam.id);
      let html = '<table style="width: 100%; border-collapse: collapse; font-size: 0.85rem;">';
      html += '<tr style="border-bottom: 1px solid var(--border-color); color: var(--text-muted);"><th style="padding: 6px; text-align: left;">题号</th><th style="padding: 6px; text-align: left;">你的作答</th><th style="padding: 6px; text-align: left;">标准答案</th><th style="padding: 6px; text-align: left;">状态</th></tr>';

      for (let i = 1; i <= 25; i++) {{
        const user = record.answers[i] || '未作答';
        const correct = currentExam.answers[i];
        const isRight = user === correct;
        const isFlag = record.flags[i];

        if (filter === 'wrong' && isRight) continue;
        if (filter === 'flagged' && !isFlag) continue;

        const statusTag = isRight ? 
          '<span style="color: var(--success); font-weight: 700;">✅ 正确</span>' : 
          '<span style="color: var(--danger); font-weight: 700;">❌ 错误</span>';

        html += `
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 6px;">Q${{i}} ${{isFlag ? '★' : ''}}</td>
            <td style="padding: 6px; font-weight: 700;">${{user}}</td>
            <td style="padding: 6px; color: var(--success); font-weight: 700;">${{correct}}</td>
            <td style="padding: 6px;">${{statusTag}}</td>
          </tr>
        `;
      }}
      html += '</table>';
      tableWrap.innerHTML = html;
    }}

    function filterModalQuestions(type) {{
      document.getElementById('btnFilterAll').className = type === 'all' ? 'btn btn-sm btn-primary' : 'btn btn-sm btn-outline';
      document.getElementById('btnFilterWrong').className = type === 'wrong' ? 'btn btn-sm btn-primary' : 'btn btn-sm btn-outline';
      document.getElementById('btnFilterFlagged').className = type === 'flagged' ? 'btn btn-sm btn-primary' : 'btn btn-sm btn-outline';
      renderModalQuestionsTable(type);
    }}

    function retryMistakes() {{
      if (!currentExam) return;
      const record = getOrCreateExamRecord(currentExam.id);
      for (let i = 1; i <= 25; i++) {{
        if (record.answers[i] !== currentExam.answers[i]) {{
          delete record.answers[i];
        }}
      }}
      record.submitted = false;
      saveExamRecord(currentExam.id, record);

      closeModal('scorecardModal');
      renderQuestions();
      updateAnswerSheetStatus();
      alert('已清空所有做错题目的选项，现在开始错题专项重练！');
    }}

    function switchToStudyAndCloseModal() {{
      closeModal('scorecardModal');
      switchMode('study');
    }}

    function resetCurrentExam() {{
      if (!currentExam) return;
      if (!confirm('确定清空本套真题的全部作答记录重做吗？')) return;
      localStorage.removeItem(`cet6_listen_rec_${{currentExam.id}}`);
      renderQuestions();
      updateAnswerSheetStatus();
      timerSeconds = 1800;
      updateTimerDisplay();
    }}

    // ==========================================================================
    // Countdown Timer
    // ==========================================================================
    function startTimer() {{
      stopTimer();
      isTimerRunning = true;
      document.getElementById('btnTimerToggle').textContent = '暂停';
      timerInterval = setInterval(() => {{
        if (timerSeconds > 0) {{
          timerSeconds--;
          updateTimerDisplay();
        }} else {{
          stopTimer();
          alert('⏰ 考试时间到！正在自动为您提交并评分...');
          submitExamGrade();
        }}
      }}, 1000);
    }}

    function stopTimer() {{
      if (timerInterval) clearInterval(timerInterval);
      isTimerRunning = false;
      const btn = document.getElementById('btnTimerToggle');
      if (btn) btn.textContent = '继续';
    }}

    function toggleTimer() {{
      if (isTimerRunning) {{
        stopTimer();
      }} else {{
        startTimer();
      }}
    }}

    function updateTimerDisplay() {{
      const m = Math.floor(timerSeconds / 60);
      const s = timerSeconds % 60;
      const widget = document.getElementById('examTimerWidget');
      const disp = document.getElementById('timerDisplay');
      disp.textContent = `${{m.toString().padStart(2, '0')}}:${{s.toString().padStart(2, '0')}}`;

      if (timerSeconds <= 300) {{
        widget.classList.add('warning');
      }} else {{
        widget.classList.remove('warning');
      }}
    }}

    // ==========================================================================
    // Dictionary Popover & Speech
    // ==========================================================================
    function handleWordClick(rawWord, e) {{
      if (!isWordLookupEnabled) return;
      e.stopPropagation();
      const clean = rawWord.toLowerCase().trim();
      const popover = document.getElementById('dictPopover');

      let entry = DICT_DATA[clean];
      let lemma = '';

      if (!entry) {{
        if (clean.endsWith('ies')) lemma = clean.slice(0, -3) + 'y';
        else if (clean.endsWith('es')) lemma = clean.slice(0, -2);
        else if (clean.endsWith('s')) lemma = clean.slice(0, -1);
        else if (clean.endsWith('ed')) lemma = clean.slice(0, -2);
        else if (clean.endsWith('ing')) lemma = clean.slice(0, -3);

        if (lemma && DICT_DATA[lemma]) {{
          entry = DICT_DATA[lemma];
        }}
      }}

      document.getElementById('dictWordText').textContent = rawWord;

      if (entry) {{
        document.getElementById('dictPhonetic').textContent = entry.p || '';
        document.getElementById('dictTrans').textContent = entry.t || '释义加载中';
        document.getElementById('dictRootHint').textContent = lemma ? `原形: ${{lemma}}` : '';
      }} else {{
        document.getElementById('dictPhonetic').textContent = '';
        document.getElementById('dictTrans').textContent = '点击扬声器发音辨析该词';
        document.getElementById('dictRootHint').textContent = '';
      }}

      const x = Math.min(window.innerWidth - 340, Math.max(10, e.clientX - 100));
      const y = Math.min(window.innerHeight - 200, e.clientY + 15);
      popover.style.left = `${{x}}px`;
      popover.style.top = `${{y}}px`;
      popover.style.display = 'block';
    }}

    function closeDictPopover() {{
      document.getElementById('dictPopover').style.display = 'none';
    }}

    function speakCurrentWord() {{
      const word = document.getElementById('dictWordText').textContent;
      if (!word) return;
      speakText(word);
    }}

    function speakQuestionOptions(qNum, e) {{
      if (e) e.stopPropagation();
      if (!currentExam) return;

      for (const secKey of ['A', 'B', 'C']) {{
        for (const grp of currentExam.sections[secKey].groups) {{
          for (const q of grp.questions) {{
            if (q.q_num === qNum) {{
              let speech = `Question ${{qNum}}. `;
              ['A', 'B', 'C', 'D'].forEach(letter => {{
                speech += `Option ${{letter}}: ${{q.options[letter]}}. `;
              }});
              speakText(speech);
              return;
            }}
          }}
        }}
      }}
    }}

    function speakText(text) {{
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = 'en-US';
      utter.rate = 0.95;
      window.speechSynthesis.speak(utter);
    }}

    // ==========================================================================
    // LocalStorage Records
    // ==========================================================================
    function getExamRecord(examId) {{
      try {{
        const raw = localStorage.getItem(`cet6_listen_rec_${{examId}}`);
        return raw ? JSON.parse(raw) : null;
      }} catch (e) {{
        return null;
      }}
    }}

    function getOrCreateExamRecord(examId) {{
      let rec = getExamRecord(examId);
      if (!rec) {{
        rec = {{ answers: {{}}, flags: {{}}, notes: {{}}, submitted: false, rawScore: 0, scaledScore: 0 }};
      }}
      return rec;
    }}

    function saveExamRecord(examId, record) {{
      try {{
        localStorage.setItem(`cet6_listen_rec_${{examId}}`, JSON.stringify(record));
      }} catch (e) {{
        console.warn('LocalStorage error:', e);
      }}
    }}

    // ==========================================================================
    // Modal Helpers
    // ==========================================================================
    function openModal(id) {{
      document.getElementById(id).classList.add('open');
    }}

    function closeModal(id) {{
      document.getElementById(id).classList.remove('open');
    }}

    function openStrategiesModal() {{
      openModal('strategiesModal');
    }}

    function openShortcutsModal() {{
      openModal('shortcutsModal');
    }}

    // ==========================================================================
    // Keyboard Shortcuts & Click Outside
    // ==========================================================================
    function initKeyboardListeners() {{
      window.addEventListener('keydown', (e) => {{
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

        const key = e.key.toUpperCase();

        if (e.code === 'Space' || key === 'K') {{
          e.preventDefault();
          togglePlayPause();
        }} else if (key === 'ARROWLEFT' || key === 'J') {{
          e.preventDefault();
          seekRelative(e.shiftKey ? -15 : -5);
        }} else if (key === 'ARROWRIGHT' || key === 'L') {{
          e.preventDefault();
          seekRelative(e.shiftKey ? 15 : 5);
        }} else if (key === '[') {{
          const select = document.getElementById('speedSelect');
          if (select.selectedIndex > 0) {{
            select.selectedIndex--;
            changePlaybackRate(select.value);
          }}
        }} else if (key === ']') {{
          const select = document.getElementById('speedSelect');
          if (select.selectedIndex < select.options.length - 1) {{
            select.selectedIndex++;
            changePlaybackRate(select.value);
          }}
        }} else if (['A', 'B', 'C', 'D'].includes(key)) {{
          if (focusedQuestionNum) {{
            selectOption(focusedQuestionNum, key);
          }}
        }} else if (key === 'F') {{
          if (focusedQuestionNum) {{
            toggleFlag(focusedQuestionNum);
          }}
        }} else if (key === '?') {{
          openShortcutsModal();
        }}
      }});
    }}

    function initClickOutsideListeners() {{
      window.addEventListener('click', (e) => {{
        const popover = document.getElementById('dictPopover');
        if (popover && !popover.contains(e.target)) {{
          popover.style.display = 'none';
        }}
      }});
    }}
  </script>
</body>
</html>
"""
    return html_content

def build_app():
    print("Loading data...")
    exams, dict_map = load_data()
    print("Generating standalone HTML platform with Synchronized Transcripts...")
    html = generate_platform_html(exams, dict_map)
    
    out_path = 'cet6_listening_platform.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Update Chinese copy
    import shutil
    shutil.copyfile('cet6_listening_platform.html', '六级听力真题研习平台.html')

    size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"Successfully generated {out_path} ({size_mb:.2f} MB)")

if __name__ == '__main__':
    build_app()
