Markdown# OmniBrain: Agentic Multimodal Financial RAG 🧠📊

OmniBrain is an enterprise-grade, agentic Multimodal Retrieval-Augmented Generation (RAG) system engineered to parse, analyze, and synthesize insights from complex financial filings (such as SEC 10-K and 10-Q reports). 

Powered by **LangGraph**, **Gemini Flash Vision Models**, and **PyMuPDF**, the architecture autonomously routes incoming natural language questions to specialized retrieval and computer-vision pipelines.

---

## 🌟 Architecture & Capabilities

              ┌───────────────────────────────┐
              │    User Financial Query       │
              └──────────────┬────────────────┘
                             │
                             ▼
              ┌───────────────────────────────┐
              │     LangGraph Supervisor      │
              └──────┬─────────────────┬──────┘
                     │                 │
        (Text / RAG) │                 │ (Visual / Multimodal)
                     ▼                 ▼
      ┌─────────────────────┐   ┌───────────────────────────┐
      │  Search Agent (RAG) │   │    Vision Agent (Gemini)  │
      │  - Vector Retrieval │   │    - PyMuPDF Page Render  │
      │  - Context Ranking  │   │    - Multi-Model Fallback │
      └──────────┬──────────┘   └─────────────┬─────────────┘
                 │                            │
                 └─────────────┬──────────────┘
                               │
                               ▼
      ┌─────────────────────────────────────────────────────┐
      │    Synthesis Node (Executive Summary & Fallbacks)   │
      └────────────────────────┬────────────────────────────┘
                               │
                               ▼
              ┌───────────────────────────────┐
              │   Structured Markdown Output  │
              └───────────────────────────────┘

- **LangGraph Supervisor Routing:** Intelligently classifies user queries to dispatch either semantic RAG retrieval nodes or visual document inspection engines.
- **Multimodal Visual Parser:** Extracts high-density tabular disclosures, stock performance comparisons, and financial statements directly from PDF document pages via PyMuPDF rendering and Gemini Vision APIs.
- **Resilient Multi-Model Fallback Pipeline:** Survives API throttling and temporary server spikes (such as HTTP 503) through a cascade of models (`gemini-2.5-flash`, `gemini-1.5-flash`, `gemini-3.8-flash`) combined with a fail-safe local PyMuPDF extraction engine.
- **Zero-Noise Financial Synthesis:** Post-processing filtering guarantees that raw excerpt tags, scraping artifacts, and document metadata headers are cleaned before executive summaries are rendered.

---

## 🛠️ Tech Stack

- **Orchestration:** LangGraph / LangChain
- **LLMs & Vision:** Google Gemini API (`gemini-2.5-flash`, `gemini-1.5-flash`)
- **PDF & Image Processing:** PyMuPDF (`fitz`), Pillow
- **Frontend & Deployment:** Streamlit, Streamlit Cloud

---

## 📂 Repository Structure

```text
OmniBrain-Agentic-Multimodal-RAG/
│
├── agents/
│   ├── supervisor.py         # Routes query to Search, Vision, or SQL agents
│   └── search_agent.py       # Vector retrieval and semantic chunk extraction
│
├── graph/
│   ├── state.py              # TypedDict agent state definitions
│   └── workflow.py           # LangGraph state machine, nodes, and synthesis logic
│
├── vision/
│   └── image_processor.py    # PyMuPDF rendering, Gemini vision extraction, fallbacks
│
├── rag/
│   └── pdf_loader.py         # Document ingestion and layout parsing
│
├── frontend/
│   └── app.py                # Streamlit UI interface and document indexing triggers
│
├── data/                     # Ingested PDF financial filings (e.g., Apple 10-K)
├── requirements.txt          # Python dependencies
└── README.md
🚀 Getting Started1. Clone the RepositoryBashgit clone [https://github.com/KAVINGUPTA09/OmniBrain-Agentic-Multimodal-RAG1.git](https://github.com/KAVINGUPTA09/OmniBrain-Agentic-Multimodal-RAG1.git)
cd OmniBrain-Agentic-Multimodal-RAG1
2. Set Up Virtual EnvironmentBashpython -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
3. Install DependenciesBashpip install --upgrade pip
pip install -r requirements.txt
4. Configure API KeysCreate a .env file in the root directory (or configure Secrets in Streamlit Cloud):Code snippetGEMINI_API_KEY=your_gemini_api_key_here
5. Launch the Streamlit AppBashstreamlit run frontend/app.py
💡 Example QueriesModeSample QueryVision Extractionvision: Extract the gross margin table and percentages for Products vs Services on page 23 of the Apple 10-K document.Vision Extractionvision: Analyze the tables and financial numbers on page 28 of the Apple 10-K document.Search / RAGFrom the Apple 10-K 2024 filing, what was the total net sales for fiscal year 2024, and what was the percentage breakdown between Products and Services? Provide exact dollar amounts and YoY growth.Search / RAGWhat were Apple's net sales specifically for iPhone, Mac, and Wearables in fiscal year 2024 compared to 2023?🛡️ LicenseDistributed under the MIT License. See LICENSE for more information.
4. Niche **"Commit changes..."** button par click kar do.

---

### Option 2: VS Code Terminal se push karna

Agar VS Code se karna chahte ho:
1. VS Code mein root folder par `README.md` open karo aur upar wala content paste karke **`Ctrl + S`** daba do.
2. Terminal mein dono remotes par push kar do:

```powershell
git add README.md
git commit -m "docs: update comprehensive agentic multimodal rag readme"
git push myfork member2-rag
git push origin member2-rag
