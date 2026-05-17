## 📊 System Architecture & Module Boundaries

The system completely transcends a single monolithic pipeline by decomposing the educational workflow into **6 specialized, highly communicative agents** with explicit, traceable inter-agent contracts and dynamic, query-driven routing.

### 🤖 The 6-Agent Collaborative Framework

1. **🛡️ Input Guardrail & Language Detector (`agents.py` & `tasks.py`)**
   * **Role:** Validates all natural language user inputs before passing them to the core LLM.
   * **Function:** Mitigates adversarial prompt-injection attacks, filters unsafe inputs, and detects the target language (Arabic/English), ensuring extreme robustness and safety.
2. **🔍 Knowledge Retrieval Specialist (`agents.py` & `tasks.py`)**
   * **Role:** Orchestrates the semantic data lookup and synthesis.
   * **Function:** Seamlessly combines local PDF context fetched via custom **RAG** tools with the foundational internal knowledge of the underlying LLM (`Llama-3.3-70b-versatile`).
3. **📐 Curriculum Architect (`agents.py` & `tasks.py`)**
   * **Role:** Formulates educational psychology-based pathways.
   * **Function:** Transforms raw synthesized knowledge dossiers into structured, logical, 3-lesson academic syllabi with defined learning outcomes.
4. **✍️ Educational Content Writer (`agents.py` & `tasks.py`)**
   * **Role:** Drafting and pedagogical content creation.
   * **Function:** Expands the syllabus outlines into comprehensive, richly structured Markdown-formatted text explanations tailored to the user's language.
5. **📝 Assessment & Evaluation Specialist (`agents.py` & `tasks.py`)**
   * **Role:** Continuous evaluation and psychometrics.
   * **Function:** Autonomously builds high-quality 5-question Multiple Choice Question (MCQ) quizzes based *only* on the newly drafted lesson text, complete with options, correct keys, and exhaustive reasoning.
6. **⚖️ Output Filter & Multilingual Reviewer (`agents.py` & `tasks.py`)**
   * **Role:** Output Guardrails and Quality Assurance.
   * **Function:** Inspects, refines, and filters the final generated output package before rendering to eliminate hallucinations, guarantee factual grounding, and enforce flawless formatting.

---

## 🛠️ Advanced Tool Integration & Memory Infrastructure

### 📥 1. Retrieval-Augmented Generation (RAG)
* Implemented a zero-hardcoded local PDF ingestion pipeline inside `tools.py`.
* Dynamically parses all uploaded academic notes and documents residing inside the `knowledge_base/` directory using an optimized `PdfReader` pipeline.
* Performs semantic line-filtering against user queries to feed contextual ground truth straight into the agent framework, ensuring the response is strictly grounded in the course's actual curriculum.

### 🧠 2. Persistent Cross-Session Student Memory
* Implemented an advanced, stateful local disk indexing system that logs student historical pathways (`memory_STUDENT-XXXX.txt`).
* Over successive interactions, the **Knowledge Retrieval Specialist** reads the student's unique historical profile.
* **Demonstrable Quality Enhancement:** The system inherently adapts to what the student has previously studied, tracking progression, avoiding redundancies, and building increasingly personalized academic content.

### 🌐 3. Out-of-Knowledge Fallback Strategy
* If a student requests information entirely outside the scope of the local files in `knowledge_base/`, the system gracefully defaults to the LLM's **Foundational Internet Knowledge Base**.
* The system explicitely flags this to the student via the Reviewer UI tab (*"Content sourced outside the local knowledge base"*), maintaining perfect transparency and preventing system freezes or blind spots.

---

## 🎨 Professional User Interface (Streamlit)

The system exposes a clean, corporate-themed, multi-tab interface built entirely via **Streamlit** incorporating an asynchronous execution monitor:
* **📖 Approved Educational Content Tab:** Displays the fully detailed explanations with direct Markdown download capability.
* **📝 Smart Quiz Tab:** Renders interactive, real-time assessment questions.
* **🛡️ Security & Guardrails Report Tab:** Shows full transparency logs detailing the Input Guardrail clearance and Output filtering metrics.
* **📊 Architecture Analytics Tab:** Breaks down the active agent execution graphs, process parameters, and metric tracking for evaluation.

---

## 📁 Modular Project Structure

The codebase strictly follows clean architectural boundaries to ease grading and future scaling:


📦 EduSphere System Workflow (Sequential Tree)
│
└── 🌐 [User Input: Topic & Language] (e.g., "Explain RAG vs CAG" | Arabic)
    │
    └── 🛠️ Step 1: 🛡️ Input Guardrail & Language Detector (Agent 1)
        ├── 📋 Task: Scan for Prompt Injections / Detect Target Language
        └── 📤 Output: [Safety Clearance Status: SAFE] + Sanitized Query
            │
            └── 🛠️ Step 2: 🔍 Knowledge Retrieval Specialist (Agent 2)
                ├── 📥 Injects Local Context: RAG (Reads from /knowledge_base/ Folder)
                ├── 📥 Injects History: Persistent Disk Memory (Reads memory_STUDENT.txt)
                ├── 📋 Task: Synthesize Data (Local PDFs + LLM Foundational Knowledge)
                └── 📤 Output: [Comprehensive Raw Knowledge Dossier]
                    │
                    └── 🛠️ Step 3: 📐 Curriculum Architect (Agent 3)
                        ├── 📋 Task: Structure pedagogical path based on the dossier
                        └── 📤 Output: [Structured 3-Lesson Syllabus Blueprint]
                            │
                            └── 🛠️ Step 4: ✍️ Educational Content Writer (Agent 4)
                                ├── 📋 Task: Expand syllabus into detailed, engaging tutorials
                                └── 📤 Output: [Rich Markdown Lesson Explanations] ──┐
                                    │                                                 │ (Passes both
                                    ├───▶ 🛠️ Step 5: 📝 Assessment Specialist (Agent 5)│  Content & Quiz)
                                    │   ├── 📋 Task: Build a 5-question MCQ quiz      │
                                    │   └── 📤 Output: [Smart Quiz with Answers & Keys]│
                                    │                                                 │
                                    └───────────────────────▶  ⚖️  ◀──────────────────┘
                                                              │
                                            🛠️ Step 6: ⚖️ Output Filter & Multilingual Reviewer (Agent 6)
                                                ├── 📋 Task: Scrub for hallucinations, refine translation, enforce format
                                                └── 📤 Output: [Polished, Verified Final Educational Package]
                                                    │
                                                    └── 🎨 [Streamlit UI Multi-Tab Rendering]
                                                        ├── 📖 Approved Educational Content Tab
                                                        ├── 📝 Smart Quiz Tab
                                                        └── 🛡️ Security & Guardrails Report Tab

[task_guardrail] (Outputs: Cleared Query)
       │
       ▼
[task_retrieval] (Context: [task_guardrail] + Python Local Functions for Memory & RAG)
       │
       ▼
[task_curriculum] (Context: [task_retrieval])
       │
       ▼
[task_content] (Context: [task_curriculum]) ──┐
       │                                       │
       ▼ (Passes Content)                      │ (Passes Content for evaluation)
[task_quiz]                                    ▼
       │                              [task_finalize] (Context: [task_content, task_quiz])
       └───────────────────────────────▶ Outputs strictly verified data to app.py
