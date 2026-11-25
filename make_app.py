# -*- coding: utf-8 -*-
"""
CET-6 Vocabulary Memorization App Builder
Generates a standalone, beautiful, and feature-rich HTML application with a bulletproof Word Spelling engine.
"""
import json
import os

def build():
    with open('words_data.json', 'r', encoding='utf-8') as f:
        words_data = json.load(f)

    with open('high_freq_data.json', 'r', encoding='utf-8') as f:
        hf_data = json.load(f)

    # Convert words_data and hf_data to compact JSON strings to embed directly in script
    words_json_str = json.dumps(words_data, ensure_ascii=False)
    hf_json_str = json.dumps(hf_data, ensure_ascii=False, separators=(',', ':'))

    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CET-6 核心词汇背诵助手 · 2220词</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%234f46e5'><path d='M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5'/></svg>">
  <style>
    :root {{
      --bg-app: #f8fafc;
      --bg-card: #ffffff;
      --bg-card-subtle: #f1f5f9;
      --bg-card-hover: #f8fafc;
      --border: #e2e8f0;
      --border-focus: #6366f1;
      --text-main: #0f172a;
      --text-sub: #475569;
      --text-muted: #94a3b8;
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-subtle: #eef2ff;
      --success: #10b981;
      --success-hover: #059669;
      --success-subtle: #ecfdf5;
      --warning: #f59e0b;
      --warning-subtle: #fffbeb;
      --danger: #ef4444;
      --danger-subtle: #fef2f2;
      --star: #f59e0b;
      --pos-v: #3b82f6;
      --pos-n: #10b981;
      --pos-adj: #8b5cf6;
      --pos-adv: #ec4899;
      --pos-other: #64748b;
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
      --bg-card-hover: #223049;
      --border: #273549;
      --border-focus: #818cf8;
      --text-main: #f8fafc;
      --text-sub: #cbd5e1;
      --text-muted: #64748b;
      --primary: #6366f1;
      --primary-hover: #818cf8;
      --primary-subtle: #1e1b4b;
      --success: #10b981;
      --success-hover: #34d399;
      --success-subtle: #064e3b;
      --warning: #f59e0b;
      --warning-subtle: #451a03;
      --danger: #f43f5e;
      --danger-subtle: #4c0519;
      --star: #fbbf24;
      --pos-v: #60a5fa;
      --pos-n: #34d399;
      --pos-adj: #a78bfa;
      --pos-adv: #f472b6;
      --pos-other: #94a3b8;
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
      display: flex;
      flex-direction: column;
      line-height: 1.5;
      transition: background-color 0.25s ease, color 0.25s ease;
    }}

    .app-container {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 16px 20px 48px;
      width: 100%;
      flex: 1;
    }}

    header.app-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 0 20px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 20px;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .brand-section {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .logo-badge {{
      background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
      color: #fff;
      font-weight: 800;
      font-size: 13px;
      letter-spacing: 0.5px;
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
    }}

    .brand-title {{
      font-size: 20px;
      font-weight: 700;
      color: var(--text-main);
      letter-spacing: -0.3px;
    }}

    .brand-subtitle {{
      font-size: 12px;
      color: var(--text-muted);
      margin-left: 6px;
      font-weight: 500;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .icon-btn {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-sub);
      padding: 8px 12px;
      border-radius: var(--radius-md);
      cursor: pointer;
      font-size: 13px;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition);
      text-decoration: none;
    }}

    .icon-btn:hover {{
      background: var(--bg-card-subtle);
      color: var(--text-main);
      border-color: var(--border-focus);
    }}

    .select-accent {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-main);
      padding: 7px 10px;
      border-radius: var(--radius-md);
      font-size: 13px;
      outline: none;
      cursor: pointer;
    }}

    .stats-ribbon {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 16px 20px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }}

    .stat-box {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .stat-label {{
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .stat-val {{
      font-size: 24px;
      font-weight: 800;
      letter-spacing: -0.5px;
      color: var(--text-main);
    }}

    .stat-val small {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      margin-left: 2px;
    }}

    .progress-bar-wrap {{
      grid-column: span 4;
      margin-top: 4px;
    }}

    .progress-track {{
      height: 8px;
      background: var(--bg-card-subtle);
      border-radius: var(--radius-full);
      overflow: hidden;
      display: flex;
    }}

    .progress-seg {{
      height: 100%;
      transition: width 0.4s ease;
    }}
    .seg-mastered {{ background: var(--success); }}
    .seg-review {{ background: var(--warning); }}

    .nav-tabs {{
      display: flex;
      gap: 8px;
      margin-bottom: 24px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
      overflow-x: auto;
    }}

    .tab-btn {{
      padding: 10px 16px;
      background: transparent;
      border: none;
      border-radius: var(--radius-md);
      font-size: 14px;
      font-weight: 600;
      color: var(--text-sub);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: var(--transition);
      white-space: nowrap;
    }}

    .tab-btn:hover {{
      color: var(--text-main);
      background: var(--bg-card-subtle);
    }}

    .tab-btn.active {{
      background: var(--primary);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
    }}

    .tab-badge {{
      font-size: 11px;
      padding: 2px 6px;
      border-radius: var(--radius-full);
      background: rgba(255, 255, 255, 0.2);
    }}
    .tab-btn:not(.active) .tab-badge {{
      background: var(--bg-card-subtle);
      color: var(--text-muted);
    }}

    .tab-pane {{
      display: none;
    }}
    .tab-pane.active {{
      display: block;
      animation: fadeIn 0.2s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Flashcard View */
    .card-workspace {{
      display: flex;
      flex-direction: column;
      align-items: center;
      max-width: 680px;
      margin: 0 auto;
    }}

    .card-toolbar {{
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .toolbar-left, .toolbar-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .list-select {{
      padding: 8px 12px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-main);
      border-radius: var(--radius-md);
      font-size: 13px;
      font-weight: 500;
      outline: none;
      cursor: pointer;
    }}

    .card-counter {{
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .checkbox-label {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 13px;
      color: var(--text-sub);
      cursor: pointer;
      user-select: none;
    }}

    .checkbox-label input {{
      cursor: pointer;
      accent-color: var(--primary);
    }}

    .flashcard-outer {{
      width: 100%;
      min-height: 340px;
      perspective: 1200px;
      cursor: pointer;
      margin-bottom: 24px;
    }}

    .flashcard-inner {{
      position: relative;
      width: 100%;
      height: 100%;
      min-height: 340px;
      text-align: center;
      transition: transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1);
      transform-style: preserve-3d;
    }}

    .flashcard-inner.flipped {{
      transform: rotateY(180deg);
    }}

    .flashcard-front, .flashcard-back {{
      position: absolute;
      width: 100%;
      height: 100%;
      min-height: 340px;
      top: 0;
      left: 0;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 36px 32px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      box-shadow: var(--shadow-lg);
      transition: border-color 0.2s ease;
    }}

    .flashcard-front:hover, .flashcard-back:hover {{
      border-color: var(--border-focus);
    }}

    .flashcard-back {{
      transform: rotateY(180deg);
      background: var(--bg-card);
    }}

    .card-top-tags {{
      position: absolute;
      top: 18px;
      left: 20px;
      right: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .status-tag {{
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .status-tag.unlearned {{ background: var(--bg-card-subtle); color: var(--text-muted); }}
    .status-tag.review {{ background: var(--warning-subtle); color: var(--warning); }}
    .status-tag.mastered {{ background: var(--success-subtle); color: var(--success); }}

    .star-btn {{
      background: none;
      border: none;
      font-size: 20px;
      cursor: pointer;
      color: var(--text-muted);
      transition: var(--transition);
      padding: 4px;
    }}
    .star-btn.starred {{
      color: var(--star);
      transform: scale(1.15);
    }}

    .card-word {{
      font-size: 44px;
      font-weight: 800;
      letter-spacing: -0.5px;
      color: var(--text-main);
      margin-bottom: 12px;
      line-height: 1.1;
    }}

    .card-phonetic-row {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: var(--bg-card-subtle);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      margin-bottom: 24px;
    }}

    .card-phonetic {{
      font-family: Georgia, "Times New Roman", serif;
      font-size: 18px;
      color: var(--text-sub);
      letter-spacing: 0.5px;
    }}

    .audio-play-btn {{
      background: var(--primary-subtle);
      border: none;
      color: var(--primary);
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
    }}
    .audio-play-btn:hover {{
      background: var(--primary);
      color: #fff;
      transform: scale(1.1);
    }}

    .card-hint {{
      position: absolute;
      bottom: 20px;
      font-size: 12px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    kbd {{
      background: var(--bg-card-subtle);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 2px 5px;
      font-size: 11px;
      font-family: inherit;
      color: var(--text-sub);
      box-shadow: 0 1px 1px rgba(0,0,0,0.1);
    }}

    .card-trans {{
      font-size: 20px;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 16px;
      line-height: 1.5;
      text-align: center;
      max-width: 90%;
    }}

    .card-detail-text {{
      font-size: 14px;
      color: var(--text-sub);
      line-height: 1.6;
      max-width: 90%;
      text-align: left;
      background: var(--bg-card-subtle);
      padding: 12px 16px;
      border-radius: var(--radius-md);
      margin-top: 10px;
      max-height: 120px;
      overflow-y: auto;
    }}

    .pos-tag {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      margin-right: 4px;
      vertical-align: middle;
      color: #fff;
      background: var(--primary);
    }}
    .pos-tag.tag-v {{ background: var(--pos-v); }}
    .pos-tag.tag-n {{ background: var(--pos-n); }}
    .pos-tag.tag-adj {{ background: var(--pos-adj); }}
    .pos-tag.tag-adv {{ background: var(--pos-adv); }}
    .pos-tag.tag-other {{ background: var(--pos-other); }}

    .card-actions {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      width: 100%;
      margin-bottom: 16px;
    }}

    .rate-btn {{
      padding: 12px 8px;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: var(--bg-card);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      transition: var(--transition);
      box-shadow: var(--shadow-sm);
    }}

    .rate-btn .btn-title {{
      font-size: 14px;
      font-weight: 700;
    }}

    .rate-btn .btn-sub {{
      font-size: 11px;
      color: var(--text-muted);
    }}

    .rate-btn.btn-again:hover {{
      border-color: var(--danger);
      background: var(--danger-subtle);
      color: var(--danger);
    }}
    .rate-btn.btn-hard:hover {{
      border-color: var(--warning);
      background: var(--warning-subtle);
      color: var(--warning);
    }}
    .rate-btn.btn-good:hover {{
      border-color: var(--success);
      background: var(--success-subtle);
      color: var(--success);
    }}
    .rate-btn.btn-easy:hover {{
      border-color: var(--primary);
      background: var(--primary-subtle);
      color: var(--primary);
    }}

    .card-nav-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
    }}

    .nav-arrow-btn {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      padding: 8px 16px;
      border-radius: var(--radius-md);
      font-size: 13px;
      font-weight: 500;
      color: var(--text-sub);
      cursor: pointer;
      transition: var(--transition);
    }}
    .nav-arrow-btn:hover {{
      color: var(--text-main);
      border-color: var(--border-focus);
    }}

    /* List View */
    .list-filter-bar {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 14px 18px;
      margin-bottom: 20px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}

    .filter-group {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .pill-filter {{
      padding: 6px 12px;
      border-radius: var(--radius-full);
      border: 1px solid var(--border);
      background: var(--bg-card);
      font-size: 12px;
      font-weight: 600;
      color: var(--text-sub);
      cursor: pointer;
      transition: var(--transition);
    }}
    .pill-filter.active {{
      background: var(--primary-subtle);
      border-color: var(--primary);
      color: var(--primary);
    }}

    .mask-options {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-card-subtle);
      padding: 4px;
      border-radius: var(--radius-md);
    }}

    .mask-btn {{
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      border: none;
      background: transparent;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-sub);
      cursor: pointer;
    }}
    .mask-btn.active {{
      background: var(--bg-card);
      color: var(--primary);
      box-shadow: var(--shadow-sm);
    }}

    .search-input-wrap {{
      position: relative;
      flex: 1;
      min-width: 200px;
      max-width: 320px;
    }}

    .search-input {{
      width: 100%;
      padding: 8px 12px 8px 34px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      background: var(--bg-card);
      color: var(--text-main);
      font-size: 13px;
      outline: none;
      transition: var(--transition);
    }}
    .search-input:focus {{
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
    }}

    .search-icon {{
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
    }}

    .word-list-container {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }}

    .word-row {{
      display: grid;
      grid-template-columns: 46px 180px 140px 1fr 100px 42px;
      align-items: center;
      padding: 12px 16px;
      border-bottom: 1px solid var(--border);
      transition: background 0.15s ease;
      font-size: 14px;
    }}

    .word-row:last-child {{
      border-bottom: none;
    }}

    .word-row:hover {{
      background: var(--bg-card-hover);
    }}

    .col-idx {{
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .col-word {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 700;
      color: var(--text-main);
      font-size: 16px;
    }}

    .col-phone {{
      font-family: Georgia, "Times New Roman", serif;
      font-size: 14px;
      color: var(--text-sub);
    }}

    .col-trans {{
      color: var(--text-main);
      line-height: 1.4;
      padding-right: 12px;
    }}

    .col-detail-sub {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .col-status {{
      display: flex;
      justify-content: flex-end;
    }}

    .badge-status {{
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      cursor: pointer;
      user-select: none;
      transition: var(--transition);
    }}
    .badge-status.s0 {{ background: var(--bg-card-subtle); color: var(--text-muted); }}
    .badge-status.s1 {{ background: var(--warning-subtle); color: var(--warning); }}
    .badge-status.s2 {{ background: var(--success-subtle); color: var(--success); }}

    .badge-status:hover {{
      filter: brightness(0.95);
    }}

    .mask-cn .col-trans {{
      filter: blur(5px);
      opacity: 0.3;
      cursor: pointer;
      transition: filter 0.2s, opacity 0.2s;
    }}
    .mask-cn .col-trans:hover, .mask-cn .col-trans.unmasked {{
      filter: blur(0);
      opacity: 1;
    }}

    .mask-en .col-word-text {{
      filter: blur(5px);
      opacity: 0.3;
      cursor: pointer;
      transition: filter 0.2s, opacity 0.2s;
    }}
    .mask-en .col-word-text:hover, .mask-en .col-word-text.unmasked {{
      filter: blur(0);
      opacity: 1;
    }}

    .list-pagination {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 16px;
      border-top: 1px solid var(--border);
      font-size: 13px;
      color: var(--text-sub);
    }}

    /* ====== SPELLING ARENA ====== */
    .spell-workspace {{
      max-width: 680px;
      margin: 0 auto;
    }}

    .spell-arena-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 36px 30px;
      box-shadow: var(--shadow-lg);
      margin-bottom: 20px;
      text-align: center;
      transition: border-color 0.25s ease;
    }}

    .spell-prompt-trans {{
      font-size: 24px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 12px;
      line-height: 1.4;
    }}

    .spell-prompt-detail {{
      font-size: 13px;
      color: var(--text-sub);
      margin-bottom: 20px;
      background: var(--bg-card-subtle);
      padding: 8px 16px;
      border-radius: var(--radius-md);
      display: inline-block;
      max-width: 90%;
    }}

    .letter-slots-row {{
      display: flex;
      gap: 6px;
      justify-content: center;
      align-items: center;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }}

    .letter-slot {{
      width: 32px;
      height: 38px;
      border-radius: var(--radius-sm);
      border: 2px dashed var(--border);
      background: var(--bg-card-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 19px;
      font-weight: 800;
      color: var(--primary);
      text-transform: uppercase;
      transition: var(--transition);
      user-select: none;
    }}
    .letter-slot.typing {{
      border-style: solid;
      border-color: var(--primary);
      background: var(--primary-subtle);
    }}
    .letter-slot.revealed {{
      border-style: solid;
      border-color: var(--warning);
      background: var(--warning-subtle);
      color: var(--warning);
    }}
    .letter-slot.correct-glow {{
      border-style: solid;
      border-color: var(--success);
      background: var(--success-subtle);
      color: var(--success);
    }}
    .letter-slot.wrong-glow {{
      border-style: solid;
      border-color: var(--danger);
      background: var(--danger-subtle);
      color: var(--danger);
    }}

    .spell-input-large {{
      width: 100%;
      max-width: 440px;
      padding: 14px 20px;
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 2px;
      text-align: center;
      border-radius: var(--radius-md);
      border: 2px solid var(--border);
      background: var(--bg-card);
      color: var(--text-main);
      outline: none;
      margin-bottom: 18px;
      transition: var(--transition);
    }}
    .spell-input-large:focus {{
      border-color: var(--primary);
      box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15);
    }}
    .spell-input-large.correct {{
      border-color: var(--success);
      color: var(--success);
      background: var(--success-subtle);
    }}
    .spell-input-large.wrong {{
      border-color: var(--danger);
      color: var(--danger);
      background: var(--danger-subtle);
      animation: shake 0.4s ease;
    }}

    .spell-actions-toolbar {{
      display: flex;
      gap: 10px;
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 16px;
    }}

    .spell-feedback-banner {{
      min-height: 52px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 15px;
      font-weight: 600;
      width: 100%;
    }}

    .reveal-box {{
      background: var(--warning-subtle);
      border: 1px solid var(--warning);
      border-radius: var(--radius-md);
      padding: 14px 18px;
      width: 100%;
      max-width: 480px;
      text-align: center;
      animation: fadeIn 0.2s ease;
    }}

    /* Quiz (Multiple Choice) */
    .quiz-workspace {{
      max-width: 680px;
      margin: 0 auto;
    }}

    .quiz-header-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 16px 20px;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: var(--shadow-sm);
      flex-wrap: wrap;
      gap: 12px;
    }}

    .quiz-hud {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .hud-item {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 13px;
      font-weight: 600;
    }}

    .quiz-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 32px 28px;
      box-shadow: var(--shadow-lg);
      margin-bottom: 20px;
      text-align: center;
    }}

    .quiz-word {{
      font-size: 38px;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 8px;
    }}

    .quiz-phone-row {{
      margin-bottom: 28px;
    }}

    .quiz-options-grid {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      text-align: left;
    }}

    .quiz-option-btn {{
      padding: 14px 18px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      background: var(--bg-card);
      color: var(--text-main);
      font-size: 15px;
      font-weight: 500;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: var(--transition);
    }}

    .quiz-option-btn:hover:not(:disabled) {{
      border-color: var(--border-focus);
      background: var(--bg-card-subtle);
      transform: translateX(4px);
    }}

    .option-key {{
      width: 24px;
      height: 24px;
      border-radius: var(--radius-sm);
      background: var(--bg-card-subtle);
      color: var(--text-sub);
      font-size: 12px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .quiz-option-btn.correct {{
      border-color: var(--success);
      background: var(--success-subtle);
      color: var(--success);
    }}
    .quiz-option-btn.correct .option-key {{
      background: var(--success);
      color: #fff;
    }}

    .quiz-option-btn.wrong {{
      border-color: var(--danger);
      background: var(--danger-subtle);
      color: var(--danger);
      animation: shake 0.4s ease;
    }}
    .quiz-option-btn.wrong .option-key {{
      background: var(--danger);
      color: #fff;
    }}

    @keyframes shake {{
      0%, 100% {{ transform: translateX(0); }}
      20%, 60% {{ transform: translateX(-6px); }}
      40%, 80% {{ transform: translateX(6px); }}
    }}

    /* Notebook */
    .notebook-header {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
    }}

    /* Stats Grid */
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      margin-bottom: 24px;
    }}

    .analytics-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      box-shadow: var(--shadow-sm);
    }}

    .card-title-lg {{
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .ebbinghaus-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      margin-top: 10px;
    }}

    .ebbinghaus-table th, .ebbinghaus-table td {{
      padding: 10px 12px;
      text-align: left;
      border-bottom: 1px solid var(--border);
    }}

    .ebbinghaus-table th {{
      background: var(--bg-card-subtle);
      font-weight: 600;
      color: var(--text-sub);
    }}

    .day-check {{
      cursor: pointer;
      accent-color: var(--success);
      width: 16px;
      height: 16px;
    }}

    /* Modal */
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
      animation: fadeIn 0.15s ease;
    }}

    .modal-content {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      max-width: 520px;
      width: 100%;
      padding: 24px;
      box-shadow: var(--shadow-lg);
    }}

    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}

    .shortcut-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 0;
      border-bottom: 1px solid var(--border);
      font-size: 13px;
    }}
    .shortcut-row:last-child {{ border-bottom: none; }}

    /* ====== HIGH FREQUENCY MODULE ====== */
    .hf-hero-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px 22px;
      margin-bottom: 18px;
      box-shadow: var(--shadow-sm);
    }}

    .hf-hero-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 14px;
    }}

    .hf-hero-title {{
      font-size: 18px;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }}

    .hf-hero-sub {{
      font-size: 13px;
      color: var(--text-sub);
    }}

    .hf-overall-prog {{
      min-width: 220px;
      flex: 0 1 280px;
    }}

    .hf-tier-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-bottom: 16px;
    }}

    .hf-tier-card {{
      background: var(--bg-card-subtle);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 12px 14px;
      cursor: pointer;
      transition: var(--transition);
      text-align: left;
    }}

    .hf-tier-card:hover {{
      border-color: var(--border-focus);
      transform: translateY(-1px);
    }}

    .hf-tier-card.active {{
      background: var(--primary-subtle);
      border-color: var(--primary);
      box-shadow: 0 2px 8px rgba(79, 70, 229, 0.14);
    }}

    .hf-tier-title {{
      font-size: 13px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 6px;
    }}

    .hf-tier-meta {{
      font-size: 12px;
      color: var(--text-sub);
      margin-bottom: 6px;
    }}

    .hf-mini-track {{
      height: 5px;
      background: rgba(148, 163, 184, 0.25);
      border-radius: var(--radius-full);
      overflow: hidden;
    }}

    .hf-mini-fill {{
      height: 100%;
      background: var(--success);
      border-radius: var(--radius-full);
      transition: width 0.35s ease;
    }}

    .hf-action-bar {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      align-items: center;
      padding-top: 12px;
      border-top: 1px solid var(--border);
    }}

    .hf-filter-bar {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 14px 18px;
      margin-bottom: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .hf-filter-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }}

    .hf-row {{
      display: grid;
      grid-template-columns: 74px 190px 1fr 112px 40px;
      align-items: start;
      gap: 12px;
      padding: 14px 16px;
      border-bottom: 1px solid var(--border);
      transition: background 0.15s ease;
      font-size: 14px;
    }}

    .hf-row:last-child {{
      border-bottom: none;
    }}

    .hf-row:hover {{
      background: var(--bg-card-hover);
    }}

    .hf-rank-col {{
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 4px;
    }}

    .hf-rank-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      color: #fff;
      background: var(--pos-other);
      min-width: 48px;
    }}
    .hf-rank-badge.tier-1 {{ background: linear-gradient(135deg, #ef4444 0%, #f97316 100%); }}
    .hf-rank-badge.tier-2 {{ background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); }}
    .hf-rank-badge.tier-3 {{ background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%); }}
    .hf-rank-badge.tier-0 {{ background: var(--success); }}

    .hf-stars {{
      font-size: 10px;
      letter-spacing: 1px;
      color: var(--star);
      line-height: 1;
    }}

    .hf-word-col {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .hf-word-head {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-weight: 800;
      font-size: 17px;
      color: var(--text-main);
    }}

    .hf-meta-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      margin-top: 4px;
    }}

    .hf-pill {{
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: var(--radius-full);
      background: var(--bg-card-subtle);
      color: var(--text-sub);
      border: 1px solid var(--border);
    }}
    .hf-pill.hot {{
      background: var(--danger-subtle);
      color: var(--danger);
      border-color: transparent;
    }}
    .hf-pill.wb {{
      background: var(--warning-subtle);
      color: var(--warning);
      border-color: transparent;
    }}
    .hf-pill.opt {{
      background: var(--primary-subtle);
      color: var(--primary);
      border-color: transparent;
    }}

    .hf-example-box {{
      margin-top: 8px;
      padding: 8px 11px;
      border-left: 3px solid var(--primary);
      background: var(--bg-card-subtle);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      font-size: 12.5px;
      color: var(--text-sub);
      line-height: 1.55;
    }}

    .hf-example-src {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      color: var(--primary);
      margin-right: 6px;
    }}

    .hf-kw {{
      background: var(--warning-subtle);
      color: var(--text-main);
      font-weight: 700;
      padding: 0 3px;
      border-radius: 3px;
      border-bottom: 1.5px solid var(--warning);
    }}

    .mask-en .hf-kw {{
      filter: blur(5px);
      opacity: 0.25;
      cursor: pointer;
      transition: filter 0.2s, opacity 0.2s;
    }}
    .mask-en .hf-kw:hover, .mask-en .hf-kw.unmasked {{
      filter: blur(0);
      opacity: 1;
    }}

    .hf-card-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      background: var(--danger-subtle);
      color: var(--danger);
      margin-bottom: 12px;
    }}

    .hf-list-badge {{
      display: inline-flex;
      align-items: center;
      font-size: 10px;
      font-weight: 700;
      padding: 1px 5px;
      border-radius: var(--radius-full);
      background: var(--warning-subtle);
      color: var(--warning);
      white-space: nowrap;
    }}

    .card-hf-example {{
      font-size: 12.5px;
      color: var(--text-sub);
      line-height: 1.5;
      max-width: 90%;
      text-align: left;
      border-left: 3px solid var(--primary);
      background: var(--bg-card-subtle);
      padding: 8px 12px;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-top: 8px;
      max-height: 82px;
      overflow-y: auto;
    }}

    @media (max-width: 768px) {{
      .hf-tier-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .hf-row {{
        grid-template-columns: 64px 1fr 38px;
        grid-template-areas:
          "rank word star"
          "trans trans trans"
          "status status status";
        gap: 8px;
      }}
      .hf-rank-col {{ grid-area: rank; }}
      .hf-word-col {{ grid-area: word; }}
      .hf-trans-col {{ grid-area: trans; }}
      .hf-status-col {{ grid-area: status; justify-content: flex-start !important; }}
      .hf-star-col {{ grid-area: star; }}
      .stats-ribbon {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .progress-bar-wrap {{
        grid-column: span 2;
      }}
      .word-row {{
        grid-template-columns: 32px 1fr 40px;
        grid-template-areas:
          "idx word star"
          "phone phone phone"
          "trans trans trans"
          "status status status";
        gap: 6px;
      }}
      .col-idx {{ grid-area: idx; }}
      .col-word {{ grid-area: word; }}
      .col-phone {{ grid-area: phone; }}
      .col-trans {{ grid-area: trans; }}
      .col-status {{ grid-area: status; justify-content: flex-start; }}
      .col-star {{ grid-area: star; }}
      .stats-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>

  <div class="app-container">
    <!-- Header -->
    <header class="app-header">
      <div class="brand-section">
        <span class="logo-badge">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
          CET-6
        </span>
        <div>
          <span class="brand-title">六级核心词汇背诵助手</span>
          <span class="brand-subtitle">大纲核心 2,220 词 · 科学记忆系统</span>
        </div>
      </div>

      <div class="header-actions">
        <!-- 45-Day Checklist Link -->
        <a href="六级45天通关打卡清单.html" class="icon-btn" style="text-decoration: none; font-weight: 600;" title="查看45天每日复习打卡清单">
          <span>📋 45天打卡清单</span>
        </a>

        <!-- Reading Real Exam Platform -->
        <a href="cet6_reading_platform.html" class="icon-btn" style="text-decoration: none; font-weight: 600; color: var(--primary); border-color: var(--border-focus); background: var(--primary-subtle);" title="前往历年阅读真题全真复习平台">
          <span>📖 六级阅读真题</span>
        </a>

        <!-- Voice Accent -->
        <select id="accentSelect" class="select-accent" title="发音口音">
          <option value="2">美音 (US)</option>
          <option value="1">英音 (UK)</option>
        </select>

        <!-- Theme Toggle -->
        <button id="themeToggleBtn" class="icon-btn" title="切换浅色/深色模式">
          <span id="themeIcon">🌙</span>
        </button>

        <!-- Shortcuts Help -->
        <button id="shortcutsBtn" class="icon-btn" title="快捷键帮助">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          <span>快捷键</span>
        </button>
      </div>
    </header>

    <!-- Global Stats Ribbon -->
    <section class="stats-ribbon">
      <div class="stat-box">
        <span class="stat-label">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          总词汇量
        </span>
        <span class="stat-val" id="statTotal">2220<small>词</small></span>
      </div>

      <div class="stat-box">
        <span class="stat-label">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          今日已背
        </span>
        <span class="stat-val" id="statToday" style="color: var(--primary);">0<small>词</small></span>
      </div>

      <div class="stat-box">
        <span class="stat-label">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          已掌握
        </span>
        <span class="stat-val" id="statMastered" style="color: var(--success);">0<small id="statMasteredPct">0%</small></span>
      </div>

      <div class="stat-box">
        <span class="stat-label">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
          需复习 / 模糊
        </span>
        <span class="stat-val" id="statReview" style="color: var(--warning);">0<small>词</small></span>
      </div>

      <div class="progress-bar-wrap">
        <div class="progress-track" title="掌握进度条">
          <div id="barMastered" class="progress-seg seg-mastered" style="width: 0%;"></div>
          <div id="barReview" class="progress-seg seg-review" style="width: 0%;"></div>
        </div>
      </div>
    </section>

    <!-- Navigation Tabs -->
    <nav class="nav-tabs">
      <button class="tab-btn active" data-tab="pane-card">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
        智能卡片
      </button>
      <button class="tab-btn" data-tab="pane-highfreq" id="navBtnHighFreq">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2c.5 3.5 3.5 5.5 3.5 9.5a3.5 3.5 0 0 1-7 0c0-1.5.5-2.8 1.4-3.8C8.5 9 8 10.5 8 12a4 4 0 0 0 8 0c0-4.2-2.5-6.6-4-10z"/><path d="M8.5 14.5A3.5 3.5 0 0 0 12 18a3.5 3.5 0 0 0 3.5-3.5"/></svg>
        真题高频词
        <span class="tab-badge" id="badgeHighFreq">600</span>
      </button>
      <button class="tab-btn" data-tab="pane-list">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
        词汇清单
      </button>
      <button class="tab-btn" data-tab="pane-spell" id="navBtnSpell">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
        单词拼写
      </button>
      <button class="tab-btn" data-tab="pane-quiz">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
        自测挑战
      </button>
      <button class="tab-btn" data-tab="pane-notebook">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
        生词错题
        <span class="tab-badge" id="badgeNotebook">0</span>
      </button>
      <button class="tab-btn" data-tab="pane-plan">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
        学习计划 &amp; 统计
      </button>
    </nav>

    <!-- ====== PANE 1: FLASHCARD ====== -->
    <div id="pane-card" class="tab-pane active">
      <div class="card-workspace">
        <div class="card-toolbar">
          <div class="toolbar-left">
            <select id="cardListSelect" class="list-select"></select>
            <span class="card-counter" id="cardCounter">1 / 50</span>
          </div>

          <div class="toolbar-right">
            <label class="checkbox-label" title="切换单词时自动播放读音">
              <input type="checkbox" id="autoPronounceCheck" checked>
              自动发音
            </label>
            <label class="checkbox-label" title="随机乱序背诵">
              <input type="checkbox" id="shuffleCheck">
              乱序
            </label>
          </div>
        </div>

        <!-- 3D Flashcard -->
        <div class="flashcard-outer" id="flashcardBox">
          <div class="flashcard-inner" id="flashcardInner">
            <!-- Front -->
            <div class="flashcard-front">
              <div class="card-top-tags">
                <span id="cardStatusTag" class="status-tag unlearned">未学习</span>
                <button id="cardStarBtn" class="star-btn" title="加入生词本 (S)">★</button>
              </div>

              <div class="card-word" id="cardWordText">abandon</div>
              <div class="card-phonetic-row">
                <span class="card-phonetic" id="cardPhoneticText">/ əˈbændən /</span>
                <button id="cardAudioBtn" class="audio-play-btn" title="发音 (R)">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>
                </button>
              </div>
              <div id="cardHfBadgeFront" class="hf-card-badge" style="display: none;"></div>

              <div class="card-hint">
                <kbd>Space</kbd> 或 点击卡片查看释义
              </div>
            </div>

            <!-- Back -->
            <div class="flashcard-back">
              <div class="card-top-tags">
                <span id="cardStatusTagBack" class="status-tag unlearned">未学习</span>
                <span id="cardHfBadgeBack" class="hf-list-badge" style="display: none;"></span>
                <span style="font-size: 12px; color: var(--text-muted);">再次点击翻转</span>
              </div>

              <div class="card-word" id="cardWordTextBack" style="font-size: 32px; margin-bottom: 8px;">abandon</div>
              <div class="card-trans" id="cardTransText">vt. 放弃, 遗弃; n. 放任, 狂热</div>
              <div class="card-detail-text" id="cardDetailText">v. 1. 抛弃，放弃 2. 离弃(家园、船只、飞机等) 3. 遗弃(妻、子女等)</div>
              <div class="card-hf-example" id="cardHfExample" style="display: none;"></div>

              <div class="card-hint">
                <kbd>1</kbd> 忘啦 &nbsp; <kbd>2</kbd> 模糊 &nbsp; <kbd>3</kbd> 记住 &nbsp; <kbd>4</kbd> 熟练
              </div>
            </div>
          </div>
        </div>

        <!-- Rating Buttons -->
        <div class="card-actions">
          <button class="rate-btn btn-again" data-rating="1" title="快捷键: 1">
            <span class="btn-title" style="color: var(--danger);">忘啦</span>
            <span class="btn-sub">重来 · 纳入复习 (1)</span>
          </button>
          <button class="rate-btn btn-hard" data-rating="2" title="快捷键: 2">
            <span class="btn-title" style="color: var(--warning);">模糊</span>
            <span class="btn-sub">不确定 · 待巩固 (2)</span>
          </button>
          <button class="rate-btn btn-good" data-rating="3" title="快捷键: 3">
            <span class="btn-title" style="color: var(--success);">记住</span>
            <span class="btn-sub">想起来了 (3)</span>
          </button>
          <button class="rate-btn btn-easy" data-rating="4" title="快捷键: 4">
            <span class="btn-title" style="color: var(--primary);">熟练</span>
            <span class="btn-sub">秒懂 · 标记掌握 (4)</span>
          </button>
        </div>

        <div class="card-nav-row">
          <button class="nav-arrow-btn" id="prevCardBtn" title="上一个 (← 或 J)">← 上一个 (J)</button>
          <button class="nav-arrow-btn" id="flipCardBtn" title="翻转 (Space)">翻转卡片 (Space)</button>
          <button class="nav-arrow-btn" id="nextCardBtn" title="下一个 (→ 或 K)">下一个 (K) →</button>
        </div>
      </div>
    </div>

    <!-- ====== PANE 1.5: HIGH FREQUENCY EXAM WORDS ====== -->
    <div id="pane-highfreq" class="tab-pane">
      <!-- Hero Dashboard -->
      <section class="hf-hero-card">
        <div class="hf-hero-top">
          <div>
            <div class="hf-hero-title">
              <span>🔥 六级真题高频核心词库</span>
              <span class="pos-tag" style="background: var(--danger); margin: 0;">考前必刷</span>
            </div>
            <p class="hf-hero-sub">基于 33 套阅读真题 + 27 套听力真题（共 60 套真题语料）实测词频统计，精准锁定高频考点与选词填空词库。</p>
          </div>

          <div class="hf-overall-prog">
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 600; margin-bottom: 6px;">
              <span style="color: var(--text-sub);">Top 600 核心高频掌握进度</span>
              <span id="hfTop600ProgText" style="color: var(--success);">0 / 600 (0%)</span>
            </div>
            <div class="progress-track" style="height: 10px;">
              <div id="hfTop600BarMastered" class="progress-seg seg-mastered" style="width: 0%;"></div>
              <div id="hfTop600BarReview" class="progress-seg seg-review" style="width: 0%;"></div>
            </div>
          </div>
        </div>

        <div class="hf-tier-grid">
          <button type="button" class="hf-tier-card" data-hf-tier-jump="tier1">
            <div class="hf-tier-title">
              <span>👑 超高频必背</span>
              <span style="font-size: 11px; color: var(--danger); font-weight: 700;">Top 1~150</span>
            </div>
            <div class="hf-tier-meta" id="hfTier1Meta">已掌握 0 / 150</div>
            <div class="hf-mini-track"><div class="hf-mini-fill" id="hfTier1Fill" style="width: 0%;"></div></div>
          </button>

          <button type="button" class="hf-tier-card" data-hf-tier-jump="tier2">
            <div class="hf-tier-title">
              <span>⚡ 高频重点词</span>
              <span style="font-size: 11px; color: var(--primary); font-weight: 700;">151~350</span>
            </div>
            <div class="hf-tier-meta" id="hfTier2Meta">已掌握 0 / 200</div>
            <div class="hf-mini-track"><div class="hf-mini-fill" id="hfTier2Fill" style="width: 0%;"></div></div>
          </button>

          <button type="button" class="hf-tier-card" data-hf-tier-jump="tier3">
            <div class="hf-tier-title">
              <span>📌 次高频常考</span>
              <span style="font-size: 11px; color: var(--pos-v); font-weight: 700;">351~600</span>
            </div>
            <div class="hf-tier-meta" id="hfTier3Meta">已掌握 0 / 250</div>
            <div class="hf-mini-track"><div class="hf-mini-fill" id="hfTier3Fill" style="width: 0%;"></div></div>
          </button>

          <button type="button" class="hf-tier-card" data-hf-tier-jump="wordbank">
            <div class="hf-tier-title">
              <span>🎯 选词填空真题词库</span>
              <span style="font-size: 11px; color: var(--warning); font-weight: 700;">Section A</span>
            </div>
            <div class="hf-tier-meta" id="hfTierWbMeta">已掌握 0 / 209</div>
            <div class="hf-mini-track"><div class="hf-mini-fill" id="hfTierWbFill" style="width: 0%;"></div></div>
          </button>
        </div>

        <div class="hf-action-bar">
          <button id="hfStartCardBtn" class="icon-btn" style="background: var(--primary); color: #fff; border-color: var(--primary); font-weight: 600;">🗂️ 当前高频卡片速刷</button>
          <button id="hfStartSpellBtn" class="icon-btn" style="background: var(--primary-subtle); color: var(--primary); border-color: var(--primary); font-weight: 600;">✍️ 当前高频拼写默写</button>
          <button id="hfStartQuizBtn" class="icon-btn" style="font-weight: 600;">🎯 当前高频四选一挑战</button>
          <button id="hfExportMdBtn" class="icon-btn">📄 导出高频词表 (.md)</button>
        </div>
      </section>

      <!-- Multi-dimensional Filter Bar -->
      <section class="hf-filter-bar">
        <div class="hf-filter-row">
          <div class="filter-group" id="hfCategoryGroup">
            <button class="pill-filter active" data-hf-cat="top600">🔥 全部高频 600</button>
            <button class="pill-filter" data-hf-cat="tier1">👑 超高频 Top 150</button>
            <button class="pill-filter" data-hf-cat="tier2">⚡ 高频重点 151-350</button>
            <button class="pill-filter" data-hf-cat="tier3">📌 次高频 351-600</button>
            <button class="pill-filter" data-hf-cat="wordbank">🎯 选词填空词库</button>
            <button class="pill-filter" data-hf-cat="options">🏆 题干选项高频</button>
            <button class="pill-filter" data-hf-cat="listening">🎧 听力高频</button>
          </div>
        </div>

        <div class="hf-filter-row">
          <div class="filter-group">
            <select id="hfSliceSelect" class="list-select" title="按50词分组练习"></select>
            <select id="hfPosSelect" class="list-select" title="按词性筛选">
              <option value="all">全部词性</option>
              <option value="v">动词 (v.)</option>
              <option value="n">名词 (n.)</option>
              <option value="adj">形容词 (adj.)</option>
              <option value="adv">副词 (adv.)</option>
            </select>
            <select id="hfStatusSelect" class="list-select" title="按掌握状态筛选">
              <option value="all">全部状态</option>
              <option value="unmastered">仅看未掌握 (未学+需复习)</option>
              <option value="0">未学习</option>
              <option value="1">需复习</option>
              <option value="2">已掌握</option>
              <option value="starred">⭐ 生词本</option>
            </select>
            <select id="hfSortSelect" class="list-select" title="排序方式">
              <option value="rank">按综合真题考频</option>
              <option value="wb">按选词填空考频优先</option>
              <option value="qf">按选项出现次数优先</option>
              <option value="alpha">按字母顺序 A-Z</option>
            </select>
          </div>

          <div class="filter-group">
            <div class="mask-options" id="hfMaskOptions">
              <button class="mask-btn active" data-hf-mask="none" title="正常显示全部">👁️ 显示</button>
              <button class="mask-btn" data-hf-mask="cn" title="遮住中文，鼠标悬停或点击查看">🙈 遮中文</button>
              <button class="mask-btn" data-hf-mask="en" title="遮住英文与原句关键词，鼠标悬停或点击查看">🙊 遮英文</button>
            </div>

            <label class="checkbox-label" title="在列表中展示历年真题原句">
              <input type="checkbox" id="hfShowExampleCheck" checked>
              📖 显示真题例句
            </label>

            <div class="search-input-wrap" style="min-width: 180px;">
              <svg class="search-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              <input type="text" id="hfSearchInput" class="search-input" placeholder="搜索高频词或释义...">
            </div>
          </div>
        </div>
      </section>

      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; font-size: 13px; color: var(--text-muted); flex-wrap: wrap; gap: 8px;">
        <span id="hfSummaryText">共筛选出 600 个高频词</span>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <button id="hfBatchMasterPageBtn" class="icon-btn" style="padding: 4px 10px; font-size: 12px;">✓ 标记本页已掌握</button>
        </div>
      </div>

      <div class="word-list-container" id="hfListContainer"></div>

      <div class="list-pagination" id="hfPagination">
        <span id="hfPageInfoText">第 1 / 1 页</span>
        <div style="display: flex; gap: 8px;">
          <button class="icon-btn" id="hfPrevPageBtn">上一页</button>
          <button class="icon-btn" id="hfNextPageBtn">下一页</button>
        </div>
      </div>
    </div>

    <!-- ====== PANE 2: LIST VIEW ====== -->
    <div id="pane-list" class="tab-pane">
      <div class="list-filter-bar">
        <div class="filter-group">
          <select id="listGroupSelect" class="list-select"></select>

          <button class="pill-filter active" data-status-filter="all">全部</button>
          <button class="pill-filter" data-status-filter="0">未学</button>
          <button class="pill-filter" data-status-filter="1">需复习</button>
          <button class="pill-filter" data-status-filter="2">已掌握</button>
          <button class="pill-filter" data-status-filter="starred">⭐ 生词本</button>
        </div>

        <div class="filter-group">
          <div class="mask-options">
            <button class="mask-btn active" data-mask="none" title="正常显示全部">👁️ 显示</button>
            <button class="mask-btn" data-mask="cn" title="遮住中文，鼠标悬停或点击查看">🙈 遮中文</button>
            <button class="mask-btn" data-mask="en" title="遮住英文，鼠标悬停或点击查看">🙊 遮英文</button>
          </div>

          <div class="search-input-wrap">
            <svg class="search-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <input type="text" id="listSearchInput" class="search-input" placeholder="搜索英文或中文释义...">
          </div>
        </div>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; font-size: 13px; color: var(--text-muted); flex-wrap: wrap; gap: 8px;">
        <span id="listSummaryText">共加载 50 个单词</span>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <button id="batchStartCardBtn" class="icon-btn" style="padding: 4px 10px; font-size: 12px;">🗂️ 本组卡片背诵</button>
          <button id="batchStartSpellBtn" class="icon-btn" style="padding: 4px 10px; font-size: 12px; background: var(--primary-subtle); color: var(--primary);">✍️ 本组拼写默写</button>
          <button id="batchMarkMasteredBtn" class="icon-btn" style="padding: 4px 10px; font-size: 12px;">✓ 标记整组掌握</button>
          <button id="batchResetBtn" class="icon-btn" style="padding: 4px 10px; font-size: 12px;">↺ 重置整组状态</button>
        </div>
      </div>

      <div class="word-list-container" id="wordListContainer"></div>

      <div class="list-pagination" id="listPagination">
        <span id="pageInfoText">第 1 / 1 页</span>
        <div style="display: flex; gap: 8px;">
          <button class="icon-btn" id="prevPageBtn">上一页</button>
          <button class="icon-btn" id="nextPageBtn">下一页</button>
        </div>
      </div>
    </div>

    <!-- ====== PANE 3: BULLETPROOF WORD SPELLING ARENA ====== -->
    <div id="pane-spell" class="tab-pane">
      <div class="spell-workspace">
        <!-- Top Toolbar -->
        <div class="quiz-header-card">
          <div class="quiz-hud">
            <div class="hud-item">
              <span style="color: var(--text-muted);">进度:</span>
              <span id="spellIndexText" style="color: var(--primary); font-weight: 700;">1 / 50</span>
            </div>
            <div class="hud-item">
              <span style="color: var(--text-muted);">初次全对:</span>
              <span id="spellAccuracyText" style="color: var(--success); font-weight: 700;">0 (100%)</span>
            </div>
            <div class="hud-item">
              <span>连胜:</span>
              <span id="spellStreakText" style="font-weight: 700;">0 🔥</span>
            </div>
          </div>

          <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
            <select id="spellScopeSelect" class="list-select" style="padding: 4px 8px; font-size: 12px;"></select>
            <button id="spellRestartBtn" class="icon-btn" style="padding: 4px 10px; font-size: 12px;">重新开始本组</button>
          </div>
        </div>

        <!-- The Spelling Arena -->
        <div class="spell-arena-card" id="spellCard">
          <div class="spell-prompt-trans" id="spellPromptTrans">vt. 放弃, 遗弃; n. 放任, 狂热</div>
          <div class="spell-prompt-detail" id="spellPromptDetail">提示与搭配: v. 1. 抛弃，放弃 2. 离弃...</div>

          <div class="card-phonetic-row" style="margin-bottom: 20px;">
            <span class="card-phonetic" id="spellPromptPhone">/ əˈbændən /</span>
            <button id="spellAudioBtn" class="audio-play-btn" style="margin-left: 8px;" title="听发音 (快捷键 R)">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>
            </button>
          </div>

          <!-- Dynamic Letter slots synced with input -->
          <div class="letter-slots-row" id="spellLetterSlots"></div>

          <div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
            <input type="text" id="spellInputMain" class="spell-input-large" placeholder="键入英文单词..." autocomplete="off" spellcheck="false" autofocus>
            
            <div class="spell-actions-toolbar">
              <button id="spellSubmitBtn" class="icon-btn" style="background: var(--primary); color: #fff; border-color: var(--primary); padding: 8px 20px; font-weight: 700;">
                确定 (Enter)
              </button>
              <button id="spellHintFirstBtn" class="icon-btn" title="显示首字母 (快捷键: Alt+1)">
                💡 首字母
              </button>
              <button id="spellHintNextBtn" class="icon-btn" title="显示下一个字母 (快捷键: Alt+2)">
                🔍 提示字母
              </button>
              <button id="spellGiveUpBtn" class="icon-btn" style="color: var(--danger);" title="不会，放弃并查看答案">
                👀 放弃查看答案
              </button>
            </div>

            <!-- Feedback Area -->
            <div id="spellFeedbackArea" class="spell-feedback-banner"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- ====== PANE 4: QUIZ VIEW (MULTIPLE CHOICE) ====== -->
    <div id="pane-quiz" class="tab-pane">
      <div class="quiz-workspace">
        <div class="quiz-header-card">
          <div class="quiz-hud">
            <div class="hud-item">
              <span style="color: var(--text-muted);">题号:</span>
              <span id="quizIndexText" style="color: var(--primary);">1 / 20</span>
            </div>
            <div class="hud-item">
              <span style="color: var(--text-muted);">得分:</span>
              <span id="quizScoreText" style="color: var(--success);">0</span>
            </div>
            <div class="hud-item">
              <span>连胜:</span>
              <span id="quizStreakText">0 🔥</span>
            </div>
          </div>

          <div style="display: flex; gap: 10px; align-items: center;">
            <select id="quizScopeSelect" class="list-select" style="padding: 4px 8px; font-size: 12px;">
              <option value="current">当前所选 List</option>
              <option value="hf_150">🔥 真题超高频 Top 150</option>
              <option value="hf_350">⚡ 真题高频 Top 350</option>
              <option value="hf_600">📌 真题高频 Top 600</option>
              <option value="hf_wb">🎯 选词填空真题词库</option>
              <option value="hf_opt">🏆 题干与选项高频词</option>
              <option value="errors">仅测试需复习/错题</option>
              <option value="starred">仅测试生词本</option>
              <option value="random20">随机 20 题 (全库)</option>
              <option value="random50">随机 50 题 (全库)</option>
            </select>
            <button id="quizRestartBtn" class="icon-btn" style="padding: 4px 10px; font-size: 12px;">重新开始</button>
          </div>
        </div>

        <div class="quiz-card" id="quizCard">
          <div class="quiz-word" id="quizQuestionWord">abandon</div>
          <div class="quiz-phone-row">
            <span class="card-phonetic" id="quizQuestionPhone">/ əˈbændən /</span>
            <button id="quizAudioBtn" class="audio-play-btn" style="margin-left: 8px;" title="发音">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>

          <div class="quiz-options-grid" id="quizOptionsGrid"></div>
        </div>
      </div>
    </div>

    <!-- ====== PANE 5: NOTEBOOK VIEW ====== -->
    <div id="pane-notebook" class="tab-pane">
      <div class="notebook-header">
        <div>
          <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 4px;">重难点 · 生词与错题本</h3>
          <p style="font-size: 13px; color: var(--text-muted);">记录所有加入生词本 (★) 或在记忆/自测中遗忘的词汇，集中逐个攻克。</p>
        </div>

        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <button id="nbStartCardBtn" class="icon-btn" style="background: var(--primary); color: #fff; border-color: var(--primary);">🗂️ 集中卡片特训</button>
          <button id="nbStartSpellBtn" class="icon-btn" style="background: var(--primary-subtle); color: var(--primary); border-color: var(--primary);">✍️ 生词拼写默写</button>
          <button id="nbStartQuizBtn" class="icon-btn">🎯 针对性单选</button>
          <button id="nbExportTextBtn" class="icon-btn">📄 导出生词清单</button>
          <button id="nbClearMasteredBtn" class="icon-btn">🧹 清理已掌握生词</button>
        </div>
      </div>

      <div class="word-list-container" id="notebookListContainer"></div>
    </div>

    <!-- ====== PANE 6: STUDY PLAN & EBBINGHAUS ====== -->
    <div id="pane-plan" class="tab-pane">
      <div class="stats-grid">
        <div class="analytics-card">
          <h4 class="card-title-lg">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            词汇掌握度全景
          </h4>
          <div style="margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
              <span>已掌握比例</span>
              <strong id="planPctLabel" style="color: var(--success);">0%</strong>
            </div>
            <div class="progress-track" style="height: 12px;">
              <div id="planBarMastered" class="progress-seg seg-mastered" style="width: 0%;"></div>
              <div id="planBarReview" class="progress-seg seg-review" style="width: 0%;"></div>
            </div>
          </div>

          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; text-align: center;">
            <div style="background: var(--bg-card-subtle); padding: 12px; border-radius: var(--radius-md);">
              <div style="font-size: 11px; color: var(--text-muted);">已掌握</div>
              <div id="planMasteredCount" style="font-size: 20px; font-weight: 800; color: var(--success);">0</div>
            </div>
            <div style="background: var(--bg-card-subtle); padding: 12px; border-radius: var(--radius-md);">
              <div style="font-size: 11px; color: var(--text-muted);">需复习</div>
              <div id="planReviewCount" style="font-size: 20px; font-weight: 800; color: var(--warning);">0</div>
            </div>
            <div style="background: var(--bg-card-subtle); padding: 12px; border-radius: var(--radius-md);">
              <div style="font-size: 11px; color: var(--text-muted);">未背诵</div>
              <div id="planUnlearnedCount" style="font-size: 20px; font-weight: 800; color: var(--text-muted);">2220</div>
            </div>
          </div>
        </div>

        <div class="analytics-card">
          <h4 class="card-title-lg">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            每日计划 &amp; 预计周期
          </h4>

          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
            <label style="font-size: 13px; color: var(--text-sub);">每日目标背诵:</label>
            <select id="dailyTargetSelect" class="list-select">
              <option value="30">30 词 / 天 (~74天)</option>
              <option value="50" selected>50 词 / 天 (~45天 - 推荐)</option>
              <option value="80">80 词 / 天 (~28天 - 冲刺)</option>
              <option value="100">100 词 / 天 (~22天 - 极限)</option>
            </select>
          </div>

          <div style="background: var(--primary-subtle); padding: 14px; border-radius: var(--radius-md); font-size: 13px; color: var(--text-main); margin-bottom: 14px;">
            💡 <strong>艾宾浩斯记忆周期律：</strong><br>
            初次学习后，在 <strong>20分钟、1天、2天、4天、7天、15天</strong> 分别进行快速复习，可将瞬时记忆转化为永久长时记忆！
          </div>

          <div style="display: flex; gap: 10px;">
            <button id="exportBackupBtn" class="icon-btn" style="flex: 1; justify-content: center;">
              💾 导出进度备份
            </button>
            <button id="importBackupBtn" class="icon-btn" style="flex: 1; justify-content: center;">
              📂 恢复学习记录
            </button>
            <input type="file" id="backupFileInput" accept=".json" style="display: none;">
          </div>
        </div>
      </div>

      <div class="analytics-card">
        <h4 class="card-title-lg">📅 45 天艾宾浩斯背诵与循环复习打卡表 (按每天 50 词)</h4>
        <div style="max-height: 420px; overflow-y: auto;">
          <table class="ebbinghaus-table">
            <thead>
              <tr>
                <th style="width: 50px; text-align: center;">打卡</th>
                <th style="width: 80px;">天数</th>
                <th style="width: 150px;">今日新学 (New)</th>
                <th>今日必须循环复习 (Review Lists)</th>
              </tr>
            </thead>
            <tbody id="ebbinghausTableBody"></tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

  <!-- Shortcuts Modal -->
  <div class="modal-overlay" id="shortcutsModal">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="font-size: 18px; font-weight: 700;">键盘快捷键指南</h3>
        <button id="closeModalBtn" class="icon-btn" style="padding: 4px 8px;">✕</button>
      </div>

      <div style="margin-bottom: 14px;">
        <h4 style="font-size: 14px; font-weight: 600; color: var(--primary); margin-bottom: 6px;">✍️ 单词拼写默写模式</h4>
        <div class="shortcut-row"><span>提交拼写</span> <span><kbd>Enter</kbd></span></div>
        <div class="shortcut-row"><span>重听发音</span> <span><kbd>R</kbd></span></div>
        <div class="shortcut-row"><span>提示首字母</span> <span><kbd>Alt</kbd> + <kbd>1</kbd></span></div>
        <div class="shortcut-row"><span>提示下一个字母</span> <span><kbd>Alt</kbd> + <kbd>2</kbd></span></div>
      </div>

      <div style="margin-bottom: 14px;">
        <h4 style="font-size: 14px; font-weight: 600; color: var(--primary); margin-bottom: 6px;">🗂️ 智能卡片模式</h4>
        <div class="shortcut-row"><span>翻转卡片 / 查看释义</span> <span><kbd>Space</kbd> 或 <kbd>Enter</kbd></span></div>
        <div class="shortcut-row"><span>评分：忘啦 / 模糊 / 记住 / 熟练</span> <span><kbd>1</kbd> <kbd>2</kbd> <kbd>3</kbd> <kbd>4</kbd></span></div>
        <div class="shortcut-row"><span>上一词 / 下一词</span> <span><kbd>←</kbd> / <kbd>→</kbd> 或 <kbd>J</kbd> / <kbd>K</kbd></span></div>
        <div class="shortcut-row"><span>重听发音</span> <span><kbd>R</kbd></span></div>
        <div class="shortcut-row"><span>收藏生词</span> <span><kbd>S</kbd></span></div>
      </div>

      <div>
        <h4 style="font-size: 14px; font-weight: 600; color: var(--primary); margin-bottom: 6px;">🎯 四选一自测模式</h4>
        <div class="shortcut-row"><span>选择选项 A / B / C / D</span> <span><kbd>A</kbd> <kbd>B</kbd> <kbd>C</kbd> <kbd>D</kbd> 或 <kbd>1</kbd> <kbd>2</kbd> <kbd>3</kbd> <kbd>4</kbd></span></div>
      </div>
    </div>
  </div>

  <audio id="nativeAudioPlayer" preload="none"></audio>

  <!-- Embedded Complete Dataset & Application Logic -->
  <script>
    // 2220 CET-6 Words Complete Dataset
    const RAW_WORDS = {words_json_str};
    // Authentic Past-Exam High Frequency Dataset (keyed by word id)
    const HF_DATA = {hf_json_str};

    function getHfInfo(id) {{
      return HF_DATA[String(id)] || null;
    }}

    const STORAGE_KEY = 'cet6_study_data_v2';

    // Application State
    let appState = {{
      progress: {{}},
      currentList: '1',
      listStatusFilter: 'all',
      listMaskMode: 'none',
      listSearchTerm: '',
      listPage: 1,
      listPageSize: 50,
      hf: {{
        cat: 'top600',
        slice: 'all',
        pos: 'all',
        status: 'all',
        sort: 'rank',
        maskMode: 'none',
        showExamples: true,
        searchTerm: '',
        page: 1,
        pageSize: 50
      }},
      cardIndex: 0,
      cardFlipped: false,
      autoAudio: true,
      shuffleCards: false,
      cardQueue: [],
      soundType: '2', // '2' for US, '1' for UK
      theme: 'light',
      // Dedicated Spelling State
      spell: {{
        questions: [],
        currentIndex: 0,
        revealedCount: 0,
        correctCount: 0,
        streak: 0,
        attemptsLeft: 3,
        answering: false,
        retryQueue: [],
        status: 'idle' // 'typing', 'revealed', 'next_ready'
      }},
      quiz: {{
        questions: [],
        currentIndex: 0,
        score: 0,
        streak: 0,
        scope: 'current',
        answering: false
      }},
      ebbinghausChecks: {{}},
      stats: {{
        todayDate: new Date().toISOString().slice(0, 10),
        todayStudiedIds: {{}}
      }}
    }};

    function loadState() {{
      try {{
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {{
          const parsed = JSON.parse(saved);
          if (parsed.progress) appState.progress = parsed.progress;
          if (parsed.soundType) appState.soundType = parsed.soundType;
          if (parsed.theme) appState.theme = parsed.theme;
          if (parsed.ebbinghausChecks) appState.ebbinghausChecks = parsed.ebbinghausChecks;
          if (parsed.stats) {{
            const today = new Date().toISOString().slice(0, 10);
            if (parsed.stats.todayDate === today) {{
              appState.stats = parsed.stats;
            }} else {{
              appState.stats.todayDate = today;
              appState.stats.todayStudiedIds = {{}};
            }}
          }}
        }}
      }} catch (e) {{
        console.warn('Load state err:', e);
      }}
    }}

    function saveState() {{
      try {{
        localStorage.setItem(STORAGE_KEY, JSON.stringify({{
          progress: appState.progress,
          soundType: appState.soundType,
          theme: appState.theme,
          ebbinghausChecks: appState.ebbinghausChecks,
          stats: appState.stats
        }}));
      }} catch (e) {{
        console.warn('Save state err:', e);
      }}
      updateGlobalStatsUI();
    }}

    function getWordStatus(id) {{
      return (appState.progress[id] && appState.progress[id].status !== undefined) ? appState.progress[id].status : 0;
    }}

    function isWordStarred(id) {{
      return !!(appState.progress[id] && appState.progress[id].starred);
    }}

    function setWordStatus(id, status) {{
      if (!appState.progress[id]) appState.progress[id] = {{}};
      appState.progress[id].status = status;
      appState.progress[id].lastStudied = Date.now();
      appState.stats.todayStudiedIds[id] = true;
      saveState();
    }}

    function toggleWordStar(id) {{
      if (!appState.progress[id]) appState.progress[id] = {{}};
      appState.progress[id].starred = !appState.progress[id].starred;
      saveState();
      return appState.progress[id].starred;
    }}

    const audioPlayer = document.getElementById('nativeAudioPlayer');
    function playAudio(word) {{
      if (!word) return;
      const cleanWord = word.trim().toLowerCase();
      const type = appState.soundType || '2';
      const audioUrl = `https://dict.youdao.com/dictvoice?audio=${{encodeURIComponent(cleanWord)}}&type=${{type}}`;
      
      audioPlayer.src = audioUrl;
      const playPromise = audioPlayer.play();
      if (playPromise !== undefined) {{
        playPromise.catch(() => {{
          if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(cleanWord);
            utterance.lang = (type === '1') ? 'en-GB' : 'en-US';
            utterance.rate = 0.95;
            window.speechSynthesis.speak(utterance);
          }}
        }});
      }}
    }}

    function formatTrans(text) {{
      if (!text) return '';
      return text.replace(/(^|[;\s])(vt\.|vi\.|v\.|n\.|adj\.|adv\.|prep\.|conj\.|pron\.|num\.|art\.|int\.)/gi, (match, p1, p2) => {{
        let cls = 'tag-other';
        const lower = p2.toLowerCase();
        if (lower.startsWith('v')) cls = 'tag-v';
        else if (lower.startsWith('n')) cls = 'tag-n';
        else if (lower.startsWith('adj')) cls = 'tag-adj';
        else if (lower.startsWith('adv')) cls = 'tag-adv';
        return `${{p1}}<span class="pos-tag ${{cls}}">${{p2}}</span> `;
      }});
    }}

    function updateGlobalStatsUI() {{
      let mastered = 0;
      let review = 0;
      let starred = 0;

      RAW_WORDS.forEach(w => {{
        const s = getWordStatus(w.id);
        if (s === 2) mastered++;
        else if (s === 1) review++;
        if (isWordStarred(w.id)) starred++;
      }});

      const total = RAW_WORDS.length;
      const masteredPct = Math.round((mastered / total) * 100);
      const reviewPct = Math.round((review / total) * 100);

      document.getElementById('statTotal').innerHTML = `${{total}}<small>词</small>`;
      document.getElementById('statToday').innerHTML = `${{Object.keys(appState.stats.todayStudiedIds || {{}}).length}}<small>词</small>`;
      document.getElementById('statMastered').innerHTML = `${{mastered}}<small>${{masteredPct}}%</small>`;
      document.getElementById('statReview').innerHTML = `${{review}}<small>词</small>`;

      document.getElementById('barMastered').style.width = masteredPct + '%';
      document.getElementById('barReview').style.width = reviewPct + '%';

      document.getElementById('badgeNotebook').textContent = starred + review;

      const planBarM = document.getElementById('planBarMastered');
      if (planBarM) planBarM.style.width = masteredPct + '%';
      const planBarR = document.getElementById('planBarReview');
      if (planBarR) planBarR.style.width = reviewPct + '%';
      const planPctLbl = document.getElementById('planPctLabel');
      if (planPctLbl) planPctLbl.textContent = masteredPct + '%';
      const planMC = document.getElementById('planMasteredCount');
      if (planMC) planMC.textContent = mastered;
      const planRC = document.getElementById('planReviewCount');
      if (planRC) planRC.textContent = review;
      const planUC = document.getElementById('planUnlearnedCount');
      if (planUC) planUC.textContent = total - mastered - review;

      if (typeof updateHfDashboard === 'function') {{
        updateHfDashboard();
      }}
    }}

    function initDropdowns() {{
      const totalLists = Math.ceil(RAW_WORDS.length / 50);
      const cardSelect = document.getElementById('cardListSelect');
      const listSelect = document.getElementById('listGroupSelect');
      const spellSelect = document.getElementById('spellScopeSelect');

      cardSelect.innerHTML = '';
      listSelect.innerHTML = '';
      spellSelect.innerHTML = '';

      const optAll = document.createElement('option');
      optAll.value = 'all';
      optAll.textContent = `全部词汇 (${{RAW_WORDS.length}} 词)`;
      listSelect.appendChild(optAll.cloneNode(true));
      cardSelect.appendChild(optAll.cloneNode(true));
      spellSelect.appendChild(optAll);

      // High-Frequency Exam Groups
      const hfOptions = [
        ['hf_150', '🔥 真题超高频 Top 150 (必背)'],
        ['hf_350', '⚡ 真题高频 Top 350 (重点)'],
        ['hf_600', '📌 真题高频 Top 600 (全库)'],
        ['hf_wb', '🎯 历年选词填空词库真题词'],
        ['hf_opt', '🏆 题干与选项高频考点词']
      ];
      [cardSelect, listSelect, spellSelect].forEach(sel => {{
        const grp = document.createElement('optgroup');
        grp.label = '🔥 真题高频专项';
        hfOptions.forEach(([val, label]) => {{
          const o = document.createElement('option');
          o.value = val;
          o.textContent = label;
          grp.appendChild(o);
        }});
        sel.appendChild(grp);
      }});

      const listGrpLabel = '📚 顺序词表 (List 01 ~ 45)';
      [cardSelect, listSelect, spellSelect].forEach(sel => {{
        const grp = document.createElement('optgroup');
        grp.label = listGrpLabel;
        for (let i = 1; i <= totalLists; i++) {{
          const start = (i - 1) * 50 + 1;
          const end = Math.min(i * 50, RAW_WORDS.length);
          const opt = document.createElement('option');
          opt.value = String(i);
          opt.textContent = `List ${{i.toString().padStart(2, '0')}} (${{start}} ~ ${{end}})`;
          if (i === 1) opt.selected = true;
          grp.appendChild(opt);
        }}
        sel.appendChild(grp);
      }});

      const optStarred = document.createElement('option');
      optStarred.value = 'starred';
      optStarred.textContent = '⭐ 仅生词本词汇';
      cardSelect.appendChild(optStarred.cloneNode(true));
      spellSelect.appendChild(optStarred);

      const optReview = document.createElement('option');
      optReview.value = 'review';
      optReview.textContent = '⚡ 仅需复习词汇';
      cardSelect.appendChild(optReview.cloneNode(true));
      spellSelect.appendChild(optReview);

      const optR20 = document.createElement('option');
      optR20.value = 'random20';
      optR20.textContent = '🎲 随机 20 词速测';
      spellSelect.appendChild(optR20);

      const optR50 = document.createElement('option');
      optR50.value = 'random50';
      optR50.textContent = '🎲 随机 50 词深测';
      spellSelect.appendChild(optR50);
    }}

    function getWordsForSelection(selectionKey) {{
      if (selectionKey === 'all') return [...RAW_WORDS];
      if (selectionKey === 'hf_150') {{
        return RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.r <= 150; }})
          .sort((a, b) => getHfInfo(a.id).r - getHfInfo(b.id).r);
      }}
      if (selectionKey === 'hf_350') {{
        return RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.r <= 350; }})
          .sort((a, b) => getHfInfo(a.id).r - getHfInfo(b.id).r);
      }}
      if (selectionKey === 'hf_600') {{
        return RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.r <= 600; }})
          .sort((a, b) => getHfInfo(a.id).r - getHfInfo(b.id).r);
      }}
      if (selectionKey === 'hf_wb') {{
        return RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.wb > 0; }})
          .sort((a, b) => (getHfInfo(b.id).wb - getHfInfo(a.id).wb) || (getHfInfo(a.id).r - getHfInfo(b.id).r));
      }}
      if (selectionKey === 'hf_opt') {{
        return RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.qf >= 3; }})
          .sort((a, b) => (getHfInfo(b.id).qf - getHfInfo(a.id).qf) || (getHfInfo(a.id).r - getHfInfo(b.id).r));
      }}
      if (selectionKey === 'starred') return RAW_WORDS.filter(w => isWordStarred(w.id));
      if (selectionKey === 'review') return RAW_WORDS.filter(w => getWordStatus(w.id) === 1);
      if (selectionKey === 'random20') return [...RAW_WORDS].sort(() => 0.5 - Math.random()).slice(0, 20);
      if (selectionKey === 'random50') return [...RAW_WORDS].sort(() => 0.5 - Math.random()).slice(0, 50);

      const listNum = parseInt(selectionKey, 10);
      if (!isNaN(listNum)) {{
        const start = (listNum - 1) * 50;
        const end = Math.min(listNum * 50, RAW_WORDS.length);
        return RAW_WORDS.slice(start, end);
      }}
      return [...RAW_WORDS];
    }}

    // ====== FLASHCARD ENGINE ======
    function setupCardQueue() {{
      const sel = document.getElementById('cardListSelect').value;
      let words = getWordsForSelection(sel);

      if (appState.shuffleCards) {{
        words = [...words];
        for (let i = words.length - 1; i > 0; i--) {{
          const j = Math.floor(Math.random() * (i + 1));
          [words[i], words[j]] = [words[j], words[i]];
        }}
      }}

      appState.cardQueue = words;
      appState.cardIndex = 0;
      appState.cardFlipped = false;
      renderCurrentCard();
    }}

    function renderCurrentCard() {{
      const inner = document.getElementById('flashcardInner');
      appState.cardFlipped = false;
      inner.classList.remove('flipped');

      const queue = appState.cardQueue;
      const counter = document.getElementById('cardCounter');

      if (!queue || queue.length === 0) {{
        document.getElementById('cardWordText').textContent = '暂无词汇';
        document.getElementById('cardPhoneticText').textContent = '';
        document.getElementById('cardTransText').textContent = '当前选择的分组暂无符合条件的单词';
        document.getElementById('cardDetailText').textContent = '请在上方切换分组或添加生词';
        document.getElementById('cardHfBadgeFront').style.display = 'none';
        document.getElementById('cardHfBadgeBack').style.display = 'none';
        document.getElementById('cardHfExample').style.display = 'none';
        counter.textContent = '0 / 0';
        return;
      }}

      if (appState.cardIndex >= queue.length) appState.cardIndex = queue.length - 1;
      if (appState.cardIndex < 0) appState.cardIndex = 0;

      const word = queue[appState.cardIndex];
      counter.textContent = `${{appState.cardIndex + 1}} / ${{queue.length}}`;

      const status = getWordStatus(word.id);
      const starred = isWordStarred(word.id);

      const statusTag = document.getElementById('cardStatusTag');
      const statusTagBack = document.getElementById('cardStatusTagBack');
      const starBtn = document.getElementById('cardStarBtn');

      const statusLabels = ['未学习', '需复习', '已掌握'];
      const statusClasses = ['unlearned', 'review', 'mastered'];

      [statusTag, statusTagBack].forEach(tag => {{
        tag.textContent = statusLabels[status];
        tag.className = 'status-tag ' + statusClasses[status];
      }});

      if (starred) {{
        starBtn.classList.add('starred');
      }} else {{
        starBtn.classList.remove('starred');
      }}

      document.getElementById('cardWordText').textContent = word.w;
      document.getElementById('cardPhoneticText').textContent = word.p ? `/${{word.p}}/` : '';

      document.getElementById('cardWordTextBack').textContent = word.w;
      document.getElementById('cardTransText').innerHTML = formatTrans(word.t);
      document.getElementById('cardDetailText').innerHTML = word.d ? word.d : '大纲核心词汇，背诵时注意词性搭配与拼写';

      const hf = getHfInfo(word.id);
      const badgeFront = document.getElementById('cardHfBadgeFront');
      const badgeBack = document.getElementById('cardHfBadgeBack');
      const cardHfEx = document.getElementById('cardHfExample');

      if (hf && (hf.tier > 0 || hf.wb > 0 || hf.qf >= 3)) {{
        const wbTxt = hf.wb > 0 ? ` · 🎯选词库×${{hf.wb}}` : '';
        const badgeLabel = hf.tier > 0
          ? `🔥 真题高频 #${{hf.r}} · 出现${{hf.f}}次${{wbTxt}}`
          : `🎯 选词填空词库×${{hf.wb}} · 真题${{hf.f}}次`;
        badgeFront.textContent = badgeLabel;
        badgeFront.style.display = 'inline-flex';
        badgeBack.textContent = hf.tier > 0 ? `🔥 高频 #${{hf.r}}` : '🎯 选词库';
        badgeBack.style.display = 'inline-flex';
      }} else {{
        badgeFront.style.display = 'none';
        badgeBack.style.display = 'none';
      }}

      if (hf && hf.ex && hf.ex.en) {{
        cardHfEx.innerHTML = `<span class="hf-example-src">📖 [${{escapeHtml(hf.ex.s)}}]</span>${{highlightKeywordInSentence(hf.ex.en, hf.ex.kw)}}`;
        cardHfEx.style.display = 'block';
      }} else {{
        cardHfEx.style.display = 'none';
      }}

      if (appState.autoAudio) {{
        playAudio(word.w);
      }}
    }}

    function flipCard() {{
      const inner = document.getElementById('flashcardInner');
      appState.cardFlipped = !appState.cardFlipped;
      if (appState.cardFlipped) {{
        inner.classList.add('flipped');
      }} else {{
        inner.classList.remove('flipped');
      }}
    }}

    function rateCurrentCard(rating) {{
      const queue = appState.cardQueue;
      if (!queue || queue.length === 0) return;
      const word = queue[appState.cardIndex];

      if (rating === 1) {{
        setWordStatus(word.id, 1);
      }} else if (rating === 2) {{
        setWordStatus(word.id, 1);
      }} else if (rating === 3 || rating === 4) {{
        setWordStatus(word.id, 2);
      }}

      if (appState.cardIndex < queue.length - 1) {{
        appState.cardIndex++;
        renderCurrentCard();
      }} else {{
        renderCurrentCard();
        alert('🎉 太棒了！当前组的所有词汇已背完一轮！');
      }}
    }}

    // ====== BULLETPROOF WORD SPELLING ENGINE ======
    function startSpellPractice(customWords = null) {{
      const selScope = document.getElementById('spellScopeSelect').value;
      let pool = customWords || getWordsForSelection(selScope);

      if (!pool || pool.length === 0) {{
        alert('当前分组没有单词可供拼写！请选择包含单词的分组。');
        return;
      }}

      pool = [...pool].sort(() => 0.5 - Math.random());

      appState.spell.questions = pool;
      appState.spell.currentIndex = 0;
      appState.spell.correctCount = 0;
      appState.spell.streak = 0;
      appState.spell.revealedCount = 0;
      appState.spell.attemptsLeft = 3;
      appState.spell.answering = true;
      appState.spell.retryQueue = [];
      appState.spell.status = 'typing';

      renderSpellQuestion();
    }}

    function renderSpellQuestion() {{
      const sState = appState.spell;
      const card = document.getElementById('spellCard');

      if (sState.currentIndex >= sState.questions.length) {{
        const total = sState.questions.length;
        const pct = Math.round((sState.correctCount / total) * 100);
        const retryCount = sState.retryQueue.length;

        card.innerHTML = `
          <div style="padding: 24px 10px; text-align: center;">
            <div style="font-size: 54px; margin-bottom: 12px;">🎖️</div>
            <h3 style="font-size: 24px; font-weight: 800; margin-bottom: 8px;">拼写听写挑战完成！</h3>
            <p style="font-size: 16px; color: var(--text-sub); margin-bottom: 20px;">
              本次共练习 <strong>${{total}}</strong> 词，初次全对 <strong style="color: var(--success); font-size: 22px;">${{sState.correctCount}}</strong> 词 (正确率 ${{pct}}%)
            </p>

            ${{retryCount > 0 ? `
              <div style="background: var(--warning-subtle); border: 1px solid var(--warning); border-radius: var(--radius-md); padding: 14px 18px; margin-bottom: 24px; text-align: left; max-width: 500px; margin-left: auto; margin-right: auto;">
                <div style="font-weight: 700; color: var(--warning); margin-bottom: 6px;">⚠️ 本次有 ${{retryCount}} 个单词需要强化巩固：</div>
                <div style="font-size: 13px; color: var(--text-sub); max-height: 120px; overflow-y: auto;">
                  ${{sState.retryQueue.map((w, i) => `${{i+1}}. <strong>${{w.w}}</strong> [/${{w.p}}/] : ${{w.t}}`).join('<br>')}}
                </div>
              </div>
              <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
                <button class="icon-btn" onclick="retrySpellingErrors()" style="background: var(--warning); color: #fff; border-color: var(--warning); padding: 10px 20px; font-weight: 700;">
                  🔄 针对拼错的 ${{retryCount}} 词重练一轮
                </button>
                <button class="icon-btn" onclick="startSpellPractice()" style="padding: 10px 20px;">
                  重新开始本组
                </button>
              </div>
            ` : `
              <div style="color: var(--success); font-weight: 700; margin-bottom: 20px;">🎉 完美通关！全部单词初次拼写完全正确！</div>
              <button class="icon-btn" onclick="startSpellPractice()" style="background: var(--primary); color: #fff; padding: 10px 24px; font-size: 15px; border-color: var(--primary);">
                再来一轮
              </button>
            `}}
          </div>
        `;
        return;
      }}

      const word = sState.questions[sState.currentIndex];
      sState.answering = true;
      sState.revealedCount = 0;
      sState.attemptsLeft = 3;
      sState.status = 'typing';

      // Update HUD
      document.getElementById('spellIndexText').textContent = `${{sState.currentIndex + 1}} / ${{sState.questions.length}}`;
      const answered = sState.currentIndex;
      const acc = answered > 0 ? Math.round((sState.correctCount / answered) * 100) : 100;
      document.getElementById('spellAccuracyText').textContent = `${{sState.correctCount}} 词 (${{acc}}%)`;
      document.getElementById('spellStreakText').textContent = `${{sState.streak}} 🔥`;

      // Prompt Content
      document.getElementById('spellPromptTrans').innerHTML = formatTrans(word.t);
      document.getElementById('spellPromptDetail').innerHTML = word.d ? `💡 考点搭配: ${{word.d}}` : '💡 大纲六级高频核心词汇';
      document.getElementById('spellPromptPhone').textContent = word.p ? `/${{word.p}}/` : '';

      // Reset Letter slots
      renderLetterSlots(word.w, '');

      // Reset Input box
      const input = document.getElementById('spellInputMain');
      input.value = '';
      input.className = 'spell-input-large';
      input.disabled = false;
      input.placeholder = `共 ${{word.w.length}} 个英文字母 (3次尝试机会)...`;
      input.focus();

      // Reset Buttons & Feedback
      document.getElementById('spellSubmitBtn').textContent = '确定 (Enter)';
      document.getElementById('spellSubmitBtn').style.display = 'inline-flex';
      document.getElementById('spellHintFirstBtn').disabled = false;
      document.getElementById('spellHintNextBtn').disabled = false;
      document.getElementById('spellGiveUpBtn').disabled = false;
      document.getElementById('spellFeedbackArea').innerHTML = `
        <span style="color: var(--text-muted); font-size: 13px;">❤️ 剩余尝试机会: <strong style="color: var(--primary);">3</strong> 次</span>
      `;

      if (appState.autoAudio) {{
        playAudio(word.w);
      }}
    }}

    // Render letter slot boxes synced with what the user has typed or revealed
    function renderLetterSlots(targetWord, currentInput = '') {{
      const container = document.getElementById('spellLetterSlots');
      container.innerHTML = '';
      const cleanTarget = targetWord.trim().toLowerCase();
      const cleanInput = currentInput.trim().toLowerCase();

      for (let i = 0; i < cleanTarget.length; i++) {{
        const targetChar = cleanTarget[i];
        const slot = document.createElement('div');
        slot.className = 'letter-slot';

        if (targetChar === '-' || targetChar === ' ' || targetChar === "'") {{
          slot.textContent = targetChar;
          slot.style.border = 'none';
          slot.style.background = 'transparent';
        }} else if (i < cleanInput.length) {{
          slot.textContent = cleanInput[i];
          slot.classList.add('typing');
        }} else if (i < appState.spell.revealedCount) {{
          slot.textContent = targetChar;
          slot.classList.add('revealed');
        }} else {{
          slot.textContent = '';
        }}
        container.appendChild(slot);
      }}

      const countBadge = document.createElement('span');
      countBadge.style.fontSize = '12px';
      countBadge.style.color = 'var(--text-muted)';
      countBadge.style.marginLeft = '8px';
      countBadge.textContent = `(${{cleanTarget.length}} 字母)`;
      container.appendChild(countBadge);
    }}

    // Live typing sync to letter slots
    function handleSpellInputLive() {{
      const sState = appState.spell;
      if (!sState.answering || sState.status !== 'typing') return;
      const word = sState.questions[sState.currentIndex];
      const input = document.getElementById('spellInputMain');
      renderLetterSlots(word.w, input.value);
    }}

    // Main Submit Action
    function handleSpellSubmitAction() {{
      const sState = appState.spell;
      if (!sState.answering) {{
        // If answer was already revealed, Enter acts as Next
        if (sState.status === 'next_ready') {{
          advanceToNextSpellWord();
        }}
        return;
      }}

      const word = sState.questions[sState.currentIndex];
      const target = word.w.trim().toLowerCase();
      const input = document.getElementById('spellInputMain');
      const val = input.value.trim().toLowerCase();
      const fb = document.getElementById('spellFeedbackArea');

      // Empty input check
      if (!val) {{
        input.focus();
        fb.innerHTML = '<span style="color: var(--warning); font-size: 13px;">⚠️ 请先在输入框中键入英文单词</span>';
        return;
      }}

      // STRICT EQUALITY CHECK
      if (val === target) {{
        // ===== CORRECT =====
        sState.answering = false;
        sState.status = 'next_ready';
        input.classList.remove('wrong');
        input.classList.add('correct');
        input.disabled = true;

        // Turn all slots green
        const slots = document.querySelectorAll('.letter-slot');
        slots.forEach(s => {{
          s.className = 'letter-slot correct-glow';
        }});

        fb.innerHTML = `
          <div style="color: var(--success); font-size: 16px; font-weight: 700; display: flex; align-items: center; gap: 6px;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
            恭喜！拼写完全正确！
          </div>
        `;

        if (sState.attemptsLeft === 3 && sState.revealedCount === 0) {{
          sState.correctCount++;
          sState.streak++;
          setWordStatus(word.id, 2); // mark mastered
        }} else {{
          setWordStatus(word.id, 1); // was helped, mark review
        }}

        // Smooth 0.85s transition to next word
        setTimeout(() => {{
          advanceToNextSpellWord();
        }}, 850);

      }} else {{
        // ===== WRONG =====
        sState.attemptsLeft--;

        input.classList.remove('correct');
        input.classList.add('wrong');
        setTimeout(() => input.classList.remove('wrong'), 450);

        if (sState.attemptsLeft > 0) {{
          // Still has attempts left
          fb.innerHTML = `
            <div style="color: var(--danger); font-size: 14px;">
              ❌ 拼写有误，不是 "<strong>${{val}}</strong>"！还剩 <strong>${{sState.attemptsLeft}}</strong> 次机会，请仔细检查后重试
            </div>
          `;
          // Select all text in input so user can effortlessly re-type
          input.focus();
          input.select();

        }} else {{
          // All 3 attempts exhausted: REVEAL CORRECT ANSWER
          sState.answering = false;
          sState.status = 'next_ready';
          sState.streak = 0;
          setWordStatus(word.id, 1);

          if (!sState.retryQueue.some(item => item.id === word.id)) {{
            sState.retryQueue.push(word);
          }}

          revealCorrectAnswer(word, `❌ 3次尝试已用完`);
        }}
      }}
    }}

    function revealCorrectAnswer(word, reasonText) {{
      const sState = appState.spell;
      sState.answering = false;
      sState.status = 'next_ready';

      const input = document.getElementById('spellInputMain');
      input.disabled = true;
      input.value = word.w;

      // Fill all slots with revealed style
      const slots = document.querySelectorAll('.letter-slot');
      const clean = word.w.trim().toLowerCase();
      slots.forEach((s, i) => {{
        if (i < clean.length) {{
          s.textContent = clean[i];
          s.className = 'letter-slot revealed';
        }}
      }});

      const fb = document.getElementById('spellFeedbackArea');
      fb.innerHTML = `
        <div class="reveal-box">
          <div style="color: var(--danger); font-weight: 700; margin-bottom: 6px;">${{reasonText}}</div>
          <div style="font-size: 16px; margin-bottom: 10px;">
            正确拼写是: <strong style="color: var(--primary); font-size: 22px; letter-spacing: 1px;">${{word.w}}</strong>
            <span style="font-size: 14px; color: var(--text-muted); margin-left: 6px;">/${{word.p}}/</span>
          </div>
          <button class="icon-btn" onclick="advanceToNextSpellWord()" style="background: var(--primary); color: #fff; padding: 6px 18px; font-weight: 700; margin: 0 auto;">
            我记住了，下一题 (Enter) →
          </button>
        </div>
      `;

      // Disable hint buttons in revealed state
      document.getElementById('spellHintFirstBtn').disabled = true;
      document.getElementById('spellHintNextBtn').disabled = true;
      document.getElementById('spellGiveUpBtn').disabled = true;
      document.getElementById('spellSubmitBtn').textContent = '下一题 (Enter)';
    }}

    function advanceToNextSpellWord() {{
      const sState = appState.spell;
      sState.currentIndex++;
      renderSpellQuestion();
    }}

    function giveSpellHint(type) {{
      const sState = appState.spell;
      if (!sState.answering || sState.status !== 'typing') return;

      const word = sState.questions[sState.currentIndex];
      const target = word.w.trim().toLowerCase();

      if (type === 'first') {{
        sState.revealedCount = Math.max(sState.revealedCount, 1);
      }} else if (type === 'next') {{
        if (sState.revealedCount < target.length) {{
          sState.revealedCount++;
        }}
      }}

      // Pre-fill input
      const input = document.getElementById('spellInputMain');
      input.value = target.slice(0, sState.revealedCount);
      renderLetterSlots(target, input.value);
      input.focus();
    }}

    function giveUpCurrentSpell() {{
      const sState = appState.spell;
      if (!sState.answering) return;

      const word = sState.questions[sState.currentIndex];
      sState.streak = 0;
      setWordStatus(word.id, 1); // mark review

      if (!sState.retryQueue.some(item => item.id === word.id)) {{
        sState.retryQueue.push(word);
      }}

      revealCorrectAnswer(word, '👀 已查看答案');
    }}

    function retrySpellingErrors() {{
      const sState = appState.spell;
      if (sState.retryQueue.length > 0) {{
        startSpellPractice([...sState.retryQueue]);
      }}
    }}

    // ====== WORD LIST ENGINE ======
    function renderWordList() {{
      const container = document.getElementById('wordListContainer');
      const selGroup = document.getElementById('listGroupSelect').value;
      const statusFilter = appState.listStatusFilter;
      const searchTerm = appState.listSearchTerm.trim().toLowerCase();

      let words = getWordsForSelection(selGroup);

      if (statusFilter === '0' || statusFilter === '1' || statusFilter === '2') {{
        const targetS = parseInt(statusFilter, 10);
        words = words.filter(w => getWordStatus(w.id) === targetS);
      }} else if (statusFilter === 'starred') {{
        words = words.filter(w => isWordStarred(w.id));
      }}

      if (searchTerm) {{
        words = words.filter(w => w.w.toLowerCase().includes(searchTerm) || w.t.includes(searchTerm));
      }}

      document.getElementById('listSummaryText').textContent = `共筛选出 ${{words.length}} 个单词`;

      const pageSize = appState.listPageSize;
      const totalPages = Math.ceil(words.length / pageSize) || 1;
      if (appState.listPage > totalPages) appState.listPage = totalPages;
      if (appState.listPage < 1) appState.listPage = 1;

      document.getElementById('pageInfoText').textContent = `第 ${{appState.listPage}} / ${{totalPages}} 页 (${{words.length}} 词)`;

      const start = (appState.listPage - 1) * pageSize;
      const pageWords = words.slice(start, start + pageSize);

      if (pageWords.length === 0) {{
        container.innerHTML = `
          <div style="padding: 48px; text-align: center; color: var(--text-muted);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin-bottom: 8px;"><circle cx="12" cy="12" r="10"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
            <p>没有找到符合条件的单词</p>
          </div>
        `;
        return;
      }}

      let html = '';
      const maskClass = appState.listMaskMode === 'cn' ? 'mask-cn' : (appState.listMaskMode === 'en' ? 'mask-en' : '');

      pageWords.forEach((w, idx) => {{
        const s = getWordStatus(w.id);
        const starred = isWordStarred(w.id);
        const statusText = s === 2 ? '已掌握' : (s === 1 ? '需复习' : '未学');
        const hf = getHfInfo(w.id);
        let hfBadgeHtml = '';
        if (hf && hf.tier > 0) {{
          hfBadgeHtml = `<span class="hf-list-badge" title="历年真题出现 ${{hf.f}} 次 (${{hf.p}} 套试卷)">🔥#${{hf.r}}</span>`;
        }} else if (hf && hf.wb > 0) {{
          hfBadgeHtml = `<span class="hf-list-badge" title="选词填空词库真题词 (${{hf.wb}} 次)">🎯词库</span>`;
        }}

        html += `
          <div class="word-row ${{maskClass}}" data-id="${{w.id}}">
            <div class="col-idx">${{start + idx + 1}}</div>
            <div class="col-word">
              <span class="col-word-text" onclick="this.classList.toggle('unmasked')">${{w.w}}</span>
              <button class="audio-play-btn" onclick="playAudio('${{w.w}}')" title="播放读音" style="width: 22px; height: 22px;">
                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
              </button>
              ${{hfBadgeHtml}}
            </div>
            <div class="col-phone">/${{w.p}}/</div>
            <div class="col-trans" onclick="this.classList.toggle('unmasked')">
              <div>${{formatTrans(w.t)}}</div>
              ${{w.d ? `<div class="col-detail-sub">${{w.d}}</div>` : ''}}
            </div>
            <div class="col-status">
              <span class="badge-status s${{s}}" onclick="cycleWordStatus(${{w.id}})" title="点击切换状态">${{statusText}}</span>
            </div>
            <div class="col-star" style="text-align: right;">
              <button class="star-btn ${{starred ? 'starred' : ''}}" onclick="toggleWordStarInList(${{w.id}}, this)" title="生词本">★</button>
            </div>
          </div>
        `;
      }});

      container.innerHTML = html;
    }}

    function cycleWordStatus(id) {{
      const current = getWordStatus(id);
      const next = (current + 1) % 3;
      setWordStatus(id, next);
      renderWordList();
    }}

    function toggleWordStarInList(id, btn) {{
      const isSt = toggleWordStar(id);
      if (isSt) {{
        btn.classList.add('starred');
      }} else {{
        btn.classList.remove('starred');
      }}
    }}

    // ====== QUIZ ENGINE ======
    function startQuiz(customWords = null) {{
      const customPool = Array.isArray(customWords) ? customWords : null;
      const scope = document.getElementById('quizScopeSelect').value;
      let pool = [];

      if (customPool) {{
        pool = [...customPool];
      }} else if (scope === 'current') {{
        const selList = document.getElementById('cardListSelect').value;
        pool = getWordsForSelection(selList);
      }} else if (scope.startsWith('hf_')) {{
        pool = getWordsForSelection(scope);
      }} else if (scope === 'errors') {{
        pool = RAW_WORDS.filter(w => getWordStatus(w.id) === 1);
      }} else if (scope === 'starred') {{
        pool = RAW_WORDS.filter(w => isWordStarred(w.id));
      }} else if (scope === 'random20') {{
        pool = [...RAW_WORDS].sort(() => 0.5 - Math.random()).slice(0, 20);
      }} else if (scope === 'random50') {{
        pool = [...RAW_WORDS].sort(() => 0.5 - Math.random()).slice(0, 50);
      }}

      if (pool.length < 4) {{
        alert('当前题库单词数量不足 4 个，请选择包含更多单词的测试范围！');
        return false;
      }}

      pool = [...pool].sort(() => 0.5 - Math.random());

      appState.quiz.questions = pool;
      appState.quiz.currentIndex = 0;
      appState.quiz.score = 0;
      appState.quiz.streak = 0;
      appState.quiz.answering = false;

      renderQuizQuestion();
      return true;
    }}

    function renderQuizQuestion() {{
      const qState = appState.quiz;
      const card = document.getElementById('quizCard');

      if (qState.currentIndex >= qState.questions.length) {{
        card.innerHTML = `
          <div style="padding: 30px 10px; text-align: center;">
            <div style="font-size: 54px; margin-bottom: 12px;">🏆</div>
            <h3 style="font-size: 24px; font-weight: 800; margin-bottom: 8px;">挑战完成！</h3>
            <p style="font-size: 16px; color: var(--text-sub); margin-bottom: 20px;">
              本次得分: <strong style="color: var(--success); font-size: 22px;">${{qState.score}}</strong> / ${{qState.questions.length}} 题
              (正确率 ${{Math.round((qState.score / qState.questions.length) * 100)}}%)
            </p>
            <button class="icon-btn" onclick="startQuiz()" style="background: var(--primary); color: #fff; padding: 10px 24px; font-size: 15px; border-color: var(--primary);">
              再来一轮
            </button>
          </div>
        `;
        return;
      }}

      const word = qState.questions[qState.currentIndex];
      qState.answering = true;

      document.getElementById('quizIndexText').textContent = `${{qState.currentIndex + 1}} / ${{qState.questions.length}}`;
      document.getElementById('quizScoreText').textContent = qState.score;
      document.getElementById('quizStreakText').textContent = `${{qState.streak}} 🔥`;

      card.innerHTML = `
        <div class="quiz-word" id="quizQuestionWord">${{word.w}}</div>
        <div class="quiz-phone-row">
          <span class="card-phonetic">/${{word.p}}/</span>
          <button class="audio-play-btn" onclick="playAudio('${{word.w}}')" style="margin-left: 8px;" title="发音">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
          </button>
        </div>
        <div class="quiz-options-grid" id="quizOptionsGrid"></div>
      `;

      if (appState.autoAudio) {{
        playAudio(word.w);
      }}

      const distractors = [];
      while (distractors.length < 3) {{
        const rand = RAW_WORDS[Math.floor(Math.random() * RAW_WORDS.length)];
        if (rand.id !== word.id && !distractors.some(d => d.id === rand.id)) {{
          distractors.push(rand);
        }}
      }}

      const options = [word, ...distractors].sort(() => 0.5 - Math.random());
      const keys = ['A', 'B', 'C', 'D'];
      const grid = document.getElementById('quizOptionsGrid');

      options.forEach((opt, i) => {{
        const btn = document.createElement('button');
        btn.className = 'quiz-option-btn';
        btn.dataset.correct = (opt.id === word.id) ? 'true' : 'false';
        btn.dataset.index = i;
        btn.innerHTML = `
          <span class="option-key">${{keys[i]}}</span>
          <span>${{opt.t}}</span>
        `;
        btn.onclick = () => handleQuizOptionClick(btn, opt.id === word.id, word);
        grid.appendChild(btn);
      }});
    }}

    function handleQuizOptionClick(chosenBtn, isCorrect, word) {{
      if (!appState.quiz.answering) return;
      appState.quiz.answering = false;

      const buttons = document.querySelectorAll('.quiz-option-btn');
      buttons.forEach(btn => btn.disabled = true);

      if (isCorrect) {{
        chosenBtn.classList.add('correct');
        appState.quiz.score++;
        appState.quiz.streak++;
        setWordStatus(word.id, 2);
      }} else {{
        chosenBtn.classList.add('wrong');
        appState.quiz.streak = 0;
        setWordStatus(word.id, 1);

        buttons.forEach(btn => {{
          if (btn.dataset.correct === 'true') {{
            btn.classList.add('correct');
          }}
        }});
      }}

      setTimeout(() => {{
        appState.quiz.currentIndex++;
        renderQuizQuestion();
      }}, 750);
    }}

    // ====== NOTEBOOK ENGINE ======
    function renderNotebook() {{
      const container = document.getElementById('notebookListContainer');
      const words = RAW_WORDS.filter(w => isWordStarred(w.id) || getWordStatus(w.id) === 1);

      if (words.length === 0) {{
        container.innerHTML = `
          <div style="padding: 48px; text-align: center; color: var(--text-muted);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin-bottom: 8px;"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
            <p>生词本还是空的！在卡片或列表中点击 ★ 或标记「忘啦」将词汇加入生词本。</p>
          </div>
        `;
        return;
      }}

      let html = '';
      words.forEach((w, idx) => {{
        const s = getWordStatus(w.id);
        const starred = isWordStarred(w.id);
        const statusText = s === 2 ? '已掌握' : (s === 1 ? '需复习' : '未学');

        html += `
          <div class="word-row" data-id="${{w.id}}">
            <div class="col-idx">${{idx + 1}}</div>
            <div class="col-word">
              <span class="col-word-text">${{w.w}}</span>
              <button class="audio-play-btn" onclick="playAudio('${{w.w}}')" title="播放读音" style="width: 22px; height: 22px;">
                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
              </button>
            </div>
            <div class="col-phone">/${{w.p}}/</div>
            <div class="col-trans">
              <div>${{formatTrans(w.t)}}</div>
              ${{w.d ? `<div class="col-detail-sub">${{w.d}}</div>` : ''}}
            </div>
            <div class="col-status">
              <span class="badge-status s${{s}}" onclick="cycleWordStatus(${{w.id}}); renderNotebook();" title="点击切换状态">${{statusText}}</span>
            </div>
            <div class="col-star" style="text-align: right;">
              <button class="star-btn ${{starred ? 'starred' : ''}}" onclick="toggleWordStarInList(${{w.id}}, this); renderNotebook();" title="生词本">★</button>
            </div>
          </div>
        `;
      }});

      container.innerHTML = html;
    }}

    function exportNotebookMarkdown() {{
      const words = RAW_WORDS.filter(w => isWordStarred(w.id) || getWordStatus(w.id) === 1);
      if (words.length === 0) {{
        alert('暂无生词记录可导出');
        return;
      }}
      let text = `# CET-6 核心生词与重难点复习清单 (${{words.length}} 词)\\n\\n`;
      words.forEach((w, i) => {{
        text += `${{i + 1}}. **${{w.w}}** [/${{w.p}}/] : ${{w.t}}\\n`;
      }});

      const blob = new Blob([text], {{ type: 'text/markdown;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `CET6_生词本_${{new Date().toISOString().slice(0, 10)}}.md`;
      a.click();
      URL.revokeObjectURL(url);
    }}

    // ====== HIGH FREQUENCY EXAM WORDS ENGINE ======
    function escapeHtml(str) {{
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }}

    function highlightKeywordInSentence(sentence, kw) {{
      const safeSent = escapeHtml(sentence);
      if (!kw) return safeSent;
      const safeKw = escapeHtml(kw).replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&');
      const re = new RegExp('\\\\b(' + safeKw + ')\\\\b', 'gi');
      return safeSent.replace(re, '<mark class="hf-kw" onclick="this.classList.toggle(\\'unmasked\\')">$1</mark>');
    }}

    function switchToTab(tabId) {{
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
      const btn = document.querySelector(`.tab-btn[data-tab="${{tabId}}"]`);
      if (btn) btn.classList.add('active');
      const pane = document.getElementById(tabId);
      if (pane) pane.classList.add('active');
    }}

    function getHfCategoryWords(cat) {{
      let list = [];
      if (cat === 'top600') {{
        list = RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.r <= 600; }});
      }} else if (cat === 'tier1') {{
        list = RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.tier === 1; }});
      }} else if (cat === 'tier2') {{
        list = RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.tier === 2; }});
      }} else if (cat === 'tier3') {{
        list = RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.tier === 3; }});
      }} else if (cat === 'wordbank') {{
        list = RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.wb > 0; }});
      }} else if (cat === 'options') {{
        list = RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.qf >= 3; }});
      }} else if (cat === 'listening') {{
        list = RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.lf >= 3; }});
      }}

      const sortBy = appState.hf.sort || 'rank';
      list.sort((a, b) => {{
        const ha = getHfInfo(a.id);
        const hb = getHfInfo(b.id);
        if (sortBy === 'wb') {{
          return (hb.wb - ha.wb) || (ha.r - hb.r);
        }}
        if (sortBy === 'qf') {{
          return (hb.qf - ha.qf) || (ha.r - hb.r);
        }}
        if (sortBy === 'alpha') {{
          return a.w.localeCompare(b.w);
        }}
        if (cat === 'wordbank') {{
          return (hb.wb - ha.wb) || (ha.r - hb.r);
        }}
        if (cat === 'options') {{
          return (hb.qf - ha.qf) || (ha.r - hb.r);
        }}
        if (cat === 'listening') {{
          return (hb.lf - ha.lf) || (ha.r - hb.r);
        }}
        return ha.r - hb.r;
      }});
      return list;
    }}

    function updateHfSliceDropdown() {{
      const sel = document.getElementById('hfSliceSelect');
      if (!sel) return;
      const baseWords = getHfCategoryWords(appState.hf.cat);
      const total = baseWords.length;
      const numGroups = Math.ceil(total / 50);

      const prevVal = appState.hf.slice || 'all';
      sel.innerHTML = '';

      const optAll = document.createElement('option');
      optAll.value = 'all';
      optAll.textContent = `全部当前分类 (${{total}} 词)`;
      sel.appendChild(optAll);

      for (let i = 1; i <= numGroups; i++) {{
        const s = (i - 1) * 50 + 1;
        const e = Math.min(i * 50, total);
        const opt = document.createElement('option');
        opt.value = String(i);
        opt.textContent = `Group ${{String(i).padStart(2, '0')}} (${{s}} ~ ${{e}})`;
        sel.appendChild(opt);
      }}

      if (prevVal !== 'all' && parseInt(prevVal, 10) <= numGroups) {{
        sel.value = prevVal;
      }} else {{
        appState.hf.slice = 'all';
        sel.value = 'all';
      }}
    }}

    function getHfFilteredWords(ignoreSlice = false) {{
      const hfState = appState.hf;
      let words = getHfCategoryWords(hfState.cat);

      if (!ignoreSlice && hfState.slice !== 'all') {{
        const gIdx = parseInt(hfState.slice, 10);
        if (!isNaN(gIdx) && gIdx >= 1) {{
          const start = (gIdx - 1) * 50;
          words = words.slice(start, start + 50);
        }}
      }}

      if (hfState.pos !== 'all') {{
        words = words.filter(w => {{
          const h = getHfInfo(w.id);
          return h && h.pos === hfState.pos;
        }});
      }}

      if (hfState.status === 'unmastered') {{
        words = words.filter(w => getWordStatus(w.id) !== 2);
      }} else if (hfState.status === '0' || hfState.status === '1' || hfState.status === '2') {{
        const targetS = parseInt(hfState.status, 10);
        words = words.filter(w => getWordStatus(w.id) === targetS);
      }} else if (hfState.status === 'starred') {{
        words = words.filter(w => isWordStarred(w.id));
      }}

      const term = (hfState.searchTerm || '').trim().toLowerCase();
      if (term) {{
        words = words.filter(w =>
          w.w.toLowerCase().includes(term) ||
          (w.t && w.t.toLowerCase().includes(term)) ||
          (w.d && w.d.toLowerCase().includes(term))
        );
      }}

      return words;
    }}

    function updateHfDashboard() {{
      const top600 = RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.r <= 600; }});
      const t1 = top600.filter(w => getHfInfo(w.id).tier === 1);
      const t2 = top600.filter(w => getHfInfo(w.id).tier === 2);
      const t3 = top600.filter(w => getHfInfo(w.id).tier === 3);
      const wb = RAW_WORDS.filter(w => {{ const h = getHfInfo(w.id); return h && h.wb > 0; }});

      const countMastered = (arr) => arr.reduce((acc, w) => acc + (getWordStatus(w.id) === 2 ? 1 : 0), 0);
      const countReview = (arr) => arr.reduce((acc, w) => acc + (getWordStatus(w.id) === 1 ? 1 : 0), 0);

      const m600 = countMastered(top600);
      const r600 = countReview(top600);
      const total600 = top600.length || 600;
      const pct600 = Math.round((m600 / total600) * 100);
      const pctR600 = Math.round((r600 / total600) * 100);

      const badge = document.getElementById('badgeHighFreq');
      if (badge) badge.textContent = total600;

      const progTxt = document.getElementById('hfTop600ProgText');
      if (progTxt) progTxt.textContent = `${{m600}} / ${{total600}} (${{pct600}}%)`;
      const barM = document.getElementById('hfTop600BarMastered');
      if (barM) barM.style.width = pct600 + '%';
      const barR = document.getElementById('hfTop600BarReview');
      if (barR) barR.style.width = pctR600 + '%';

      const tiers = [
        [t1, 'hfTier1Meta', 'hfTier1Fill'],
        [t2, 'hfTier2Meta', 'hfTier2Fill'],
        [t3, 'hfTier3Meta', 'hfTier3Fill'],
        [wb, 'hfTierWbMeta', 'hfTierWbFill']
      ];
      tiers.forEach(([arr, metaId, fillId]) => {{
        const m = countMastered(arr);
        const tot = arr.length || 1;
        const pct = Math.round((m / tot) * 100);
        const metaEl = document.getElementById(metaId);
        const fillEl = document.getElementById(fillId);
        if (metaEl) metaEl.textContent = `已掌握 ${{m}} / ${{arr.length}} (${{pct}}%)`;
        if (fillEl) fillEl.style.width = pct + '%';
      }});

      document.querySelectorAll('.hf-tier-card').forEach(card => {{
        card.classList.toggle('active', card.dataset.hfTierJump === appState.hf.cat);
      }});
    }}

    function renderHighFreqPane() {{
      updateHfDashboard();
      const container = document.getElementById('hfListContainer');
      if (!container) return;

      const words = getHfFilteredWords(false);
      document.getElementById('hfSummaryText').textContent = `共筛选出 ${{words.length}} 个真题高频词`;

      const pageSize = appState.hf.pageSize || 50;
      const totalPages = Math.ceil(words.length / pageSize) || 1;
      if (appState.hf.page > totalPages) appState.hf.page = totalPages;
      if (appState.hf.page < 1) appState.hf.page = 1;

      document.getElementById('hfPageInfoText').textContent = `第 ${{appState.hf.page}} / ${{totalPages}} 页 (${{words.length}} 词)`;

      const start = (appState.hf.page - 1) * pageSize;
      const pageWords = words.slice(start, start + pageSize);

      if (pageWords.length === 0) {{
        container.innerHTML = `
          <div style="padding: 48px; text-align: center; color: var(--text-muted);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin-bottom: 8px;"><circle cx="12" cy="12" r="10"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
            <p>当前筛选条件下暂无符合的高频词，试试切换分类或放宽筛选条件。</p>
          </div>
        `;
        return;
      }}

      const maskClass = appState.hf.maskMode === 'cn' ? 'mask-cn' : (appState.hf.maskMode === 'en' ? 'mask-en' : '');
      const showEx = appState.hf.showExamples;
      let html = '';

      pageWords.forEach(w => {{
        const hf = getHfInfo(w.id);
        const s = getWordStatus(w.id);
        const starred = isWordStarred(w.id);
        const statusText = s === 2 ? '已掌握' : (s === 1 ? '需复习' : '未学');

        const tierClass = hf.tier === 1 ? 'tier-1' : (hf.tier === 2 ? 'tier-2' : (hf.tier === 3 ? 'tier-3' : 'tier-0'));
        const rankLabel = hf.tier > 0 ? `#${{hf.r}}` : '词库';
        const starsStr = hf.tier === 1 ? '★★★★★' : (hf.tier === 2 ? '★★★★' : (hf.tier === 3 ? '★★★' : '🎯 考点'));

        const wbPill = hf.wb > 0 ? `<span class="hf-pill wb">🎯 选词库×${{hf.wb}}</span>` : '';
        const qfPill = hf.qf > 0 ? `<span class="hf-pill opt">🏆 选项×${{hf.qf}}</span>` : '';
        const exHtml = (showEx && hf.ex && hf.ex.en)
          ? `<div class="hf-example-box"><span class="hf-example-src">[${{escapeHtml(hf.ex.s)}}]</span>${{highlightKeywordInSentence(hf.ex.en, hf.ex.kw)}}</div>`
          : '';

        html += `
          <div class="hf-row ${{maskClass}}" data-id="${{w.id}}">
            <div class="hf-rank-col">
              <span class="hf-rank-badge ${{tierClass}}">${{rankLabel}}</span>
              <span class="hf-stars">${{starsStr}}</span>
            </div>

            <div class="hf-word-col">
              <div class="hf-word-head">
                <span class="col-word-text" onclick="this.classList.toggle('unmasked')">${{escapeHtml(w.w)}}</span>
                <button class="audio-play-btn" onclick="playAudio('${{w.w}}')" title="播放读音" style="width: 24px; height: 24px;">
                  <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                </button>
              </div>
              <div class="col-phone">/${{escapeHtml(w.p)}}/</div>
              <div class="hf-meta-pills">
                <span class="hf-pill hot">🔥 ${{hf.f}}次 · ${{hf.p}}套</span>
                <span class="hf-pill">阅${{hf.rf}} / 听${{hf.lf}}</span>
                ${{wbPill}}
                ${{qfPill}}
              </div>
            </div>

            <div class="hf-trans-col col-trans" onclick="this.classList.toggle('unmasked')">
              <div>${{formatTrans(w.t)}}</div>
              ${{w.d ? `<div class="col-detail-sub">${{escapeHtml(w.d)}}</div>` : ''}}
              ${{exHtml}}
            </div>

            <div class="hf-status-col col-status">
              <span class="badge-status s${{s}}" onclick="cycleHfWordStatus(${{w.id}})" title="点击切换状态">${{statusText}}</span>
            </div>

            <div class="hf-star-col col-star" style="text-align: right;">
              <button class="star-btn ${{starred ? 'starred' : ''}}" onclick="toggleHfWordStar(${{w.id}}, this)" title="加入生词本">★</button>
            </div>
          </div>
        `;
      }});

      container.innerHTML = html;
    }}

    function cycleHfWordStatus(id) {{
      const current = getWordStatus(id);
      const next = (current + 1) % 3;
      setWordStatus(id, next);
      renderHighFreqPane();
    }}

    function toggleHfWordStar(id, btn) {{
      const isSt = toggleWordStar(id);
      if (isSt) btn.classList.add('starred');
      else btn.classList.remove('starred');
    }}

    function jumpToHfCategory(cat) {{
      appState.hf.cat = cat;
      appState.hf.slice = 'all';
      appState.hf.page = 1;
      document.querySelectorAll('#hfCategoryGroup .pill-filter').forEach(b => {{
        b.classList.toggle('active', b.dataset.hfCat === cat);
      }});
      updateHfSliceDropdown();
      renderHighFreqPane();
    }}

    function exportHighFreqMarkdown() {{
      const words = getHfFilteredWords(false);
      if (words.length === 0) {{
        alert('当前筛选条件下暂无高频词可导出');
        return;
      }}
      let text = `# CET-6 真题高频核心词表 (${{words.length}} 词)\\n\\n`;
      words.forEach((w, i) => {{
        const hf = getHfInfo(w.id);
        const rankStr = hf && hf.tier > 0 ? `#${{hf.r}}` : '词库';
        const freqStr = hf ? `真题${{hf.f}}次/${{hf.p}}套` : '';
        text += `${{i + 1}}. [${{rankStr}}] **${{w.w}}** [/${{w.p}}/] (${{freqStr}}) — ${{w.t}}\\n`;
        if (hf && hf.ex && hf.ex.en) {{
          text += `   > [${{hf.ex.s}}] ${{hf.ex.en}}\\n`;
        }}
      }});

      const blob = new Blob([text], {{ type: 'text/markdown;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `CET6_真题高频词_${{appState.hf.cat}}_${{new Date().toISOString().slice(0, 10)}}.md`;
      a.click();
      URL.revokeObjectURL(url);
    }}

    // ====== EBBINGHAUS TABLE GENERATOR ======
    function renderEbbinghausTable() {{
      const tbody = document.getElementById('ebbinghausTableBody');
      tbody.innerHTML = '';
      const totalLists = 45;

      for (let day = 1; day <= totalLists; day++) {{
        const reviews = [];
        if (day >= 2) reviews.push(`List ${{day - 1}} (昨天)`);
        if (day >= 3) reviews.push(`List ${{day - 2}} (前天)`);
        if (day >= 5) reviews.push(`List ${{day - 4}} (4天前)`);
        if (day >= 8) reviews.push(`List ${{day - 7}} (1周前)`);
        if (day >= 16) reviews.push(`List ${{day - 15}} (半月前)`);

        const isChecked = !!appState.ebbinghausChecks[day];

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="text-align: center;">
            <input type="checkbox" class="day-check" ${{isChecked ? 'checked' : ''}} onchange="toggleDayCheck(${{day}}, this.checked)">
          </td>
          <td><strong>第 ${{day}} 天</strong></td>
          <td><span class="pos-tag" style="background: var(--primary-subtle); color: var(--primary);">List ${{day}} (50词)</span></td>
          <td style="color: var(--text-sub);">${{reviews.length > 0 ? reviews.join(' · ') : '无 (初次启动，专注新词)'}}</td>
        `;
        tbody.appendChild(tr);
      }}
    }}

    function toggleDayCheck(day, checked) {{
      appState.ebbinghausChecks[day] = checked;
      saveState();
    }}

    // ====== BACKUP & RESTORE ======
    function exportBackup() {{
      const dataStr = JSON.stringify({{
        version: 2,
        exportTime: new Date().toISOString(),
        progress: appState.progress,
        ebbinghausChecks: appState.ebbinghausChecks,
        stats: appState.stats
      }}, null, 2);

      const blob = new Blob([dataStr], {{ type: 'application/json;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `CET6_学习进度备份_${{new Date().toISOString().slice(0, 10)}}.json`;
      a.click();
      URL.revokeObjectURL(url);
    }}

    function importBackup(e) {{
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(evt) {{
        try {{
          const data = JSON.parse(evt.target.result);
          if (data && data.progress) {{
            appState.progress = data.progress;
            if (data.stats) appState.stats = data.stats;
            if (data.ebbinghausChecks) appState.ebbinghausChecks = data.ebbinghausChecks;
            saveState();
            setupCardQueue();
            renderWordList();
            renderHighFreqPane();
            renderEbbinghausTable();
            alert('🎉 学习进度恢复成功！');
          }} else {{
            alert('文件格式不正确，未能解析学习记录！');
          }}
        }} catch (err) {{
          alert('解析备份文件失败: ' + err.message);
        }}
      }};
      reader.readAsText(file);
    }}

    // ====== EVENT LISTENERS & INIT ======
    document.addEventListener('DOMContentLoaded', () => {{
      loadState();

      if (appState.theme === 'dark') {{
        document.documentElement.setAttribute('data-theme', 'dark');
        document.getElementById('themeIcon').textContent = '☀️';
      }}

      document.getElementById('themeToggleBtn').onclick = () => {{
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        if (isDark) {{
          document.documentElement.removeAttribute('data-theme');
          appState.theme = 'light';
          document.getElementById('themeIcon').textContent = '🌙';
        }} else {{
          document.documentElement.setAttribute('data-theme', 'dark');
          appState.theme = 'dark';
          document.getElementById('themeIcon').textContent = '☀️';
        }}
        saveState();
      }};

      const accentSelect = document.getElementById('accentSelect');
      accentSelect.value = appState.soundType || '2';
      accentSelect.onchange = () => {{
        appState.soundType = accentSelect.value;
        saveState();
      }};

      initDropdowns();
      updateHfSliceDropdown();
      setupCardQueue();
      updateGlobalStatsUI();
      renderEbbinghausTable();

      // Tab switching
      document.querySelectorAll('.tab-btn').forEach(btn => {{
        btn.onclick = () => {{
          document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
          document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
          btn.classList.add('active');
          const target = btn.dataset.tab;
          document.getElementById(target).classList.add('active');

          if (target === 'pane-highfreq') renderHighFreqPane();
          if (target === 'pane-list') renderWordList();
          if (target === 'pane-spell') startSpellPractice();
          if (target === 'pane-quiz') startQuiz();
          if (target === 'pane-notebook') renderNotebook();
        }};
      }});

      // Card Events
      document.getElementById('flashcardBox').onclick = flipCard;
      document.getElementById('flipCardBtn').onclick = flipCard;
      document.getElementById('cardAudioBtn').onclick = (e) => {{
        e.stopPropagation();
        const queue = appState.cardQueue;
        if (queue && queue[appState.cardIndex]) playAudio(queue[appState.cardIndex].w);
      }};

      document.getElementById('cardStarBtn').onclick = (e) => {{
        e.stopPropagation();
        const queue = appState.cardQueue;
        if (queue && queue[appState.cardIndex]) {{
          const isSt = toggleWordStar(queue[appState.cardIndex].id);
          e.target.classList.toggle('starred', isSt);
        }}
      }};

      document.getElementById('cardListSelect').onchange = setupCardQueue;
      document.getElementById('autoPronounceCheck').onchange = (e) => {{
        appState.autoAudio = e.target.checked;
      }};
      document.getElementById('shuffleCheck').onchange = (e) => {{
        appState.shuffleCards = e.target.checked;
        setupCardQueue();
      }};

      document.getElementById('prevCardBtn').onclick = () => {{
        if (appState.cardIndex > 0) {{
          appState.cardIndex--;
          renderCurrentCard();
        }}
      }};
      document.getElementById('nextCardBtn').onclick = () => {{
        if (appState.cardIndex < appState.cardQueue.length - 1) {{
          appState.cardIndex++;
          renderCurrentCard();
        }}
      }};

      document.querySelectorAll('.rate-btn').forEach(btn => {{
        btn.onclick = () => {{
          const r = parseInt(btn.dataset.rating, 10);
          rateCurrentCard(r);
        }};
      }});

      // List Filter Events
      document.getElementById('listGroupSelect').onchange = () => {{
        appState.listPage = 1;
        renderWordList();
      }};

      document.querySelectorAll('#pane-list .pill-filter').forEach(btn => {{
        btn.onclick = () => {{
          document.querySelectorAll('#pane-list .pill-filter').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          appState.listStatusFilter = btn.dataset.statusFilter;
          appState.listPage = 1;
          renderWordList();
        }};
      }});

      document.querySelectorAll('#pane-list .mask-btn').forEach(btn => {{
        btn.onclick = () => {{
          document.querySelectorAll('#pane-list .mask-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          appState.listMaskMode = btn.dataset.mask;
          renderWordList();
        }};
      }});

      // High-Frequency Events
      document.querySelectorAll('.hf-tier-card').forEach(card => {{
        card.onclick = () => {{
          const targetCat = card.dataset.hfTierJump;
          if (targetCat) jumpToHfCategory(targetCat);
        }};
      }});

      document.querySelectorAll('#hfCategoryGroup .pill-filter').forEach(btn => {{
        btn.onclick = () => {{
          jumpToHfCategory(btn.dataset.hfCat);
        }};
      }});

      document.getElementById('hfSliceSelect').onchange = (e) => {{
        appState.hf.slice = e.target.value;
        appState.hf.page = 1;
        renderHighFreqPane();
      }};

      document.getElementById('hfPosSelect').onchange = (e) => {{
        appState.hf.pos = e.target.value;
        appState.hf.page = 1;
        renderHighFreqPane();
      }};

      document.getElementById('hfStatusSelect').onchange = (e) => {{
        appState.hf.status = e.target.value;
        appState.hf.page = 1;
        renderHighFreqPane();
      }};

      document.getElementById('hfSortSelect').onchange = (e) => {{
        appState.hf.sort = e.target.value;
        appState.hf.page = 1;
        updateHfSliceDropdown();
        renderHighFreqPane();
      }};

      document.querySelectorAll('#hfMaskOptions .mask-btn').forEach(btn => {{
        btn.onclick = () => {{
          document.querySelectorAll('#hfMaskOptions .mask-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          appState.hf.maskMode = btn.dataset.hfMask;
          renderHighFreqPane();
        }};
      }});

      document.getElementById('hfShowExampleCheck').onchange = (e) => {{
        appState.hf.showExamples = e.target.checked;
        renderHighFreqPane();
      }};

      document.getElementById('hfSearchInput').oninput = (e) => {{
        appState.hf.searchTerm = e.target.value;
        appState.hf.page = 1;
        renderHighFreqPane();
      }};

      document.getElementById('hfPrevPageBtn').onclick = () => {{
        if (appState.hf.page > 1) {{
          appState.hf.page--;
          renderHighFreqPane();
          window.scrollTo({{ top: 320, behavior: 'smooth' }});
        }}
      }};

      document.getElementById('hfNextPageBtn').onclick = () => {{
        const totalWords = getHfFilteredWords(false).length;
        const totalPages = Math.ceil(totalWords / (appState.hf.pageSize || 50)) || 1;
        if (appState.hf.page < totalPages) {{
          appState.hf.page++;
          renderHighFreqPane();
          window.scrollTo({{ top: 320, behavior: 'smooth' }});
        }}
      }};

      document.getElementById('hfBatchMasterPageBtn').onclick = () => {{
        const words = getHfFilteredWords(false);
        const pageSize = appState.hf.pageSize || 50;
        const start = (appState.hf.page - 1) * pageSize;
        const pageWords = words.slice(start, start + pageSize);
        if (pageWords.length === 0) return;
        if (confirm(`确定将当前页展示的 ${{pageWords.length}} 个高频词全部标记为「已掌握」吗？`)) {{
          pageWords.forEach(w => setWordStatus(w.id, 2));
          renderHighFreqPane();
        }}
      }};

      document.getElementById('hfStartCardBtn').onclick = () => {{
        const words = getHfFilteredWords(false);
        if (words.length === 0) {{
          alert('当前筛选条件下没有高频词可供卡片背诵！');
          return;
        }}
        let queue = [...words];
        if (appState.shuffleCards) {{
          for (let i = queue.length - 1; i > 0; i--) {{
            const j = Math.floor(Math.random() * (i + 1));
            [queue[i], queue[j]] = [queue[j], queue[i]];
          }}
        }}
        const catToSelect = {{ top600: 'hf_600', tier1: 'hf_150', wordbank: 'hf_wb', options: 'hf_opt' }};
        if (catToSelect[appState.hf.cat]) {{
          document.getElementById('cardListSelect').value = catToSelect[appState.hf.cat];
        }}
        appState.cardQueue = queue;
        appState.cardIndex = 0;
        appState.cardFlipped = false;
        switchToTab('pane-card');
        renderCurrentCard();
      }};

      document.getElementById('hfStartSpellBtn').onclick = () => {{
        const words = getHfFilteredWords(false);
        if (words.length === 0) {{
          alert('当前筛选条件下没有高频词可供拼写默写！');
          return;
        }}
        switchToTab('pane-spell');
        startSpellPractice(words);
      }};

      document.getElementById('hfStartQuizBtn').onclick = () => {{
        const words = getHfFilteredWords(false);
        if (words.length < 4) {{
          alert('当前筛选出的高频词不足 4 个，请放宽筛选条件后再开始四选一挑战！');
          return;
        }}
        switchToTab('pane-quiz');
        startQuiz(words);
      }};

      document.getElementById('hfExportMdBtn').onclick = exportHighFreqMarkdown;

      document.getElementById('listSearchInput').oninput = (e) => {{
        appState.listSearchTerm = e.target.value;
        appState.listPage = 1;
        renderWordList();
      }};

      document.getElementById('prevPageBtn').onclick = () => {{
        if (appState.listPage > 1) {{
          appState.listPage--;
          renderWordList();
          window.scrollTo({{ top: 300, behavior: 'smooth' }});
        }}
      }};
      document.getElementById('nextPageBtn').onclick = () => {{
        appState.listPage++;
        renderWordList();
        window.scrollTo({{ top: 300, behavior: 'smooth' }});
      }};

      // Batch Actions
      document.getElementById('batchStartCardBtn').onclick = () => {{
        const selGroup = document.getElementById('listGroupSelect').value;
        document.getElementById('cardListSelect').value = selGroup;
        document.querySelector('.tab-btn[data-tab="pane-card"]').click();
        setupCardQueue();
      }};

      document.getElementById('batchStartSpellBtn').onclick = () => {{
        const selGroup = document.getElementById('listGroupSelect').value;
        document.getElementById('spellScopeSelect').value = selGroup;
        document.getElementById('navBtnSpell').click();
      }};

      document.getElementById('batchMarkMasteredBtn').onclick = () => {{
        const selGroup = document.getElementById('listGroupSelect').value;
        const words = getWordsForSelection(selGroup);
        if (confirm(`确定要将当前组的 ${{words.length}} 个单词全部标记为「已掌握」吗？`)) {{
          words.forEach(w => setWordStatus(w.id, 2));
          renderWordList();
        }}
      }};

      document.getElementById('batchResetBtn').onclick = () => {{
        const selGroup = document.getElementById('listGroupSelect').value;
        const words = getWordsForSelection(selGroup);
        if (confirm(`确定要将当前组的 ${{words.length}} 个单词重置为「未学」状态吗？`)) {{
          words.forEach(w => setWordStatus(w.id, 0));
          renderWordList();
        }}
      }};

      // Spelling Arena Events & Listeners
      const spellInput = document.getElementById('spellInputMain');
      
      document.getElementById('spellScopeSelect').onchange = () => startSpellPractice();
      document.getElementById('spellRestartBtn').onclick = () => startSpellPractice();
      document.getElementById('spellSubmitBtn').onclick = handleSpellSubmitAction;
      document.getElementById('spellHintFirstBtn').onclick = () => giveSpellHint('first');
      document.getElementById('spellHintNextBtn').onclick = () => giveSpellHint('next');
      document.getElementById('spellGiveUpBtn').onclick = giveUpCurrentSpell;

      document.getElementById('spellAudioBtn').onclick = () => {{
        const sState = appState.spell;
        if (sState.questions[sState.currentIndex]) {{
          playAudio(sState.questions[sState.currentIndex].w);
        }}
      }};

      // Realtime input sync to letter slots
      spellInput.addEventListener('input', handleSpellInputLive);

      // Prevent IME composition bug on Enter
      spellInput.addEventListener('keydown', (e) => {{
        if (e.isComposing || e.keyCode === 229) {{
          return; // User is choosing Chinese characters or typing composition
        }}
        if (e.key === 'Enter') {{
          e.preventDefault();
          handleSpellSubmitAction();
        }}
      }});

      // Quiz Scope
      document.getElementById('quizScopeSelect').onchange = startQuiz;
      document.getElementById('quizRestartBtn').onclick = startQuiz;

      // Notebook Actions
      document.getElementById('nbStartCardBtn').onclick = () => {{
        document.getElementById('cardListSelect').value = 'starred';
        document.querySelector('.tab-btn[data-tab="pane-card"]').click();
        setupCardQueue();
      }};
      document.getElementById('nbStartSpellBtn').onclick = () => {{
        document.getElementById('spellScopeSelect').value = 'starred';
        document.getElementById('navBtnSpell').click();
      }};
      document.getElementById('nbStartQuizBtn').onclick = () => {{
        document.getElementById('quizScopeSelect').value = 'starred';
        document.querySelector('.tab-btn[data-tab="pane-quiz"]').click();
        startQuiz();
      }};
      document.getElementById('nbExportTextBtn').onclick = exportNotebookMarkdown;
      document.getElementById('nbClearMasteredBtn').onclick = () => {{
        const masteredStarred = RAW_WORDS.filter(w => isWordStarred(w.id) && getWordStatus(w.id) === 2);
        if (masteredStarred.length === 0) {{
          alert('暂无已掌握的生词需要清理');
          return;
        }}
        if (confirm(`是否从生词本中移出 ${{masteredStarred.length}} 个已标记为「掌握」的生词？`)) {{
          masteredStarred.forEach(w => {{
            appState.progress[w.id].starred = false;
          }});
          saveState();
          renderNotebook();
        }}
      }};

      // Backup & Restore
      document.getElementById('exportBackupBtn').onclick = exportBackup;
      document.getElementById('importBackupBtn').onclick = () => {{
        document.getElementById('backupFileInput').click();
      }};
      document.getElementById('backupFileInput').onchange = importBackup;

      // Shortcuts Modal
      const modal = document.getElementById('shortcutsModal');
      document.getElementById('shortcutsBtn').onclick = () => modal.classList.add('active');
      document.getElementById('closeModalBtn').onclick = () => modal.classList.remove('active');
      modal.onclick = (e) => {{
        if (e.target === modal) modal.classList.remove('active');
      }};

      // Global Keyboard Shortcuts
      document.addEventListener('keydown', (e) => {{
        const activePane = document.querySelector('.tab-pane.active').id;

        if (activePane === 'pane-spell') {{
          if (e.key.toLowerCase() === 'r' && (e.ctrlKey || e.altKey || document.activeElement !== spellInput)) {{
            e.preventDefault();
            document.getElementById('spellAudioBtn').click();
          }} else if (e.key === '1' && e.altKey) {{
            e.preventDefault();
            giveSpellHint('first');
          }} else if (e.key === '2' && e.altKey) {{
            e.preventDefault();
            giveSpellHint('next');
          }}
          return;
        }}

        if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;

        if (activePane === 'pane-card') {{
          if (e.code === 'Space' || e.key === 'Enter') {{
            e.preventDefault();
            flipCard();
          }} else if (e.key === '1') {{
            rateCurrentCard(1);
          }} else if (e.key === '2') {{
            rateCurrentCard(2);
          }} else if (e.key === '3') {{
            rateCurrentCard(3);
          }} else if (e.key === '4') {{
            rateCurrentCard(4);
          }} else if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'j') {{
            document.getElementById('prevCardBtn').click();
          }} else if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'k') {{
            document.getElementById('nextCardBtn').click();
          }} else if (e.key.toLowerCase() === 'r') {{
            document.getElementById('cardAudioBtn').click();
          }} else if (e.key.toLowerCase() === 's') {{
            document.getElementById('cardStarBtn').click();
          }}
        }} else if (activePane === 'pane-quiz') {{
          if (e.key.toLowerCase() === 'r') {{
            const q = appState.quiz.questions[appState.quiz.currentIndex];
            if (q) playAudio(q.w);
          }} else {{
            const keyMap = {{ '1': 0, 'a': 0, 'A': 0, '2': 1, 'b': 1, 'B': 1, '3': 2, 'c': 2, 'C': 2, '4': 3, 'd': 3, 'D': 3 }};
            if (e.key in keyMap) {{
              const idx = keyMap[e.key];
              const btn = document.querySelector(`.quiz-option-btn[data-index="${{idx}}"]`);
              if (btn && !btn.disabled) btn.click();
            }}
          }}
        }}
      }});
    }});
  </script>
</body>
</html>
'''

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated index.html successfully')

    with open('六级词汇背诵助手.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated 六级词汇背诵助手.html successfully')

if __name__ == '__main__':
    build()
