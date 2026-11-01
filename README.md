# learn-notebooks

Runnable companion notebooks for the tutorials at **[anacodicai.org/learn](https://anacodicai.org/learn)**.

Each notebook pairs with one article. The article explains the concept; the notebook lets you change the numbers and watch the conclusion move. Almost all run on the standard library plus `matplotlib` — **no API key, no accounts, no paid services**. The few that call a real model say so in their row and need only a free key (add it in Colab's 🔑 *Secrets* panel).

## How to use these

- **Run it now** — click the Colab link. Nothing to install.
- **Read it instead** — each notebook is also rendered inline at the bottom of its article, under *Runnable notebook*.
- **Run it locally** — `pip install jupyter matplotlib`, then open the `.ipynb`.

## Notebooks

| Topic | Level | Article | Run |
|---|---|---|---|
| What Are Agents | Beginner | [read](https://anacodicai.org/learn/ai-agents/6-1/what-are-agents) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/ai-agents/6-1/what-are-agents.ipynb) |
| Hallucination Detection & Grounding | Intermediate | [read](https://anacodicai.org/learn/ai-safety/7-2/hallucination-detection) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/ai-safety/7-2/hallucination-detection.ipynb) |
| Guardrails & Output Validation | Intermediate | [read](https://anacodicai.org/learn/ai-safety/7-3/guardrails-implementation) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/ai-safety/7-3/guardrails-implementation.ipynb) |
| Heterogeneity & Forest Plots | Intermediate | [read](https://anacodicai.org/learn/evidence-synthesis/15-1/heterogeneity-and-forest-plots) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/evidence-synthesis/15-1/heterogeneity-and-forest-plots.ipynb) |
| Meta-Analysis: Pooling Studies (Fixed vs Random Effects) | Intermediate | [read](https://anacodicai.org/learn/evidence-synthesis/15-1/meta-analysis) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/evidence-synthesis/15-1/meta-analysis.ipynb) |
| 2×2 Tables & Effect Measures (OR, RR, RD, NNT, HR) | Intermediate | [read](https://anacodicai.org/learn/evidence-synthesis/15-1/two-by-two-and-effect-measures) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/evidence-synthesis/15-1/two-by-two-and-effect-measures.ipynb) |
| GRADE: Rating Certainty of Evidence | Advanced | [read](https://anacodicai.org/learn/evidence-synthesis/15-2/grade-certainty) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/evidence-synthesis/15-2/grade-certainty.ipynb) |
| Risk of Bias: RoB2, ROBINS-I, AMSTAR-2 | Advanced | [read](https://anacodicai.org/learn/evidence-synthesis/15-2/risk-of-bias) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/evidence-synthesis/15-2/risk-of-bias.ipynb) |
| Summary of Findings & Evidence-to-Decision | Advanced | [read](https://anacodicai.org/learn/evidence-synthesis/15-2/summary-of-findings-and-etd) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/evidence-synthesis/15-2/summary-of-findings-and-etd.ipynb) |
| Logarithms, Exponents & the Log Scale | Beginner | [read](https://anacodicai.org/learn/foundations/1-2/logarithms-and-exponents) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/foundations/1-2/logarithms-and-exponents.ipynb) |
| Probability & Statistics Foundations | Beginner | [read](https://anacodicai.org/learn/foundations/1-2/probability-statistics) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/foundations/1-2/probability-statistics.ipynb) |
| Reasoning Budgets: When Thinking Tokens Are Waste | Intermediate | [read](https://anacodicai.org/learn/llm-engineering/4-3/reasoning-budgets) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/llm-engineering/4-3/reasoning-budgets.ipynb) |
| Logistic Regression | Beginner | [read](https://anacodicai.org/learn/machine-learning/2-1/logistic-regression) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/machine-learning/2-1/logistic-regression.ipynb) |
| Turn-Taking in Voice Agents: Endpointing, VAD and Barge-In | Advanced | [read](https://anacodicai.org/learn/system-design/11-2/turn-taking-and-endpointing) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/system-design/11-2/turn-taking-and-endpointing.ipynb) |
| Chunk Size, Overlap, and Retrieval Thresholds in RAG Systems | Intermediate | [read](https://anacodicai.org/learn/rag-systems/5-2/chunking-and-retrieval-thresholds) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/rag-systems/5-2/chunking-and-retrieval-thresholds.ipynb) |
| API Best Practices | Intermediate | [read](https://anacodicai.org/learn/llm-engineering/4-3/api-best-practices) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/llm-engineering/4-3/api-best-practices.ipynb) |
| RAG at Scale | Advanced | [read](https://anacodicai.org/learn/genai-design/9-5/rag-at-scale) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/genai-design/9-5/rag-at-scale.ipynb) |
| Consistency Memory: Making Repeated AI Judgments Agree With Each Other | Advanced | [read](https://anacodicai.org/learn/ai-agents/6-5/consistency-memory) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/ai-agents/6-5/consistency-memory.ipynb) |
| Prompt Management Architecture: Prompts as Files, Not Strings | Intermediate | [read](https://anacodicai.org/learn/llm-engineering/4-2/prompt-management-architecture) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/llm-engineering/4-2/prompt-management-architecture.ipynb) |
| Designing a Self-Serve Platform: One Model for Individuals and Organizations | Intermediate | [read](https://anacodicai.org/learn/system-design/11-1/self-serve-workspace-model) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/system-design/11-1/self-serve-workspace-model.ipynb) |
| Effective Access: Combining Two Levels of Role-Based Permissions | Intermediate | [read](https://anacodicai.org/learn/system-design/11-1/effective-access-two-tier-rbac) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/system-design/11-1/effective-access-two-tier-rbac.ipynb) |
| Streaming Progress for Long-Running Jobs | Intermediate | [read](https://anacodicai.org/learn/system-design/11-1/streaming-progress-long-running-jobs) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/system-design/11-1/streaming-progress-long-running-jobs.ipynb) |
| Grounding and Abstention by Design | Advanced | [read](https://anacodicai.org/learn/rag-systems/5-4/grounding-and-abstention-by-design) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/rag-systems/5-4/grounding-and-abstention-by-design.ipynb) |
| LangGraph | Intermediate | [read](https://anacodicai.org/learn/ai-agents/6-2/langgraph) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/ai-agents/6-2/langgraph.ipynb) |
| LangChain | Intermediate | [read](https://anacodicai.org/learn/ai-agents/6-2/langchain) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/ai-agents/6-2/langchain.ipynb) |
| CrewAI | Intermediate | [read](https://anacodicai.org/learn/ai-agents/6-2/crewai) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/ai-agents/6-2/crewai.ipynb) |
| AutoGen | Intermediate | [read](https://anacodicai.org/learn/ai-agents/6-2/autogen) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/ai-agents/6-2/autogen.ipynb) |
| MCP Fundamentals | Intermediate | [read](https://anacodicai.org/learn/ai-agents/6-3/mcp-fundamentals) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/ai-agents/6-3/mcp-fundamentals.ipynb) |
| From Prompt to Agent: tools, sub-agents, memory, guardrails, evaluation (needs a free Groq key) | Advanced | [read](https://anacodicai.org/learn/ai-agents/6-5/production-agents) | [Colab](https://colab.research.google.com/github/anacodicAI-labs/learn-notebooks/blob/main/ai-agents/6-5/production-agents.ipynb) |

## Layout

```
<module>/<sub>/<slug>.ipynb      mirrors the article path exactly, so
                                 anacodicai.org/learn/<module>/<sub>/<slug>
                                 is the article for <module>/<sub>/<slug>.ipynb
```

## Rendering (maintainers)

`render_notebook.py` executes a notebook and writes the rendered HTML next to the matching article in the site repo, which is a **separate repository**. Check it out as a sibling of this one:

```bash
python3 render_notebook.py system-design/11-2/turn-taking-and-endpointing.ipynb

# or point at the article tree explicitly
LEARN_TUTORIALS_DIR=/path/to/s3-content/learn/tutorials \
  python3 render_notebook.py <module>/<sub>/<slug>.ipynb
```

It executes the notebook first, so the committed `.ipynb` always carries real outputs rather than empty cells.

## Licence

MIT — see [LICENSE](LICENSE). Use them, fork them, teach from them.
