# Enterprise-technical-support-Agentic-RAG-chatbot
This RAG chatbot helps to answer typical technical questions from complex large pool of technical documents with noisy data. It dynamically decides whether to retrieve documents or answer from conversation history. Answers are grounded with citations. 

The chatbot also incorporates input guardrails, LangGraph-based orchestration, LLM Gateway integration, conversational memory, document citations, and retrieval reranking to provide reliable and traceable technical answers.

# Intelligent flow diagram
```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'fontSize': '13px',
    'lineColor': '#94A3B8',
    'edgeLabelBackground': '#1E293B',
    'textColor': '#E2E8F0'
  },
  'flowchart': {
    'curve': 'stepAfter',
    'nodeSpacing': 35,
    'rankSpacing': 40
  }
}}%%
graph TD
    %% 3-Color High-Contrast Palette
    classDef default fill:#1E293B,stroke:#64748B,stroke-width:1.5px,color:#F8FAFC;
    classDef core fill:#0F172A,stroke:#3B82F6,stroke-width:1.5px,color:#93C5FD;
    classDef alert fill:#450A0A,stroke:#EF4444,stroke-width:1.5px,color:#FCA5A5;

    %% Global Line Styling (Bright Slate for dark backgrounds)
    linkStyle default stroke:#94A3B8,stroke-width:1.5px;

    %% Ingestion Pipeline (Feeds Qdrant)
    Docs[Documents<br/>PDF, HTML]:::default --> Embed[Gemini Embeddings]:::default
    Embed --> DB[(Qdrant VectorDB)]:::default

    %% User Request Flow
    User((User)):::default --> UI[Streamlit UI]:::default
    UI --> API[FastAPI /query]:::default
    API --> Guard{NeMo Guardrails}:::alert

    %% Guardrail Decisions
    Guard -->|Blocked| BlockedMsg[Blocked Screen]:::alert
    Guard -->|Pass| Planner{Planner Node}:::core

    %% Planner Routing
    Planner -->|Conversational| Responder[Responder Node]:::core
    Planner -->|Technical| Retriever[Retriever Node]:::default

    %% Retrieval & Reranking
    DB -.->|Query Match| Retriever
    Retriever --> Reranker[FlashRank Reranker]:::default
    Reranker --> Responder

    %% Response Delivery & State
    Responder -.-> Memory[(LangGraph Memory)]:::default
    Responder --> Out[Streamlit Response View]:::default
```