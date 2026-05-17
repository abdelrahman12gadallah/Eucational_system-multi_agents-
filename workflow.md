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