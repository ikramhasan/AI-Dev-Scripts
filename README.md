<p align="center">
    <h1 align="center">AI DEV SCRIPTS</h1>
</p>
<p align="center">
    <em>Streamline Code Review, Commit & Speed Up Dev Process. Your Own Personal Senior Engineer For Free!</em>
</p>
<p align="center">
	</p>

<br><!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary><br>

- [📍 Overview](#-overview)
- [🧩 Features](#-features)
- [📦 Scripts](#-scripts)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🔗 Acknowledgments](#-acknowledgments)
</details>
<hr>

## 📍 Overview

AI DEV SCRIPTS, leverages Local LLMs to streamline code improvement workflows and enhance your coding. It includes scripts like `ai_review` for suggestion generation, `ai_pr` for pull request analysis, and `ai_commit` for suggested commit messages. Additionally, it features an `ai_readme` script that generates customized readmes based on directory locations. Overall, it utilizes Ollama's DeepSeek Coder, and Mistral model to automate code improvements, security checks, and documentation within the repository ecosystem.

---

## 🧩 Features

- **AI Review**: Scours through specified file formats and requests AI-generated suggestions for improvement.
- **AI PR**: Analyzes GitHub Pull Requests by calling an external Ollama DeepSeek Coder service.
- **AI Commit**: Generates commit messages using an AI model, adhering to conventional commit style and active voice guidelines.
- **AI Readme**: Generates customized readmes based on the repository's location, utilizing OpenAI's Ollama API and the Mistral model.

---

## 📦 Scripts

| File                   | Summary                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ai_review](ai_review) | This ai_review file initiates the script that scours through specified file formats and requests AI-generated suggestions for improvement. It generates a markdown file containing improvements, best practices, readability enhancements, maintainability tips, and potential code examples, creating an impactful code improvement workflow within this repository's ecosystem. |
| [ai_pr](ai_pr)         | The `ai_pr` script analyzes GitHub Pull Requests by calling an external Ollama DeepSeek Coder service. It generates brief summaries and flags potential security or coding best practices issues from the presented git changes. This tool supports automated PR review processes in the given repository infrastructure.                                                         |
| [ai_commit](ai_commit) | The ai_commit script in this repository's scripts folder is designed to generate commit messages using an AI model. This tool runs the deepseek-coder model from Ollama to suggest a commit message based on the git diff provided as input, adhering to conventional commit style and active voice guidelines.                                                                   |
| [ai_readme](ai_readme) | Generate readme files for directories using the AI, named ai_readme script. The script triggers an AI to produce customized readmes based on the repository's location, utilizing OpenAI's Ollama API and the Mistral model. Emojis and flat-square badge styles are incorporated in the readme generation process.                                                               |
| [ai_chat_md](ai_chat_md) | Chat with markdown files of any size. Complete rag functionality.                                                               |
| [ai_chat_pdf](ai_chat_pdf) | Chat with pdf files of any size. Complete rag functionality.                                                                |

---

## 🚀 Getting Started

**Requirements:**

- Bash
- readmeai
- ollama
- deepseek-coder
- mistral

### ⚙️ Installation

**1. Clone the repository:**

```sh
git clone https://github.com/ikramhasan/AI-Dev-Scripts.git
```

**2. Install the required dependencies:**

```sh
pip install readmeai
```

**3. Install ollama:** Download the latest release from [here](https://ollama.com/download)

**4. Install deepseek-coder:**

```sh
ollama run deepseek-coder:6.7b-instruct
```

**5. Install mistral:**

```sh
ollama run mistral:7b-instruct
```

**6. Make the scripts executable:**

```sh
chmod +x ./ai_review
```

**7. (Optional) Add the scripts to your PATH:**

```sh
export PATH=$PATH:/path/to/AI-Dev-Scripts
```


### 🤖 Usage

<h4>ai_review</h4>

> Navigate to the directory where you want to run the script and execute the command below:
>
> ```console
> $ ./ai_review file.py file.js # for specific files
> ```
>
> Or,
>
> ```console
> $ ./ai_review *.py *.js # for all files with .py and .js extensions
> ```

<h4>ai_readme</h4>

> Navigate to the directory where you want to generate the readme and run the command below:
>
> ```console
> $ ./ai_readme
> ```

<h4>ai_commit</h4>

> Navigate to your repo and run ai_commit using the command below:
>
> ```console
> $ ./ai_commit
> ```

<h4>ai_pr</h4>

> Copy the pr link and run the command below:
>
> ```console
> $ ./ai_pr <pr_link>
> ```

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/ikramhasan/AI-Dev-Scripts/issues)**: Submit bugs found or log feature requests for the `scripts` project.
- **[Submit Pull Requests](https://github.com/ikramhasan/AI-Dev-Scripts/pulls)**: Review open PRs, and submit your own PRs.
<!-- - **[Join the Discussions](https://local/scripts/discussions)**: Share your insights, provide feedback, or ask questions. -->

<!-- <details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://local{/scripts/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=scripts">
   </a>
</p>
</details> -->

---

## 🎗 License

This project is protected under the [MIT](https://choosealicense.com/licenses/mit) License.

---

## 🔗 Acknowledgments

- ollama
- readmeai

[**Return**](#-overview)

---
