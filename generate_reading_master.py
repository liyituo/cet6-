# -*- coding: utf-8 -*-
"""
Enhanced CET-6 Reading Platform Builder (Ultra-Polished Edition)
Full features:
- Dual Split-Screen, Reader-Only, Console-Only, Stacked Layouts
- Floating View Switcher pill + Full Keyboard Shortcuts (V, 1/2/3/4, A/B/C/D, F, J/K, ?)
- Interactive Highlighting & Annotation Tool (Yellow, Green, Pink, Underline, Pronounce, Clear)
- Question Flagging (⭐ 待复查) with Answer Matrix indicators
- Section A Smart Cloze (In-place fill/clear, auto-advance, used word badge, definitions)
- Section B Paragraph Preview Tooltip & Live Hover Highlight
- Section C Paragraph Jumpers & Evidence Locators with Golden Pulse
- Auto-save answers, flags, timer, and highlights to localStorage
- Deep Study Mode with paragraph bilingual translations and point-by-point explanations
- Offline 3,996-word dictionary popover with Web Speech API audio
"""

import json
import os
import re
import sys

from build_full_master_pipeline import get_all_exams_master

def build_app_html():
    final_exams = get_all_exams_master()
    print(f"Loaded master exams: {len(final_exams)}")

    # Load dictionary
    dict_map = {}
    if os.path.exists('comprehensive_cet6_dict.json'):
        with open('comprehensive_cet6_dict.json', 'r', encoding='utf-8') as f:
            dict_map = json.load(f)
        print(f"Loaded comprehensive dictionary: {len(dict_map)} entries")
    else:
        if os.path.exists('words_data.json'):
            wdata = json.load(open('words_data.json', 'r', encoding='utf-8'))
            for item in wdata:
                w = item.get('w', '').strip().lower()
                if w and w not in dict_map:
                    dict_map[w] = {
                        'p': item.get('p', ''),
                        't': item.get('t', '')
                    }

        if os.path.exists('temp_astrbot'):
            for fname in os.listdir('temp_astrbot'):
                if fname.startswith('4-CET6') and fname.endswith('.json'):
                    ext_data = json.load(open(os.path.join('temp_astrbot', fname), 'r', encoding='utf-8'))
                    for item in ext_data:
                        w = item.get('word', '').strip().lower()
                        if w and w not in dict_map:
                            trs = item.get('translations', [])
                            tr_text = '; '.join([f"{t.get('type', '')} {t.get('translation', '')}".strip() for t in trs]) if isinstance(trs, list) else str(trs)
                            dict_map[w] = {
                                'p': '',
                                't': tr_text
                            }

    exams_json = json.dumps(final_exams, ensure_ascii=False)
    dict_json = json.dumps(dict_map, ensure_ascii=False).replace('</script>', '<\\/script>')

    print("Generating ultra-polished HTML template...")

    html_template = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CET-6 英语六级历年阅读真题全真研习平台 (2021 - 2024 重点特训)</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%234f46e5'><path d='M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5'/></svg>">
  <style>
    /* ==========================================================================
       CSS Variables & Themes
       ========================================================================== */
    :root {
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-subtle: #eef2ff;
      --primary-border: #c7d2fe;
      --bg-body: #f8fafc;
      --bg-panel: #ffffff;
      --bg-subtle: #f1f5f9;
      --bg-hover: #e2e8f0;
      --text-main: #0f172a;
      --text-sub: #475569;
      --text-muted: #94a3b8;
      --border: #e2e8f0;
      --border-focus: #94a3b8;
      --success: #10b981;
      --success-subtle: #ecfdf5;
      --danger: #ef4444;
      --danger-subtle: #fef2f2;
      --warning: #f59e0b;
      --warning-subtle: #fffbeb;
      --info: #0ea5e9;
      --info-subtle: #f0f9ff;
      --reader-font: "Charter", "Merriweather", "Georgia", "Cambria", serif;
      --body-font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
      --radius-sm: 4px;
      --radius-md: 8px;
      --radius-lg: 12px;
      --radius-full: 9999px;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
      --transition: all 0.2s ease;
      --hl-yellow: #fef08a;
      --hl-green: #bbf7d0;
      --hl-pink: #fbcfe8;
      --hl-blue: #bae6fd;
    }

    [data-theme="sepia"] {
      --primary: #854d0e;
      --primary-hover: #713f12;
      --primary-subtle: #fef9c3;
      --primary-border: #fde047;
      --bg-body: #f4ecd8;
      --bg-panel: #faf6ea;
      --bg-subtle: #ede2c7;
      --bg-hover: #e5d7b5;
      --text-main: #3d3024;
      --text-sub: #5c4b3a;
      --text-muted: #8c7862;
      --border: #dccfb0;
      --border-focus: #b8a682;
      --success: #15803d;
      --success-subtle: #dcfce7;
      --danger: #b91c1c;
      --danger-subtle: #fee2e2;
      --shadow-sm: 0 1px 2px 0 rgba(61, 48, 36, 0.08);
      --shadow-md: 0 4px 6px -1px rgba(61, 48, 36, 0.12);
      --shadow-lg: 0 10px 15px -3px rgba(61, 48, 36, 0.15);
    }

    [data-theme="dark"] {
      --primary: #818cf8;
      --primary-hover: #6366f1;
      --primary-subtle: #1e1e38;
      --primary-border: #3730a3;
      --bg-body: #0b0f19;
      --bg-panel: #131b2e;
      --bg-subtle: #1e293b;
      --bg-hover: #334155;
      --text-main: #f1f5f9;
      --text-sub: #cbd5e1;
      --text-muted: #64748b;
      --border: #243048;
      --border-focus: #475569;
      --success: #34d399;
      --success-subtle: #064e3b;
      --danger: #f87171;
      --danger-subtle: #7f1d1d;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.4);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.6);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: var(--body-font);
      background-color: var(--bg-body);
      color: var(--text-main);
      line-height: 1.6;
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    /* Header Bar */
    header.top-header {
      flex-shrink: 0;
      z-index: 50;
      background: var(--bg-panel);
      border-bottom: 1px solid var(--border);
      padding: 8px 20px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      box-shadow: var(--shadow-sm);
    }

    .header-row-1 {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .logo-badge {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 36px;
      height: 36px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, var(--primary) 0%, #a855f7 100%);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      box-shadow: 0 3px 8px rgba(99, 102, 241, 0.3);
    }

    .brand-title h1 {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .brand-title .badge-tag {
      font-size: 0.72rem;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      background: var(--primary-subtle);
      color: var(--primary);
      border: 1px solid var(--primary-border);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: var(--radius-md);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--border);
      background: var(--bg-panel);
      color: var(--text-main);
      transition: var(--transition);
      user-select: none;
      white-space: nowrap;
    }

    .btn:hover {
      background: var(--bg-hover);
      border-color: var(--border-focus);
      transform: translateY(-1px);
    }

    .btn-primary {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 2px 6px rgba(79, 70, 229, 0.25);
    }

    .btn-primary:hover {
      background: var(--primary-hover);
      border-color: var(--primary-hover);
      color: #ffffff;
    }

    .btn-outline {
      background: transparent;
      border-color: var(--border);
    }

    .badge-count {
      background: var(--danger);
      color: #ffffff;
      font-size: 0.68rem;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: var(--radius-full);
      margin-left: 2px;
    }

    /* Header Row 2: Filtering & Section Tabs */
    .header-row-2 {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      padding-top: 4px;
      border-top: 1px dashed var(--border);
    }

    .year-pills {
      display: flex;
      align-items: center;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 2px;
    }

    .pill {
      padding: 4px 10px;
      border-radius: var(--radius-full);
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--border);
      background: var(--bg-panel);
      color: var(--text-sub);
      transition: var(--transition);
      white-space: nowrap;
    }

    .pill:hover {
      background: var(--bg-hover);
      color: var(--text-main);
    }

    .pill.active {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 2px 5px rgba(79, 70, 229, 0.25);
    }

    .exam-select-group {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    select.custom-select {
      padding: 5px 10px;
      border-radius: var(--radius-md);
      font-size: 0.8rem;
      font-weight: 600;
      border: 1px solid var(--border);
      background: var(--bg-panel);
      color: var(--text-main);
      cursor: pointer;
      outline: none;
      transition: var(--transition);
      max-width: 280px;
    }

    select.custom-select:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 2px var(--primary-subtle);
    }

    .section-tabs {
      display: flex;
      align-items: center;
      background: var(--bg-subtle);
      padding: 3px;
      border-radius: var(--radius-md);
      gap: 3px;
      border: 1px solid var(--border);
    }

    .section-tab {
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--text-sub);
      cursor: pointer;
      transition: var(--transition);
      user-select: none;
      white-space: nowrap;
    }

    .section-tab:hover {
      color: var(--text-main);
      background: var(--bg-hover);
    }

    .section-tab.active {
      background: var(--primary);
      color: #ffffff;
      box-shadow: var(--shadow-sm);
    }

    /* Mode Banner & Layout Controls Strip */
    .mode-bar {
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--primary-subtle);
      border-bottom: 1px solid var(--primary-border);
      padding: 6px 20px;
      font-size: 0.8rem;
      color: var(--primary);
      font-weight: 600;
      flex-wrap: wrap;
      gap: 8px;
    }

    .mode-bar-left {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .mode-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      background: var(--primary);
      color: #ffffff;
      font-size: 0.72rem;
    }

    .mode-bar-right {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
    }

    .layout-mode-group {
      display: inline-flex;
      align-items: center;
      background: var(--bg-panel);
      border: 1px solid var(--primary-border);
      border-radius: var(--radius-md);
      padding: 2px;
      gap: 2px;
    }

    .layout-toggle-btn {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 600;
      border: none;
      background: transparent;
      color: var(--text-sub);
      cursor: pointer;
      transition: var(--transition);
      user-select: none;
      white-space: nowrap;
    }

    .layout-toggle-btn:hover {
      color: var(--primary);
      background: var(--primary-subtle);
    }

    .layout-toggle-btn.active {
      background: var(--primary);
      color: #ffffff;
      box-shadow: 0 1px 3px rgba(79, 70, 229, 0.3);
    }

    .split-preset-group {
      display: inline-flex;
      align-items: center;
      gap: 3px;
    }

    .split-preset-btn {
      padding: 2px 6px;
      border-radius: var(--radius-sm);
      font-size: 0.7rem;
      font-weight: 600;
      border: 1px solid var(--primary-border);
      background: var(--bg-panel);
      color: var(--text-sub);
      cursor: pointer;
      transition: var(--transition);
    }

    .split-preset-btn:hover {
      color: var(--primary);
      border-color: var(--primary);
    }

    .split-preset-btn.active {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }

    .reading-prefs {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .pref-item {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      cursor: pointer;
      font-size: 0.76rem;
      color: var(--text-sub);
      user-select: none;
    }

    .pref-item:hover {
      color: var(--primary);
    }

    /* ==========================================================================
       Main Workspace Layout (Split, Reader-Only, Console-Only, Stacked)
       ========================================================================== */
    main.app-workspace {
      flex: 1;
      min-height: 0;
      display: flex;
      overflow: hidden;
      position: relative;
    }

    /* 1. Split Layout (Default) */
    main.app-workspace.layout-split {
      flex-direction: row;
    }
    main.app-workspace.layout-split .pane-reader {
      min-width: 280px;
      display: block;
    }
    main.app-workspace.layout-split .pane-resizer {
      display: block;
      width: 6px;
      cursor: col-resize;
      background: var(--border);
      transition: background 0.2s;
      flex-shrink: 0;
      position: relative;
      z-index: 10;
    }
    main.app-workspace.layout-split .pane-resizer:hover,
    main.app-workspace.layout-split .pane-resizer.dragging {
      background: var(--primary);
    }
    main.app-workspace.layout-split .pane-console {
      min-width: 320px;
      display: flex;
    }

    /* 2. Reader Only (纯享阅读模式) */
    main.app-workspace.layout-reader-only {
      flex-direction: row;
    }
    main.app-workspace.layout-reader-only .pane-reader {
      width: 100% !important;
      max-width: 100% !important;
      flex: 1 1 100% !important;
      display: block;
      border-right: none;
      padding: 32px calc(max(24px, (100% - 920px) / 2));
    }
    main.app-workspace.layout-reader-only .pane-resizer {
      display: none !important;
    }
    main.app-workspace.layout-reader-only .pane-console {
      display: none !important;
    }

    /* 3. Console Only (专注做题模式) */
    main.app-workspace.layout-console-only {
      flex-direction: row;
    }
    main.app-workspace.layout-console-only .pane-reader {
      display: none !important;
    }
    main.app-workspace.layout-console-only .pane-resizer {
      display: none !important;
    }
    main.app-workspace.layout-console-only .pane-console {
      width: 100% !important;
      max-width: 100% !important;
      flex: 1 1 100% !important;
      display: flex;
      padding: 24px calc(max(20px, (100% - 960px) / 2));
    }

    /* 4. Stacked Layout (上下分屏) */
    main.app-workspace.layout-stacked {
      flex-direction: column !important;
    }
    main.app-workspace.layout-stacked .pane-reader {
      width: 100% !important;
      height: 50% !important;
      flex: none !important;
      border-right: none;
      border-bottom: 2px solid var(--border);
      padding: 24px 36px;
    }
    main.app-workspace.layout-stacked .pane-resizer {
      display: block;
      width: 100% !important;
      height: 6px !important;
      cursor: row-resize !important;
      background: var(--border);
      flex-shrink: 0;
    }
    main.app-workspace.layout-stacked .pane-resizer:hover,
    main.app-workspace.layout-stacked .pane-resizer.dragging {
      background: var(--primary);
    }
    main.app-workspace.layout-stacked .pane-console {
      width: 100% !important;
      height: 50% !important;
      flex: none !important;
      padding: 20px 32px;
    }

    /* Left Pane: Passage Reader */
    .pane-reader {
      flex: 1;
      height: 100%;
      overflow-y: auto;
      padding: 28px 36px;
      background: var(--bg-panel);
      border-right: 1px solid var(--border);
      scroll-behavior: smooth;
    }

    /* Right Pane: Question & Answering Console */
    .pane-console {
      flex: 1;
      height: 100%;
      overflow-y: auto;
      padding: 20px 28px;
      background: var(--bg-body);
      scroll-behavior: smooth;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* Floating Text Selection Annotation Toolbar */
    .text-selection-toolbar {
      position: fixed;
      display: none;
      z-index: 120;
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: var(--radius-full);
      box-shadow: var(--shadow-lg);
      padding: 4px 8px;
      align-items: center;
      gap: 4px;
      animation: popIn 0.15s ease-out;
    }

    .text-selection-toolbar button {
      background: transparent;
      border: none;
      padding: 4px 8px;
      border-radius: var(--radius-full);
      cursor: pointer;
      font-size: 0.78rem;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      color: var(--text-main);
      transition: var(--transition);
    }

    .text-selection-toolbar button:hover {
      background: var(--bg-hover);
    }

    .color-dot {
      width: 14px;
      height: 14px;
      border-radius: 50%;
      border: 1px solid rgba(0,0,0,0.15);
      display: inline-block;
    }

    /* User Custom Highlight Styles */
    mark.user-hl-yellow { background-color: var(--hl-yellow); color: inherit; padding: 1px 2px; border-radius: 2px; }
    mark.user-hl-green { background-color: var(--hl-green); color: inherit; padding: 1px 2px; border-radius: 2px; }
    mark.user-hl-pink { background-color: var(--hl-pink); color: inherit; padding: 1px 2px; border-radius: 2px; }
    mark.user-hl-underline { background-color: transparent; text-decoration: underline wavy var(--primary); text-underline-offset: 3px; color: inherit; }

    /* Sticky Reader Toolbar */
    .reader-toolbar {
      position: sticky;
      top: -28px;
      z-index: 20;
      margin: -28px -36px 20px -36px;
      padding: 10px 24px;
      background: var(--bg-panel);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
    }

    .reader-toolbar-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .reader-badge {
      padding: 2px 8px;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 700;
      background: var(--primary-subtle);
      color: var(--primary);
      border: 1px solid var(--primary-border);
    }

    .reader-stat {
      font-size: 0.78rem;
      color: var(--text-muted);
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    .reader-toolbar-right {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .para-jump-list {
      display: flex;
      align-items: center;
      gap: 4px;
      flex-wrap: wrap;
    }

    .p-jump-pill {
      padding: 2px 7px;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-weight: 700;
      border: 1px solid var(--border);
      background: var(--bg-subtle);
      color: var(--text-sub);
      cursor: pointer;
      transition: var(--transition);
    }

    .p-jump-pill:hover {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }

    /* Passage Typography */
    .passage-header {
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border);
    }

    .passage-title {
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.35;
      font-family: var(--reader-font);
    }

    .passage-meta-info {
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-top: 6px;
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .passage-content {
      font-family: var(--reader-font);
      font-size: 17px;
      line-height: 1.85;
      color: var(--text-main);
    }

    .para-wrap {
      margin-bottom: 18px;
      position: relative;
    }

    .para-marker {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--primary);
      background: var(--primary-subtle);
      border: 1px solid var(--primary-border);
      padding: 1px 6px;
      border-radius: 3px;
      margin-right: 6px;
      vertical-align: middle;
      cursor: pointer;
      user-select: none;
    }

    .para-marker:hover {
      background: var(--primary);
      color: #fff;
    }

    .para-body {
      display: inline;
      text-align: justify;
    }

    /* Section A Interactive Blank */
    .passage-blank {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 60px;
      height: 26px;
      padding: 0 8px;
      margin: 0 4px;
      border-bottom: 2px solid var(--primary);
      background: var(--primary-subtle);
      color: var(--primary);
      font-weight: 700;
      font-family: var(--body-font);
      border-radius: 4px 4px 0 0;
      cursor: pointer;
      transition: var(--transition);
      font-size: 0.88rem;
    }

    .passage-blank:hover {
      background: var(--primary);
      color: #ffffff;
    }

    .passage-blank.filled {
      background: #ecfdf5;
      color: #065f46;
      border-bottom-color: #10b981;
    }

    .passage-blank.active-blank {
      box-shadow: 0 0 0 2px var(--warning);
      border-color: var(--warning);
    }

    .blank-clear-btn {
      margin-left: 4px;
      font-size: 0.72rem;
      opacity: 0.7;
      cursor: pointer;
    }
    .blank-clear-btn:hover {
      opacity: 1;
      color: var(--danger);
    }

    /* Bilingual Paragraph Translation in Study Mode */
    .para-zh-trans {
      display: none;
      font-family: var(--body-font);
      font-size: 0.86rem;
      line-height: 1.6;
      color: var(--text-sub);
      background: var(--bg-subtle);
      padding: 10px 14px;
      border-radius: var(--radius-md);
      margin-top: 14px;
      margin-bottom: 14px;
      border-left: 3px solid var(--primary);
    }

    body.show-bilingual .para-zh-trans, .study-mode .para-zh-trans {
      display: block;
    }

    /* Evidence Highlight Pulse */
    .evidence-highlight {
      background-color: #fef08a !important;
      padding: 2px 4px;
      border-radius: 4px;
      box-shadow: 0 0 0 3px #facc15;
      transition: background 0.3s;
    }

    /* Clickable Word Token for Dictionary */
    .word-token {
      cursor: pointer;
      border-radius: 3px;
      padding: 0 1px;
      transition: background 0.12s, color 0.12s;
    }

    .word-token:hover {
      background: rgba(99, 102, 241, 0.18);
      color: var(--primary);
    }

    .word-token.active-word {
      background: var(--primary) !important;
      color: #ffffff !important;
      border-radius: 3px;
      box-shadow: 0 2px 6px rgba(79, 70, 229, 0.35);
    }

    /* Reader Footer Actions */
    .reader-footer-actions {
      margin-top: 32px;
      padding-top: 18px;
      border-top: 1px dashed var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
    }

    .btn-action-lg {
      padding: 9px 20px;
      font-size: 0.92rem;
      font-weight: 700;
      border-radius: var(--radius-md);
      box-shadow: 0 3px 10px rgba(79, 70, 229, 0.25);
    }

    /* ==========================================================================
       Console Panel Components
       ========================================================================== */
    .console-header-card {
      background: var(--bg-panel);
      padding: 14px 18px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .console-top-strip {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }

    .timer-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: monospace;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary);
      background: var(--primary-subtle);
      padding: 3px 10px;
      border-radius: var(--radius-md);
      border: 1px solid var(--primary-border);
    }

    .timer-ctrls {
      display: flex;
      gap: 4px;
    }

    .timer-btn {
      padding: 3px 8px;
      font-size: 0.72rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
      border: 1px solid var(--border);
      background: var(--bg-panel);
      color: var(--text-sub);
    }

    /* Progress bar */
    .progress-bar-wrap {
      width: 100%;
      height: 6px;
      background: var(--bg-subtle);
      border-radius: var(--radius-full);
      overflow: hidden;
      margin-top: 2px;
    }

    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--primary) 0%, #10b981 100%);
      width: 0%;
      transition: width 0.3s ease;
    }

    .matrix-summary {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.76rem;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .q-matrix {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      width: 100%;
      margin-top: 4px;
    }

    .matrix-item {
      width: 30px;
      height: 30px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: var(--radius-sm);
      font-size: 0.76rem;
      font-weight: 700;
      background: var(--bg-subtle);
      color: var(--text-sub);
      cursor: pointer;
      border: 1px solid var(--border);
      transition: var(--transition);
      position: relative;
    }

    .matrix-item:hover {
      background: var(--primary-subtle);
      color: var(--primary);
      border-color: var(--primary-border);
    }

    .matrix-item.answered {
      background: var(--primary-subtle);
      color: var(--primary);
      border-color: var(--primary);
    }

    .matrix-item.flagged::after {
      content: '★';
      position: absolute;
      top: -3px;
      right: 1px;
      font-size: 0.65rem;
      color: #f59e0b;
    }

    .matrix-item.correct {
      background: var(--success-subtle);
      color: var(--success);
      border-color: var(--success);
    }

    .matrix-item.wrong {
      background: var(--danger-subtle);
      color: var(--danger);
      border-color: var(--danger);
    }

    /* Section A Word Bank Card */
    .word-bank-card {
      background: var(--bg-panel);
      padding: 14px 16px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }

    .word-bank-title {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .word-chips-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
      gap: 6px;
    }

    .word-chip {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 6px;
      padding: 5px 8px;
      border-radius: var(--radius-md);
      font-size: 0.8rem;
      font-weight: 600;
      border: 1px solid var(--border);
      background: var(--bg-subtle);
      color: var(--text-main);
      cursor: pointer;
      transition: var(--transition);
      user-select: none;
    }

    .word-chip:hover {
      background: var(--primary-subtle);
      color: var(--primary);
      border-color: var(--primary-border);
      transform: translateY(-1px);
    }

    .word-chip.used {
      opacity: 0.55;
      background: var(--bg-hover);
    }

    .word-chip-left {
      display: flex;
      align-items: center;
      gap: 6px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .word-chip .chip-letter {
      width: 18px;
      height: 18px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--primary);
      color: #ffffff;
      border-radius: 50%;
      font-size: 0.7rem;
      font-weight: 700;
      flex-shrink: 0;
    }

    .word-chip.used .chip-letter {
      background: var(--text-muted);
    }

    .used-badge {
      font-size: 0.68rem;
      padding: 1px 4px;
      border-radius: 3px;
      background: var(--border);
      color: var(--text-sub);
    }

    /* Question Cards */
    .question-card {
      background: var(--bg-panel);
      padding: 18px 20px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: var(--transition);
      position: relative;
    }

    .question-card.active-target {
      border-color: var(--primary);
      box-shadow: 0 0 0 2px var(--primary-subtle);
    }

    .question-card.flagged {
      border-color: #f59e0b;
      background: #fffdfa;
    }

    .question-card.is-correct {
      border-color: var(--success);
      background: #fcfdfd;
    }

    .question-card.is-wrong {
      border-color: var(--danger);
      background: #fffdfd;
    }

    .q-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }

    .q-header-left {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .q-header-right {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .q-num-pill {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      background: var(--primary-subtle);
      color: var(--primary);
      font-size: 0.76rem;
      font-weight: 700;
      flex-shrink: 0;
    }

    .btn-flag-review {
      display: inline-flex;
      align-items: center;
      gap: 3px;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-weight: 600;
      border: 1px solid var(--border);
      background: var(--bg-panel);
      color: var(--text-muted);
      cursor: pointer;
      transition: var(--transition);
    }

    .btn-flag-review:hover {
      border-color: #f59e0b;
      color: #d97706;
    }

    .btn-flag-review.active {
      background: #fef3c7;
      border-color: #f59e0b;
      color: #b45309;
      font-weight: 700;
    }

    .locate-para-btn {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-weight: 600;
      border: 1px solid var(--primary-border);
      background: var(--primary-subtle);
      color: var(--primary);
      cursor: pointer;
      transition: var(--transition);
      white-space: nowrap;
    }

    .locate-para-btn:hover {
      background: var(--primary);
      color: #ffffff;
      transform: translateY(-1px);
    }

    .q-stem {
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.5;
    }

    .q-stem-zh {
      font-size: 0.82rem;
      color: var(--text-sub);
      margin-top: 4px;
      display: none;
    }

    body.show-bilingual .q-stem-zh, .study-mode .q-stem-zh {
      display: block;
    }

    /* Options */
    .options-group {
      display: flex;
      flex-direction: column;
      gap: 7px;
    }

    .option-label {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 9px 12px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      background: var(--bg-panel);
      cursor: pointer;
      transition: var(--transition);
      font-size: 0.88rem;
      line-height: 1.45;
    }

    .option-label:hover {
      background: var(--bg-hover);
      border-color: var(--border-focus);
    }

    .option-label input[type="radio"] {
      margin-top: 3px;
      accent-color: var(--primary);
      cursor: pointer;
    }

    .option-label.selected {
      background: var(--primary-subtle);
      border-color: var(--primary);
      color: var(--primary);
      font-weight: 600;
    }

    .option-label.correct-choice {
      background: var(--success-subtle) !important;
      border-color: var(--success) !important;
      color: #065f46 !important;
      font-weight: 700;
    }

    .option-label.wrong-choice {
      background: var(--danger-subtle) !important;
      border-color: var(--danger) !important;
      color: #991b1b !important;
      text-decoration: line-through;
    }

    /* Section B Paragraph Buttons */
    .para-select-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 6px;
    }

    .para-badge-btn {
      width: 32px;
      height: 32px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      border: 1px solid var(--border);
      background: var(--bg-subtle);
      color: var(--text-main);
      cursor: pointer;
      transition: var(--transition);
      position: relative;
    }

    .para-badge-btn:hover {
      background: var(--primary-subtle);
      color: var(--primary);
      border-color: var(--primary-border);
      transform: translateY(-1px);
    }

    .para-badge-btn.selected {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 2px 4px rgba(79, 70, 229, 0.3);
    }

    .para-badge-btn.correct-match {
      background: var(--success) !important;
      color: #ffffff !important;
      border-color: var(--success) !important;
    }

    .para-badge-btn.wrong-match {
      background: var(--danger) !important;
      color: #ffffff !important;
      border-color: var(--danger) !important;
    }

    /* Explanation Box */
    .explanation-box {
      display: none;
      background: var(--bg-subtle);
      padding: 12px 14px;
      border-radius: var(--radius-md);
      border-left: 3px solid var(--primary);
      font-size: 0.84rem;
      line-height: 1.55;
      color: var(--text-main);
    }

    .study-mode .explanation-box, 
    .show-answers .explanation-box,
    .explanation-box.is-visible,
    .question-card.is-submitted .explanation-box {
      display: block;
    }

    .expl-tag {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--primary);
      background: var(--primary-subtle);
      padding: 2px 6px;
      border-radius: 3px;
      margin-bottom: 6px;
    }

    /* Console Stepper & Submission Bar */
    .console-nav-stepper {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-top: 8px;
    }

    .console-submit-bar {
      background: var(--bg-panel);
      padding: 14px 18px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 10px;
    }

    /* Floating Dictionary Popover */
    .dict-popover {
      position: fixed;
      display: none;
      z-index: 9999;
      width: 330px;
      max-width: calc(100vw - 24px);
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      box-shadow: 0 14px 34px -4px rgba(0, 0, 0, 0.22), 0 4px 12px rgba(0, 0, 0, 0.08);
      padding: 14px 16px;
      font-family: var(--body-font);
      animation: popIn 0.16s cubic-bezier(0.16, 1, 0.3, 1);
      backdrop-filter: blur(10px);
    }

    .dict-popover::after {
      content: '';
      position: absolute;
      width: 10px;
      height: 10px;
      background: var(--bg-panel);
      border-left: 1px solid var(--border);
      border-top: 1px solid var(--border);
      transform: rotate(45deg);
      top: -6px;
      left: var(--arrow-left, 24px);
      pointer-events: none;
    }

    .dict-popover.popover-above::after {
      top: auto;
      bottom: -6px;
      border-left: none;
      border-top: none;
      border-right: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
    }

    @keyframes popIn {
      from { opacity: 0; transform: scale(0.95) translateY(4px); }
      to { opacity: 1; transform: scale(1) translateY(0); }
    }

    .dict-word {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary);
      display: flex;
      align-items: baseline;
      gap: 8px;
    }

    .dict-phonetic {
      font-size: 0.82rem;
      color: var(--text-muted);
      font-family: 'Times New Roman', serif;
    }

    .dict-root-hint {
      font-size: 0.74rem;
      color: var(--primary);
      background: var(--primary-subtle);
      display: inline-block;
      padding: 1px 6px;
      border-radius: 4px;
      margin-top: 4px;
    }

    .dict-trans {
      font-size: 0.88rem;
      color: var(--text-main);
      line-height: 1.55;
      margin: 10px 0;
      max-height: 180px;
      overflow-y: auto;
    }

    .dict-trans-line {
      margin-bottom: 3px;
    }

    .dict-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px dashed var(--border);
      padding-top: 8px;
      margin-top: 6px;
    }

    /* Keyboard Shortcuts Modal */
    .kbd-modal {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(15, 23, 42, 0.5);
      backdrop-filter: blur(4px);
      z-index: 210;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .kbd-card {
      background: var(--bg-panel);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-lg);
      width: 100%;
      max-width: 440px;
      padding: 24px;
      animation: popIn 0.2s ease-out;
    }

    .kbd-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 0;
      border-bottom: 1px solid var(--border);
      font-size: 0.86rem;
    }

    kbd {
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: 4px;
      box-shadow: 0 1px 0 rgba(0,0,0,0.15);
      font-size: 0.8rem;
      font-family: monospace;
      padding: 2px 6px;
      font-weight: 700;
      color: var(--primary);
    }

    /* Score Modal */
    .score-summary-modal {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(15, 23, 42, 0.6);
      backdrop-filter: blur(4px);
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .score-card {
      background: var(--bg-panel);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-lg);
      width: 100%;
      max-width: 480px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      animation: popIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .score-circle {
      width: 110px;
      height: 110px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--primary) 0%, #a855f7 100%);
      color: #ffffff;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      box-shadow: 0 6px 18px rgba(79, 70, 229, 0.35);
    }

    .score-circle .big-num {
      font-size: 1.9rem;
      font-weight: 800;
      line-height: 1;
    }

    .score-circle .score-label {
      font-size: 0.68rem;
      opacity: 0.85;
      margin-top: 3px;
    }

    .score-stats-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      text-align: center;
    }

    .stat-box {
      background: var(--bg-subtle);
      padding: 10px 8px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
    }

    .stat-val {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary);
    }

    .stat-lbl {
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-top: 2px;
    }

    /* Drawers */
    .drawer-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(15, 23, 42, 0.4);
      z-index: 150;
      display: none;
    }

    .drawer {
      position: fixed;
      top: 0;
      right: -420px;
      bottom: 0;
      width: 420px;
      max-width: 90vw;
      background: var(--bg-panel);
      box-shadow: var(--shadow-lg);
      z-index: 160;
      display: flex;
      flex-direction: column;
      transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      border-left: 1px solid var(--border);
    }

    .drawer.open {
      right: 0;
    }

    .drawer-header {
      padding: 14px 18px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .drawer-body {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    /* Print Styles */
    @media print {
      body {
        height: auto !important;
        overflow: visible !important;
        background: #fff !important;
        color: #000 !important;
      }
      header.top-header, .mode-bar, .pane-resizer, .reader-toolbar, .console-header-card, .console-submit-bar, .text-selection-toolbar {
        display: none !important;
      }
      main.app-workspace {
        display: block !important;
        height: auto !important;
        overflow: visible !important;
      }
      .pane-reader, .pane-console {
        width: 100% !important;
        height: auto !important;
        overflow: visible !important;
        padding: 0 !important;
        border: none !important;
      }
      .question-card {
        break-inside: avoid;
        box-shadow: none !important;
        border: 1px solid #ccc !important;
        margin-bottom: 14px !important;
      }
    }
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header class="top-header">
    <div class="header-row-1">
      <div class="brand-group">
        <div class="logo-badge">6</div>
        <div class="brand-title">
          <h1>
            CET-6 英语六级阅读真题复习平台
            <span class="badge-tag">2021 - 2024 重点真题特训 · 33套全真题库</span>
          </h1>
        </div>
      </div>

      <div class="header-actions">
        <a href="index.html" class="btn" title="返回六级核心词汇背诵系统" style="text-decoration: none;">
          <span>🔤 核心词汇</span>
        </a>

        <a href="六级45天通关打卡清单.html" class="btn" title="查看45天每日复习打卡清单" style="text-decoration: none;">
          <span>📅 打卡清单</span>
        </a>

        <button class="btn btn-primary" id="btnModeToggle" onclick="toggleMode()">
          <span id="modeIcon">⚡</span>
          <span id="modeText">模考模式</span>
        </button>

        <button class="btn" onclick="cycleTheme()" title="切换主题 (浅色 / 羊皮纸护眼 / 深色夜读)">
          <span id="themeIcon">☀️</span>
          <span id="themeName">浅色</span>
        </button>

        <button class="btn" onclick="openDrawer('mistakes')" title="查看错题本">
          <span>📕 错题本</span>
          <span class="badge-count" id="mistakeBadge">0</span>
        </button>

        <button class="btn" onclick="openDrawer('vocab')" title="查看生词本">
          <span>⭐ 生词本</span>
          <span class="badge-count" id="vocabBadge">0</span>
        </button>

        <button class="btn" onclick="openDrawer('strategy')" title="六级阅读高分提分秘籍">
          <span>💡 解题秘籍</span>
        </button>

        <button class="btn" onclick="openKbdModal()" title="查看键盘快捷键帮助 (或按 ? 键)">
          <span>⌨️ 快捷键</span>
        </button>

        <button class="btn" onclick="window.print()" title="纯净试卷排版打印 / 导出PDF">
          <span>🖨️ 打印试卷</span>
        </button>
      </div>
    </div>

    <!-- Filter Toolbar -->
    <div class="header-row-2">
      <!-- Year Pills -->
      <div class="year-pills" id="yearPills">
        <div class="pill active" onclick="filterByYear('recent', this)">🔥 2021-2024 重点真题 (12套)</div>
        <div class="pill" onclick="filterByYear('2024', this)">2024年</div>
        <div class="pill" onclick="filterByYear('2023', this)">2023年</div>
        <div class="pill" onclick="filterByYear('2022', this)">2022年</div>
        <div class="pill" onclick="filterByYear('2021', this)">2021年</div>
        <div class="pill" onclick="filterByYear('all', this)">全部真题 (33套)</div>
        <div class="pill" onclick="filterByYear('archive', this)">2014-2020 往年归档</div>
      </div>

      <!-- Exam Selector & Section Tabs -->
      <div class="exam-select-group">
        <select class="custom-select" id="examSelect" onchange="onExamChange(this.value)">
          <!-- Populated dynamically -->
        </select>

        <div class="section-tabs" id="sectionTabs">
          <div class="section-tab active" data-sec="sec_c1" onclick="switchSection('sec_c1', this)">仔细阅读 C1 (Q46-Q50)</div>
          <div class="section-tab" data-sec="sec_c2" onclick="switchSection('sec_c2', this)">仔细阅读 C2 (Q51-Q55)</div>
          <div class="section-tab" data-sec="sec_b" onclick="switchSection('sec_b', this)">长篇匹配 B (Q36-Q45)</div>
          <div class="section-tab" data-sec="sec_a" onclick="switchSection('sec_a', this)">选词填空 A (Q26-Q35)</div>
          <div class="section-tab" data-sec="all" onclick="switchSection('all', this)">全卷总览 (All)</div>
        </div>
      </div>
    </div>
  </header>

  <!-- Mode & Layout Strip -->
  <div class="mode-bar">
    <div class="mode-bar-left">
      <span class="mode-badge" id="currentModeBadge">⚡ 全真模考模式</span>
      <span id="examTitleBrief" style="font-weight: 700; color: var(--text-main);">当前：2024年12月 六级真题 (第1套)</span>
    </div>

    <div class="mode-bar-right">
      <!-- Layout Modes Switcher -->
      <div style="display: flex; align-items: center; gap: 6px;">
        <span style="font-size: 0.74rem; color: var(--text-muted);">界面布局：</span>
        <div class="layout-mode-group">
          <button class="layout-toggle-btn active" data-layout="split" onclick="setLayoutMode('split')" title="左右分屏对照（左文章右题目，经典考场）">
            <span>⚖️ 左右分屏</span>
          </button>
          <button class="layout-toggle-btn" data-layout="reader-only" onclick="setLayoutMode('reader-only')" title="全屏文章，专注阅读">
            <span>📖 仅看文章</span>
          </button>
          <button class="layout-toggle-btn" data-layout="console-only" onclick="setLayoutMode('console-only')" title="专注做题界面（全屏题目，舒展选项）">
            <span>✍️ 仅看题目</span>
          </button>
          <button class="layout-toggle-btn" data-layout="stacked" onclick="setLayoutMode('stacked')" title="上下分屏（上文下题）">
            <span>📑 上下分屏</span>
          </button>
        </div>

        <div class="split-preset-group" id="splitPresets">
          <button class="split-preset-btn" data-ratio="40" onclick="setSplitRatio(40)" title="题宽文窄 (40:60)">4:6</button>
          <button class="split-preset-btn active" data-ratio="50" onclick="setSplitRatio(50)" title="对半平分 (50:50)">5:5</button>
          <button class="split-preset-btn" data-ratio="60" onclick="setSplitRatio(60)" title="文宽题窄 (60:40)">6:4</button>
        </div>
      </div>

      <!-- Typography & Bilingual Strip -->
      <div class="reading-prefs">
        <span class="pref-item" style="color: var(--primary); font-weight: 600; cursor: default;" title="点击阅读文章中任意单词，即可浮现地道音标、中文释义与真题例解">👆 点击单词查释义</span>
        <span class="pref-item" onclick="adjustFontSize(-1)">A- 缩小</span>
        <span class="pref-item" onclick="adjustFontSize(1)">A+ 放大</span>
        <span class="pref-item" onclick="toggleReaderFont()">🔠 衬线字体</span>
        <label class="pref-item" id="bilingualToggleGroup" style="cursor: pointer;">
          <input type="checkbox" id="chkShowBilingual" onchange="toggleBilingual(this.checked)">
          <span>中英双语</span>
        </label>
      </div>
    </div>
  </div>

  <!-- Main Workspace (Dual Split-Screen) -->
  <main class="app-workspace layout-split" id="appWorkspace">
    <!-- Left Pane: Passage Reading Area -->
    <section class="pane-reader" id="paneReader">
      <div id="readerContainer">
        <!-- Populated dynamically by renderPassage() -->
      </div>
    </section>

    <!-- Resizer Divider -->
    <div class="pane-resizer" id="paneResizer"></div>

    <!-- Right Pane: Answering & Explanation Console -->
    <section class="pane-console" id="paneConsole">
      <!-- Console Header (Timer & Navigator) -->
      <div class="console-header-card">
        <div class="console-top-strip">
          <div style="display: flex; align-items: center; gap: 10px;">
            <div class="timer-badge">
              <span>⏱️</span>
              <span id="timerDisplay">40:00</span>
            </div>
            <div class="timer-ctrls">
              <button class="timer-btn" onclick="toggleTimer()" id="btnTimerToggle">暂停</button>
              <button class="timer-btn" onclick="resetTimer()">重置</button>
            </div>
          </div>

          <div style="font-size: 0.82rem; font-weight: 600; color: var(--text-sub);">
            已完成：<span id="answeredCount" style="color: var(--primary);">0</span> / <span id="totalQuestionsCount">5</span> 题
          </div>
        </div>

        <!-- Progress bar -->
        <div class="progress-bar-wrap">
          <div class="progress-bar-fill" id="progressBarFill"></div>
        </div>

        <div class="matrix-summary">
          <span>答题卡快速定位导航：</span>
          <span id="matrixSummaryCounts">未作答: 5 · 待复查: 0</span>
        </div>

        <div class="q-matrix" id="questionMatrix">
          <!-- Matrix buttons Q26..Q55 -->
        </div>
      </div>

      <!-- Section A Word Bank Card (Visible when Section A is present) -->
      <div class="word-bank-card" id="wordBankCard" style="display: none;">
        <div class="word-bank-title">
          <span>🔤 选词填空备选词库 (15 选 10)</span>
          <span style="font-size: 0.74rem; font-weight: normal; color: var(--text-muted);">点击空位后点击词汇填入</span>
        </div>
        <div class="word-chips-grid" id="wordChipsContainer">
          <!-- Word chips A to O -->
        </div>
      </div>

      <!-- Questions Container -->
      <div id="questionsContainer" style="display: flex; flex-direction: column; gap: 14px;">
        <!-- Question cards rendered dynamically -->
      </div>

      <!-- Stepper & Submit Bar -->
      <div class="console-nav-stepper" id="consoleStepper">
        <button class="btn btn-outline" onclick="goToPrevSection()">◀ 上一模块</button>
        <button class="btn btn-outline" onclick="goToNextSection()">下一模块 ▶</button>
      </div>

      <!-- Bottom Submission Bar -->
      <div class="console-submit-bar" id="submitBar">
        <div style="font-size: 0.82rem; color: var(--text-muted);">
          答题进度实时本地保存，不慎关闭网页可无缝恢复
        </div>
        <div style="display: flex; gap: 8px;">
          <button class="btn btn-outline" onclick="resetCurrentExam()">重新作答</button>
          <button class="btn btn-primary" onclick="submitExam()">提交试卷并核对答案</button>
        </div>
      </div>
    </section>
  </main>

  <!-- Floating Text Selection Annotation Toolbar -->
  <div class="text-selection-toolbar" id="textSelectionToolbar">
    <button onclick="applyUserHighlight('yellow')" title="黄色高亮"><span class="color-dot" style="background:#fef08a;"></span> 高亮</button>
    <button onclick="applyUserHighlight('green')" title="绿色高亮"><span class="color-dot" style="background:#bbf7d0;"></span> 重点</button>
    <button onclick="applyUserHighlight('pink')" title="粉色高亮"><span class="color-dot" style="background:#fbcfe8;"></span> 考点</button>
    <button onclick="applyUserHighlight('underline')" title="下划线标注">✏️ 下划线</button>
    <button onclick="speakSelectedText()" title="朗读选中英文">🔊 朗读</button>
    <button onclick="lookupSelectedText()" title="查词典">🔍 查词</button>
    <button onclick="clearUserHighlight()" title="清除选中区域高亮" style="color:var(--text-muted);">✕ 清除</button>
  </div>

  <!-- Dictionary Popover Card -->
  <div class="dict-popover" id="dictPopover" onclick="event.stopPropagation()">
    <div style="display: flex; align-items: flex-start; justify-content: space-between;">
      <div>
        <div class="dict-word">
          <span id="dictWordText">word</span>
          <span class="dict-phonetic" id="dictPhonetic">/wɜːrd/</span>
        </div>
        <div class="dict-root-hint" id="dictRootHint" style="display: none;">
          原形: <strong id="dictRootText"></strong>
        </div>
      </div>
      <div style="display: flex; align-items: center; gap: 4px;">
        <button class="btn btn-sm" style="padding: 2px 7px; font-size: 0.75rem;" onclick="speakCurrentWord()" title="朗读单词发音">🔊</button>
        <button class="btn btn-outline btn-sm" style="padding: 2px 6px; font-size: 0.75rem; border-color: transparent;" onclick="closeDictPopover()" title="关闭">✕</button>
      </div>
    </div>
    <div class="dict-trans" id="dictTrans">
      n. 单词，话语
    </div>
    <div class="dict-actions">
      <span class="badge" id="dictTagPill" style="font-size: 0.7rem; background: var(--primary-subtle); color: var(--primary);">CET-6 核心词汇</span>
      <button class="btn btn-primary btn-sm" id="btnAddToVocab" style="padding: 3px 10px; font-size: 0.75rem;" onclick="addCurrentWordToVocab()">⭐ 存入生词本</button>
    </div>
  </div>

  <!-- Keyboard Shortcuts Cheat Sheet Modal -->
  <div class="kbd-modal" id="kbdModal" onclick="closeKbdModal()">
    <div class="kbd-card" onclick="event.stopPropagation()">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
        <h3 style="font-size: 1.1rem; color: var(--primary);">⌨️ 全键盘极速刷题指南</h3>
        <button class="btn btn-outline" onclick="closeKbdModal()" style="padding: 2px 6px;">✕</button>
      </div>
      <div class="kbd-row"><span>选择当前题目选项</span><div><kbd>A</kbd> <kbd>B</kbd> <kbd>C</kbd> <kbd>D</kbd></div></div>
      <div class="kbd-row"><span>在阅读界面与答题界面切换</span><div><kbd>V</kbd></div></div>
      <div class="kbd-row"><span>标记 / 取消标记当前题目待复查</span><div><kbd>F</kbd></div></div>
      <div class="kbd-row"><span>切换至上一题 / 下一题</span><div><kbd>K</kbd> / <kbd>J</kbd> 或 <kbd>↑</kbd> / <kbd>↓</kbd></div></div>
      <div class="kbd-row"><span>直达模块：选词填空 A</span><div><kbd>1</kbd></div></div>
      <div class="kbd-row"><span>直达模块：长篇匹配 B</span><div><kbd>2</kbd></div></div>
      <div class="kbd-row"><span>直达模块：仔细阅读 C1</span><div><kbd>3</kbd></div></div>
      <div class="kbd-row"><span>直达模块：仔细阅读 C2</span><div><kbd>4</kbd></div></div>
      <div class="kbd-row"><span>全卷总览</span><div><kbd>0</kbd></div></div>
      <div class="kbd-row"><span>打开快捷键帮助</span><div><kbd>?</kbd></div></div>
      <div class="kbd-row"><span>关闭浮层 / 弹窗</span><div><kbd>Esc</kbd></div></div>
    </div>
  </div>

  <!-- Score Summary Modal -->
  <div class="score-summary-modal" id="scoreModal">
    <div class="score-card">
      <div style="text-align: center;">
        <h2 style="font-size: 1.25rem; margin-bottom: 4px;" id="modalScoreHeading">作答成绩单</h2>
        <p style="font-size: 0.78rem; color: var(--text-muted);" id="modalExamTitle">2024年12月 六级阅读真题 (第1套)</p>
      </div>

      <div class="score-circle">
        <div class="big-num" id="modalScoreVal">71.0</div>
        <div class="score-label" id="modalScoreLabel">本篇折合分 (满分 71.0 分)</div>
      </div>

      <div class="score-stats-grid">
        <div class="stat-box">
          <div class="stat-val" id="modalAccuracy">100%</div>
          <div class="stat-lbl" id="modalAccuracyLabel">本篇正确率</div>
        </div>
        <div class="stat-box">
          <div class="stat-val" id="modalCorrectCount">5 / 5</div>
          <div class="stat-lbl" id="modalCountLabel">答对题数</div>
        </div>
        <div class="stat-box">
          <div class="stat-val" id="modalTimeSpent">05:12</div>
          <div class="stat-lbl">作答用时</div>
        </div>
      </div>

      <div style="display: flex; gap: 8px; justify-content: flex-end; flex-wrap: wrap;" id="modalActionButtons">
        <button class="btn btn-outline" onclick="closeScoreModal()">关闭并复盘错题</button>
        <button class="btn btn-primary" onclick="switchToStudyModeAndReview()">进入深度精读解析</button>
      </div>
    </div>
  </div>

  <!-- Slide-over Drawer: Mistakes Notebook -->
  <div class="drawer-overlay" id="drawerOverlay" onclick="closeAllDrawers()"></div>
  <div class="drawer" id="mistakesDrawer">
    <div class="drawer-header">
      <h3>📕 错题本 <span class="badge-count" id="drawerMistakeCount">0</span></h3>
      <button class="btn btn-outline" onclick="closeAllDrawers()">✕</button>
    </div>
    <div class="drawer-body" id="mistakesListContainer">
      <!-- Populated by renderMistakes() -->
    </div>
  </div>

  <!-- Slide-over Drawer: Vocabulary Notebook -->
  <div class="drawer" id="vocabDrawer">
    <div class="drawer-header">
      <h3>⭐ 核心生词本 <span class="badge-count" id="drawerVocabCount">0</span></h3>
      <div style="display: flex; gap: 6px;">
        <button class="btn" style="font-size: 0.75rem;" onclick="exportVocabTxt()">导出文本</button>
        <button class="btn btn-outline" onclick="closeAllDrawers()">✕</button>
      </div>
    </div>
    <div class="drawer-body" id="vocabListContainer">
      <!-- Populated by renderVocab() -->
    </div>
  </div>

  <!-- Slide-over Drawer: Exam Strategies Masterclass -->
  <div class="drawer" id="strategyDrawer">
    <div class="drawer-header">
      <h3>💡 六级阅读高分提分通关秘籍</h3>
      <button class="btn btn-outline" onclick="closeAllDrawers()">✕</button>
    </div>
    <div class="drawer-body">
      <div style="line-height: 1.7; font-size: 0.88rem; color: var(--text-main);">
        <h4 style="color: var(--primary); margin-bottom: 6px;">一、Section A · 选词填空“词性预判五大口诀”</h4>
        <p>1. <strong>主谓之间、动宾之间找副词：</strong>前后成分完整，空位多为副词（以 -ly 结尾，如 drastically, substantially）。</p>
        <p>2. <strong>冠词/形容词与名词之间找形容词：</strong>修饰名词中心词（-ive, -able, -al, -ous 后缀）。</p>
        <p>3. <strong>及物动词或介词之后找名词：</strong>若为空白，通常为抽象名词或复数名词（-tion, -ty, -ance）。</p>
        <p>4. <strong>助动词与被动语态找过去分词：</strong>be/have + ____ 多为过去分词（-ed）或现在分词（-ing）。</p>
        <hr style="border: none; border-top: 1px dashed var(--border); margin: 14px 0;">

        <h4 style="color: var(--primary); margin-bottom: 6px;">二、Section B · 长篇阅读“极速两遍定位法”</h4>
        <p>1. <strong>先题后文，抓取三大特征定位词：</strong>人名、地名、数字年代、专有名词、以及独特的比较级/复合词。</p>
        <p>2. <strong>警惕同义替换法则：</strong>正确答案绝少照抄题干原词，90%为同义词替换（如 increase 替换为 surge, reduce 替换为 curb, danger 替换为 jeopardy）。</p>
        <p>3. <strong>首尾句与转折词：</strong>各段首句和末句、以及 However, Yet, Crucially 之后是高频命题点。</p>
        <hr style="border: none; border-top: 1px dashed var(--border); margin: 14px 0;">

        <h4 style="color: var(--primary); margin-bottom: 6px;">三、Section C · 仔细阅读“五大题型解题防坑指南”</h4>
        <p>1. <strong>细节事实题：</strong>准确定位至原文1-2句话，紧扣原文同义改写，凡与原文细节张冠李戴者坚决排除。</p>
        <p>2. <strong>主旨大意题：</strong>串联各段首末句，排除“以偏概全（只讲其中一段例子）”与“过度推断”选项。</p>
        <p>3. <strong>作者态度题：</strong>关注带有褒贬色彩的形容词与动词（objective 客观, skeptical 怀疑, critical 批评, cautious 谨慎）。</p>
      </div>
    </div>
  </div>

  <!-- Embedded Datasets -->
  <script>
    window.CET6_EXAMS = """ + exams_json + """;
    window.CET6_DICT = """ + dict_json + """;
  </script>

  <!-- Application Logic -->
  <script>
    /* ==========================================================================
       Application State
       ========================================================================== */
    const state = {
      currentExamIndex: 0,
      currentSection: 'sec_c1', // Default to Section C1 as requested!
      yearFilter: 'recent',
      layoutMode: localStorage.getItem('cet6_layout_mode') || 'split',
      splitRatio: parseInt(localStorage.getItem('cet6_split_ratio') || '50'),
      isStudyMode: false,
      fontSize: 17,
      isSerifFont: true,
      showBilingual: false,
      userAnswers: {},
      flaggedQuestions: {}, // key: qNum, val: true
      activeBlank: null,
      submittedSections: {}, // key: sec_a, sec_b, sec_c1, sec_c2
      examSubmitted: false,
      timerSeconds: 40 * 60,
      timerInterval: null,
      timerRunning: false,
      focusedQuestionNum: 46,
      mistakes: JSON.parse(localStorage.getItem('cet6_mistakes') || '[]'),
      vocab: JSON.parse(localStorage.getItem('cet6_vocab') || '[]'),
      currentPopoverWord: null
    };

    const SECTION_SEQUENCE = ['sec_a', 'sec_b', 'sec_c1', 'sec_c2', 'all'];

    function isSectionSubmitted(secKey) {
      if (!state.submittedSections) return false;
      return Boolean(state.submittedSections[secKey]);
    }

    function isQuestionSubmitted(qNum) {
      const n = parseInt(qNum, 10);
      if (n >= 26 && n <= 35) return isSectionSubmitted('sec_a');
      if (n >= 36 && n <= 45) return isSectionSubmitted('sec_b');
      if (n >= 46 && n <= 50) return isSectionSubmitted('sec_c1');
      if (n >= 51 && n <= 55) return isSectionSubmitted('sec_c2');
      return false;
    }

    /* ==========================================================================
       Initialization
       ========================================================================== */
    document.addEventListener('DOMContentLoaded', () => {
      initExamSelector();
      loadCurrentExam();
      initResizer();
      initWordClickListeners();
      initTextSelectionToolbar();
      updateBadgeCounts();
      startTimer();
      loadTheme();
      setLayoutMode(state.layoutMode);
      setSplitRatio(state.splitRatio);
      initKeyboardShortcuts();
    });

    function initExamSelector() {
      const select = document.getElementById('examSelect');
      select.innerHTML = '';
      
      const filtered = getFilteredExams();
      filtered.forEach((ex, idx) => {
        const opt = document.createElement('option');
        opt.value = idx;
        opt.textContent = `${ex.title} [${ex.theme || '综合精选'}]`;
        select.appendChild(opt);
      });

      state.currentExamIndex = 0;
    }

    function getFilteredExams() {
      if (state.yearFilter === 'all') return window.CET6_EXAMS;
      if (state.yearFilter === 'recent') return window.CET6_EXAMS.filter(ex => parseInt(ex.year) >= 2021);
      if (state.yearFilter === 'archive') return window.CET6_EXAMS.filter(ex => parseInt(ex.year) <= 2020);
      return window.CET6_EXAMS.filter(ex => ex.year === state.yearFilter);
    }

    function filterByYear(year, el) {
      state.yearFilter = year;
      document.querySelectorAll('#yearPills .pill').forEach(p => p.classList.remove('active'));
      if (el) {
        el.classList.add('active');
      } else if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active');
      }

      initExamSelector();
      state.currentExamIndex = 0;
      loadCurrentExam();
    }

    function onExamChange(index) {
      state.currentExamIndex = parseInt(index);
      loadCurrentExam();
    }

    function switchSection(secKey, el) {
      state.currentSection = secKey;
      document.querySelectorAll('#sectionTabs .section-tab').forEach(t => t.classList.remove('active'));
      if (el) {
        el.classList.add('active');
      } else {
        const targetTab = document.querySelector(`#sectionTabs .section-tab[data-sec="${secKey}"]`);
        if (targetTab) targetTab.classList.add('active');
      }

      renderPassage();
      renderQuestions();

      // Set default focused question
      if (secKey === 'sec_a') state.focusedQuestionNum = 26;
      else if (secKey === 'sec_b') state.focusedQuestionNum = 36;
      else if (secKey === 'sec_c1') state.focusedQuestionNum = 46;
      else if (secKey === 'sec_c2') state.focusedQuestionNum = 51;

      // Reset scroll position to top
      const reader = document.getElementById('paneReader');
      const consolePane = document.getElementById('paneConsole');
      if (reader) reader.scrollTop = 0;
      if (consolePane) consolePane.scrollTop = 0;

      updateFloatingSwitchButton();
    }

    function goToNextSection() {
      const idx = SECTION_SEQUENCE.indexOf(state.currentSection);
      if (idx >= 0 && idx < SECTION_SEQUENCE.length - 1) {
        switchSection(SECTION_SEQUENCE[idx + 1]);
      }
    }

    function goToPrevSection() {
      const idx = SECTION_SEQUENCE.indexOf(state.currentSection);
      if (idx > 0) {
        switchSection(SECTION_SEQUENCE[idx - 1]);
      }
    }

    function loadCurrentExam() {
      const exams = getFilteredExams();
      if (!exams.length) return;
      const ex = exams[state.currentExamIndex];

      const briefEl = document.getElementById('examTitleBrief');
      if (briefEl) briefEl.textContent = `当前试卷：${ex.title}`;

      // Restore saved state from localStorage
      const savedKey = `cet6_answers_${ex.id}`;
      const savedFlagsKey = `cet6_flags_${ex.id}`;
      const savedTimeKey = `cet6_time_${ex.id}`;
      const savedSubmittedKey = `cet6_submitted_${ex.id}`;

      state.userAnswers = JSON.parse(localStorage.getItem(savedKey) || '{}');
      state.flaggedQuestions = JSON.parse(localStorage.getItem(savedFlagsKey) || '{}');
      state.submittedSections = JSON.parse(localStorage.getItem(savedSubmittedKey) || '{}');
      state.examSubmitted = ['sec_a', 'sec_b', 'sec_c1', 'sec_c2'].every(k => state.submittedSections[k]);
      state.activeBlank = null;

      const savedTime = localStorage.getItem(savedTimeKey);
      state.timerSeconds = savedTime ? parseInt(savedTime) : (40 * 60);

      renderPassage();
      renderQuestions();
    }

    function saveExamProgress() {
      const exams = getFilteredExams();
      if (!exams.length) return;
      const ex = exams[state.currentExamIndex];
      if (!ex) return;

      localStorage.setItem(`cet6_answers_${ex.id}`, JSON.stringify(state.userAnswers));
      localStorage.setItem(`cet6_flags_${ex.id}`, JSON.stringify(state.flaggedQuestions));
      localStorage.setItem(`cet6_time_${ex.id}`, state.timerSeconds);
    }

    /* ==========================================================================
       Layout Modes (Split / Reader-Only / Console-Only / Stacked)
       ========================================================================== */
    function setLayoutMode(mode) {
      state.layoutMode = mode;
      localStorage.setItem('cet6_layout_mode', mode);

      const workspace = document.getElementById('appWorkspace');
      workspace.className = `app-workspace layout-${mode}`;

      document.querySelectorAll('.layout-toggle-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.layout === mode);
      });

      const splitPresets = document.getElementById('splitPresets');
      if (splitPresets) {
        splitPresets.style.display = (mode === 'split') ? 'inline-flex' : 'none';
      }

      const leftPane = document.getElementById('paneReader');
      const rightPane = document.getElementById('paneConsole');
      if (mode !== 'split') {
        leftPane.style.width = '';
        leftPane.style.height = '';
        leftPane.style.flex = '';
        rightPane.style.width = '';
        rightPane.style.height = '';
        rightPane.style.flex = '';
      } else {
        applySplitRatio(state.splitRatio);
      }

      updateFloatingSwitchButton();
    }

    function setSplitRatio(ratio) {
      state.splitRatio = ratio;
      localStorage.setItem('cet6_split_ratio', ratio);
      applySplitRatio(ratio);
      document.querySelectorAll('.split-preset-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.ratio === String(ratio));
      });
    }

    function applySplitRatio(ratio) {
      if (state.layoutMode !== 'split') return;
      const leftPane = document.getElementById('paneReader');
      const rightPane = document.getElementById('paneConsole');
      const r = parseInt(ratio) || 50;
      leftPane.style.flex = `0 0 ${r}%`;
      leftPane.style.width = `${r}%`;
      rightPane.style.flex = `0 0 ${100 - r}%`;
      rightPane.style.width = `${100 - r}%`;
    }

    function toggleReaderConsoleView() {
      if (state.layoutMode === 'reader-only') {
        setLayoutMode('console-only');
      } else if (state.layoutMode === 'console-only') {
        setLayoutMode('reader-only');
      } else {
        setLayoutMode('reader-only');
      }
    }

    function switchToQuestionsView() {
      if (state.layoutMode === 'reader-only') {
        setLayoutMode('console-only');
      }
      const consolePane = document.getElementById('paneConsole');
      if (consolePane) {
        consolePane.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    function switchToReaderView() {
      if (state.layoutMode === 'console-only') {
        setLayoutMode('reader-only');
      }
      const reader = document.getElementById('paneReader');
      if (reader) {
        reader.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    function updateFloatingSwitchButton() {
      // Floating switch pill removed per user preference
    }

    /* ==========================================================================
       Paragraph Navigation & Evidence Locating
       ========================================================================== */
    function jumpToPara(paraId) {
      const el = document.getElementById(paraId);
      const reader = document.getElementById('paneReader');
      if (el && reader) {
        const topPos = el.offsetTop - 70;
        reader.scrollTo({ top: Math.max(0, topPos), behavior: 'smooth' });
        el.classList.add('evidence-highlight');
        setTimeout(() => el.classList.remove('evidence-highlight'), 2200);
      }
    }

    function locateParagraph(secType, paraNum) {
      if (state.layoutMode === 'console-only') {
        setLayoutMode('split');
      }
      const paraId = (secType === 'c1' || secType === 'c2') 
        ? `${secType}_para_${paraNum}` 
        : `para_${paraNum}`;
      jumpToPara(paraId);
    }

    /* ==========================================================================
       Rendering Passages (Left Column)
       ========================================================================== */
    function renderPassage() {
      const exams = getFilteredExams();
      const ex = exams[state.currentExamIndex];
      const container = document.getElementById('readerContainer');
      container.innerHTML = '';

      if (!ex) return;

      const sec = state.currentSection;

      // Section A
      if ((sec === 'all' || sec === 'sec_a') && ex.section_a) {
        container.appendChild(createSectionAElement(ex.section_a, ex));
      }

      // Section B
      if ((sec === 'all' || sec === 'sec_b') && ex.section_b) {
        container.appendChild(createSectionBElement(ex.section_b, ex));
      }

      // Section C1
      if ((sec === 'all' || sec === 'sec_c1') && ex.section_c1) {
        container.appendChild(createSectionCElement(ex.section_c1, 'Passage One', 1, ex));
      }

      // Section C2
      if ((sec === 'all' || sec === 'sec_c2') && ex.section_c2) {
        container.appendChild(createSectionCElement(ex.section_c2, 'Passage Two', 2, ex));
      }

      applyReaderStyles();
      restoreSavedHighlights();
      wrapWordsWithTokens();
    }

    function createSectionAElement(secA, ex) {
      const wrap = document.createElement('article');
      wrap.className = 'passage-block';
      wrap.style.marginBottom = '30px';

      const wordCount = (secA.passage || '').split(/\\s+/).filter(Boolean).length;
      let passageHtml = secA.passage;

      secA.questions.forEach(q => {
        const bNum = q.num;
        const filledAns = state.userAnswers[bNum] || '';
        const wordText = filledAns && secA.word_bank[filledAns] ? secA.word_bank[filledAns] : '';
        const displayLabel = wordText ? `[${bNum}] ${wordText}` : `[${bNum}] ______`;
        const isFilled = Boolean(wordText);
        const clearBtn = isFilled ? `<span class="blank-clear-btn" onclick="clearBlankAnswer(${bNum}, event)" title="清空此题">✕</span>` : '';
        const blankSpan = `<span class="passage-blank ${isFilled ? 'filled' : ''}" data-bnum="${bNum}" onclick="onBlankClick(${bNum})">${displayLabel}${clearBtn}</span>`;
        
        const regex = new RegExp(`\\\\b${bNum}\\\\b(?=[\\\\s\\\\.,;:\\\\?!]|$)`, 'g');
        passageHtml = passageHtml.replace(regex, blankSpan);
      });

      wrap.innerHTML = `
        <div class="reader-toolbar">
          <div class="reader-toolbar-left">
            <span class="reader-badge">Part III · Section A · 选词填空</span>
            <span class="reader-stat">📝 <strong>${wordCount}</strong> 词</span>
            <span class="reader-stat">⏱ 建议用时 7-8 分钟</span>
          </div>
          <div class="reader-toolbar-right">
            <button class="btn btn-sm btn-primary" onclick="switchToQuestionsView()" title="切换到对应做题界面">
              ✍️ 去填空
            </button>
          </div>
        </div>

        <div class="passage-header">
          <h2 class="passage-title">${secA.title || 'Section A · Banked Cloze'}</h2>
          <div class="passage-meta-info">
            <span>题号：Q26 - Q35 (共10题)</span>
            <span>分值权重：每题 0.5% (总分约 35.5 分)</span>
          </div>
        </div>
        <div class="passage-content">
          <p>${passageHtml.split('\\n').join('</p><p>')}</p>
          <div class="para-zh-trans">
            <strong>【全文参考译文】：</strong><br>${secA.translation || '暂无译文'}
          </div>
        </div>

        <div class="reader-footer-actions">
          <span></span>
          <button class="btn btn-primary btn-action-lg" onclick="submitCurrentSection('sec_a')">
            📝 阅读作答完毕，提交选词填空 A (Q26-Q35) ➔
          </button>
          <button class="btn btn-outline" onclick="switchSection('sec_b')">下一节: 长篇匹配 B ▶</button>
        </div>
      `;
      return wrap;
    }

    function createSectionBElement(secB, ex) {
      const wrap = document.createElement('article');
      wrap.className = 'passage-block';
      wrap.style.marginBottom = '30px';

      const paragraphs = secB.paragraphs || [];
      const wordCount = (secB.passage || paragraphs.map(p => p.text).join(' ')).split(/\\s+/).filter(Boolean).length;

      let parasHtml = '';
      let paraJumpListHtml = '';
      if (paragraphs.length) {
        paragraphs.forEach(p => {
          paraJumpListHtml += `<button class="p-jump-pill" onclick="jumpToPara('para_${p.label}')">${p.label}</button>`;
          parasHtml += `
            <div class="para-wrap" id="para_${p.label}">
              <span class="para-marker" onclick="jumpToPara('para_${p.label}')" title="点击定位高亮本段">${p.label}</span>
              <p class="para-body">${p.text}</p>
            </div>
          `;
        });
      } else {
        parasHtml = `<p>${secB.passage || ''}</p>`;
      }

      wrap.innerHTML = `
        <div class="reader-toolbar">
          <div class="reader-toolbar-left">
            <span class="reader-badge">Part III · Section B · 长篇阅读 (段落匹配)</span>
            <span class="reader-stat">📝 <strong>${wordCount}</strong> 词</span>
            <span class="reader-stat">⏱ 建议用时 12-15 分钟</span>
          </div>
          <div class="reader-toolbar-right">
            <span style="font-size: 0.76rem; color: var(--text-muted); margin-right: 2px;">段落直达:</span>
            <div class="para-jump-list">${paraJumpListHtml}</div>
            <button class="btn btn-sm btn-primary" onclick="switchToQuestionsView()" title="切换到对应做题界面">
              ✍️ 去匹配
            </button>
          </div>
        </div>

        <div class="passage-header">
          <h2 class="passage-title">${secB.title || 'Section B · Long Reading Matching'}</h2>
          <div class="passage-meta-info">
            <span>题号：Q36 - Q45 (共10题)</span>
            <span>分值权重：每题 1.0% (总分约 71.0 分)</span>
          </div>
        </div>
        <div class="passage-content">
          ${parasHtml}
          <div class="para-zh-trans">
            <strong>【长篇要点与中文解析】：</strong><br>${secB.translation || '本篇详尽考察核心词同义替换定位法则。'}
          </div>
        </div>

        <div class="reader-footer-actions">
          <button class="btn btn-outline" onclick="switchSection('sec_a')">◀ 上一节: 选词填空 A</button>
          <button class="btn btn-primary btn-action-lg" onclick="submitCurrentSection('sec_b')">
            📝 阅读作答完毕，提交长篇匹配 B (Q36-Q45) ➔
          </button>
          <button class="btn btn-outline" onclick="switchSection('sec_c1')">下一节: 仔细阅读 C1 ▶</button>
        </div>
      `;
      return wrap;
    }

    function createSectionCElement(secC, label, idx, ex) {
      const wrap = document.createElement('article');
      wrap.className = 'passage-block';
      wrap.id = `passage_sec_c${idx}`;
      wrap.style.marginBottom = '30px';

      const paragraphs = (secC.passage || '').split('\\n').filter(p => p.trim());
      const wordCount = (secC.passage || '').split(/\\s+/).filter(Boolean).length;

      let bodyHtml = '';
      let paraJumpListHtml = '';
      paragraphs.forEach((pText, pIdx) => {
        const pNum = pIdx + 1;
        paraJumpListHtml += `<button class="p-jump-pill" onclick="jumpToPara('c${idx}_para_${pNum}')">P${pNum}</button>`;
        bodyHtml += `
          <div class="para-wrap" id="c${idx}_para_${pNum}">
            <span class="para-marker" title="点击定位高亮本段" onclick="jumpToPara('c${idx}_para_${pNum}')">P${pNum}</span>
            <p class="para-body">${pText}</p>
          </div>
        `;
      });

      const nextSecName = (idx === 1) ? '仔细阅读 C2' : '全卷答案核对';
      const nextSecAction = (idx === 1) ? `switchSection('sec_c2')` : `submitExam()`;

      wrap.innerHTML = `
        <div class="reader-toolbar">
          <div class="reader-toolbar-left">
            <span class="reader-badge">Part III · Section C · ${label}</span>
            <span class="reader-stat">📝 <strong>${wordCount}</strong> 词</span>
            <span class="reader-stat">⏱ 建议阅读 6-8 分钟</span>
          </div>
          <div class="reader-toolbar-right">
            <span style="font-size: 0.76rem; color: var(--text-muted); margin-right: 2px;">段落直达:</span>
            <div class="para-jump-list">${paraJumpListHtml}</div>
            <button class="btn btn-sm btn-primary" onclick="switchToQuestionsView()" title="切换到做题界面">
              ✍️ 去答题
            </button>
          </div>
        </div>

        <div class="passage-header">
          <h2 class="passage-title">${secC.title || `Section C · ${label}`}</h2>
          <div class="passage-meta-info">
            <span>题号：${idx === 1 ? 'Q46 - Q50' : 'Q51 - Q55'} (共5题)</span>
            <span>分值权重：每题 2.0% (总分约 71.0 分)</span>
            <span style="color: var(--success); font-weight: 600;">✓ 题源权威完整长文</span>
          </div>
        </div>
        <div class="passage-content">
          ${bodyHtml}
          <div class="para-zh-trans">
            <strong>【篇章主旨概括与中文精析】：</strong><br>
            <p><em>${secC.main_idea_zh || '暂无主旨概括'}</em></p>
          </div>
        </div>

        <div class="reader-footer-actions">
          <button class="btn btn-outline" onclick="${idx === 1 ? `switchSection('sec_b')` : `switchSection('sec_c1')`}">
            ◀ 上一节: ${idx === 1 ? '长篇匹配 B' : '仔细阅读 C1'}
          </button>
          <button class="btn btn-primary btn-action-lg" onclick="submitCurrentSection('${idx === 1 ? 'sec_c1' : 'sec_c2'}')">
            📝 阅读作答完毕，提交${idx === 1 ? '仔细阅读 1 (Q46-Q50)' : '仔细阅读 2 (Q51-Q55)'}核对答案 ➔
          </button>
          <button class="btn btn-outline" onclick="${nextSecAction}">${nextSecName} ▶</button>
        </div>
      `;
      return wrap;
    }

    /* ==========================================================================
       Rendering Questions (Right Column)
       ========================================================================== */
    function renderQuestions() {
      const exams = getFilteredExams();
      const ex = exams[state.currentExamIndex];
      const container = document.getElementById('questionsContainer');
      const matrix = document.getElementById('questionMatrix');
      const wbCard = document.getElementById('wordBankCard');
      const wbContainer = document.getElementById('wordChipsContainer');

      container.innerHTML = '';
      matrix.innerHTML = '';

      if (!ex) return;

      const sec = state.currentSection;
      let allQuestions = [];

      // Section A
      if ((sec === 'all' || sec === 'sec_a') && ex.section_a) {
        wbCard.style.display = 'block';
        wbContainer.innerHTML = '';
        const wb = ex.section_a.word_bank || {};
        
        Object.keys(wb).sort().forEach(letter => {
          const chip = document.createElement('div');
          const isUsed = Object.values(state.userAnswers).includes(letter);
          const usedInQ = isUsed ? Object.keys(state.userAnswers).find(k => state.userAnswers[k] === letter) : '';
          
          chip.className = `word-chip ${isUsed ? 'used' : ''}`;
          chip.dataset.letter = letter;
          chip.innerHTML = `
            <div class="word-chip-left">
              <span class="chip-letter">${letter}</span>
              <span>${wb[letter]}</span>
            </div>
            ${isUsed ? `<span class="used-badge" title="已填入第${usedInQ}空">[${usedInQ}]</span>` : ''}
          `;
          chip.onclick = () => onWordChipClick(letter, wb[letter]);
          wbContainer.appendChild(chip);
        });

        ex.section_a.questions.forEach(q => {
          allQuestions.push({ ...q, type: 'sec_a', secRef: ex.section_a });
        });
      } else {
        wbCard.style.display = 'none';
      }

      // Section B
      if ((sec === 'all' || sec === 'sec_b') && ex.section_b) {
        ex.section_b.questions.forEach(q => {
          allQuestions.push({ ...q, type: 'sec_b', secRef: ex.section_b });
        });
      }

      // Section C1
      if ((sec === 'all' || sec === 'sec_c1') && ex.section_c1) {
        ex.section_c1.questions.forEach(q => {
          allQuestions.push({ ...q, type: 'sec_c1', secRef: ex.section_c1, secIdx: 1 });
        });
      }

      // Section C2
      if ((sec === 'all' || sec === 'sec_c2') && ex.section_c2) {
        ex.section_c2.questions.forEach(q => {
          allQuestions.push({ ...q, type: 'sec_c2', secRef: ex.section_c2, secIdx: 2 });
        });
      }

      document.getElementById('totalQuestionsCount').textContent = allQuestions.length;

      // Render Matrix & Question Cards
      allQuestions.forEach((q, index) => {
        const qNum = q.num;
        const userAnswer = (state.userAnswers[qNum] || '').trim().toUpperCase();
        const isAnswered = Boolean(userAnswer);
        const isFlagged = Boolean(state.flaggedQuestions[qNum]);
        const isSubmitted = isQuestionSubmitted(qNum);
        const isCorrect = isSubmitted && userAnswer === (q.answer || '').trim().toUpperCase();
        const isWrong = isSubmitted && isAnswered && !isCorrect;
        const isUnansweredSubmitted = isSubmitted && !isAnswered;

        // Matrix Item
        const mItem = document.createElement('div');
        mItem.className = `matrix-item ${isAnswered ? 'answered' : ''} ${isFlagged ? 'flagged' : ''} ${isCorrect ? 'correct' : ''} ${(isWrong || isUnansweredSubmitted) ? 'wrong' : ''}`;
        mItem.id = `matrix_q_${qNum}`;
        mItem.dataset.qnum = qNum;
        mItem.textContent = qNum;
        mItem.onclick = () => scrollToQuestion(qNum);
        matrix.appendChild(mItem);

        // Card Element
        const card = document.createElement('div');
        card.className = `question-card ${isFlagged ? 'flagged' : ''} ${isSubmitted ? 'is-submitted' : ''} ${isCorrect ? 'is-correct' : ''} ${(isWrong || isUnansweredSubmitted) ? 'is-wrong' : ''}`;
        card.id = `qcard_${qNum}`;
        card.dataset.qnum = qNum;

        if (q.type === 'sec_a') {
          card.innerHTML = renderSecAQuestionCard(q, userAnswer);
        } else if (q.type === 'sec_b') {
          card.innerHTML = renderSecBQuestionCard(q, userAnswer);
        } else {
          card.innerHTML = renderSecCQuestionCard(q, userAnswer, q.secIdx || 1, index);
        }

        container.appendChild(card);
      });

      updateAnsweredCount();
      renderSubmitBar();
    }

    function renderSecAQuestionCard(q, userAnswer) {
      const wb = q.secRef.word_bank || {};
      const currentWord = userAnswer ? wb[userAnswer] : '';
      const isFlagged = Boolean(state.flaggedQuestions[q.num]);
      const isSubmitted = isQuestionSubmitted(q.num);

      let resultBadgeHtml = '';
      if (isSubmitted) {
        if (userAnswer && userAnswer.toUpperCase() === (q.answer || '').toUpperCase()) {
          resultBadgeHtml = `<span class="badge" style="background:#ecfdf5; color:#059669; font-weight:700;">✓ 回答正确 (+3.55分)</span>`;
        } else if (userAnswer) {
          resultBadgeHtml = `<span class="badge" style="background:#fef2f2; color:#dc2626; font-weight:700;">✕ 错误 (你填: ${userAnswer} · 正确: ${q.answer})</span>`;
        } else {
          resultBadgeHtml = `<span class="badge" style="background:#fef3c7; color:#d97706; font-weight:700;">⚠️ 未填入 (正确: ${q.answer})</span>`;
        }
      }

      return `
        <div class="q-header">
          <div class="q-header-left">
            <span class="q-num-pill">第 ${q.num} 题 · 选词填空</span>
            ${resultBadgeHtml}
            <button class="btn-flag-review ${isFlagged ? 'active' : ''}" onclick="toggleFlagReview(${q.num})" title="标记为待复查题">
              ⭐ 待复查
            </button>
          </div>
          <div class="q-header-right">
            <button class="locate-para-btn" onclick="onBlankClick(${q.num})" title="定位到左侧文章对应空位">📍 定位空位</button>
          </div>
        </div>
        <div class="q-stem">
          请为第 [${q.num}] 处选入最契合文意的词汇：
          <span class="q-stem-ans" style="color: var(--primary); font-weight: 700; margin-left: 8px;">
            ${userAnswer ? `${userAnswer}) ${currentWord}` : '（未填）'}
          </span>
          ${userAnswer && !isSubmitted ? `<span style="font-size: 0.76rem; color: var(--danger); cursor: pointer; margin-left: 6px;" onclick="clearBlankAnswer(${q.num}, event)">[清空]</span>` : ''}
        </div>
        <div style="font-size: 0.82rem; color: var(--text-muted);">
          提示：点击上方备选词库即可快速填入本题，或在文章中直接点击空位。
        </div>
        ${renderExplanationBlock(q, `正确答案：${q.answer}) ${wb[q.answer] || ''}`)}
      `;
    }

    function renderSecBQuestionCard(q, userAnswer) {
      const paras = (q.secRef.paragraphs || []).map(p => p.label);
      const isFlagged = Boolean(state.flaggedQuestions[q.num]);
      const isSubmitted = isQuestionSubmitted(q.num);

      let badgesHtml = '';
      paras.forEach(label => {
        const isSel = userAnswer === label;
        const isRightMatch = isSubmitted && q.answer === label;
        const isWrongMatch = isSubmitted && isSel && q.answer !== label;
        badgesHtml += `
          <button class="para-badge-btn ${isSel ? 'selected' : ''} ${isRightMatch ? 'correct-match' : ''} ${isWrongMatch ? 'wrong-match' : ''}" 
            data-para="${label}"
            onmouseenter="previewParagraph('${label}')"
            onclick="selectAnswer(${q.num}, '${label}')">${label}</button>
        `;
      });

      let resultBadgeHtml = '';
      if (isSubmitted) {
        if (userAnswer && userAnswer.toUpperCase() === (q.answer || '').toUpperCase()) {
          resultBadgeHtml = `<span class="badge" style="background:#ecfdf5; color:#059669; font-weight:700;">✓ 回答正确 (+7.1分)</span>`;
        } else if (userAnswer) {
          resultBadgeHtml = `<span class="badge" style="background:#fef2f2; color:#dc2626; font-weight:700;">✕ 错误 (你选: ${userAnswer}段 · 正确: ${q.answer}段)</span>`;
        } else {
          resultBadgeHtml = `<span class="badge" style="background:#fef3c7; color:#d97706; font-weight:700;">⚠️ 未作答 (正确答案: ${q.answer}段)</span>`;
        }
      }

      return `
        <div class="q-header">
          <div class="q-header-left">
            <span class="q-num-pill">第 ${q.num} 题 · 段落信息匹配</span>
            ${resultBadgeHtml}
            <button class="btn-flag-review ${isFlagged ? 'active' : ''}" onclick="toggleFlagReview(${q.num})" title="标记为待复查题">
              ⭐ 待复查
            </button>
          </div>
          <div class="q-header-right">
            <button class="locate-para-btn" onclick="jumpToPara('para_${userAnswer || q.answer || 'A'}')" title="查看对应段落">
              🔍 查看段落
            </button>
          </div>
        </div>
        <div class="q-stem">${q.num}. ${q.stem}</div>
        <div class="para-select-grid">
          ${badgesHtml}
        </div>
        ${renderExplanationBlock(q, `对应段落：[${q.answer}] 段`)}
      `;
    }

    function renderSecCQuestionCard(q, userAnswer, secIdx, questionIndex) {
      const isFlagged = Boolean(state.flaggedQuestions[q.num]);
      const isSubmitted = isQuestionSubmitted(q.num);

      let optionsHtml = '';
      (q.options || []).forEach(opt => {
        const isChecked = userAnswer === opt.label;
        const isCorrectChoice = isSubmitted && q.answer === opt.label;
        const isWrongChoice = isSubmitted && isChecked && !isCorrectChoice;
        optionsHtml += `
          <label class="option-label ${isChecked ? 'selected' : ''} ${isCorrectChoice ? 'correct-choice' : ''} ${isWrongChoice ? 'wrong-choice' : ''}"
            onclick="selectAnswer(${q.num}, '${opt.label}')">
            <input type="radio" name="opt_${q.num}" value="${opt.label}" ${isChecked ? 'checked' : ''} ${isSubmitted ? 'disabled' : ''}>
            <span><strong>${opt.label})</strong> ${opt.text}</span>
          </label>
        `;
      });

      let resultBadgeHtml = '';
      if (isSubmitted) {
        if (userAnswer && userAnswer.toUpperCase() === (q.answer || '').toUpperCase()) {
          resultBadgeHtml = `<span class="badge" style="background:#ecfdf5; color:#059669; font-weight:700;">✓ 回答正确 (+14.2分)</span>`;
        } else if (userAnswer) {
          resultBadgeHtml = `<span class="badge" style="background:#fef2f2; color:#dc2626; font-weight:700;">✕ 错误 (你选: ${userAnswer} · 正确: ${q.answer})</span>`;
        } else {
          resultBadgeHtml = `<span class="badge" style="background:#fef3c7; color:#d97706; font-weight:700;">⚠️ 未作答 (正确答案: ${q.answer})</span>`;
        }
      }

      const baseNum = (secIdx === 1) ? 46 : 51;
      const paraTarget = Math.max(1, Math.min(5, (q.num - baseNum) + 1));

      return `
        <div class="q-header">
          <div class="q-header-left">
            <span class="q-num-pill">第 ${q.num} 题 · 仔细阅读</span>
            ${resultBadgeHtml}
            <button class="btn-flag-review ${isFlagged ? 'active' : ''}" onclick="toggleFlagReview(${q.num})" title="标记为待复查题">
              ⭐ 待复查
            </button>
          </div>
          <div class="q-header-right">
            <button class="locate-para-btn" onclick="locateParagraph('c${secIdx}', ${paraTarget})" title="在左侧文章定位第 ${paraTarget} 段">
              📍 原文定位 (第 ${paraTarget} 段)
            </button>
          </div>
        </div>
        <div class="q-stem">
          ${q.num}. ${q.stem}
          <div class="q-stem-zh">${q.question_zh || ''}</div>
        </div>
        <div class="options-group">
          ${optionsHtml}
        </div>
        ${renderExplanationBlock(q, `正确答案：${q.answer} 项`)}
      `;
    }

    function renderExplanationBlock(q, answerSummary) {
      const isSubmitted = isQuestionSubmitted(q.num);
      return `
        <div class="explanation-box ${isSubmitted ? 'is-visible' : ''}" id="expl_${q.num}">
          <div class="expl-tag">${answerSummary}</div>
          <div><strong>【考点定位与精析】：</strong>${q.explanation || q.analysis || '详见真题考点分析'}</div>
          ${q.answer_zh ? `<div style="margin-top: 4px; color: var(--text-sub);"><strong>【答案释义】：</strong>${q.answer_zh}</div>` : ''}
        </div>
      `;
    }

    /* ==========================================================================
       Interaction & Non-Destructive Answering
       ========================================================================== */
    function onBlankClick(bNum) {
      state.activeBlank = bNum;
      state.focusedQuestionNum = bNum;
      document.querySelectorAll('.passage-blank').forEach(b => b.classList.remove('active-blank'));
      const target = document.querySelector(`.passage-blank[data-bnum="${bNum}"]`);
      if (target) target.classList.add('active-blank');

      scrollToQuestion(bNum);
    }

    function clearBlankAnswer(bNum, event) {
      if (event) event.stopPropagation();
      delete state.userAnswers[bNum];
      saveExamProgress();

      // Update blank in reader
      const blankSpan = document.querySelector(`.passage-blank[data-bnum="${bNum}"]`);
      if (blankSpan) {
        blankSpan.textContent = `[${bNum}] ______`;
        blankSpan.classList.remove('filled');
      }

      // Update card stem
      const card = document.getElementById(`qcard_${bNum}`);
      if (card) {
        const stemAns = card.querySelector('.q-stem-ans');
        if (stemAns) {
          stemAns.textContent = '（未填）';
          stemAns.style.color = 'var(--text-muted)';
        }
      }

      // Update word chips
      renderWordChipsStatus();

      // Update matrix
      const matrixItem = document.getElementById(`matrix_q_${bNum}`);
      if (matrixItem) matrixItem.classList.remove('answered');

      updateAnsweredCount();
    }

    function onWordChipClick(letter, word) {
      if (!state.activeBlank) {
        const exams = getFilteredExams();
        const ex = exams[state.currentExamIndex];
        if (ex && ex.section_a) {
          for (let q of ex.section_a.questions) {
            if (!state.userAnswers[q.num]) {
              state.activeBlank = q.num;
              break;
            }
          }
        }
      }

      if (!state.activeBlank) {
        alert('请先在文章中点击需要填入的空位 [26]..[35]');
        return;
      }

      selectAnswer(state.activeBlank, letter);

      // Auto advance to next unfilled blank
      const exams = getFilteredExams();
      const ex = exams[state.currentExamIndex];
      let nextBlank = null;
      if (ex && ex.section_a) {
        for (let q of ex.section_a.questions) {
          if (!state.userAnswers[q.num]) {
            nextBlank = q.num;
            break;
          }
        }
      }
      state.activeBlank = nextBlank;
      document.querySelectorAll('.passage-blank').forEach(b => {
        b.classList.toggle('active-blank', b.dataset.bnum == nextBlank);
      });
    }

    function selectAnswer(qNum, answerVal) {
      if (isQuestionSubmitted(qNum)) return;
      state.userAnswers[qNum] = answerVal;
      state.focusedQuestionNum = qNum;
      saveExamProgress();

      // 1. In-place DOM update of question card
      const card = document.getElementById(`qcard_${qNum}`);
      if (card) {
        card.querySelectorAll('.option-label').forEach(lbl => {
          const radio = lbl.querySelector('input[type="radio"]');
          if (radio && radio.value === answerVal) {
            lbl.classList.add('selected');
            radio.checked = true;
          } else if (radio) {
            lbl.classList.remove('selected');
            radio.checked = false;
          }
        });

        card.querySelectorAll('.para-badge-btn').forEach(btn => {
          btn.classList.toggle('selected', btn.dataset.para === answerVal);
        });

        const stemAns = card.querySelector('.q-stem-ans');
        if (stemAns) {
          const exams = getFilteredExams();
          const ex = exams[state.currentExamIndex];
          const wb = (ex && ex.section_a && ex.section_a.word_bank) || {};
          stemAns.textContent = `${answerVal}) ${wb[answerVal] || ''}`;
          stemAns.style.color = 'var(--primary)';
        }
      }

      // 2. In-place DOM update of Section A blank
      const blankSpan = document.querySelector(`.passage-blank[data-bnum="${qNum}"]`);
      if (blankSpan) {
        const exams = getFilteredExams();
        const ex = exams[state.currentExamIndex];
        const wb = (ex && ex.section_a && ex.section_a.word_bank) || {};
        const wordText = wb[answerVal] || '';
        blankSpan.innerHTML = `[${qNum}] ${wordText}<span class="blank-clear-btn" onclick="clearBlankAnswer(${qNum}, event)" title="清空此题">✕</span>`;
        blankSpan.classList.add('filled');
      }

      renderWordChipsStatus();

      // 3. Update Matrix Item
      const matrixItem = document.getElementById(`matrix_q_${qNum}`);
      if (matrixItem) {
        matrixItem.classList.add('answered');
      }

      updateAnsweredCount();
    }

    function renderWordChipsStatus() {
      document.querySelectorAll('#wordChipsContainer .word-chip').forEach(chip => {
        const letter = chip.dataset.letter;
        const isUsed = Object.values(state.userAnswers).includes(letter);
        const usedInQ = isUsed ? Object.keys(state.userAnswers).find(k => state.userAnswers[k] === letter) : '';
        chip.classList.toggle('used', isUsed);
        
        let badge = chip.querySelector('.used-badge');
        if (isUsed) {
          if (!badge) {
            badge = document.createElement('span');
            badge.className = 'used-badge';
            chip.appendChild(badge);
          }
          badge.textContent = `[${usedInQ}]`;
        } else if (badge) {
          badge.remove();
        }
      });
    }

    function toggleFlagReview(qNum) {
      state.flaggedQuestions[qNum] = !state.flaggedQuestions[qNum];
      saveExamProgress();

      const card = document.getElementById(`qcard_${qNum}`);
      if (card) {
        card.classList.toggle('flagged', Boolean(state.flaggedQuestions[qNum]));
        const btn = card.querySelector('.btn-flag-review');
        if (btn) btn.classList.toggle('active', Boolean(state.flaggedQuestions[qNum]));
      }

      const mItem = document.getElementById(`matrix_q_${qNum}`);
      if (mItem) {
        mItem.classList.toggle('flagged', Boolean(state.flaggedQuestions[qNum]));
      }

      updateAnsweredCount();
    }

    function previewParagraph(label) {
      const el = document.getElementById(`para_${label}`);
      if (el) {
        el.classList.add('evidence-highlight');
        setTimeout(() => el.classList.remove('evidence-highlight'), 1200);
      }
    }

    function scrollToQuestion(qNum) {
      state.focusedQuestionNum = qNum;
      const card = document.getElementById(`qcard_${qNum}`);
      if (card) {
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        card.classList.add('active-target');
        setTimeout(() => card.classList.remove('active-target'), 1500);
      } else {
        let targetSec = 'all';
        if (qNum >= 26 && qNum <= 35) targetSec = 'sec_a';
        else if (qNum >= 36 && qNum <= 45) targetSec = 'sec_b';
        else if (qNum >= 46 && qNum <= 50) targetSec = 'sec_c1';
        else if (qNum >= 51 && qNum <= 55) targetSec = 'sec_c2';

        switchSection(targetSec);
        setTimeout(() => {
          const c = document.getElementById(`qcard_${qNum}`);
          if (c) {
            c.scrollIntoView({ behavior: 'smooth', block: 'center' });
            c.classList.add('active-target');
            setTimeout(() => c.classList.remove('active-target'), 1500);
          }
        }, 150);
      }
    }

    function updateAnsweredCount() {
      const answered = Object.keys(state.userAnswers).length;
      const countEl = document.getElementById('answeredCount');
      if (countEl) countEl.textContent = answered;

      const totalCount = parseInt(document.getElementById('totalQuestionsCount').textContent) || 30;
      const pct = Math.min(100, Math.round((answered / totalCount) * 100));
      const bar = document.getElementById('progressBarFill');
      if (bar) bar.style.width = `${pct}%`;

      const flagCount = Object.values(state.flaggedQuestions).filter(Boolean).length;
      const summaryEl = document.getElementById('matrixSummaryCounts');
      if (summaryEl) {
        summaryEl.textContent = `已作答: ${answered} · 待复查: ${flagCount}`;
      }
    }

    /* ==========================================================================
       Interactive Highlighting & Annotation Tool
       ========================================================================== */
    let currentTextRange = null;

    function initTextSelectionToolbar() {
      const reader = document.getElementById('paneReader');
      const toolbar = document.getElementById('textSelectionToolbar');

      document.addEventListener('selectionchange', () => {
        const sel = window.getSelection();
        if (!sel.isCollapsed && sel.toString().trim().length > 1) {
          const range = sel.getRangeAt(0);
          if (reader.contains(range.commonAncestorContainer)) {
            currentTextRange = range.cloneRange();
            const rect = range.getBoundingClientRect();
            toolbar.style.display = 'inline-flex';
            toolbar.style.top = `${rect.top - 44}px`;
            toolbar.style.left = `${Math.min(window.innerWidth - 300, Math.max(10, rect.left + rect.width / 2 - 140))}px`;
            return;
          }
        }
        if (toolbar.style.display !== 'none' && !toolbar.contains(document.activeElement)) {
          toolbar.style.display = 'none';
        }
      });
    }

    function applyUserHighlight(colorType) {
      if (!currentTextRange) return;
      const sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(currentTextRange);

      const mark = document.createElement('mark');
      mark.className = `user-hl-${colorType}`;
      
      try {
        currentTextRange.surroundContents(mark);
      } catch (err) {
        // Fallback for non-simple range
        const contents = currentTextRange.extractContents();
        mark.appendChild(contents);
        currentTextRange.insertNode(mark);
      }

      document.getElementById('textSelectionToolbar').style.display = 'none';
      saveHighlightsToStorage();
    }

    function clearUserHighlight() {
      if (!currentTextRange) return;
      const container = currentTextRange.commonAncestorContainer.parentElement;
      if (container && container.tagName === 'MARK') {
        const parent = container.parentNode;
        while (container.firstChild) parent.insertBefore(container.firstChild, container);
        parent.removeChild(container);
      }
      document.getElementById('textSelectionToolbar').style.display = 'none';
      saveHighlightsToStorage();
    }

    function speakSelectedText() {
      if (currentTextRange) {
        speakWord(currentTextRange.toString().trim());
      }
      document.getElementById('textSelectionToolbar').style.display = 'none';
    }

    function lookupSelectedText() {
      if (currentTextRange) {
        const text = currentTextRange.toString().trim();
        if (text) {
          showWordPopover(null, text, currentTextRange.getBoundingClientRect());
        }
      }
      document.getElementById('textSelectionToolbar').style.display = 'none';
    }

    function saveHighlightsToStorage() {
      const exams = getFilteredExams();
      if (!exams.length) return;
      const ex = exams[state.currentExamIndex];
      const readerHtml = document.getElementById('readerContainer').innerHTML;
      // Stored per exam & section
      localStorage.setItem(`cet6_hl_${ex.id}_${state.currentSection}`, readerHtml);
    }

    function restoreSavedHighlights() {
      const exams = getFilteredExams();
      if (!exams.length) return;
      const ex = exams[state.currentExamIndex];
      const savedHtml = localStorage.getItem(`cet6_hl_${ex.id}_${state.currentSection}`);
      if (savedHtml) {
        document.getElementById('readerContainer').innerHTML = savedHtml;
      }
    }

    /* ==========================================================================
       Modes (Mock Exam vs Deep Study)
       ========================================================================== */
    function toggleMode() {
      state.isStudyMode = !state.isStudyMode;
      const badge = document.getElementById('currentModeBadge');
      const icon = document.getElementById('modeIcon');
      const text = document.getElementById('modeText');

      if (state.isStudyMode) {
        document.body.classList.add('study-mode');
        badge.textContent = '📖 深度精读复盘模式';
        icon.textContent = '📖';
        text.textContent = '精读模式';
        document.getElementById('chkShowBilingual').checked = true;
        toggleBilingual(true);
      } else {
        document.body.classList.remove('study-mode');
        badge.textContent = '⚡ 全真模考刷题模式';
        icon.textContent = '⚡';
        text.textContent = '模考模式';
        document.getElementById('chkShowBilingual').checked = false;
        toggleBilingual(false);
      }
    }

    function toggleBilingual(checked) {
      state.showBilingual = checked;
      document.body.classList.toggle('show-bilingual', checked);
    }

    /* ==========================================================================
       Timer Management
       ========================================================================== */
    function startTimer() {
      if (state.timerInterval) clearInterval(state.timerInterval);
      state.timerRunning = true;
      state.timerInterval = setInterval(() => {
        if (state.timerSeconds > 0) {
          state.timerSeconds--;
          updateTimerDisplay();
          if (state.timerSeconds % 10 === 0) saveExamProgress();
        } else {
          clearInterval(state.timerInterval);
          state.timerRunning = false;
          alert('⏰ 40分钟模考时间到！系统正在为您核对试卷得分。');
          submitExam();
        }
      }, 1000);
    }

    function toggleTimer() {
      const btn = document.getElementById('btnTimerToggle');
      if (state.timerRunning) {
        clearInterval(state.timerInterval);
        state.timerRunning = false;
        btn.textContent = '继续';
      } else {
        startTimer();
        btn.textContent = '暂停';
      }
    }

    function resetTimer() {
      state.timerSeconds = 40 * 60;
      updateTimerDisplay();
      if (!state.timerRunning) startTimer();
    }

    function updateTimerDisplay() {
      const m = Math.floor(state.timerSeconds / 60);
      const s = state.timerSeconds % 60;
      document.getElementById('timerDisplay').textContent = 
        `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }

    /* ==========================================================================
       Single-Section & Full-Exam Submission & Scoring
       ========================================================================== */
    function submitCurrentSection(targetSec = null) {
      const secKey = targetSec || state.currentSection;
      if (secKey === 'all') {
        submitFullExam();
        return;
      }

      const exams = getFilteredExams();
      const ex = exams[state.currentExamIndex];
      if (!ex) return;

      let questions = [];
      let secName = '';
      let weightPerQ = 0;
      let maxScore = 0;

      if (secKey === 'sec_a' && ex.section_a) {
        questions = ex.section_a.questions;
        secName = '选词填空 (Section A)';
        weightPerQ = 3.55;
        maxScore = 35.5;
      } else if (secKey === 'sec_b' && ex.section_b) {
        questions = ex.section_b.questions;
        secName = '长篇阅读 · 段落匹配 (Section B)';
        weightPerQ = 7.1;
        maxScore = 71.0;
      } else if (secKey === 'sec_c1' && ex.section_c1) {
        questions = ex.section_c1.questions;
        secName = '仔细阅读 · 篇章一 (Passage One)';
        weightPerQ = 14.2;
        maxScore = 71.0;
      } else if (secKey === 'sec_c2' && ex.section_c2) {
        questions = ex.section_c2.questions;
        secName = '仔细阅读 · 篇章二 (Passage Two)';
        weightPerQ = 14.2;
        maxScore = 71.0;
      }

      if (!questions.length) {
        alert('当前模块暂无题目可提交！');
        return;
      }

      // Check unanswered questions in this section
      const unanswered = questions.filter(q => !state.userAnswers[q.num]);
      if (unanswered.length > 0 && !isSectionSubmitted(secKey)) {
        const confirmMsg = `本篇阅读共有 ${questions.length} 题，您还有 ${unanswered.length} 道题尚未作答（题号：${unanswered.map(q => q.num).join(', ')}）。\n\n确认现在提交本篇核对答案吗？（未作答题目将按错题计入本篇评分）`;
        if (!confirm(confirmMsg)) {
          return;
        }
      }

      // Mark ONLY this section as submitted
      state.submittedSections[secKey] = true;
      localStorage.setItem(`cet6_submitted_${ex.id}`, JSON.stringify(state.submittedSections));
      state.examSubmitted = ['sec_a', 'sec_b', 'sec_c1', 'sec_c2'].every(k => state.submittedSections[k]);

      // Calculate score for this section
      let correct = 0;
      let total = questions.length;
      let earnedScore = 0;

      questions.forEach(q => {
        const uAns = (state.userAnswers[q.num] || '').trim().toUpperCase();
        const rAns = (q.answer || '').trim().toUpperCase();
        if (uAns && uAns === rAns) {
          correct++;
          earnedScore += weightPerQ;
        } else {
          recordMistake(ex, secName, q);
        }
      });

      // Update question cards & matrix
      renderQuestions();
      updateAnsweredCount();
      renderSubmitBar();

      // Show Score Modal tailored specifically for THIS reading section
      const accuracy = total ? ((correct / total) * 100).toFixed(1) : '0.0';
      const timeSpentSec = (40 * 60) - state.timerSeconds;
      const timeSpentStr = `${Math.floor(timeSpentSec / 60)}分${timeSpentSec % 60}秒`;

      const headingEl = document.getElementById('modalScoreHeading');
      if (headingEl) headingEl.textContent = '单篇阅读作答报告';
      document.getElementById('modalExamTitle').textContent = `${ex.title} · ${secName}`;
      document.getElementById('modalScoreVal').textContent = earnedScore.toFixed(1);
      const scoreLabelEl = document.getElementById('modalScoreLabel');
      if (scoreLabelEl) {
        scoreLabelEl.textContent = `本篇折合分 (满分 ${maxScore.toFixed(1)} 分 · 共 ${total} 题)`;
      }
      document.getElementById('modalAccuracy').textContent = `${accuracy}%`;
      const accLabel = document.getElementById('modalAccuracyLabel');
      if (accLabel) accLabel.textContent = '本篇正确率';
      document.getElementById('modalCorrectCount').textContent = `${correct} / ${total}`;
      const cntLabel = document.getElementById('modalCountLabel');
      if (cntLabel) cntLabel.textContent = '答对题数';
      document.getElementById('modalTimeSpent').textContent = timeSpentStr;

      // Update modal action buttons
      const modalActions = document.getElementById('modalActionButtons');
      if (modalActions) {
        let nextBtnHtml = '';
        if (secKey === 'sec_a') {
          nextBtnHtml = `<button class="btn btn-primary" onclick="closeScoreModal(); switchSection('sec_b');">做下一节: 长篇匹配 B ▶</button>`;
        } else if (secKey === 'sec_b') {
          nextBtnHtml = `<button class="btn btn-primary" onclick="closeScoreModal(); switchSection('sec_c1');">做下一节: 仔细阅读 1 ▶</button>`;
        } else if (secKey === 'sec_c1') {
          nextBtnHtml = `<button class="btn btn-primary" onclick="closeScoreModal(); switchSection('sec_c2');">做下一篇: 仔细阅读 2 ▶</button>`;
        } else if (secKey === 'sec_c2') {
          nextBtnHtml = `<button class="btn btn-primary" onclick="closeScoreModal(); submitFullExam();">查看全卷总分报告 ➔</button>`;
        }

        modalActions.innerHTML = `
          <button class="btn btn-outline" onclick="closeScoreModal();">查看本篇解析与错题</button>
          <button class="btn btn-outline" onclick="closeScoreModal(); resetCurrentSection();">重做本篇</button>
          ${nextBtnHtml}
        `;
      }

      document.getElementById('scoreModal').style.display = 'flex';
    }

    function submitFullExam() {
      const exams = getFilteredExams();
      const ex = exams[state.currentExamIndex];
      if (!ex) return;

      state.submittedSections = { sec_a: true, sec_b: true, sec_c1: true, sec_c2: true };
      localStorage.setItem(`cet6_submitted_${ex.id}`, JSON.stringify(state.submittedSections));
      state.examSubmitted = true;
      document.body.classList.add('show-answers');
      clearInterval(state.timerInterval);

      let correct = 0;
      let total = 0;
      let weightedScore = 0;

      if (ex.section_a) {
        ex.section_a.questions.forEach(q => {
          total++;
          if ((state.userAnswers[q.num] || '').trim().toUpperCase() === (q.answer || '').trim().toUpperCase()) {
            correct++;
            weightedScore += 3.55;
          } else {
            recordMistake(ex, '选词填空 A', q);
          }
        });
      }

      if (ex.section_b) {
        ex.section_b.questions.forEach(q => {
          total++;
          if ((state.userAnswers[q.num] || '').trim().toUpperCase() === (q.answer || '').trim().toUpperCase()) {
            correct++;
            weightedScore += 7.1;
          } else {
            recordMistake(ex, '长篇匹配 B', q);
          }
        });
      }

      ['section_c1', 'section_c2'].forEach((secKey, idx) => {
        if (ex[secKey]) {
          ex[secKey].questions.forEach(q => {
            total++;
            if ((state.userAnswers[q.num] || '').trim().toUpperCase() === (q.answer || '').trim().toUpperCase()) {
              correct++;
              weightedScore += 14.2;
            } else {
              recordMistake(ex, idx === 0 ? '仔细阅读 1' : '仔细阅读 2', q);
            }
          });
        }
      });

      renderQuestions();
      updateAnsweredCount();
      renderSubmitBar();

      const accuracy = total ? ((correct / total) * 100).toFixed(1) : '0.0';
      const timeSpentSec = (40 * 60) - state.timerSeconds;
      const timeSpentStr = `${Math.floor(timeSpentSec / 60)}分${timeSpentSec % 60}秒`;

      const headingEl = document.getElementById('modalScoreHeading');
      if (headingEl) headingEl.textContent = '全套真题总成绩单';
      document.getElementById('modalExamTitle').textContent = `${ex.title} · 全卷总评`;
      document.getElementById('modalScoreVal').textContent = weightedScore.toFixed(1);
      const scoreLabelEl = document.getElementById('modalScoreLabel');
      if (scoreLabelEl) {
        scoreLabelEl.textContent = '六级标准分 (满分 248.5 分 · 全卷30题)';
      }
      document.getElementById('modalAccuracy').textContent = `${accuracy}%`;
      const accLabel = document.getElementById('modalAccuracyLabel');
      if (accLabel) accLabel.textContent = '综合正确率';
      document.getElementById('modalCorrectCount').textContent = `${correct} / ${total}`;
      const cntLabel = document.getElementById('modalCountLabel');
      if (cntLabel) cntLabel.textContent = '答对题数';
      document.getElementById('modalTimeSpent').textContent = timeSpentStr;

      const modalActions = document.getElementById('modalActionButtons');
      if (modalActions) {
        modalActions.innerHTML = `
          <button class="btn btn-outline" onclick="closeScoreModal()">关闭并复盘错题</button>
          <button class="btn btn-outline" onclick="closeScoreModal(); resetCurrentExam();">清空全卷重考</button>
          <button class="btn btn-primary" onclick="switchToStudyModeAndReview()">进入深度精读解析</button>
        `;
      }

      document.getElementById('scoreModal').style.display = 'flex';
    }

    function submitExam() {
      submitCurrentSection();
    }

    function resetCurrentSection() {
      const secKey = state.currentSection;
      if (secKey === 'all') {
        resetCurrentExam();
        return;
      }
      if (!confirm('确认清空当前这篇阅读的已选答案并重新作答吗？')) return;

      const exams = getFilteredExams();
      const ex = exams[state.currentExamIndex];
      if (!ex) return;

      let qNums = [];
      if (secKey === 'sec_a' && ex.section_a) qNums = ex.section_a.questions.map(q => q.num);
      else if (secKey === 'sec_b' && ex.section_b) qNums = ex.section_b.questions.map(q => q.num);
      else if (secKey === 'sec_c1' && ex.section_c1) qNums = ex.section_c1.questions.map(q => q.num);
      else if (secKey === 'sec_c2' && ex.section_c2) qNums = ex.section_c2.questions.map(q => q.num);

      qNums.forEach(num => {
        delete state.userAnswers[num];
        delete state.flaggedQuestions[num];
      });

      state.submittedSections[secKey] = false;
      state.examSubmitted = ['sec_a', 'sec_b', 'sec_c1', 'sec_c2'].every(k => state.submittedSections[k]);
      localStorage.setItem(`cet6_answers_${ex.id}`, JSON.stringify(state.userAnswers));
      localStorage.setItem(`cet6_flags_${ex.id}`, JSON.stringify(state.flaggedQuestions));
      localStorage.setItem(`cet6_submitted_${ex.id}`, JSON.stringify(state.submittedSections));

      renderQuestions();
      updateAnsweredCount();
      renderSubmitBar();
    }

    function renderSubmitBar() {
      const bar = document.getElementById('submitBar');
      if (!bar) return;

      const sec = state.currentSection;
      const isSub = isSectionSubmitted(sec);

      let secTitle = '本篇阅读';
      let qRange = '';
      if (sec === 'sec_a') { secTitle = '选词填空 A'; qRange = 'Q26-Q35'; }
      else if (sec === 'sec_b') { secTitle = '长篇匹配 B'; qRange = 'Q36-Q45'; }
      else if (sec === 'sec_c1') { secTitle = '仔细阅读篇章一'; qRange = 'Q46-Q50'; }
      else if (sec === 'sec_c2') { secTitle = '仔细阅读篇章二'; qRange = 'Q51-Q55'; }
      else { secTitle = '整卷全部题目'; qRange = 'Q26-Q55'; }

      if (sec === 'all') {
        bar.innerHTML = `
          <div style="font-size: 0.82rem; color: var(--text-muted);">
            答题进度实时本地保存 · 全卷 30 题满分 248.5 分
          </div>
          <div style="display: flex; gap: 8px; align-items: center;">
            <button class="btn btn-outline" onclick="resetCurrentExam()">清空全卷重考</button>
            <button class="btn btn-primary" onclick="submitFullExam()">📝 提交整卷并核对答案 (30题)</button>
          </div>
        `;
      } else {
        if (isSub) {
          bar.innerHTML = `
            <div style="font-size: 0.82rem; color: #059669; font-weight: 600;">
              ✓ ${secTitle}已提交评分，解析已展开
            </div>
            <div style="display: flex; gap: 8px; align-items: center;">
              <button class="btn btn-outline" onclick="resetCurrentSection()">重做本篇</button>
              <button class="btn btn-primary" onclick="submitCurrentSection()">查看本篇得分报告</button>
            </div>
          `;
        } else {
          bar.innerHTML = `
            <div style="font-size: 0.82rem; color: var(--text-muted);">
              单篇即做即评 · 仅提交当前<strong>${secTitle}</strong> (${qRange})
            </div>
            <div style="display: flex; gap: 8px; align-items: center;">
              <button class="btn btn-outline" onclick="resetCurrentSection()" title="清空本篇已选答案">重做本篇</button>
              <button class="btn btn-primary" onclick="submitCurrentSection()" style="font-size: 0.88rem; font-weight: 700; padding: 6px 14px;">
                📝 提交本篇并核对答案 (${qRange})
              </button>
              <button class="btn btn-outline" onclick="submitFullExam()" title="如果整套做完，可直接一键交全卷" style="font-size: 0.74rem; padding: 4px 8px; color: var(--text-muted);">
                交整卷
              </button>
            </div>
          `;
        }
      }
    }

    function closeScoreModal() {
      document.getElementById('scoreModal').style.display = 'none';
    }

    function switchToStudyModeAndReview() {
      closeScoreModal();
      if (!state.isStudyMode) toggleMode();
      scrollToQuestion(Object.keys(state.userAnswers)[0] || 46);
    }

    function resetCurrentExam() {
      if (confirm('确认清空整套试卷的所有作答记录并重新开始吗？')) {
        const exams = getFilteredExams();
        const ex = exams[state.currentExamIndex];
        if (ex) {
          localStorage.removeItem(`cet6_answers_${ex.id}`);
          localStorage.removeItem(`cet6_flags_${ex.id}`);
          localStorage.removeItem(`cet6_time_${ex.id}`);
          localStorage.removeItem(`cet6_submitted_${ex.id}`);
          localStorage.removeItem(`cet6_hl_${ex.id}_${state.currentSection}`);
        }
        loadCurrentExam();
      }
    }

    /* ==========================================================================
       Mistakes & Vocab Notebooks
       ========================================================================== */
    function recordMistake(ex, secType, q) {
      const key = `${ex.id}_${q.num}`;
      const exists = state.mistakes.some(m => m.key === key);
      if (!exists) {
        state.mistakes.unshift({
          key,
          examId: ex.id,
          examTitle: ex.title,
          secType,
          qNum: q.num,
          stem: q.stem || `第 [${q.num}] 处选词填空`,
          correctAnswer: q.answer,
          userAnswer: state.userAnswers[q.num] || '未答',
          explanation: q.explanation || q.analysis || '详见真题考点分析',
          date: new Date().toLocaleDateString()
        });
        localStorage.setItem('cet6_mistakes', JSON.stringify(state.mistakes));
        updateBadgeCounts();
      }
    }

    function updateBadgeCounts() {
      document.getElementById('mistakeBadge').textContent = state.mistakes.length;
      document.getElementById('vocabBadge').textContent = state.vocab.length;
    }

    function openDrawer(type) {
      document.getElementById('drawerOverlay').style.display = 'block';
      if (type === 'mistakes') {
        renderMistakes();
        document.getElementById('mistakesDrawer').classList.add('open');
      } else if (type === 'vocab') {
        renderVocab();
        document.getElementById('vocabDrawer').classList.add('open');
      } else if (type === 'strategy') {
        document.getElementById('strategyDrawer').classList.add('open');
      }
    }

    function closeAllDrawers() {
      document.getElementById('drawerOverlay').style.display = 'none';
      document.querySelectorAll('.drawer').forEach(d => d.classList.remove('open'));
    }

    function renderMistakes() {
      const container = document.getElementById('mistakesListContainer');
      document.getElementById('drawerMistakeCount').textContent = state.mistakes.length;
      if (!state.mistakes.length) {
        container.innerHTML = '<div style="text-align: center; color: var(--text-muted); padding: 40px 0;">错题本空空如也，继续保持！</div>';
        return;
      }

      container.innerHTML = state.mistakes.map(m => `
        <div style="background: var(--bg-subtle); padding: 12px; border-radius: var(--radius-md); border-left: 3px solid var(--danger);">
          <div style="font-size: 0.76rem; color: var(--text-muted); display: flex; justify-content: space-between; margin-bottom: 4px;">
            <span>${m.examTitle}</span>
            <span>${m.date}</span>
          </div>
          <div style="font-weight: 700; font-size: 0.86rem; margin-bottom: 6px;">第 ${m.qNum} 题 · ${m.secType}</div>
          <div style="font-size: 0.82rem; margin-bottom: 6px;">${m.stem}</div>
          <div style="display: flex; gap: 12px; font-size: 0.8rem; margin-bottom: 6px;">
            <span style="color: var(--danger);">你的作答: ${m.userAnswer}</span>
            <span style="color: var(--success); font-weight: 700;">正确答案: ${m.correctAnswer}</span>
          </div>
          <div style="font-size: 0.78rem; color: var(--text-sub); line-height: 1.45;"><strong>解析:</strong> ${m.explanation}</div>
          <div style="display: flex; justify-content: flex-end; margin-top: 8px;">
            <button class="btn" style="padding: 2px 6px; font-size: 0.72rem;" onclick="removeMistake('${m.key}')">移出错题本</button>
          </div>
        </div>
      `).join('');
    }

    function removeMistake(key) {
      state.mistakes = state.mistakes.filter(m => m.key !== key);
      localStorage.setItem('cet6_mistakes', JSON.stringify(state.mistakes));
      renderMistakes();
      updateBadgeCounts();
    }

    function renderVocab() {
      const container = document.getElementById('vocabListContainer');
      document.getElementById('drawerVocabCount').textContent = state.vocab.length;
      if (!state.vocab.length) {
        container.innerHTML = '<div style="text-align: center; color: var(--text-muted); padding: 40px 0;">生词本暂无词汇，阅读文章点击任意生词即可加入！</div>';
        return;
      }

      container.innerHTML = state.vocab.map(item => `
        <div style="background: var(--bg-subtle); padding: 10px 12px; border-radius: var(--radius-md); display: flex; align-items: center; justify-content: space-between;">
          <div>
            <div style="font-weight: 700; font-size: 0.92rem; color: var(--primary); display: flex; align-items: center; gap: 6px;">
              <span>${item.w}</span>
              <span style="font-size: 0.75rem; font-weight: normal; color: var(--text-muted);">${item.p || ''}</span>
              <button class="btn" style="padding: 1px 4px; font-size: 0.68rem;" onclick="speakWord('${item.w}')">🔊</button>
            </div>
            <div style="font-size: 0.8rem; color: var(--text-sub); margin-top: 2px;">${item.t || '六级大纲词汇'}</div>
          </div>
          <button class="btn btn-outline" style="padding: 2px 6px; font-size: 0.72rem;" onclick="removeVocab('${item.w}')">✕</button>
        </div>
      `).join('');
    }

    function addCurrentWordToVocab() {
      if (!state.currentPopoverWord) return;
      const w = state.currentPopoverWord;
      const clean = (w.clean || w.w).toLowerCase();
      const exists = state.vocab.some(item => (item.clean || item.w).toLowerCase() === clean);
      const btn = document.getElementById('btnAddToVocab');
      if (!exists) {
        state.vocab.unshift({
          w: w.w,
          clean: clean,
          p: w.p || '',
          t: w.t || '',
          date: new Date().toLocaleDateString('zh-CN')
        });
        localStorage.setItem('cet6_vocab', JSON.stringify(state.vocab));
        updateBadgeCounts();
        if (btn) {
          btn.textContent = '✓ 已存入生词本';
          btn.disabled = true;
        }
      } else {
        if (btn) {
          btn.textContent = '✓ 已在生词本';
          btn.disabled = true;
        }
      }
    }

    function removeVocab(word) {
      state.vocab = state.vocab.filter(item => item.w !== word && item.clean !== word);
      localStorage.setItem('cet6_vocab', JSON.stringify(state.vocab));
      renderVocab();
      updateBadgeCounts();
      const btn = document.getElementById('btnAddToVocab');
      if (btn && state.currentPopoverWord && (state.currentPopoverWord.w === word || state.currentPopoverWord.clean === word)) {
        btn.textContent = '⭐ 存入生词本';
        btn.disabled = false;
      }
    }

    function exportVocabTxt() {
      if (!state.vocab.length) {
        alert('生词本为空，无法导出！');
        return;
      }
      const text = state.vocab.map(item => `${item.w}  [${item.p || ''}]  ${item.t || ''}`).join('\\n');
      const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `CET6_Reading_Vocabulary_${new Date().toISOString().slice(0, 10)}.txt`;
      a.click();
    }

    /* ==========================================================================
       Offline Dictionary Popover & Smart Stemming Engine
       ========================================================================== */
    const IRREGULAR_VERBS_NOUNS = {
      'children': 'child', 'men': 'man', 'women': 'woman', 'people': 'person',
      'feet': 'foot', 'teeth': 'tooth', 'geese': 'goose', 'mice': 'mouse',
      'better': 'good', 'best': 'good', 'worse': 'bad', 'worst': 'bad',
      'went': 'go', 'gone': 'go', 'ran': 'run', 'saw': 'see', 'seen': 'see',
      'came': 'come', 'taken': 'take', 'took': 'take', 'gave': 'give', 'given': 'give',
      'made': 'make', 'found': 'find', 'knew': 'know', 'known': 'know',
      'thought': 'think', 'told': 'tell', 'became': 'become', 'shown': 'show',
      'left': 'leave', 'felt': 'feel', 'brought': 'bring', 'began': 'begin', 'begun': 'begin',
      'kept': 'keep', 'held': 'hold', 'wrote': 'write', 'written': 'write',
      'stood': 'stand', 'heard': 'hear', 'let': 'let', 'meant': 'mean',
      'set': 'set', 'met': 'meet', 'paid': 'pay', 'sat': 'sit',
      'spoke': 'speak', 'spoken': 'speak', 'lain': 'lie', 'laid': 'lay',
      'led': 'lead', 'grew': 'grow', 'grown': 'grow',
      'lost': 'lose', 'fell': 'fall', 'fallen': 'fall', 'sent': 'send',
      'built': 'build', 'understood': 'understand', 'drew': 'draw', 'drawn': 'draw',
      'broke': 'break', 'broken': 'break', 'spent': 'spend',
      'rose': 'rise', 'risen': 'rise', 'drove': 'drive', 'driven': 'drive',
      'bought': 'buy', 'wore': 'wear', 'worn': 'wear', 'chose': 'choose', 'chosen': 'choose'
    };

    function lookupWord(rawWord) {
      if (!rawWord) return null;
      let w = rawWord.toLowerCase().replace(/^[^a-z]+|[^a-z]+$/g, '');
      if (!w) return null;

      // Strip trailing 's (e.g. woman's -> woman)
      w = w.replace(/'s$/, '');

      // 1. Direct exact lookup
      if (window.CET6_DICT && window.CET6_DICT[w]) {
        return { matchedWord: w, rootWord: w, isStemmed: false, ...window.CET6_DICT[w] };
      }

      // 2. Irregular mappings (e.g. children -> child)
      if (IRREGULAR_VERBS_NOUNS[w] && window.CET6_DICT && window.CET6_DICT[IRREGULAR_VERBS_NOUNS[w]]) {
        const root = IRREGULAR_VERBS_NOUNS[w];
        return { matchedWord: root, rootWord: root, isStemmed: true, ...window.CET6_DICT[root] };
      }

      // 3. Suffix reduction & stemming candidates
      const candidates = [];
      if (w.endsWith('ies') && w.length > 4) candidates.push({ root: w.slice(0, -3) + 'y', desc: '复数/单三原形' });
      if (w.endsWith('ied') && w.length > 4) candidates.push({ root: w.slice(0, -3) + 'y', desc: '过去式原形' });
      if (w.endsWith('es') && w.length > 3) {
        candidates.push({ root: w.slice(0, -2), desc: '原形' });
        candidates.push({ root: w.slice(0, -1), desc: '原形' });
      }
      if (w.endsWith('s') && !w.endsWith('ss') && w.length > 3) {
        candidates.push({ root: w.slice(0, -1), desc: '单数原形' });
      }
      if (w.endsWith('ing') && w.length > 4) {
        candidates.push({ root: w.slice(0, -3), desc: '动词原形' });
        candidates.push({ root: w.slice(0, -3) + 'e', desc: '动词原形' });
        if (w.length > 5 && w[w.length - 4] === w[w.length - 5]) {
          candidates.push({ root: w.slice(0, -4), desc: '动词原形' });
        }
      }
      if (w.endsWith('ed') && w.length > 4) {
        candidates.push({ root: w.slice(0, -2), desc: '动词原形' });
        candidates.push({ root: w.slice(0, -1), desc: '动词原形' });
        if (w.length > 5 && w[w.length - 3] === w[w.length - 4]) {
          candidates.push({ root: w.slice(0, -3), desc: '动词原形' });
        }
      }
      if (w.endsWith('ily') && w.length > 4) candidates.push({ root: w.slice(0, -3) + 'y', desc: '形容词原形' });
      if (w.endsWith('ly') && w.length > 4) candidates.push({ root: w.slice(0, -2), desc: '形容词原形' });
      if (w.endsWith('er') && w.length > 4) {
        candidates.push({ root: w.slice(0, -2), desc: '比较级原形' });
        candidates.push({ root: w.slice(0, -1), desc: '比较级原形' });
      }
      if (w.endsWith('est') && w.length > 4) {
        candidates.push({ root: w.slice(0, -3), desc: '最高级原形' });
        candidates.push({ root: w.slice(0, -2), desc: '最高级原形' });
      }

      for (const item of candidates) {
        if (window.CET6_DICT && window.CET6_DICT[item.root]) {
          return {
            matchedWord: item.root,
            rootWord: item.root,
            stemDesc: item.desc,
            isStemmed: true,
            ...window.CET6_DICT[item.root]
          };
        }
      }

      return null;
    }

    function wrapWordsWithTokens() {
      const container = document.getElementById('readerContainer');
      if (!container) return;
      const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
      const textNodes = [];
      while (walker.nextNode()) {
        const node = walker.currentNode;
        if (node.parentElement && 
            !node.parentElement.classList.contains('word-token') &&
            !node.parentElement.classList.contains('para-marker') && 
            !node.parentElement.classList.contains('passage-blank') &&
            !node.parentElement.classList.contains('p-jump-pill') &&
            !node.parentElement.classList.contains('btn') &&
            !node.parentElement.classList.contains('para-zh-trans') &&
            !node.parentElement.closest('.para-zh-trans')) {
          textNodes.push(node);
        }
      }

      textNodes.forEach(node => {
        const text = node.nodeValue;
        if (!/[a-zA-Z]/.test(text)) return;
        const frag = document.createDocumentFragment();
        const regex = /([a-zA-Z]+(?:'[a-zA-Z]+)?)/g;
        let lastIdx = 0;
        let match;
        while ((match = regex.exec(text)) !== null) {
          if (match.index > lastIdx) {
            frag.appendChild(document.createTextNode(text.substring(lastIdx, match.index)));
          }
          const span = document.createElement('span');
          span.className = 'word-token';
          span.dataset.word = match[1];
          span.textContent = match[1];
          frag.appendChild(span);
          lastIdx = regex.lastIndex;
        }
        if (lastIdx < text.length) {
          frag.appendChild(document.createTextNode(text.substring(lastIdx)));
        }
        node.parentElement.replaceChild(frag, node);
      });
    }

    function showWordPopover(anchorEl, rawWord, fallbackRect = null) {
      if (!rawWord) return;
      const popover = document.getElementById('dictPopover');
      if (!popover) return;

      document.querySelectorAll('.word-token.active-word').forEach(el => el.classList.remove('active-word'));
      if (anchorEl) anchorEl.classList.add('active-word');

      const cleanWord = rawWord.toLowerCase().replace(/^[^a-z]+|[^a-z]+$/g, '').replace(/'s$/, '');
      if (!cleanWord) return;

      const res = lookupWord(cleanWord);

      state.currentPopoverWord = {
        w: rawWord,
        clean: cleanWord,
        p: res ? res.p : '',
        t: res ? res.t : ''
      };

      document.getElementById('dictWordText').textContent = rawWord;
      document.getElementById('dictPhonetic').textContent = res && res.p ? `/${res.p}/` : '';

      const rootHint = document.getElementById('dictRootHint');
      if (res && res.isStemmed && res.rootWord && res.rootWord !== cleanWord) {
        rootHint.style.display = 'inline-block';
        document.getElementById('dictRootText').textContent = `${res.rootWord} (${res.stemDesc || '原形'})`;
      } else {
        rootHint.style.display = 'none';
      }

      const transEl = document.getElementById('dictTrans');
      const vocabBtn = document.getElementById('btnAddToVocab');
      vocabBtn.textContent = '⭐ 存入生词本';
      vocabBtn.disabled = false;

      if (res && res.t) {
        const parts = res.t.split(/\\s*\\|\\s*|\\s*;\\s*/).filter(Boolean);
        if (parts.length > 1) {
          transEl.innerHTML = parts.map(p => `<div class="dict-trans-line">• ${p}</div>`).join('');
        } else {
          transEl.textContent = res.t;
        }
      } else {
        transEl.innerHTML = '<span style="color: var(--text-muted);">正在检索中文释义...</span>';
        fetchOnlineDefinition(cleanWord, rawWord);
      }

      if (state.vocab && state.vocab.some(item => (item.clean || item.w).toLowerCase() === cleanWord)) {
        vocabBtn.textContent = '✓ 已在生词本';
        vocabBtn.disabled = true;
      }

      const rect = anchorEl ? anchorEl.getBoundingClientRect() : fallbackRect;
      if (!rect) return;

      popover.style.display = 'block';
      const popWidth = 330;
      let left = rect.left + (rect.width / 2) - 30;
      if (left + popWidth > window.innerWidth - 14) {
        left = window.innerWidth - popWidth - 14;
      }
      if (left < 14) left = 14;
      popover.style.left = `${left}px`;

      const arrowLeft = Math.max(16, Math.min(popWidth - 24, rect.left + (rect.width / 2) - left - 5));
      popover.style.setProperty('--arrow-left', `${arrowLeft}px`);

      const popHeight = popover.offsetHeight || 160;
      const spaceBelow = window.innerHeight - rect.bottom;
      if (spaceBelow < popHeight + 16 && rect.top > popHeight + 16) {
        popover.classList.add('popover-above');
        popover.style.top = `${rect.top - popHeight - 10}px`;
      } else {
        popover.classList.remove('popover-above');
        popover.style.top = `${rect.bottom + 8}px`;
      }
    }

    function fetchOnlineDefinition(cleanWord, rawWord) {
      fetch(`https://dict.youdao.com/suggest?num=1&doctype=json&q=${encodeURIComponent(cleanWord)}`)
        .then(r => r.json())
        .then(data => {
          const entries = data?.data?.entries;
          if (entries && entries.length > 0 && entries[0].explain) {
            const exp = entries[0].explain;
            if (state.currentPopoverWord && state.currentPopoverWord.clean === cleanWord) {
              document.getElementById('dictTrans').textContent = exp;
              state.currentPopoverWord.t = exp;
              if (window.CET6_DICT) {
                window.CET6_DICT[cleanWord] = { p: '', t: exp };
              }
            }
          } else {
            if (state.currentPopoverWord && state.currentPopoverWord.clean === cleanWord) {
              document.getElementById('dictTrans').textContent = '六级真题阅读高频语篇词汇';
            }
          }
        })
        .catch(() => {
          if (state.currentPopoverWord && state.currentPopoverWord.clean === cleanWord) {
            document.getElementById('dictTrans').textContent = '六级真题阅读核心词汇';
          }
        });
    }

    function closeDictPopover() {
      const popover = document.getElementById('dictPopover');
      if (popover) popover.style.display = 'none';
      document.querySelectorAll('.word-token.active-word').forEach(el => el.classList.remove('active-word'));
    }

    function initWordClickListeners() {
      const reader = document.getElementById('paneReader');

      if (reader) {
        reader.addEventListener('click', (e) => {
          const token = e.target.closest('.word-token');
          if (token) {
            const rawWord = token.dataset.word || token.textContent;
            showWordPopover(token, rawWord);
            e.stopPropagation();
          } else if (!e.target.closest('.dict-popover') && !e.target.closest('#textSelectionToolbar')) {
            closeDictPopover();
          }
        });
      }

      const questionsPane = document.getElementById('paneConsole');
      if (questionsPane) {
        questionsPane.addEventListener('click', (e) => {
          const token = e.target.closest('.word-token');
          if (token) {
            const rawWord = token.dataset.word || token.textContent;
            showWordPopover(token, rawWord);
            e.stopPropagation();
          } else if (!e.target.closest('.dict-popover')) {
            closeDictPopover();
          }
        });
      }

      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          closeDictPopover();
        }
      });
    }

    function speakCurrentWord() {
      if (state.currentPopoverWord) {
        speakWord(state.currentPopoverWord.w);
      }
    }

    function speakWord(text) {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const u = new SpeechSynthesisUtterance(text);
        u.lang = 'en-US';
        u.rate = 0.9;
        window.speechSynthesis.speak(u);
      }
    }

    /* ==========================================================================
       Themes & Reader Typography
       ========================================================================== */
    const THEMES = ['light', 'sepia', 'dark'];
    function cycleTheme() {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = THEMES[(THEMES.indexOf(current) + 1) % THEMES.length];
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('cet6_reading_theme', next);
      updateThemeDisplay(next);
    }

    function loadTheme() {
      const saved = localStorage.getItem('cet6_reading_theme') || 'light';
      document.documentElement.setAttribute('data-theme', saved);
      updateThemeDisplay(saved);
    }

    function updateThemeDisplay(theme) {
      const icon = document.getElementById('themeIcon');
      const name = document.getElementById('themeName');
      if (theme === 'light') {
        icon.textContent = '☀️';
        name.textContent = '浅色';
      } else if (theme === 'sepia') {
        icon.textContent = '📜';
        name.textContent = '羊皮纸';
      } else {
        icon.textContent = '🌙';
        name.textContent = '深色';
      }
    }

    function adjustFontSize(delta) {
      state.fontSize = Math.max(14, Math.min(24, state.fontSize + delta));
      applyReaderStyles();
    }

    function toggleReaderFont() {
      state.isSerifFont = !state.isSerifFont;
      applyReaderStyles();
    }

    function applyReaderStyles() {
      const contents = document.querySelectorAll('.passage-content');
      contents.forEach(el => {
        el.style.fontSize = `${state.fontSize}px`;
        el.style.fontFamily = state.isSerifFont ? 'var(--reader-font)' : 'var(--body-font)';
      });
    }

    /* ==========================================================================
       Split Resizer
       ========================================================================== */
    function initResizer() {
      const resizer = document.getElementById('paneResizer');
      const leftPane = document.getElementById('paneReader');
      let isDragging = false;

      resizer.addEventListener('mousedown', (e) => {
        isDragging = true;
        resizer.classList.add('dragging');
        document.body.style.cursor = (state.layoutMode === 'stacked') ? 'row-resize' : 'col-resize';
        document.body.style.userSelect = 'none';
      });

      document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        if (state.layoutMode === 'split') {
          const workspace = document.getElementById('appWorkspace');
          const offsetLeft = workspace.offsetLeft;
          const newWidth = e.clientX - offsetLeft;
          if (newWidth > 240 && newWidth < workspace.clientWidth - 280) {
            leftPane.style.flex = 'none';
            leftPane.style.width = `${newWidth}px`;
          }
        } else if (state.layoutMode === 'stacked') {
          const workspace = document.getElementById('appWorkspace');
          const offsetTop = workspace.offsetTop;
          const newHeight = e.clientY - offsetTop;
          if (newHeight > 150 && newHeight < workspace.clientHeight - 150) {
            leftPane.style.height = `${newHeight}px`;
          }
        }
      });

      document.addEventListener('mouseup', () => {
        if (isDragging) {
          isDragging = false;
          resizer.classList.remove('dragging');
          document.body.style.cursor = '';
          document.body.style.userSelect = '';
        }
      });
    }

    /* ==========================================================================
       Keyboard Shortcuts Modal & Handler
       ========================================================================== */
    function openKbdModal() {
      document.getElementById('kbdModal').style.display = 'flex';
    }

    function closeKbdModal() {
      document.getElementById('kbdModal').style.display = 'none';
    }

    function initKeyboardShortcuts() {
      document.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;

        // Answering shortcuts A/B/C/D for focused question
        const keyUpper = e.key.toUpperCase();
        if (['A', 'B', 'C', 'D'].includes(keyUpper) && state.focusedQuestionNum) {
          selectAnswer(state.focusedQuestionNum, keyUpper);
          return;
        }

        // V: toggle reader and questions view
        if (e.key === 'v' || e.key === 'V') {
          e.preventDefault();
          toggleReaderConsoleView();
        } else if (e.key === 'f' || e.key === 'F') {
          if (state.focusedQuestionNum) toggleFlagReview(state.focusedQuestionNum);
        } else if (e.key === 'j' || e.key === 'J' || e.key === 'ArrowDown') {
          e.preventDefault();
          scrollToQuestion(state.focusedQuestionNum + 1);
        } else if (e.key === 'k' || e.key === 'K' || e.key === 'ArrowUp') {
          e.preventDefault();
          scrollToQuestion(state.focusedQuestionNum - 1);
        } else if (e.key === '1') {
          switchSection('sec_a');
        } else if (e.key === '2') {
          switchSection('sec_b');
        } else if (e.key === '3') {
          switchSection('sec_c1');
        } else if (e.key === '4') {
          switchSection('sec_c2');
        } else if (e.key === '0') {
          switchSection('all');
        } else if (e.key === '?' || (e.shiftKey && e.key === '/')) {
          openKbdModal();
        } else if (e.key === 'Escape') {
          closeAllDrawers();
          closeScoreModal();
          closeKbdModal();
          document.getElementById('dictPopover').style.display = 'none';
          document.getElementById('textSelectionToolbar').style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
"""

    out_path = 'cet6_reading_platform.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"Ultra-polished HTML application successfully created at: {out_path} ({os.path.getsize(out_path):,} bytes)")

if __name__ == '__main__':
    build_app_html()
