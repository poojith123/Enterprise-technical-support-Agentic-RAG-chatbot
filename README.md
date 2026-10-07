# Enterprise-technical-support-Agentic-RAG-chatbot
This RAG chatbot helps to answer typical technical questions from complex large pool of technical documents with noisy data. It dynamically decides whether to retrieve documents or answer from conversation history. Answers are grounded with citations. 

The chatbot also incorporates input guardrails, LangGraph-based orchestration, LLM Gateway integration, conversational memory, document citations, and retrieval reranking to provide reliable and traceable technical answers.

# Intelligent flow diagram
```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'fontSize': '13px'}, 'flowchart': {'curve': 'stepAfter', 'nodeSpacing': 35, 'rankSpacing': 40}}}%%
graph TD
    %% 3-Color Clean Palette: Slate (Default), Blue (Core Agent), Rose (Alert)
    classDef default fill:#1E293B,stroke:#475569,stroke-width:1.5px,color:#F8FAFC;
    classDef core fill:#0F172A,stroke:#3B82F6,stroke-width:1.5px,color:#93C5FD;
    classDef alert fill:#450A0A,stroke:#EF4444,stroke-width:1.5px,color:#FCA5A5;

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