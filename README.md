# 🍎 Awesome Mac AI

> **The Definitive macOS AI Ecosystem Directory & Workflow Index**  
> 专为 macOS（针对 Apple Silicon M 系列芯片与 Intel Mac）打造的全景 AI 工具链与工作流生态数据库。

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![macOS](https://img.shields.io/badge/Platform-macOS%2014%2B-black?logo=apple)](https://apple.com)
[![Apple Silicon](https://img.shields.io/badge/Hardware-Apple%20Silicon%20(Metal)-blue)](https://developer.apple.com/metal/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![English](https://img.shields.io/badge/Language-English-blue)](README.en.md)

---

## 🧭 项目架构与分类哲学

本项目彻底摒弃“仅按应用名称堆砌链接”的传统模式，确立**三维正交分类法**，清晰解决“它本质是什么”与“通过什么界面使用”的区别：

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

- **`Primary Type`（本质是什么）**：定义其在技术架构中的真实角色（如 `Agent Harness`、`Local Model Runtime`、`Computer Agent`）。
- **`Surface`（交互载体）**：定义用户操作的入口（如 `Desktop`、`CLI`、`TUI`、`IDE`、`IDE Extension`、`Browser`、`Browser CLI`、`Menu Bar`、`Daemon/API`）。
- **`Capabilities`（核心能力）**：定义其实际具备的执行能力（如 `Computer Use`、`MCP`、`Skills`、`Subagents`、`Local Metal`）。

---

## 🌱 小白新手 3 分钟极速装机套件 (Beginner's Fast Track)

> **如果您刚接触 Mac AI 或追求零门槛开箱即用，推荐直接按照您的核心需求选择对应组合：**

| 用户角色 / 场景 | 推荐黄金组合 (开箱即用) | 为什么选这个组合？ |
| :--- | :--- | :--- |
| **日常办公 / 写作 / 学生党** | **ChatGPT 桌面端 + ima (腾讯智能工作台) + Raycast AI** | 顶级通用对话 + 微信/公众号知识库沉淀 + 全局划词秒翻译与快捷指令 |
| **零基础 / 进阶编程开发** | **Cursor 或 Trae + Claude Code 或 Codex CLI** | 像聊天一样让 AI 写代码并自动修改多文件，全中文友好，支持终端自动跑通测试 |
| **职场办公与文件自动化** | **WorkBuddy + Bob** | 自动读写生成 Word/Excel/PPT 文档，屏幕划词精准学术翻译与 OCR 识别 |
| **视觉创意与 UI 原型** | **MiniMax Design + Recraft + v0** | 一键生成商业海报物料、导出无损 SVG 矢量图标与自然语言生成前端界面 |
| **本地离线模型 / 隐私玩家** | **LM Studio + MacWhisper + Draw Things** | 全可视化界面一键下载运行 DeepSeek/Llama 模型，本地离线语音转写与 AI 画图 |

---

## 📑 16 大一级模块总目录

- [01. 通用 Mac AI 桌面助手（Desktop AI Assistants）](#01-desktop-ai-assistants通用-mac-ai-桌面助手)
- [02. 智能编程 IDE 与代码编辑器（AI IDEs & Code Editors）](#02-ai-ides--code-editors智能编程-ide-与代码编辑器)
- [03. 终端编程 Agent 与 Harness（Agent Harnesses & CLI）](#03-agent-harnesses--terminal-agents终端编程-agent-与-harness)
- [04. 电脑操作与职场办公智能体（Computer & Office Agents）](#04-computer--office-agents电脑操作与职场办公智能体)
- [05. 本地大模型运行与推理引擎（Local Model Runtimes）](#05-local-model-runtimes本地大模型运行与推理引擎)
- [06. 多模型聚合桌面客户端（AI Workspaces & Clients）](#06-ai-workspaces--clients多模型聚合桌面客户端)
- [07. 智能知识库与第二大脑（Knowledge & RAG）](#07-knowledge--rag智能知识库与第二大脑)
- [08. 系统级效率与全局快捷层（Productivity & System AI）](#08-productivity--system-ai系统级效率与全局快捷层)
- [09. 语音转写与会议纪要（Voice & Transcription）](#09-voice--transcription语音转写与会议纪要)
- [10. AI 设计、UI/UX 与视觉创意（AI Design & Creative）](#10-ai-design--creative-ai-设计uiux-与视觉创意)
- [11. 智能体终端与 AI 原生浏览器（Agentic Terminals & Browsers）](#11-agentic-terminals--browsers智能体终端与-ai-原生浏览器)
- [12. 智能体管理器与控制平面（Agent Managers & Control Planes）](#12-agent-managers--control-planes智能体管理器与控制平面)
- [13. 编辑器插件与扩展体系（IDE Extensions & Plugins）](#13-ide-extensions--plugins编辑器插件与扩展体系)
- [14. 浏览器与电脑控制基础设施（Browser & Computer-Use Infra）](#14-browser--computer-use-infra浏览器与电脑控制基础设施)
- [15. 智能体评测基准与测试套件（Evaluation & Harnesses）](#15-evaluation--harnesses智能体评测基准与测试套件)
- [16. 归档与已停运项目清单（Archive & Legacy）](#16-archive--legacy归档与已停运项目清单)

---

### 01. Desktop AI Assistants（通用 Mac AI 桌面助手）

> **场景定位**：日常随时唤起、深度融入 macOS 屏幕上下文与文件系统的通用 AI 助手。

- **[ChatGPT for Mac](https://openai.com/chatgpt/download/)** ⚡ 🍏 🍺 **`[S 级 / 零门槛]`**
  - **Primary Type**: Desktop AI Assistant / Agent Workspace | **Surface**: `Desktop`
  - **核心能力**：OpenAI 官方新版客户端，整合 **Chat + Work + Codex** 统一架构；支持 `⌥ + Space` 全局呼出、选区屏幕感知（Screen Context）、本地文件读写与高级实时语音模式（Advanced Voice）。
  - **安装**：`brew install --cask chatgpt`
- **[Claude for Mac](https://claude.ai/download)** ⚡ 🍏 🍺 **`[S 级 / 零门槛]`**
  - **Primary Type**: Desktop AI Assistant | **Surface**: `Desktop`
  - **核心能力**：Anthropic 官方客户端，文本撰写与代码逻辑标杆；支持全局快捷呼出、独立 Artifacts 窗口实时交互渲染，并深度集成 Cowork 与 Claude Code。
  - **安装**：`brew install --cask claude`
- **[Gemini for Mac](https://gemini.google.com/)** ⚡ 🍏 **`[S 级 / 零门槛]`**
  - **Primary Type**: Desktop AI Assistant | **Surface**: `Desktop`
  - **核心能力**：Google 原生桌面应用，依托 Gemini 1.5/2.0 超长上下文；支持屏幕上下文即时捕获、实时语音、Spark 创意工作区与长文档/多模态分析。
- **[豆包 (Doubao)](https://www.doubao.com/)** 🆓 🍏 🍺 **`[中文热门 / 零门槛]`**
  - **Primary Type**: Desktop AI Assistant | **Surface**: `Desktop`
  - **核心能力**：字节跳动官方桌面端，响应速度极快；涵盖中文深度问答、长文精读速读、文本创意与一键生图。
  - **安装**：`brew install --cask doubao`
- **[通义千问 / 通义桌面端](https://tongyi.aliyun.com/)** 🆓 🍏 **`[中文热门 / 零门槛]`**
  - **Primary Type**: Desktop AI Assistant | **Surface**: `Desktop`
  - **核心能力**：阿里巴巴官方出品，擅长百万 Token 级超长研报提炼、音视频实时转写速读与 PPT 提纲生成。
- **[Pi (Inflection AI)](https://pi.ai/)** 🆓 🍏 **`[高情商伴侣 / 零门槛]`**
  - **Primary Type**: Conversational Companion | **Surface**: `Desktop / Web`
  - **核心能力**：语言风格极其自然温和，擅长头脑风暴、日常咨询、心理疏导与口语化交流。
- **[Meta AI for Mac](https://ai.meta.com/)** 🆓 🍏 **`[Beta / 探索型]`**
  - **Primary Type**: Desktop AI Assistant | **Surface**: `Desktop`
  - **核心能力**：独立窗口上下文捕获、系统级跨应用语音输入听写与 Deep Research 研报检索。

---

### 02. AI IDEs & Code Editors（智能编程 IDE 与代码编辑器）

> **场景定位**：以代码编辑与工程组织为第一优先级的开发环境，自身内置或能够宿主外部 Agent。

- **[Cursor](https://www.cursor.com/)** ⚡ 🍏 🍺 **`[全球顶流 S 级 / 极低门槛]`**
  - **Primary Type**: Agent-first IDE | **Surface**: `Desktop IDE + CLI`
  - **核心能力**：全球最流行的 AI 代码编辑器（基于 VS Code）；支持 `⌘ + K` 局部精准改写、`⌘ + I` Composer 跨文件多步骤自动编码、全项目语义索引与 Agentic 调试。
  - **安装**：`brew install --cask cursor`
- **[Trae (TraeCode)](https://www.trae.ai/)** 🆓 🍏 🍺 **`[国内首选 S 级 / 极低门槛]`**
  - **Primary Type**: Adaptive AI IDE | **Surface**: `Desktop IDE`
  - **核心能力**：字节跳动推出的自适应 AI IDE。原生集成 Claude 3.5 / GPT-4o 等顶尖模型，具备深度项目上下文理解与 SOLO / 多 Agent 模式；一键无痛迁移 VS Code 所有插件与配置。
  - **安装**：`brew install --cask trae`
- **[Zed](https://zed.dev/)** 🆓 🍏 🍺 **`[极速原生 S 级 / 低门槛]`**
  - **Primary Type**: High-performance AI Code Editor | **Surface**: `Desktop IDE`
  - **核心能力**：基于 Rust 与 Metal 原生开发，毫秒级启动与输入响应；内置 Zed Agent，且是目前最佳的 **ACP (Agent Context Protocol) 宿主**，可直接无缝挂载 Claude、Codex、Antigravity 等外部 Harness。
  - **安装**：`brew install --cask zed`
- **[Devin Desktop *(原 Windsurf)*](https://docs.windsurf.com/)** ⚡ 🍏 🍺 **`[S 级 / 低门槛]`**
  - **Primary Type**: Agent IDE / Command Center | **Surface**: `Desktop IDE`
  - **核心能力**：由原 Windsurf 正式升级过渡为 Devin 体系桌面 IDE；内置 Devin Local 执行引擎，具备深度上下文理解与工程级断点调试流。
  - **安装**：`brew install --cask windsurf`
- **[Antigravity IDE](https://github.com/google-deepmind)** ⚡ 🍏 **`[S 级 / 专业级]`**
  - **Primary Type**: Agentic IDE | **Surface**: `Desktop IDE`
  - **核心能力**：Google DeepMind 体系的高级 Agent IDE，深度集成规划模式（Planning Mode）、子代理调度与双向审查控制台。
- **[Xcode (26.3+)](https://developer.apple.com/xcode/)** 🆓 🍏 **`[Apple 原生标杆 S 级]`**
  - **Primary Type**: Native Apple IDE + Agent Host | **Surface**: `Desktop IDE`
  - **核心能力**：Apple 官方开发套件，自 26.3 起正式原生支持 Claude Agent、Codex、Gemini，并提供标准的 MCP / ACP 接入能力。
- **[Visual Studio Code](https://code.visualstudio.com/)** 🆓 🍏 🍺 **`[经典生态 / 插件驱动]`**
  - **Primary Type**: Extensible Code Editor | **Surface**: `Desktop IDE`
  - **必装 AI 扩展**：
    - **GitHub Copilot** 💎：官方代码行内补全与 Copilot Chat 侧边栏。
    - **Cline (前 Claude Dev)** 🆓：经人类逐步确认的终端命令与跨文件修改代理。
    - **Roo Code (Roo Cline)** 🆓：支持根据架构师、编码者不同角色进行模式切换。

---

### 03. Agent Harnesses & Terminal Agents（终端编程 Agent 与 Harness）

> **场景定位**：负责将 `Model + Tools + Loop + Context + Memory + MCP + Subagents` 组装运行的终端自治执行骨架。

- **[Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)** ⚡ 🍏 **`[终端顶流 S 级 / 上手极易]`**
  - **Primary Type**: Agent Harness / CLI Agent | **Surface**: `CLI / TUI`
  - **核心能力**：Anthropic 官方终端 Agent。能自主分析上万行的大型工程仓库，在终端里定位缺陷、跨目录重构代码、运行测试并生成标准 Git Commit。
  - **快速使用**：`npm install -g @anthropic-ai/claude-code` ➔ 终端输入 `claude`。
- **[Codex CLI](https://openai.com/)** ⚡ 🍏 **`[顶流 S 级 / 上手极易]`**
  - **Primary Type**: Agent Harness / CLI Agent | **Surface**: `CLI / TUI`
  - **核心能力**：OpenAI 官方终端编码智能体，具备多步骤自主规划、工具链调用与测试验证能力。
- **[Antigravity CLI](https://github.com/google-antigravity/antigravity-cli)** 🆓 🍏 **`[Google 主力 S 级 / 推荐必装]`**
  - **Primary Type**: Agent Harness / CLI Agent | **Surface**: `CLI / TUI`
  - **核心能力**：Google 终端 Agent 主力入口（个人用户自 Gemini CLI 迁入）；采用精美 TUI 界面，支持规划模式（Planning Mode）、子代理并行派发（Subagents Dispatching）、持久化工程记忆与 MCP 工具扩展。
- **[GitHub Copilot CLI](https://github.com/features/copilot/cli/)** ⚡ 🍏 **`[S 级 / 简单强大]`**
  - **Primary Type**: Agent Harness | **Surface**: `CLI / TUI`
  - **核心能力**：支持 `/fleet` 多子代理并行协作、`/plan` 架构规划、Autopilot 自治执行与 MCP 工具集成。
- **[Aider](https://aider.chat/)** 🆓 🍏 🍺 **`[经典结对神器 / 极低门槛]`**
  - **Primary Type**: CLI Coding Agent | **Surface**: `CLI`
  - **核心能力**：终端配对编程标杆工具，自动与 Git 深度整合，每次代码修改均输出严谨精准的提交信息。
  - **安装**：`brew install aider`
- **[Qwen Code](https://github.com/QwenLM)** 🆓 🍏 & **[Kimi Code CLI](https://kimi.moonshot.cn/)** ⚡ 🍏 **`[国产模型专属 S 级]`**
  - **Primary Type**: CLI Coding Agent | **Surface**: `CLI / TUI`
  - **核心能力**：专为通义千问超长上下文与月之暗面 Kimi 代码推理优化调优的终端 Agent。
- **[DeepSeek Harness](https://github.com/deepseek-ai)** 🆓 🍏 **`[深度求索专用 S 级]`**
  - **Primary Type**: Agent Harness | **Surface**: `CLI + Web UI`
  - **核心能力**：专为 DeepSeek-R1 / V3 模型设计的推理与代码执行代理框架。
- **[CodeBuddy Code](https://www.codebuddy.ai/)** 🆓 🍏 **`[腾讯出品 S 级]`**
  - **Primary Type**: CLI Agent | **Surface**: `CLI / TUI`
  - **核心能力**：支持 npm / brew 原生安装，可通过 ACP / MCP 与 Zed、VS Code、Cursor 无缝协同。
- **[Muse Code](https://research.meta.ai/)** 🆓 🍏 **`[Meta 旗下 A 级 / Beta]`**
  - **Primary Type**: Terminal Coding Agent | **Surface**: `CLI`
  - **核心能力**：Meta 于 2026 年 8 月发布的终端 Agent，核心亮点是能保持多个常驻后台的 Subagents 持续运行。
- **[MiniMax Code](https://www.minimax.io/)** ⚡ 🍏 **`[S 级 / 注意非 CLI]`**
  - **Primary Type**: Agent Harness / Desktop Agent | **Surface**: `Desktop / Web` *(非 CLI)*
  - **核心能力**：MiniMax 官方构建的代码与任务工作台，支持 Computer Use、Agent Team 协同、长期记忆与自动化定时任务调度。
- **[OpenCode](https://github.com/opencode-ai)** 🆓 🍏 & **[goose CLI](https://github.com/block/goose)** 🆓 🍏 **`[开源高自由度 S 级]`**
  - **Primary Type**: Open-source Agent Harness | **Surface**: `CLI / TUI`
  - **核心能力**：具备完整的 MCP / ACP 支持，开源无绑定，可自由切换任意模型后端。

---

### 04. Computer & Office Agents（电脑操作与职场办公智能体）

> **场景定位**：真正帮你“干活交付”的桌面智能体，能自主读写本地文件、操控应用并产出 Word/Excel/PPT 等最终成果。

- **[WorkBuddy](https://www.workbuddy.ai/)** ⚡ 🍏 **`[职场办公首选 S 级 / 零门槛]`**
  - **Primary Type**: Office Agent Workbench | **Surface**: `Desktop`
  - **核心能力**：腾讯系全场景职场 AI 智能体桌面工作台。支持自主规划步骤、读写本地文件夹，全自动批量处理与生成 Word 文档、Excel 数据表和 PPT 幻灯片；完美适配 Apple Silicon 与 Intel Mac。
- **[Perplexity Personal Computer](https://www.perplexity.ai/)** ⚡ 🍏 **`[顶流电脑控制 S 级 / 零门槛]`**
  - **Primary Type**: Computer Agent | **Surface**: `Desktop`
  - **核心能力**：具备 Computer Use 能力，获得授权后可在 Mac 上操作 Finder、发送系统邮件、读取文档并进行全网深度交叉检索。
- **[Antigravity 2.0](https://github.com/google-deepmind)** ⚡ 🍏 **`[桌面 Agent 工作台 S 级]`**
  - **Primary Type**: Desktop Agent Workspace | **Surface**: `Desktop`
  - **核心能力**：多 Agent 协作工作区，内置沙箱安全隔离、任务规划看板、Artifacts 成果交付与长效上下文记忆。
- **[TRAE Work](https://www.trae.ai/work)** 🆓 🍏 **`[字节办公 Agent A 级 / 零门槛]`**
  - **Primary Type**: General Work Agent | **Surface**: `Desktop / Web / Mobile`
  - **核心能力**：专为职场打造，支持商业分析报告生成、数据图表可视化、演示文稿排版与多模态调研。
- **[QoderWork](https://qoder.com/)** & **[QoderWake](https://qoder.com/)** ⚡ 🍏 **`[AI 虚拟员工 A 级]`**
  - **Primary Type**: Persistent Worker Runtime | **Surface**: `Desktop / Daemon`
  - **核心能力**：QoderWork 专注于桌面日常办公；QoderWake 则提供常驻本地的“数字化员工”，每个 Worker 具备独立身份、Memory、Skills 与专属工作区。
- **[OpenClaw](https://github.com/openclaw)** 🆓 🍏 **`[个人 Agent 网关 A 级]`**
  - **Primary Type**: Personal Agent / Gateway | **Surface**: `Desktop / CLI`
  - **核心能力**：本地个人自主代理网关，支持多渠道消息接入、系统任务自动化与技能包热加载。
- **[goose Desktop](https://github.com/block/goose)** 🆓 🍏 **`[开源通用 Agent S 级]`**
  - **Primary Type**: General-purpose Agent | **Surface**: `Desktop`
  - **核心能力**：Block 开源的通用桌面智能体，擅长代码重构、自动化研究与工具链调用。

---

### 05. Local Model Runtimes（本地大模型运行与推理引擎）

> **场景定位**：充分榨干 Mac 统一内存与 Metal 算力，在本地完全免费、离线、隐私安全地运行大模型。

- **[LM Studio](https://lmstudio.ai/)** 🆓 🍏 🍺 **`[小白体验最好 S 级 / 极低门槛]`**
  - **Primary Type**: Local Studio & Runtime | **Surface**: `Desktop / CLI (lms) / Daemon / API`
  - **核心能力**：Mac 上颜值最高的可视化模型管理工具。像应用商店一样一键搜索并下载 DeepSeek、Qwen、Llama 等 GGUF 模型，内置 Chat 界面并可一键启动兼容 OpenAI 的本地 API 服务。
  - **安装**：`brew install --cask lm-studio`
- **[Ollama](https://ollama.com/)** 🆓 🍏 🍺 **`[开发者装机标杆 S 级 / 低门槛]`**
  - **Primary Type**: Local Model Runtime | **Surface**: `CLI / Daemon / API`
  - **核心能力**：本地模型部署事实上的行业标准。终端输入 `ollama run deepseek-r1:8b` 即可自动拉取并运行，后台自动管理显存与并发。
  - **安装**：`brew install --cask ollama`
- **[Jan](https://jan.ai/)** 🆓 🍏 🍺 **`[开源纯净客户端 S 级 / 极低门槛]`**
  - **Primary Type**: Local AI Client & Runtime | **Surface**: `Desktop`
  - **核心能力**：100% 开源且注重隐私，界面体验极贴近 ChatGPT，支持全离线模型运行与自定义远端 API 聚合。
  - **安装**：`brew install --cask jan`
- **[llama.cpp](https://github.com/ggerganov/llama.cpp)** 🆓 🍏 🍺 **`[纯 C++ 底层基石 S 级 / 极客必选]`**
  - **Primary Type**: Local Inference Runtime | **Surface**: `CLI / Server`
  - **核心能力**：极致轻量与高能效比，Apple Silicon 纯 C++ 和 Metal 加速的核心技术底座。
  - **安装**：`brew install llama.cpp`
- **[MLX / MLX-LM](https://github.com/ml-explore/mlx)** 🆓 🍏 **`[Apple 官方框架 A 级 / 研发专精]`**
  - **Primary Type**: Apple Silicon AI Framework | **Surface**: `CLI / Python / API`
  - **核心能力**：苹果机器学习团队开源框架，专为 M 系列统一内存架构的高带宽吞吐优化设计。

---

### 06. AI Workspaces & Clients（多模型聚合桌面客户端）

> **场景定位**：不绑定单一厂商，一个客户端填入各大模型 API Key 或连接本地 Ollama，统管所有对话。

- **[Cherry Studio](https://cherry-studio.net/)** 🆓 🍏 🍺 **`[国内最火开源工作台 S 级 / 极低门槛]`**
  - **Primary Type**: Multi-model Workspace | **Surface**: `Desktop`
  - **核心能力**：支持聚合接入数十家云端大模型 API 与本地 Ollama；内置庞大的智能体（Agents）市场、支持多格式本地知识库挂载与 MCP 扩展。
  - **安装**：`brew install --cask cherry-studio`
- **[Chatbox](https://chatboxai.app/)** 🆓 🍏 🍺 **`[经典轻量客户端 S 级 / 极低门槛]`**
  - **Primary Type**: AI Client | **Surface**: `Desktop`
  - **核心能力**：经典开源跨平台客户端，简洁无冗余，支持 Prompt 预设管理与数据本地加密保存。
  - **安装**：`brew install --cask chatbox`
- **[Msty](https://msty.app/)** 🆓 🍏 **`[多模型对比神器 A 级 / 低门槛]`**
  - **Primary Type**: AI Workspace | **Surface**: `Desktop`
  - **核心能力**：支持同一个问题让多个模型分屏同时作答，直观对比不同模型的思考与生成质量。
- **[OpenCat](https://opencat.app/)** 💎 🍏 **`[原生极简客户端 A 级]`**
  - **Primary Type**: Native macOS Client | **Surface**: `Desktop / Menu Bar`
  - **核心能力**：采用 Swift 原生开发，极低内存占用与电量消耗，支持本地 MLX 模型与 iCloud 多端同步。

---

### 07. Knowledge & RAG（智能知识库与第二大脑）

> **场景定位**：管理海量个人笔记、技术文档与资料库，利用向量语义检索构建完全私密的第二大脑。

- **[ima (腾讯智能工作台)](https://ima.qq.com/)** 🆓 🍏 **`[中文知识库首选 S 级 / 零门槛]`**
  - **Primary Type**: Knowledge Agent Workspace | **Surface**: `Desktop`
  - **核心能力**：深度打通微信公众号、微信读书、网页与本地 PDF 知识沉淀；支持 Copilot 划词智能提炼、记忆管理（Memory）、Skills 技能包，并在最新版本中**原生支持 Copilot MCP 协议**。
- **[AnythingLLM](https://anythingllm.com/)** 🆓 🍏 🍺 **`[全能私有化 RAG S 级 / 低门槛]`**
  - **Primary Type**: Local-First RAG Workspace | **Surface**: `Desktop`
  - **核心能力**：开箱即用的个人/企业知识库桌面应用，拖入文档即可离线检索问答，内置多向量数据库隔离机制。
  - **安装**：`brew install --cask anythingllm`
- **[Obsidian + 插件生态](https://obsidian.md/)** 🆓 🍏 🍺 **`[双链笔记玩家必选 A 级]`**
  - **Primary Type**: Local Markdown Second Brain | **Surface**: `Desktop`
  - **必装 AI 插件**：
    - **Smart Connections** 🆓：利用本地 Embeddings 自动发现全库笔记之间的潜在语义联系。
    - **Copilot for Obsidian** 🆓：在侧边栏直接基于整库笔记上下文进行多轮问答。
  - **安装**：`brew install --cask obsidian`
- **[Notion AI](https://www.notion.so/)** ⚡ 🍏 🍺 **`[云端团队协作标杆 A 级]`**
  - **Primary Type**: Cloud Knowledge Workspace | **Surface**: `Desktop / Web`
  - **核心能力**：无缝融入页面块级编辑，支持跨页面全库问答、数据库字段自动提取与会议总结。
  - **安装**：`brew install --cask notion`
- **[NotebookLM](https://notebooklm.google.com/)** 🆓 **`[研报文献深度分析神器]`**
  - **Primary Type**: Research & Audio Notebook | **Surface**: `Web / PWA`
  - **核心能力**：Google 基于 Gemini 构建，支持同时上传数十篇长论文，一键生成极为逼真的双人对谈播客（Audio Overview）。

---

### 08. Productivity & System AI（系统级效率与全局快捷层）

> **场景定位**：嵌入 macOS 系统底层与交互细节，从快捷启动、划词翻译到自动化执行。

- **[Raycast (Raycast AI)](https://www.raycast.com/)** ⚡ 🍏 🍺 **`[Mac 必备第一神器 S 级 / 极低门槛]`**
  - **Primary Type**: AI Launcher / OS Command Layer | **Surface**: `Desktop / Launcher`
  - **核心能力**：替代 Spotlight 的超级启动器。按下快捷键随时全局提问、选中文本一键改写润色、翻译代码、调用自定义 AI 命令库与操作系统设置。
  - **安装**：`brew install --cask raycast`
- **[Bob](https://bobtranslate.com/)** 💎 🍏 🍺 **`[划词翻译天花板 S 级 / 极低门槛]`**
  - **Primary Type**: OCR & Translate Utility | **Surface**: `Desktop / Menu Bar`
  - **核心能力**：macOS 划词翻译标杆软件，无缝接入各大模型 API，支持精准的长句学术润色、语法解析与截图 OCR。
- **[PopClip](https://pilotmoon.com/popclip/)** 💎 🍏 🍺 **`[划词增强胶囊 A/S 级 / 极低门槛]`**
  - **Primary Type**: Contextual Selection Tool | **Surface**: `Desktop Floating`
  - **核心能力**：鼠标选中文本即刻弹出操作气泡，配合 AI 扩展一键语法纠错、扩写、生成摘要或提取代码。
- **[CleanShot X](https://cleanshot.com/)** 💎 🍏 **`[顶尖截图 OCR A 级 / 零门槛]`**
  - **Primary Type**: Capture & OCR Utility | **Surface**: `Desktop`
  - **核心能力**：体验极佳的截图录屏软件，内置 AI 驱动的高精度本地 OCR 文字识别与二维码提取。

---

### 09. Voice & Transcription（语音转写与会议纪要）

> **场景定位**：结合本地 Metal 算力，实现极速、高精度、完全离线的语音转文字与会议总结。

- **[MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper)** ⚡ 🍏 🍺 **`[离线转写标杆 S 级 / 零门槛]`**
  - **Primary Type**: Transcription & Meeting App | **Surface**: `Desktop + CLI`
  - **核心能力**：基于 OpenAI Whisper 的 macOS 原生应用，拖入音频瞬间生成精准字幕与逐字稿，完全在本地离线运行保护隐私。
  - **安装**：`brew install --cask macwhisper`
- **[VoiceInk](https://github.com/)** 🆓 🍏 **`[开源语音输入法 S 级 / 极低门槛]`**
  - **Primary Type**: Voice Dictation | **Surface**: `Desktop`
  - **核心能力**：全局长按快捷键说话，松开立刻在当前光标处打出排版完美的文字，告别打字。
- **[Granola](https://www.granola.so/)** ⚡ 🍏 **`[AI 会议笔记神器 S 级 / 零门槛]`**
  - **Primary Type**: Meeting AI Notepad | **Surface**: `Desktop`
  - **核心能力**：开会时无需逐字记录，手写少量要点后 AI 自动结合会议音频生成结构清晰的高质量会议纪要。
- **[Superwhisper](https://superwhisper.com/)** ⚡ 🍏 **`[专业级原生语音听写 A 级]`**
  - **Primary Type**: AI Dictation | **Surface**: `Desktop`
  - **核心能力**：针对不同应用自动切换不同的转写语气和词汇偏好。

---

### 10. AI Design & Creative（AI 设计、UI/UX 与视觉创意）

> **场景定位**：从营销物料、UI/UX 原型生成、矢量图标设计到本地离线高精度绘图。

- **[MiniMax Design (海螺创意 / MiniMax 视觉)](https://www.minimax.io/)** ⚡ 🍏 **`[创意与物料神器 S 级 / 小白友好]`**
  - **Primary Type**: Visual & Creative Design Platform | **Surface**: `Desktop / Web`
  - **核心能力**：依托 MiniMax 多模态视觉模型，专为营销海报、UI 概念图与商业视觉物料设计；文字渲染精准、中文理解深刻，零设计基础一键出图。
- **[OpenDesign](https://github.com/)** 🆓 🍏 **`[设计到代码交付 S 级 / 开发者与设计师桥梁]`**
  - **Primary Type**: Open Design-to-Code Framework | **Surface**: `Desktop / CLI / Web`
  - **核心能力**：支持通过自然语言 Prompt 或线框草图，自动生成生产级 React/Tailwind/Vue 组件与规范设计资产，打通 Figma 与本地代码库。
- **[v0 (by Vercel)](https://v0.dev/)** ⚡ 🍏 **`[Web 原型设计顶流 S 级 / 极低门槛]`**
  - **Primary Type**: Generative UI / Design-to-Code | **Surface**: `Web / CLI`
  - **核心能力**：自然语言描述界面或上传草图截图，瞬间生成完全可交互的现代化前端 UI 页面与高质量代码。
- **[Recraft](https://www.recraft.ai/)** ⚡ 🍏 🍺 **`[矢量图与 Icon 第一神器 S 级 / 极低门槛]`**
  - **Primary Type**: Vector & Icon AI Design Tool | **Surface**: `Desktop / Web`
  - **核心能力**：专为 UI 设计师打造，**最大亮点是能直接导出无损 SVG 矢量图**、3D 图标与统一风格的设计系统资产（Design System）。
- **[Draw Things](https://drawthings.ai/)** 🆓 🍏 **`[Mac 本地生图第一标杆 S 级 / 低门槛]`**
  - **Primary Type**: Local Stable Diffusion Studio | **Surface**: `Desktop + CLI (draw-things-cli)`
  - **核心能力**：专为 Apple Silicon 统一内存优化，完美支持 8-bit 量化，出图快、省内存，完全断网离线保护隐私，现已推出 CLI 接口。
- **[Upscayl](https://upscayl.org/)** 🆓 🍏 🍺 **`[一键高清修复 A 级 / 零门槛]`**
  - **Primary Type**: AI Image Upscaler | **Surface**: `Desktop`
  - **核心能力**：完全开源免费，一键将模糊截图、老照片放大 4 倍至 4K/8K 分辨率。
  - **安装**：`brew install --cask upscayl`
- **[ComfyUI](https://github.com/comfyanonymous/ComfyUI)** 🆓 🍏 **`[专业节点流 S 级 / 极客专精]`**
  - **Primary Type**: Node-based Generative Workflow | **Surface**: `Web UI / CLI`
  - **核心能力**：自由拼接 ControlNet、LoRA 与重绘工作流，是高阶视觉创作者的终极引擎。

---

### 11. Agentic Terminals & Browsers（智能体终端与 AI 原生浏览器）

> **场景定位**：环境本身即具备智能交互感知的终端与浏览器。

- **[Warp](https://www.warp.dev/)** ⚡ 🍏 🍺 **`[现代化智能终端 S 级]`**
  - **Primary Type**: Agentic Terminal | **Surface**: `Terminal App`
  - **核心能力**：Rust 与 Metal GPU 加速；内置 Warp AI，支持自然语言转换 Shell 命令、会话报错智能排查与工作流云端协作。
  - **安装**：`brew install --cask warp`
- **[Opera Neon](https://www.opera.com/)** 🆓 🍏 **`[Agentic 浏览器标杆 S 级]`**
  - **Primary Type**: Agentic Browser | **Surface**: `Browser + Browser CLI + MCP`
  - **核心能力**：内置 **MCP Connector** 与 **`opera-browser-cli`**，允许 Claude Code / OpenClaw 等外部 Agent 直接操作用户当前已经登录的真实浏览器会话。
- **[Perplexity Comet](https://www.perplexity.ai/)** ⚡ 🍏 **`[AI 搜索原生浏览器 S 级]`**
  - **Primary Type**: AI Browser | **Surface**: `Browser`
  - **核心能力**：深度集成 Perplexity 交叉搜索，支持跨标签页信息提炼与智能侧边栏。
- **[Dia](https://dia.com/)** ⚡ 🍏 **`[极简 AI 浏览器 A 级]`**
  - **Primary Type**: AI Browser | **Surface**: `Browser`
  - **核心能力**：以极简界面著称，内置网页交互 Skills 自动化与内容总结。

---

### 12. Agent Managers & Control Planes（智能体管理器与控制平面）

> **场景定位**：随着各类 Agent 增多，用于统一监控、管理、调度与配置多个 Agent 实例的控制台。

- **[Supacode](https://github.com/)** ⚡ 🍏 **`[编码 Agent 管理器 A/S 级]`**
  - **Primary Type**: Coding Agent Manager | **Surface**: `Desktop`
  - **核心能力**：集中管理 Claude Code、Codex CLI 等多个并发任务进程，提供图形化进度追踪与状态监控。
- **[Kiro Crew](https://kiro.dev/)** ⚡ 🍏 **`[持久化 Agent 工作区 A/S 级]`**
  - **Primary Type**: Persistent Agent Workspace | **Surface**: `Desktop / CLI / Web`
  - **核心能力**：团队化持久运行的个人与业务智能体集群管理，独立于 IDE 存在。
- **[CodexBar](https://github.com/)** 🆓 🍏 **`[菜单栏配额监控 A 级]`**
  - **Primary Type**: Agent Usage Monitor | **Surface**: `Menu Bar`
  - **核心能力**：常驻 macOS 顶部菜单栏，随时查看 Codex、Claude、Cursor 等各大模型 API 配额与费用消耗。

---

### 13. IDE Extensions & Plugins（编辑器插件与扩展体系）

> **场景定位**：寄生于宿主编辑器（VS Code / JetBrains / Xcode）中的辅助插件。

- **[GitHub Copilot](https://github.com/features/copilot)** 💎 **`[S 级]`**：官方行内补全与 Copilot Chat 侧边栏。
- **[Cline](https://github.com/cline/cline)** 🆓 🍏 **`[A/S 级]`**：经人类逐步确认的终端命令执行与跨文件修改代理。
- **[Roo Code (Roo Cline)](https://github.com/RooVetGit/Roo-Cline)** 🆓 🍏 **`[A 级]`**：增强分支版本，支持针对架构师、编码者不同角色设定自定义模式。
- **[Kilo Code](https://github.com/kilo-ai)** 🆓 🍏 **`[A 级]`**：支持多模型热切换与技能扩展包管理。
- **[Augment Code (Auggie)](https://www.augmentcode.com/)** 💎 **`[企业级 A 级]`**：面向超大型代码库的深度依赖图谱索引与精准代码补全。

---

### 14. Browser & Computer-Use Infra（浏览器与电脑控制基础设施）

> **场景定位**：让外部 Agent（如 Claude Code、Antigravity CLI）能够安全操控真实浏览器或 macOS GUI 的中间件。

- **`opera-browser-cli`**：允许命令行 Agent 直接调用已运行的 Opera Neon 浏览器执行网页任务。
- **Opera Neon MCP Connector**：将已登录的真实网页会话作为标准 MCP 工具暴露给外部智能体。
- **Playwright**：现代 Web 自动化底座，供 Agent 构建自动化测试与动态页面数据提取。
- **Chrome DevTools MCP**：将 Chrome / Chromium 的远程调试端口桥接为标准 MCP 协议。
- **Juno / Agent! / Local Operator**：基于 Accessibility API、AppleScript 与视觉多模态的本地桌面 GUI 操作代理。

---

### 15. Evaluation & Harnesses（智能体评测基准与测试套件）

> **场景定位**：用于衡量、测试与验证大模型及 Agent 编码与推理能力的专业框架。

- **[SWE-bench / SWE-harness](https://github.com/princeton-nlp/SWE-bench)** 🆓 🍏 **`[黄金评测基准 S 级]`**
  - **核心能力**：评估大语言模型解决真实 GitHub 仓库 Issue 能力的行业黄金标准评测套件。
- **[Promptfoo](https://github.com/promptfoo/promptfoo)** 🆓 🍏 🍺 **`[Prompt 与安全测试 S 级]`**
  - **核心能力**：CLI 与轻量 WebUI 工具，系统化评测 Prompt 质量、模型输出一致性与防越狱安全测试。
  - **安装**：`brew install promptfoo`
- **[AgentBench](https://github.com/THUDM/AgentBench)** 🆓 🍏 **`[多维 Agent 评测 A 级]`**
  - **核心能力**：清华大学等开源的多维度 LLM 智能体综合能力评测基准。

---

### 16. Archive & Legacy（归档与已停运项目清单）

> ⚠️ **避免装错与踩坑**：明确记录停止服务、主产品更名或进入维护期的项目：

| 产品名称 | 历史身份 | 变动原因与迁移建议 | 状态标记 |
| :--- | :--- | :--- | :---: |
| **ChatGPT Atlas** | AI 原生浏览器 | 已于 2026-08-09 正式停运，浏览器 Agent 能力已整合至 ChatGPT Desktop / Codex | ❌ **Deprecated** |
| **Gemini CLI (个人)** | 个人终端客户端 | 2026-06 停止对个人账户服务，个人用户请统一使用 **Antigravity CLI** | ⚠️ **Legacy** |
| **Windsurf** | 独立 AI IDE | 品牌与底层架构正式升级过渡为 **Devin Desktop**（内置 Devin Local） | 🔄 **Transitioned** |
| **Continue** | 开源编码插件 | 团队加入 Cursor，原开源仓库停止功能迭代转为 Read-only 维护状态 | ⚠️ **Maintenance Ended** |
| **ChatGPT Classic** | 早期单体聊天客户端 | 功能已全面转向包含 Chat+Work+Codex 的统一架构新版 macOS App | ⚠️ **Legacy App** |

---

## 💡 Apple Silicon 统一内存本地部署配置选型指南

在 Mac 上运行本地模型，**统一内存（Unified Memory）容量是唯一的决定性瓶颈**：

```text
┌─────────────────┬───────────────────────────────┬──────────────────────────────────────────┐
│   统一内存规格   │        推荐模型量化规格        │                 经典模型推荐              │
├─────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 8GB - 16GB      │ 1.5B ~ 8B (4-bit Q4_K_M)      │ Qwen2.5-7B, Llama-3.1-8B, DeepSeek-7B    │
│ 24GB - 36GB     │ 14B ~ 32B (4-bit Q4_K_M)     │ Qwen2.5-14B/32B, DeepSeek-Coder-33B      │
│ 64GB - 128GB    │ 70B ~ 72B (4-bit / 8-bit)    │ Qwen2.5-72B-Instruct, Llama-3.3-70B      │
│ 128GB+ (M Max)  │ MoE 专家混合大模型 / 70B+ FP16│ DeepSeek-R1/V3 蒸馏版, 巨型知识库 RAG    │
└─────────────────┴───────────────────────────────┴──────────────────────────────────────────┘
```

---

## 🤝 参与贡献 (Contributing)

欢迎提交 Issue 或 Pull Request 推荐优秀的 macOS AI 工具：
1. **核验标准**：请确保推荐的项目在 macOS（优先 Apple Silicon）上有良好体验。
2. **多维标注**：提交时请注明 `Primary Type`、`Surface`、`Capabilities` 及开源状态。

---

*Licensed under [MIT](LICENSE).*
