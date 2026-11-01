<h1 align="center">Awesome Mac AI</h1>

<p align="center">
  The Definitive macOS AI Ecosystem Directory, Agent Harnesses, IDEs, and Local Runtimes
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> • <b>English</b>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/Platform-macOS%2014%2B-black?logo=apple" alt="macOS 14+">
  <img src="https://img.shields.io/badge/Hardware-Apple%20Silicon%20(Metal)-blue" alt="Apple Silicon Metal">
  <a href="https://github.com/245678000000/awesome-mac-ai/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
</p>

---

## Highlights

- **3-Dimensional Taxonomy**: Clear separation between `Primary Type` (architecture), `Surface` (interface), and `Capabilities` (execution scope).
- **2026 Ecosystem Alignment**: Incorporates recent ecosystem shifts, including unified ChatGPT Work/Codex, Devin Desktop, Antigravity CLI, Opera Neon MCP connector, and persistent Subagents.
- **Machine-Readable Dataset**: All tools backed by `data/apps.json` with strict schema validation via `scripts/validate.py`.
- **Beginner Fast Track**: Instant curated bundles for general productivity, zero-to-hero coding, visual design, and local offline inference.

## Architecture

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        macOS AI Workflow Stack                         │
├────────────────────────────────────────────────────────────────────────┤
│  Layer 4: Interaction & OS     │ Desktop App, CLI/TUI, Menu Bar, IDE   │
│  Layer 3: Agent & Harness      │ Loops, Memory, Subagents, MCP, Skills │
│  Layer 2: Tools & Infra        │ Browser Automation, Computer Use, RAG │
│  Layer 1: Runtime & Models     │ Local Metal (MLX/Ollama), Cloud APIs  │
└────────────────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/245678000000/awesome-mac-ai.git
cd awesome-mac-ai
```

### 2. Validate dataset
Verify that all entries in the structured database meet schema requirements:
```bash
python3 scripts/validate.py
```

### 3. Explore tools by workflow
Refer to the curated catalog below to install and configure software for your specific macOS environment.

---

## Beginner's Fast Track

| Scenario / Role | Recommended Stack | Value Proposition |
| :--- | :--- | :--- |
| **General Productivity & Writing** | **ChatGPT Desktop + ima + Raycast AI** | Top-tier multi-modal reasoning + knowledge base + system-wide spotlight AI |
| **Zero-to-Hero AI Coding** | **Cursor / Trae + Claude Code / Codex CLI** | Chat-driven multi-file coding with automated terminal test execution |
| **Office & File Automation** | **WorkBuddy + Bob** | Automated Word/Excel/PPT generation & screen OCR translation |
| **Visual Design & UI Prototype** | **MiniMax Design + Recraft + v0 + Lovable** | Instant marketing graphics, lossless SVG export & prompt-to-fullstack app |
| **Local Offline Models** | **LM Studio + MacWhisper + Draw Things** | Zero-config local GGUF execution, local Whisper transcription & Metal SD |

---

## Table of Contents

- [01. Desktop AI Assistants](#01-desktop-ai-assistants)
- [02. AI IDEs & Code Editors](#02-ai-ides--code-editors)
- [03. Agent Harnesses & Terminal Agents](#03-agent-harnesses--terminal-agents)
- [04. Computer & Office Agents](#04-computer--office-agents)
- [05. Local Model Runtimes](#05-local-model-runtimes)
- [06. AI Workspaces & Multi-Model Clients](#06-ai-workspaces--multi-model-clients)
- [07. Knowledge & RAG](#07-knowledge--rag)
- [08. Productivity & System AI](#08-productivity--system-ai)
- [09. Voice & Transcription](#09-voice--transcription)
- [10. AI Design, UI/UX & App Builders](#10-ai-design-uiux--app-builders)
- [11. Agentic Terminals & Browsers](#11-agentic-terminals--browsers)
- [12. Agent Managers & Control Planes](#12-agent-managers--control-planes)
- [13. IDE Extensions & Plugins](#13-ide-extensions--plugins)
- [14. Browser & Computer-Use Infrastructure](#14-browser--computer-use-infrastructure)
- [15. Evaluation & Harnesses](#15-evaluation--harnesses)
- [16. Archive & Legacy](#16-archive--legacy)
- [Apple Silicon Memory Matrix](#apple-silicon-memory-matrix)

---

### 01. Desktop AI Assistants

- **[ChatGPT for Mac](https://openai.com/chatgpt/download/)** `[Tier: S]` - Unified Chat + Work + Codex architecture, screen context perception, local file processing & Advanced Voice.
  ```bash
  brew install --cask chatgpt
  ```
- **[Claude for Mac](https://claude.ai/download)** `[Tier: S]` - Gold-standard reasoning & writing, real-time Artifacts rendering, Cowork & Claude Code integration.
  ```bash
  brew install --cask claude
  ```
- **[Gemini for Mac](https://gemini.google.com/)** `[Tier: S]` - Native screen context understanding, live voice, Spark workspace & multi-modal file ingestion.
- **[Doubao (豆包)](https://www.doubao.com/)** `[Tier: A]` - Ultra-fast response desktop assistant by ByteDance.
  ```bash
  brew install --cask doubao
  ```
- **[Tongyi (通义千问)](https://tongyi.aliyun.com/)** `[Tier: A]` - Alibaba's assistant optimized for million-token documents & audio/video summaries.
- **[Pi](https://pi.ai/)** `[Tier: A]` - High-EQ conversational assistant by Inflection AI.
- **[Meta AI for Mac](https://ai.meta.com/)** `[Tier: Beta]` - Desktop window context capture, system-wide cross-app dictation & deep research.

---

### 02. AI IDEs & Code Editors

- **[Cursor](https://www.cursor.com/)** `[Tier: S]` - Flagship AI-first IDE with Composer multi-file editing and codebase semantic index.
  ```bash
  brew install --cask cursor
  ```
- **[Trae](https://www.trae.ai/)** `[Tier: S]` - Adaptive AI IDE by ByteDance with native Claude 3.5/GPT-4o and 1-click VS Code migration.
  ```bash
  brew install --cask trae
  ```
- **[Zed](https://zed.dev/)** `[Tier: S]` - High-performance Rust & Metal editor; premier native ACP host for Claude/Codex/Antigravity harnesses.
  ```bash
  brew install --cask zed
  ```
- **[Devin Desktop](https://docs.windsurf.com/)** `[Tier: S]` - Successor to Windsurf, featuring Devin Local execution engine and workflow debugging.
  ```bash
  brew install --cask windsurf
  ```
- **[Antigravity IDE](https://github.com/google-deepmind)** `[Tier: S]` - Google DeepMind's agentic IDE with dual-view planning, human-in-the-loop review, and subagent orchestration.
- **[Xcode (26.3+)](https://developer.apple.com/xcode/)** `[Tier: S]` - Apple's official IDE with native Claude Agent, Codex, Gemini and MCP/ACP support.
- **[Visual Studio Code](https://code.visualstudio.com/)** `[Tier: S]` - Extensible editor platform powered by GitHub Copilot, Cline, and Roo Code.
  ```bash
  brew install --cask visual-studio-code
  ```

---

### 03. Agent Harnesses & Terminal Agents

- **[Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)** `[Tier: S]` - Anthropic's official terminal agent for autonomous codebase refactoring and git commits.
  ```bash
  npm install -g @anthropic-ai/claude-code
  ```
- **[Codex CLI](https://openai.com/)** `[Tier: S]` - OpenAI's autonomous coding harness with multi-step verification.
- **[Antigravity CLI](https://github.com/google-antigravity/antigravity-cli)** `[Tier: S]` - Google's primary terminal agent with planning mode, parallel subagent dispatching, and persistent memory.
- **[GitHub Copilot CLI](https://github.com/features/copilot/cli/)** `[Tier: S]` - Terminal coding agent with `/fleet` parallel subagents, `/plan`, and autopilot execution.
- **[Aider](https://aider.chat/)** `[Tier: A]` - The classic CLI pair-programming tool with automated git commit generation.
  ```bash
  brew install aider
  ```
- **[Qwen Code](https://github.com/QwenLM)** & **[Kimi Code CLI](https://kimi.moonshot.cn/)** `[Tier: S]` - Specialized terminal coding agents optimized for long-context models.
- **[DeepSeek Harness](https://github.com/deepseek-ai)** `[Tier: S]` - Inference and execution harness tailored for DeepSeek-R1/V3.
- **[CodeBuddy Code](https://www.codebuddy.ai/)** `[Tier: S]` - Tencent's terminal agent with ACP/MCP IDE integration.
- **[Muse Code](https://research.meta.ai/)** `[Tier: Beta]` - Meta's coding agent supporting persistent background subagents.
- **[MiniMax Code](https://www.minimax.io/)** `[Tier: S]` *(Desktop / Web)* - Official harness for MiniMax models with computer use, agent teams, and memory.
- **[OpenCode](https://github.com/opencode-ai)** & **[goose CLI](https://github.com/block/goose)** `[Tier: S]` - Open-source, unconstrained agent harnesses with MCP/ACP support.

---

### 04. Computer & Office Agents

- **[WorkBuddy](https://www.workbuddy.ai/)** `[Tier: S]` - Full-stack office AI agent workbench for automated Word/Excel/PPT generation on Apple Silicon and Intel.
- **[Perplexity Personal Computer](https://www.perplexity.ai/)** `[Tier: S]` - Controlled Finder, mail, and local file operations with web research.
- **[Antigravity 2.0](https://github.com/google-deepmind)** `[Tier: S]` - Desktop Agent workspace with multi-agent orchestration, sandbox isolation, and artifacts delivery.
- **[TRAE Work](https://www.trae.ai/work)** `[Tier: A]` - Office work agent for reports, data visualization, and presentation drafting.
- **[QoderWork](https://qoder.com/)** & **[QoderWake](https://qoder.com/)** `[Tier: A]` - Desktop work agent and persistent AI employee runtime with dedicated skills.
- **[OpenClaw](https://github.com/openclaw)** `[Tier: A]` - Local personal agent gateway with multi-channel integration.
- **[goose Desktop](https://github.com/block/goose)** `[Tier: S]` - General-purpose desktop agent for coding, research, and automation.

---

### 05. Local Model Runtimes

- **[LM Studio](https://lmstudio.ai/)** `[Tier: S]` - The most intuitive local model GUI + `lms` CLI + local OpenAI-compatible API server.
  ```bash
  brew install --cask lm-studio
  ```
- **[Ollama](https://ollama.com/)** `[Tier: S]` - Industry standard CLI/Daemon for running DeepSeek, Llama 3, and Qwen locally.
  ```bash
  brew install --cask ollama
  ```
- **[Jan](https://jan.ai/)** `[Tier: S]` - 100% open-source, privacy-focused local AI client.
  ```bash
  brew install --cask jan
  ```
- **[llama.cpp](https://github.com/ggerganov/llama.cpp)** `[Tier: S]` - Ultra-lightweight C++ & Metal inference engine.
  ```bash
  brew install llama.cpp
  ```
- **[MLX / MLX-LM](https://github.com/ml-explore/mlx)** `[Tier: A]` - Apple Silicon native machine learning framework by Apple Research.

---

### 06. AI Workspaces & Multi-Model Clients

- **[Cherry Studio](https://cherry-studio.net/)** `[Tier: S]` - Open-source multi-model client with rich agent marketplace and local RAG.
  ```bash
  brew install --cask cherry-studio
  ```
- **[Chatbox](https://chatboxai.app/)** `[Tier: S]` - Clean, cross-platform client with prompt presets and local encryption.
  ```bash
  brew install --cask chatbox
  ```
- **[Msty](https://msty.app/)** `[Tier: A]` - Side-by-side multi-model comparison workspace.
- **[OpenCat](https://opencat.app/)** `[Tier: A]` - Native Swift client supporting MLX local models and iCloud sync.

---

### 07. Knowledge & RAG

- **[ima](https://ima.qq.com/)** `[Tier: S]` - Tencent's personal knowledge workspace with Copilot MCP support and WeChat ecosystem sync.
- **[AnythingLLM](https://anythingllm.com/)** `[Tier: S]` - All-in-one local-first RAG desktop application.
  ```bash
  brew install --cask anythingllm
  ```
- **[Obsidian + Smart Connections](https://obsidian.md/)** `[Tier: A]` - Local-first markdown second brain with semantic linkage.
  ```bash
  brew install --cask obsidian
  ```
- **[Notion AI](https://www.notion.so/)** `[Tier: A]` - Cloud team workspace with cross-page retrieval and automated database synthesis.
  ```bash
  brew install --cask notion
  ```
- **[NotebookLM](https://notebooklm.google.com/)** `[Tier: S]` - Deep research notebook with lifelike multi-source audio overview podcasts.

---

### 08. Productivity & System AI

- **[Raycast AI](https://www.raycast.com/)** `[Tier: S]` - macOS spotlight replacement with global AI commands and OS integration.
  ```bash
  brew install --cask raycast
  ```
- **[Bob](https://bobtranslate.com/)** `[Tier: S]` - Premier screen OCR and translation utility with custom API keys.
- **[PopClip](https://pilotmoon.com/popclip/)** `[Tier: A]` - Text selection capsule bar with AI rewrite extensions.
- **[CleanShot X](https://cleanshot.com/)** `[Tier: A]` - Screen capture tool with built-in AI OCR.

---

### 09. Voice & Transcription

- **[MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper)** `[Tier: S]` - Native macOS offline speech-to-text powered by OpenAI Whisper.
  ```bash
  brew install --cask macwhisper
  ```
- **[VoiceInk](https://github.com/)** `[Tier: S]` - Open-source system-wide voice dictation replacement.
- **[Granola](https://www.granola.so/)** `[Tier: S]` - AI meeting notepad blending audio transcription and typed notes.
- **[Superwhisper](https://superwhisper.com/)** `[Tier: A]` - Context-aware AI dictation tailored to specific macOS apps.

---

### 10. AI Design, UI/UX & App Builders

- **[Lovable](https://lovable.dev/)** `[Tier: S]` - Premier fullstack prompt-to-app generator with Supabase and GitHub sync.
- **[Replit (Replit Agent)](https://replit.com/)** `[Tier: S]` - Autonomous fullstack coding environment and instant cloud deployment.
  ```bash
  brew install --cask replit
  ```
- **[MiniMax Design](https://www.minimax.io/)** `[Tier: S]` - Visual design platform for marketing assets and consistent character styling.
- **[OpenDesign](https://github.com/)** `[Tier: S]` - Open design-to-code framework bridging Figma with React/Tailwind codebases.
- **[v0 (by Vercel)](https://v0.dev/)** `[Tier: S]` - Prompt-to-UI generative interface builder.
- **[Recraft](https://www.recraft.ai/)** `[Tier: S]` - Lossless vector SVG and icon generation platform.
- **[Draw Things](https://drawthings.ai/)** `[Tier: S]` - Native offline Stable Diffusion studio with 8-bit Metal acceleration and CLI.
- **[Upscayl](https://upscayl.org/)** `[Tier: A]` - Open-source AI image upscaler.
  ```bash
  brew install --cask upscayl
  ```
- **[ComfyUI](https://github.com/comfyanonymous/ComfyUI)** `[Tier: S]` - Node-based generative workflow runtime.

---

### 11. Agentic Terminals & Browsers

- **[Warp](https://www.warp.dev/)** `[Tier: S]` - Modern Rust/GPU terminal with built-in Warp AI.
  ```bash
  brew install --cask warp
  ```
- **[Opera Neon](https://www.opera.com/)** `[Tier: S]` - Agentic browser featuring **MCP Connector** and **`opera-browser-cli`** to reuse live sessions.
- **[Perplexity Comet](https://www.perplexity.ai/)** `[Tier: S]` - AI-native search browser with cross-tab reasoning.
- **[Dia](https://dia.com/)** `[Tier: A]` - Minimalist AI browser with automated web skills.

---

### 12. Agent Managers & Control Planes

- **[Supacode](https://github.com/)** `[Tier: A]` - Desktop controller for concurrent Claude Code and Codex processes.
- **[Kiro Crew](https://kiro.dev/)** `[Tier: A]` - Persistent personal and team agent workspace.
- **[CodexBar](https://github.com/)** `[Tier: A]` - Menu bar monitor for LLM usage and API quotas.

---

### 13. IDE Extensions & Plugins

- **[GitHub Copilot](https://github.com/features/copilot)** `[Tier: S]` - Official inline completion & Copilot Chat.
- **[Cline](https://github.com/cline/cline)** `[Tier: S]` - Autonomous human-in-the-loop coding agent extension.
- **[Roo Code](https://github.com/RooVetGit/Roo-Cline)** `[Tier: A]` - Multi-role customizable coding agent.
- **[Kilo Code](https://github.com/kilo-ai)** `[Tier: A]` - Fast model switcher and agent skills manager.
- **[Augment Code](https://www.augmentcode.com/)** `[Tier: A]` - Enterprise-grade codebase dependency indexing.

---

### 14. Browser & Computer-Use Infrastructure

- **`opera-browser-cli`**: Command-line control over running Opera Neon browser sessions.
- **Opera Neon MCP Connector**: Standard MCP server exposing live browser tabs to external agents.
- **Playwright**: Universal web automation framework.
- **Chrome DevTools MCP**: Exposing Chromium remote debugging as standard MCP tools.
- **Juno / Agent! / Local Operator**: Accessibility and vision-driven macOS GUI automation agents.

---

### 15. Evaluation & Harnesses

- **[SWE-bench](https://github.com/princeton-nlp/SWE-bench)** `[Tier: S]` - Gold standard benchmark for software engineering agents.
- **[Promptfoo](https://github.com/promptfoo/promptfoo)** `[Tier: S]` - CLI & Web tool for prompt evaluation and red-teaming.
  ```bash
  brew install promptfoo
  ```
- **[AgentBench](https://github.com/THUDM/AgentBench)** `[Tier: A]` - Multi-dimensional benchmark for LLM agents.
- **[agent-qa](https://vostride.com)** `[Tier: B]` - QA harness for web, Android and iOS with persistent memidex memory and evidence-gated self-improvement. Runs through a CLI, local dashboard or MCP; requires Node.js 24+, and local iOS testing requires a Mac with Xcode and Appium. Early v0.2; FSL-1.1-ALv2 with commercial restrictions.

---

### 16. Archive & Legacy

| Product Name | Former Identity | Reason for Transition | Status |
| :--- | :--- | :--- | :---: |
| **ChatGPT Atlas** | AI Native Browser | Deprecated on 2026-08-09; capabilities merged into ChatGPT Desktop / Codex | ❌ **Deprecated** |
| **Gemini CLI (Personal)** | CLI Client | Individual personal OAuth shut down; migrated to **Antigravity CLI** | ⚠️ **Legacy** |
| **Windsurf** | Standalone AI IDE | Brand and engine upgraded into **Devin Desktop** (with Devin Local) | 🔄 **Transitioned** |
| **Continue** | Coding Plugin | Team joined Cursor; repository set to read-only | ⚠️ **Maintenance Ended** |
| **ChatGPT Classic** | Legacy Chat App | Superseded by the unified Chat+Work+Codex macOS Desktop App | ⚠️ **Legacy App** |

---

## Apple Silicon Memory Matrix

```text
┌─────────────────┬───────────────────────────────┬──────────────────────────────────────────┐
│ Unified Memory  │ Recommended Quantization      │ Classic Model Recommendations            │
├─────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 8GB - 16GB      │ 1.5B ~ 8B (4-bit Q4_K_M)      │ Qwen2.5-7B, Llama-3.1-8B, DeepSeek-7B    │
│ 24GB - 36GB     │ 14B ~ 32B (4-bit Q4_K_M)     │ Qwen2.5-14B/32B, DeepSeek-Coder-33B      │
│ 64GB - 128GB    │ 70B ~ 72B (4-bit / 8-bit)    │ Qwen2.5-72B-Instruct, Llama-3.3-70B      │
│ 128GB+ (M Max)  │ MoE Models / 70B+ FP16        │ DeepSeek-R1/V3 Distills, Massive RAG     │
└─────────────────┴───────────────────────────────┴──────────────────────────────────────────┘
```

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a Pull Request.

1. Fork the repo and add entries to `README.md`, `README.zh-CN.md`, and `data/apps.json`.
2. Run validation:
   ```bash
   python3 scripts/validate.py
   ```
3. Submit a PR with clear rationale.

---

## License

Released under the [MIT License](LICENSE).
