# AI Researcher 🔬🤖 — Project Documentation

## 1. Project Overview

**AI Researcher** is an agentic GenAI application that automatically generates *ready-to-publish research papers within 2–3 minutes*. The system leverages **LangGraph-based AI agents**, **tool orchestration**, and **LLM-powered reasoning** to perform literature review, paper reading, content synthesis, and final PDF generation in a fully automated workflow.

The primary objective of this project is to simulate how real-world research assistants work—searching academic literature, extracting insights, maintaining context across multiple documents, and producing a structured research paper with minimal human intervention.

---

## 2. Tech Stack Used

### Core AI & Agent Framework

* **LangGraph** – For building agent-based workflows using nodes and edges
* **LangChain** – Tool abstraction, prompt handling, and LLM integration
* **LLM** – Google Gemini 2.5-Pro (used for reasoning, summarization, and generation)

### Agent Tools

* **arXiv Tool** – Fetches relevant research papers for literature review
* **PDF Reader Tool** – Reads and extracts content from academic papers
* **PDF Writer Tool** – Generates a structured, publishable research paper in PDF format

### Frontend

* **Streamlit** – Lightweight UI for user interaction and PDF download

### Architecture Style

* **Agentic Workflow (Tool-Augmented LLMs)**
* **Event-driven graph execution using LangGraph**

---

## 3. High-Level System Architecture

The project follows a **node–edge architecture** using LangGraph, where each node represents a specific responsibility in the research pipeline and edges define execution flow and decision-making logic.

**Main Components:**

1. User Interface (Streamlit)
2. AI Agent (LangGraph)
3. Tool Layer (arXiv, PDF Reader, PDF Writer)
4. LLM Reasoning Engine

---

## 4. End-to-End Workflow Explanation

### Step 1: User Input (Frontend)

* The user enters a research topic or question via Streamlit UI
* Example: *"Impact of AI on Climate Change Mitigation"*

---

### Step 2: Agent Initialization (LangGraph)

* The LangGraph agent is initialized with a **shared state** (messages, tool outputs)
* The agent acts as a **research coordinator**, deciding when and how to invoke tools

**Key Concept:**

* State persistence across nodes enables multi-step reasoning without losing context

---

### Step 3: Literature Review (arXiv Tool)

* The agent invokes the **arXiv tool** to retrieve relevant research papers
* Metadata retrieved:

  * Paper title
  * Abstract
  * Authors
  * PDF URLs

**Why this matters:**

* Automates a task that usually takes researchers hours or days

---

### Step 4: Paper Reading & Content Extraction

* Retrieved PDFs are passed to the **PDF Reader Tool**
* The tool extracts:

  * Abstracts
  * Key methodologies
  * Results & conclusions

**Agent Responsibility:**

* Decide which sections are important
* Ignore noisy or irrelevant text

---

### Step 5: Context Management & Chunking

* Extracted content is **chunked and summarized**
* Only the most relevant insights are retained

**This step directly addresses LLM context overflow issues** (explained later)

---

### Step 6: Research Paper Generation

* The agent invokes the **PDF Writer Tool**
* Output structure includes:

  * Abstract
  * Introduction
  * Literature Review
  * Methodology
  * Results & Discussion
  * Conclusion

**Output:**

* A ready-to-publish research paper in PDF format

---

### Step 7: Output Delivery (Frontend)

* Streamlit displays:

  * Agent response
  * Downloadable research paper PDF

---

## 5. Key Concepts Learned

### 1. Agentic AI Design

* Agents are **decision-makers**, not just text generators
* LLM decides *which tool to call, when, and why*

### 2. LangGraph (Nodes & Edges)

* Nodes = Tasks (search, read, write)
* Edges = Control flow & reasoning paths
* Enables **deterministic + flexible workflows**

### 3. Tool-Augmented LLMs

* LLMs alone are limited
* Tools extend capabilities beyond text generation

### 4. State Management in AI Systems

* Persistent state allows:

  * Multi-step reasoning
  * Reduced hallucinations
  * Better output consistency

### 5. GenAI Application Development

* Combining backend agents with frontend UX
* Production-style GenAI architecture

---

## 6. Real-World Pain Points Faced & Solutions Opted

This project closely mirrors real-world GenAI system challenges. Below are the major pain points encountered during development and the concrete solutions implemented to address them.

---

### Pain Point 1: Context Window Overflow

**Problem:**
Academic research papers are lengthy and unstructured. Passing entire PDFs or large extracted text chunks to the LLM frequently caused **context window overflow**, leading to model crashes, incomplete responses, or degraded output quality.

**Solution Opted:**

* Switched from **gpt-3.5-turbo** to **gpt-4o-mini**, which provides better efficiency and stability for tool-augmented workflows
* Limited content extraction strictly to relevant sections (abstract, methodology, results)
* Enforced a **word limit** while forwarding extracted content between agent nodes

**Outcome:**

* Prevented model crashes
* Reduced token usage significantly
* Ensured stable multi-step agent execution

---

### Pain Point 2: Tool Invocation Loops

**Problem:**
During early iterations, the agent repeatedly invoked the same tools (e.g., paper reader or arXiv search), resulting in inefficient execution and longer response times.

**Solution Opted:**

* Implemented a **graph-based workflow using LangGraph**
* Defined strict **edges** to control execution flow
* Added clear **entry and exit points** for each node to prevent redundant tool calls

**Outcome:**

* Predictable agent behavior
* Faster execution
* No infinite or redundant tool loops

---

### Pain Point 3: Noisy and Irrelevant Academic Content

**Problem:**
Research PDFs contain references, equations, citations, tables, and formatting artifacts that add noise and reduce the quality of LLM-generated summaries.

**Solution Opted:**

* Implemented **selective content extraction**, filtering out:

  * References and bibliography sections
  * Mathematical derivations and equations
  * Page headers, footers, and citations
* Passed only semantically meaningful text to the LLM

**Outcome:**

* Improved signal-to-noise ratio
* Higher-quality literature summaries
* More coherent and research-aligned final papers

---

### Solution 2: Selective Content Extraction

* Agent filters sections like:

  * References
  * Footnotes
  * Mathematical derivations

**Result:**

* Higher signal-to-noise ratio
* Improved research quality

---

### Solution 3: Controlled Tool Invocation

* LangGraph edges restrict unnecessary tool calls
* Clear entry and exit points for each node

**Result:**

* Faster execution
* Predictable agent behavior

---

# AI-Researcher


## Output Snapshots : 

<img width="1470" height="956" alt="Screenshot 2026-01-26 at 1 49 53 PM" src="https://github.com/user-attachments/assets/afa78465-ceda-4e66-bd53-1e99a1d3aa78" />
<img width="1470" height="956" alt="Screenshot 2026-01-26 at 1 50 36 PM" src="https://github.com/user-attachments/assets/edd52d93-b240-47b4-b2c4-0dda64548813" />

<img width="1470" height="956" alt="Screenshot 2026-01-26 at 1 50 54 PM" src="https://github.com/user-attachments/assets/22c5bd4e-2965-486c-806a-de3b5f9ba3ab" />

<img width="1470" height="956" alt="Screenshot 2026-01-26 at 1 52 09 PM" src="https://github.com/user-attachments/assets/cfc4a747-7f59-467f-b926-5c0cac378e91" />

<img width="1470" height="956" alt="Screenshot 2026-01-26 at 1 52 26 PM" src="https://github.com/user-attachments/assets/f8bf9ea8-a361-4bd0-918b-5c0c926e6562" />

<img width="1470" height="956" alt="Screenshot 2026-01-26 at 1 53 01 PM" src="https://github.com/user-attachments/assets/39853e3e-ed55-466a-b8be-6ab25d837816" />

<img width="1470" height="956" alt="Screenshot 2026-01-26 at 1 53 39 PM" src="https://github.com/user-attachments/assets/2353c43a-d47b-47c2-8adc-c8fab74148f8" />


<img width="1470" height="956" alt="Screenshot 2026-01-26 at 1 53 19 PM" src="https://github.com/user-attachments/assets/a7d14540-869b-4e5c-a642-9467cd9a1b79" />


<img width="1470" height="956" alt="Screenshot 2026-01-26 at 1 54 40 PM" src="https://github.com/user-attachments/assets/4c6f41ec-e7f0-47cc-be7a-6ddbedf40e3b" />


[paper_20260126_135432.pdf](https://github.com/user-attachments/files/24855803/paper_20260126_135432.pdf)

