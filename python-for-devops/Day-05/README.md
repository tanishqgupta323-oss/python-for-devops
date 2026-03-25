# CLI Arguments vs Environment Variables (DevOps Notes)

1. Command Line Arguments (CLI Args)

### 📌 Definition

CLI arguments are values passed to a program at runtime via the terminal.

---

### 📌 Syntax (Python)

```python
import sys

arg1 = sys.argv[1]
```

---

### 📌 Example

```bash
python app.py dev
```

```python
import sys
env = sys.argv[1]
print(env)
```

**Output:**

```
dev
```

---

### 📌 Use Cases

* Selecting environment (dev / prod)
* Passing dynamic inputs
* File processing
* Running scripts with parameters

---

### 📌 Key Points

* Passed at runtime
* Always strings
* Must convert if needed (`int()`, etc.)
* Visible in terminal

---

---
2. Environment Variables (ENV VARS)

# Definition
Environment variables are system-level variables used to store configuration or sensitive data.

### 📌 Set Variable (Linux)
export DB_PASSWORD="12345"

### 📌 Access in Python
import os

password = os.getenv("DB_PASSWORD")
print(password)

### 📌 Use Cases

* Database credentials
* API keys
* Config settings
* Environment modes

### 📌 Key Points

* Stored outside code
* More secure than CLI args
* Used for configuration
* Persistent (session-based or system-based)

## 🔥 3. CLI Args vs Environment Variables

| Feature          | CLI Arguments | Environment Variables |
| ---------------- | ------------- | --------------------- |
| Purpose          | Input         | Configuration         |
| Timing           | Runtime       | Predefined            |
| Security         | ❌ Less secure | ✅ More secure         |
| Visibility       | Visible       | Hidden                |
| Change Frequency | Frequent      | Rare                  |


## 🔥 4. Combined Usage (Real DevOps Example)

export DB_PASSWORD=12345
python deploy.py prod
```

```python
import sys
import os

env = sys.argv[1]
password = os.getenv("DB_PASSWORD")

print(env, password)
```

## 🧠 Interview Questions

### ❓ Q1: What are CLI arguments?

👉 Values passed to a script at runtime via command line.

---

### ❓ Q2: What are environment variables?

👉 System-level variables used for configuration and secrets.

---

### ❓ Q3: Difference between CLI args and env vars?

👉 CLI = input
👉 ENV = configuration

---

### ❓ Q4: Why use environment variables for passwords?

👉 Security (avoid hardcoding sensitive data)

---

### ❓ Q5: Which one is used for dynamic input?

👉 CLI arguments

---

---

## 💯 Golden Rule

> **CLI = control input**
> **ENV = configuration & secrets**

---

## 🚀 DevOps Tip

* Use CLI for flexibility
* Use ENV for security
* Use both together in real projects

---
