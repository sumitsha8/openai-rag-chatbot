# 📘 AI, ML, DL, LLM & RAG etc — Notes

A clean, beginner‑friendly cheatsheet summarizing all core AI concepts:
AI → ML → DL → LLMs → Embeddings → RAG → Agents.

---

## 🤖 What is Artificial Intelligence (AI)?

**Artificial Intelligence (AI)** is the field of creating machines that can perform tasks requiring human intelligence such as:

- Understanding language  
- Recognizing patterns  
- Making decisions  
- Learning from experience  
- Generating content (text, images, code)

**Simple:**  
> AI = Making machines act smart like humans.

---

## 📚 Machine Learning (ML)

Machine Learning is a **subset of AI** where systems learn patterns from **data** instead of being manually programmed.

ML models:
- Improve with more data  
- Make predictions  
- Recognize patterns  
- Classify information  

**Key requirement:** Large amounts of training data.

---

## 🧠 Deep Learning (DL)

Deep Learning is a **subset of Machine Learning** that uses **Neural Networks** inspired by the structure of the human brain.

DL is especially good for:
- Image recognition  
- Speech understanding  
- Complex classification  
- Large-scale pattern discovery  

**Simple:**  
> Deep Learning = ML + Neural Networks + High Accuracy for complex problems.

---

## 📝 Large Language Models (LLMs)

LLMs are AI models trained on massive text datasets so they can understand and generate human‑like text.

Examples of LLMs:
- ChatGPT  
- GPT‑4o / GPT‑5  
- Llama  
- Claude  
- Gemini  

What LLMs can do:
- Answer questions  
- Summarize text  
- Translate languages  
- Generate content  
- Explain concepts  

**Simple:**  
> LLMs primarily work with text (unless in multimodal form).

---

## 🔧 Fine‑Tuning

Fine‑tuning = training a base model further using **domain‑specific data**.

Used when:
- You want specialization (medical bot, finance bot, legal bot, etc.)
- General knowledge models are not accurate enough
- Business processes need custom understanding

**Simple:**  
> Fine‑tuning = customizing an LLM to your domain.

---
##  What is FAISS? (Simple Explanation)
FAISS stands for Facebook AI Similarity Search.
It is a library created by Meta (Facebook) for very fast similarity search on vectors.
In RAG systems (like yours), embeddings are vectors — long lists of numbers that represent the meaning of text.

```
FAISS helps you:
✅ Store many embeddings
(Your PDF or GitHub docs → chunked → embedded → stored in FAISS)
✅ Search through them efficiently
Given a user question → embed it → find the closest chunks using FAISS.
```
🎯 Why FAISS?
Because it’s:
- Extremely fast
- Works offline
- Works on CPU or GPU
- Handles thousands → millions of vectors
- Open-source
- Perfect for RAG applications

---

## 🧭 Embeddings (Vector Representations)

Embeddings convert text into **numerical vectors** that capture meaning.

Example:  
“The server is down” → `[0.12, -0.33, 0.87, ...]`

Why embeddings matter:
- Semantic search  
- Similarity comparison  
- Grouping related concepts  
- RAG systems (vector retrieval)

**Simple:**  
> Embeddings turn text into “meaning coordinates”.

---

## 🔍 Retrieval‑Augmented Generation (RAG)

LLMs have a **knowledge cutoff** and cannot see your private documents.

RAG solves this by giving the LLM **exact context** from your documents.

### How RAG works:
1. **Retrieve** → fetch the most relevant chunks from your PDFs or DB  
2. **Augment** → insert those chunks into the prompt  
3. **Generate** → LLM answers using ONLY the provided context  

### Why RAG?
- Prevents hallucination  
- Uses your real data  
- Keeps answers accurate  
- No fine‑tuning required  

**Simple:**  
> RAG = LLM + your documents → safe, accurate answers.

---

## 🧠 Agentic AI (AI Agents)

Agents are AI systems that **reason + plan + act**.

Agents can:
- Use tools  
- Perform multi‑step tasks  
- Make decisions  
- Execute workflows  
- Act autonomously  

Examples:
- Email sorter bot  
- Meeting scheduling bot  
- Automation agents  
- Retrieval + Action bots  

**Simple:**  
> Agentic AI = LLM that can think + decide + take actions.

---

## 🧩 AI Concepts in One Simple Map

```
AI
 └── Machine Learning
      └── Deep Learning
            └── Large Language Models (LLMs)
                  ├── Embeddings (vector meaning)
                  ├── Fine‑Tuning (domain specialization)
                  └── RAG (retrieval + generation)
                        └── Agentic AI (LLMs that act)
```


