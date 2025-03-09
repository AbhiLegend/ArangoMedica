##🚀 Autogen & LangChain-Based Agentic AI for Graph Analytics
ArangoMedica is an AI-powered graph query system that uses Autogen and LangChain to analyze medical knowledge graphs. It enables natural language querying for complex medical relationships, leveraging ArangoDB, NetworkX, and GPT-4o to extract insights, compute graph algorithms, and visualize results.

🔹 Features
✅ Agentic AI-Driven Query Processing – Automatically selects and executes the best tool based on query intent.
✅ Hybrid Query Execution – Combines ArangoDB (AQL) for data retrieval and NetworkX for graph analytics.
✅ Dynamic Tool Selection – Uses Autogen AI agents to process medical knowledge graph queries efficiently.
✅ Graph Visualization – Provides graph-based insights using centrality, shortest paths, and community detection.
✅ Natural Language Interface – No need for AQL or SQL expertise, just ask questions in plain English!

🛠️ Tech Stack
🔗 Graph Database: ArangoDB (AQL-based graph storage)
📊 Graph Analysis: NetworkX (Graph algorithms & metrics)
🧠 AI Processing: OpenAI GPT-4o (via LangChain & Autogen)
🚀 Autonomous Agents: Autogen-based AssistantAgent
📉 Visualization: Matplotlib & Streamlit
🛠️ How It Works
1️⃣ User Submits a Natural Language Query
The user asks a question like:

"Find all patients diagnosed with Diabetes."
"Which symptoms are most important based on PageRank?"
2️⃣ AI Agent Selects the Right Tool
The Autogen Agent (GraphAssistant) analyzes the query and selects one of the following tools:

Tool Name	Function
text_to_aql_to_text	Converts text to AQL and retrieves data from ArangoDB.
text_to_nx_algorithm_to_text	Generates & executes NetworkX graph algorithms (PageRank, Betweenness Centrality, etc.).
execute_hybrid_query	Runs AQL + NetworkX together for deeper insights.
extract_nx_subgraph	Extracts subgraphs for focused analysis.
visualize_metrics	Computes graph metrics & visualizes results.
3️⃣ Query Execution & AI Processing
If AQL is needed, it fetches data from ArangoDB.
If graph computations are needed, it runs NetworkX code dynamically.
If both are required, it executes a hybrid query.
4️⃣ AI-Generated Insights & Visualizations
Summarized Text Response: Uses GPT-4o to explain results in plain English.
Graph Visualization: Highlights important nodes & relationships.
