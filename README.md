# OmniBrain: Agentic Multimodal Financial RAG 🧠📊

OmniBrain is an agentic Multimodal Retrieval-Augmented Generation (RAG) system engineered to parse, analyze, and synthesize insights from SEC 10-K and financial filings. Orchestrated via **LangGraph**, it dynamically routes queries between a **Semantic Vector RAG Agent**, a **Gemini Multimodal Vision Agent**, and a structured **SQL Analytics Engine**.

---

## 🏛️ System Architecture

```text
                           ┌───────────────────────────────┐
                           │    User Financial Query       │
                           └──────────────┬────────────────┘
                                          │
                                          ▼
                           ┌───────────────────────────────┐
                           │     LangGraph Supervisor      │
                           └──────┬───────┬─────────┬──────┘
                                  │       │         │
               ┌──────────────────┘       │         └──────────────────┐
               ▼                          ▼                            ▼
  ┌─────────────────────────┐  ┌─────────────────────┐  ┌─────────────────────────────┐
  │   Search Agent (RAG)    │  │ Vision Agent (VLM)  │  │     SQL Analytics Agent     │
  │ - In-Memory / Vector DB │  │ - PyMuPDF Page Dumps│  │ - Structured Database Lookup│
  │ - Semantic Chunk Match  │  │ - Multi-Model Fallback││ - Financial Math Aggregation│
  └────────────┬────────────┘  └──────────┬──────────┘  └──────────────┬──────────────┘
               │                          │                            │
               └──────────────────┐       │       ┌────────────────────┘
                                  ▼       ▼       ▼
                           ┌───────────────────────────────┐
                           │    Executive Synthesis Node   │
                           │ - Clean Markdown Formatter    │
                           │ - Metadata Artifact Stripper  │
                           └──────────────┬────────────────┘
                                          ▼
                           ┌───────────────────────────────┐
                           │   Streamlit Web Interface    │
                           └───────────────────────────────┘
⚡ Key CapabilitiesDeterministic Supervisor Routing: Identifies visual cues (table, chart, page), database intents (sql, grouped by, revenue), or standard research questions to route directly to the optimal sub-agent.Multimodal Document Vision: Converts target PDF pages to images via PyMuPDF and utilizes Gemini Vision (gemini-2.5-flash, gemini-1.5-flash) to reconstruct complex financial matrices and indexed comparison graphs.Resilient Cascade Fallbacks: Safeguards API uptime against 503 load spikes with automatic multi-model retry cascades and direct in-memory PyMuPDF extraction fallbacks.Zero-Artifact Output Engine: Post-processing pipeline sanitizes raw ingestion artifacts, scrap tags ([Excerpt X]), and repetitive header rows into clean executive tables.📁 Repository StructurePlaintext├── agents/
│   ├── supervisor.py         # Deterministic routing logic (SQL vs Vision vs Search)
│   ├── search_agent.py       # Semantic vector retrieval and context ranking
│   └── sql_agent.py          # Structured analytical query processing
├── graph/
│   ├── state.py              # LangGraph AgentState TypedDict schema
│   └── workflow.py           # State machine execution graph and synthesis nodes
├── vision/
│   └── image_processor.py    # PyMuPDF page rendering and Gemini Vision extraction
├── rag/
│   └── pdf_loader.py         # Financial document ingestion and chunk indexing
├── frontend/
│   └── app.py                # Streamlit UI dashboard and real-time trace display
├── data/                     # Ingested PDF filings (e.g., Apple FY24 10-K)
├── requirements.txt          # Production dependencies
└── README.md                 # Project documentation
🚀 Quick Start Guide1. Setup Local EnvironmentBashgit clone https://github.com/KAVINGUPTA09/OmniBrain-Agentic-Multimodal-RAG1.git
cd OmniBrain-Agentic-Multimodal-RAG1
python -m venv venv
.\venv\Scripts\activate   # Linux/macOS: source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
2. Configure Environment KeysCreate a .env file in the root folder:Code snippetGEMINI_API_KEY=your_gemini_api_key_here
3. Launch ApplicationBashstreamlit run frontend/app.py
🧪 Benchmark PromptsTarget NodeQuery FormulationVision Agentvision: Extract the gross margin table and percentages for Products vs Services on page 23 of the Apple 10-K document.SQL EngineRun a SQL query to calculate the average quarterly revenue for 2024.Search / RAGFrom the Apple 10-K 2024 filing, what was the total net sales for fiscal year 2024, and what was the percentage breakdown between Products and Services?📜 LicenseDistributed under the MIT License. See LICENSE for details.
