# 🤖 my-ai-app

Welcome to **my-ai-app**! 

This is a simple, beginner-friendly Python project created to help you understand **how different files in an application connect and work together**.

---

## 💡 What Is This Project?

When building software, developers divide code into multiple small files where each file has one specific job.

This project mimics how a simple AI assistant works:
1. **You ask a question** (`main.py`).
2. **The chatbot takes charge** (`chatbot.py`).
3. **Helper tools clean up your text** (`utils.py`).
4. **Relevant knowledge is fetched** (`rag.py`).
5. **The conversation is saved for later** (`database.py`).

> **Note for Beginners:** This project does **not** use real AI models, API keys, or internet connections. Everything is written with simple, standard Python so that the connections between files are 100% clear and easy to follow.

---

## 🗺️ How the Files Connect (Visual Flow)

Here is a map showing how data flows through the files:

```text
       [ main.py ]             <-- 1. Starts the app & asks a question
            ↓
      [ chatbot.py ]           <-- 2. Manages the whole process
      /     |      \
     /      |       \
    ↓       ↓        ↓
 [ rag.py ] |   [ database.py ] <-- 5. Saves the question & answer
    │       │
    ▼       ▼
   [ utils.py ]                 <-- 3 & 4. Cleans text for RAG and Chatbot
```

---

## 📁 What Does Each File Do?

Here is what each file is responsible for, explained in plain language:

| File | Nickname | What It Does |
| :--- | :--- | :--- |
| **`main.py`** | 🟢 **The Start Button** | The entry point. Runs the application and sends a question to the chatbot. |
| **`chatbot.py`** | 🧠 **The Manager** | Coordinates the entire process. It calls the text cleaner, fetches context, creates an answer, and saves the chat. |
| **`rag.py`** | 📚 **The Researcher** | Simulates RAG (Retrieval-Augmented Generation). It finds mock knowledge to help answer your question. |
| **`database.py`** | 💾 **The Notebook** | Stores questions and answers in memory so you can look at the chat history anytime. |
| **`utils.py`** | 🔧 **The Helper Tool** | A shared helper that cleans up text (removes extra spaces and converts text to lowercase). |

---

## 🚀 How to Run the Project Normally

You only need standard Python installed. No extra packages are needed to run the code!

### Step 1: Open your terminal
Navigate into the project folder:
```powershell
cd my-ai-app
```

### Step 2: Run the program
Execute `main.py` using Python:
```powershell
python main.py
```

### Expected Output:
```text
[Main] Starting process with query: 'What is Artificial Intelligence?'

[RAG] Retrieving context for query: 'what is artificial intelligence?'
[Database] Saved chat record: What is Artificial Intelligence? -> Generated answer for 'what is artificial intelligence?' based on: [Retrieved knowledge context relevant to 'what is artificial intelligence?']

[Main] Response received:
Generated answer for 'what is artificial intelligence?' based on: [Retrieved knowledge context relevant to 'what is artificial intelligence?']
```

---

## 📦 How to Install CodeGraph

To convert this codebase into an interactive visual graph, you can install the **`codegraph`** tool via `pip`:

```bash
pip install codegraph
```

> **Why CodeGraph?** It analyzes your Python files statically using syntax parsing without executing any code.

---

## 📊 How to Generate & View the HTML Visualization

CodeGraph generates an interactive **`codegraph.html`** file that you can view in any web browser.

### Step 1: Generate the Graph
Make sure you are in the `my-ai-app` directory in your terminal, then run:

```bash
codegraph .
```

> **Note for Windows users:** If `codegraph` is not found directly on your command line, run it through Python:
> ```bash
> python -c "from codegraph.main import cli; cli()" .
> ```

### Step 2: Open `codegraph.html` in Your Browser
- Running the command will automatically generate `codegraph.html` and open it in your default browser.
- If it does not pop up automatically, you can manually open it:
  - **Windows:** `start codegraph.html` (or double-click the file in File Explorer)
  - **Mac:** `open codegraph.html`
  - **Linux:** `xdg-open codegraph.html`

### Step 3: Interacting with the HTML Diagram
Once the visualizer opens in your browser:
- **Zoom & Pan:** Use your mouse wheel to zoom in/out, and click + drag the background to pan around.
- **Move Boxes (Nodes):** Click and drag any node to reposition it.
- **Highlight Connections:** Click on any node (e.g. `chatbot.py`) to highlight all connected files and dim the rest.
- **Inspect Relationships:**
  - `main.py` points directly to `chatbot.py`.
  - `chatbot.py` connects out to `rag.py`, `database.py`, and `utils.py`.
  - `rag.py` connects to `utils.py`.
  - Notice `utils.py` receives connections from both `chatbot.py` and `rag.py`.
- **Search:** Press `Ctrl + F` to search for specific files, functions, or modules.
