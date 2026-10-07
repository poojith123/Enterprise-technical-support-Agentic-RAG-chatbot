# Enterprise-technical-support-Agentic-RAG-chatbot
This RAG chatbot helps to answer typical technical questions from complex large pool of technical documents with noisy data. It dynamically decides whether to retrieve documents or answer from conversation history. Answers are grounded with citations. 

The chatbot also incorporates input guardrails, LangGraph-based orchestration, LLM Gateway integration, conversational memory, document citations, and retrieval reranking to provide reliable and traceable technical answers.

# Intelligent flow diagram
```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'fontSize': '13px',
    'primaryTextColor': '#FFFFFF',
    'textColor': '#FFFFFF',
    'lineColor': '#94A3B8',
    'edgeLabelBackground': '#334155'
  },
  'flowchart': {
    'curve': 'stepAfter',
    'nodeSpacing': 40,
    'rankSpacing': 45
  }
}}%%
graph TD
    %% Explicit Edge Label CSS Overrides for GitHub Dark Mode
    classDef default fill:#1E293B,stroke:#64748B,stroke-width:1.5px,color:#FFFFFF;
    classDef core fill:#0F172A,stroke:#3B82F6,stroke-width:1.5px,color:#93C5FD;
    classDef alert fill:#450A0A,stroke:#EF4444,stroke-width:1.5px,color:#FCA5A5;

    %% Global Edge styling
    linkStyle default stroke:#94A3B8,stroke-width:1.5px;

    %% Ingestion Pipeline
    Docs[Documents<br/>PDF, HTML]:::default --> Embed[Gemini Embeddings]:::default
    Embed --> DB[(Qdrant VectorDB)]:::default

    %% User Request Flow
    User((User)):::default --> UI[Streamlit UI]:::default
    UI --> API[FastAPI /query]:::default
    API --> Guard{NeMo Guardrails}:::alert

    %% Guardrail Decisions
    Guard -->|Blocked| BlockedMsg[Blocked Screen]:::alert
    BlockedMsg --> UI
    Guard -->|Pass| Planner{Planner Node}:::core

    %% Planner Routing
    Planner -->|Conversational| Responder[Responder Node]:::core
    Planner -->|Technical| Retriever[Retriever Node]:::default

    %% Retrieval & Reranking
    DB -.->|Query Match| Retriever
    Retriever --> Reranker[FlashRank Reranker]:::default
    Reranker --> Responder

    %% Response Delivery & Memory
    Responder -.-> Memory[(LangGraph Memory)]:::default
    Responder -->|Return Response| UI
```