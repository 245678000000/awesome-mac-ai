# 🍎 Awesome Mac AI

> **The Definitive macOS AI Ecosystem Directory & Workflow Index**  
> A curated guide to AI applications, Agent harnesses, CLI/TUIs, IDEs, and local runtimes for macOS (optimized for Apple Silicon).

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![macOS](https://img.shields.io/badge/Platform-macOS%2014%2B-black?logo=apple)](https://apple.com)
[![Apple Silicon](https://img.shields.io/badge/Hardware-Apple%20Silicon%20(Metal)-blue)](https://developer.apple.com/metal/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Chinese](https://img.shields.io/badge/Language-中文-red)](README.md)

---

## 🧭 Architecture & Taxonomy

This list uses a **3-dimensional orthogonal classification** to avoid confusing user interfaces with underlying architecture:

- **`Primary Type`**: What the product fundamentally is (`Desktop AI Assistant`, `Agent Harness`, `AI IDE`, `Local Runtime`, etc.).
- **`Surface`**: How the user interacts with it (`Desktop`, `CLI`, `TUI`, `IDE`, `IDE Extension`, `Browser`, `Browser CLI`, `Menu Bar`, `Daemon/API`).
- **`Capabilities`**: What it actually does (`Computer Use`, `MCP`, `Skills`, `Subagents`, `Local Metal`, `RAG`).

---

## 🌱 Beginner's Fast Track (Top Picks)

| Role / Scenario | Recommended Stack | Why choose this? |
| :--- | :--- | :--- |
| **General Productivity & Writing** | **ChatGPT Desktop + ima + Raycast AI** | Top-tier multi-modal reasoning + knowledge base + system-wide spotlight AI |
| **Zero-to-Hero AI Coding** | **Cursor / Trae + Claude Code / Codex CLI** | Chat-driven multi-file coding with automated terminal test execution |
| **Office & File Automation** | **WorkBuddy + Bob** | Automated Word/Excel/PPT generation & screen OCR translation |
| **Visual Design & UI Prototype** | **MiniMax Design + Recraft + v0** | Instant marketing graphics, lossless SVG export & prompt-to-UI code |
| **Local Offline Models** | **LM Studio + MacWhisper + Draw Things** | Zero-config local GGUF execution, local Whisper transcription & Metal SD |

---

## 📑 Table of Contents

1. [Desktop AI Assistants](#01-desktop-ai-assistants)
2. [AI IDEs & Code Editors](#02-ai-ides--code-editors)
3. [Agent Harnesses & Terminal Agents](#03-agent-harnesses--terminal-agents)
4. [Computer & Office Agents](#04-computer--office-agents)
5. [Local Model Runtimes](#05-local-model-runtimes)
6. [AI Workspaces & Multi-Model Clients](#06-ai-workspaces--multi-model-clients)
7. [Knowledge & RAG](#07-knowledge--rag)
8. [Productivity & System AI](#08-productivity--system-ai)
9. [Voice & Transcription](#09-voice--transcription)
10. [AI Design & Creative](#10-ai-design--creative)
11. [Agentic Terminals & Browsers](#11-agentic-terminals--browsers)
12. [Agent Managers & Control Planes](#12-agent-managers--control-planes)
13. [IDE Extensions & Plugins](#13-ide-extensions--plugins)
14. [Browser & Computer-Use Infrastructure](#14-browser--computer-use-infrastructure)
15. [Evaluation & Harnesses](#15-evaluation--harnesses)
16. [Archive & Legacy](#16-archive--legacy)

---

### 01. Desktop AI Assistants
- **[ChatGPT for Mac](https://openai.com/chatgpt/download/)** ⚡ 🍏 🍺 `[Tier: S]` - Unified Chat + Work + Codex architecture, screen context perception, local file processing & Advanced Voice.
- **[Claude for Mac](https://claude.ai/download)** ⚡ 🍏 🍺 `[Tier: S]` - Gold-standard reasoning & writing, real-time Artifacts rendering, Cowork & Claude Code integration.
- **[Gemini for Mac](https://gemini.google.com/)** ⚡ 🍏 `[Tier: S]` - Native screen context understanding, live voice, Spark workspace & multi-modal file ingestion.
- **[Doubao (豆包)](https://www.doubao.com/)** 🆓 🍏 🍺 `[Tier: A]` - Ultra-fast response desktop assistant by ByteDance.
- **[Tongyi (通义千问)](https://tongyi.aliyun.com/)** 🆓 🍏 `[Tier: A]` - Alibaba's assistant optimized for million-token documents & audio/video summaries.
- **[Pi](https://pi.ai/)** 🆓 🍏 `[Tier: A]` - High-EQ conversational assistant by Inflection AI.

---

### 02. AI IDEs & Code Editors
- **[Cursor](https://www.cursor.com/)** ⚡ 🍏 🍺 `[Tier: S]` - Flagship AI-first IDE with Composer multi-file editing and codebase semantic index.
- **[Trae](https://www.trae.ai/)** 🆓 🍏 🍺 `[Tier: S]` - Adaptive AI IDE by ByteDance with native Claude 3.5/GPT-4o and 1-click VS Code migration.
- **[Zed](https://zed.dev/)** 🆓 🍏 🍺 `[Tier: S]` - High-performance Rust & Metal editor; premier native ACP host for Claude/Codex/Antigravity harnesses.
- **[Devin Desktop](https://docs.windsurf.com/)** ⚡ 🍏 🍺 `[Tier: S]` - Successor to Windsurf, featuring Devin Local execution engine and workflow debugging.
- **[Xcode (26.3+)](https://developer.apple.com/xcode/)** 🆓 🍏 `[Tier: S]` - Apple's official IDE with native Claude Agent, Codex, Gemini and MCP/ACP support.

---

### 03. Agent Harnesses & Terminal Agents
- **[Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)** ⚡ 🍏 `[Tier: S]` - Anthropic's official terminal agent for autonomous codebase refactoring and git commits.
- **[Codex CLI](https://openai.com/)** ⚡ 🍏 `[Tier: S]` - OpenAI's autonomous coding harness with multi-step verification.
- **[Antigravity CLI](https://github.com/google-antigravity/antigravity-cli)** 🆓 🍏 `[Tier: S]` - Google's primary terminal agent with planning mode, parallel subagent dispatching and persistent memory.
- **[GitHub Copilot CLI](https://github.com/features/copilot/cli/)** ⚡ 🍏 `[Tier: S]` - Terminal coding agent with `/fleet` parallel subagents, `/plan`, and autopilot execution.
- **[Aider](https://aider.chat/)** 🆓 🍏 🍺 `[Tier: A]` - The classic CLI pair-programming tool with automated git commit generation.

---

### 04. Computer & Office Agents
- **[WorkBuddy](https://www.workbuddy.ai/)** ⚡ 🍏 `[Tier: S]` - Full-stack office AI agent workbench for automated Word/Excel/PPT generation.
- **[Perplexity Personal Computer](https://www.perplexity.ai/)** ⚡ 🍏 `[Tier: S]` - Controlled Finder, mail, and local file operations with web research.
- **[Antigravity 2.0](https://github.com/google-deepmind)** ⚡ 🍏 `[Tier: S]` - Desktop Agent workspace with multi-agent orchestration, sandbox isolation, and artifacts delivery.
- **[TRAE Work](https://www.trae.ai/work)** 🆓 🍏 `[Tier: A]` - Office work agent for reports, data visualization, and presentation drafting.
- **[MiniMax Code](https://www.minimax.io/)** ⚡ 🍏 `[Tier: S]` - Desktop & web harness with computer use, agent teams, and memory.

---

### 05. Local Model Runtimes
- **[LM Studio](https://lmstudio.ai/)** 🆓 🍏 🍺 `[Tier: S]` - The most intuitive local model GUI + `lms` CLI + local OpenAI-compatible API server.
- **[Ollama](https://ollama.com/)** 🆓 🍏 🍺 `[Tier: S]` - Industry standard CLI/Daemon for running DeepSeek, Llama 3, and Qwen locally.
- **[llama.cpp](https://github.com/ggerganov/llama.cpp)** 🆓 🍏 🍺 `[Tier: S]` - Ultra-lightweight C++ & Metal inference engine.
- **[MLX](https://github.com/ml-explore/mlx)** 🆓 🍏 `[Tier: A]` - Apple Silicon native machine learning framework by Apple Research.

---

### 06. AI Workspaces & Multi-Model Clients
- **[Cherry Studio](https://cherry-studio.net/)** 🆓 🍏 🍺 `[Tier: S]` - Open-source multi-model client with rich agent marketplace and local RAG.
- **[Chatbox](https://chatboxai.app/)** 🆓 🍏 🍺 `[Tier: S]` - Clean, cross-platform client with prompt presets and local encryption.
- **[Msty](https://msty.app/)** 🆓 🍏 `[Tier: A]` - Side-by-side multi-model comparison workspace.

---

### 07. Knowledge & RAG
- **[ima](https://ima.qq.com/)** 🆓 🍏 `[Tier: S]` - Tencent's personal knowledge workspace with Copilot MCP support.
- **[AnythingLLM](https://anythingllm.com/)** 🆓 🍏 🍺 `[Tier: S]` - All-in-one local-first RAG desktop application.
- **[Obsidian](https://obsidian.md/) + Smart Connections** 🆓 🍏 🍺 `[Tier: A]` - Local-first markdown second brain with semantic linkage.
- **[Notion AI](https://www.notion.so/)** ⚡ 🍏 🍺 `[Tier: A]` - Cloud team workspace with cross-page retrieval.

---

### 08. Productivity & System AI
- **[Raycast AI](https://www.raycast.com/)** ⚡ 🍏 🍺 `[Tier: S]` - macOS spotlight replacement with global AI commands and OS integration.
- **[Bob](https://bobtranslate.com/)** 💎 🍏 🍺 `[Tier: S]` - Premier screen OCR and translation utility with custom API keys.
- **[PopClip](https://pilotmoon.com/popclip/)** 💎 🍏 🍺 `[Tier: A]` - Text selection capsule bar with AI rewrite extensions.

---

### 09. Voice & Transcription
- **[MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper)** ⚡ 🍏 🍺 `[Tier: S]` - Native macOS offline speech-to-text powered by OpenAI Whisper.
- **[VoiceInk](https://github.com/)** 🆓 🍏 `[Tier: S]` - Open-source system-wide voice dictation replacement.
- **[Granola](https://www.granola.so/)** ⚡ 🍏 `[Tier: S]` - AI meeting notepad blending audio transcription and typed notes.

---

### 10. AI Design & Creative
- **[Lovable](https://lovable.dev/)** ⚡ 🍏 `[Tier: S]` - Premier fullstack prompt-to-app generator with Supabase and GitHub sync.
- **[Replit (Replit Agent)](https://replit.com/)** ⚡ 🍏 🍺 `[Tier: S]` - Autonomous fullstack coding environment and instant cloud deployment.
- **[MiniMax Design](https://www.minimax.io/)** ⚡ 🍏 `[Tier: S]` - Visual design platform for marketing assets and consistent character styling.
- **[OpenDesign](https://github.com/)** 🆓 🍏 `[Tier: S]` - Open design-to-code framework bridging Figma with React/Tailwind codebases.
- **[v0 (by Vercel)](https://v0.dev/)** ⚡ 🍏 `[Tier: S]` - Prompt-to-UI generative interface builder.
- **[Recraft](https://www.recraft.ai/)** ⚡ 🍏 🍺 `[Tier: S]` - Lossless vector SVG and icon generation platform.
- **[Draw Things](https://drawthings.ai/)** 🆓 🍏 `[Tier: S]` - Native offline Stable Diffusion studio with 8-bit Metal acceleration.
- **[Upscayl](https://upscayl.org/)** 🆓 🍏 🍺 `[Tier: A]` - Open-source AI image upscaler.

---

### 11. Agentic Terminals & Browsers
- **[Warp](https://www.warp.dev/)** ⚡ 🍏 🍺 `[Tier: S]` - Modern Rust/GPU terminal with built-in Warp AI.
- **[Opera Neon](https://www.opera.com/)** 🆓 🍏 `[Tier: S]` - Agentic browser featuring **MCP Connector** and **`opera-browser-cli`** to reuse live sessions.

---

### 12. Agent Managers & Control Planes
- **[Supacode](https://github.com/)** ⚡ 🍏 `[Tier: A]` - Desktop controller for concurrent Claude Code and Codex processes.
- **[CodexBar](https://github.com/)** 🆓 🍏 `[Tier: A]` - Menu bar monitor for LLM usage and API quotas.

---

### 13. IDE Extensions & Plugins
- **[GitHub Copilot](https://github.com/features/copilot)** 💎 `[Tier: S]` - Official inline completion & Copilot Chat.
- **[Cline](https://github.com/cline/cline)** 🆓 🍏 `[Tier: S]` - Autonomous human-in-the-loop coding agent extension.
- **[Roo Code](https://github.com/RooVetGit/Roo-Cline)** 🆓 🍏 `[Tier: A]` - Multi-role customizable coding agent.

---

### 14. Browser & Computer-Use Infrastructure
- **`opera-browser-cli`**: Command-line control over running Opera Neon browser sessions.
- **Opera Neon MCP Connector**: Standard MCP server exposing live browser tabs to external agents.
- **Playwright**: Universal web automation framework.
- **Chrome DevTools MCP**: Exposing Chromium remote debugging as standard MCP tools.

---

### 15. Evaluation & Harnesses
- **[SWE-bench](https://github.com/princeton-nlp/SWE-bench)** 🆓 🍏 `[Tier: S]` - Gold standard benchmark for software engineering agents.
- **[Promptfoo](https://github.com/promptfoo/promptfoo)** 🆓 🍏 🍺 `[Tier: S]` - CLI & Web tool for prompt evaluation and red-teaming.

---

### 16. Archive & Legacy
| Name | Former Role | Reason | Status |
| :--- | :--- | :--- | :---: |
| **ChatGPT Atlas** | AI Browser | Deprecated on 2026-08-09; merged into ChatGPT Desktop | ❌ **Deprecated** |
| **Gemini CLI (Personal)** | CLI Client | Individual personal OAuth shut down; migrated to Antigravity CLI | ⚠️ **Legacy** |
| **Windsurf** | AI IDE | Rebranded & evolved into Devin Desktop | 🔄 **Transitioned** |
| **Continue** | Coding Plugin | Team joined Cursor; repository set to read-only | ⚠️ **Maintenance Ended** |

---

*Licensed under [MIT](LICENSE).*
