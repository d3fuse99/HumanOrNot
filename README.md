Project VOID
Project VOID is a high-performance, real-time Turing Test simulation. It is designed to evaluate linguistic patterns, differentiate between artificial and human communication styles, and demonstrate advanced branching dialogue logic in a clean, messenger-styled interface.
Built with a focus on psychological immersion and technical scalability, this tool allows researchers and enthusiasts to observe how artificial mimicry compares to organic human interaction across multiple context-driven scenarios.
Development Note
[!IMPORTANT]
Linguistic Status: The current dialogue generation is in an early experimental stage. While the logic is functional, some sentence structures may appear "janky" or "crooked" (диалоги немного кривые, но это рабочая база). It is a proof-of-concept meant to demonstrate the branching system rather than perfect natural language processing.
Features
Context-Aware Logic: 10,000+ unique dialogue nodes driven by a high-performance Python-generated JSON database.
Bimodal Personality Simulation: Built-in interaction between two distinct entities—a formal, high-complexity AI Mimic and an informal, slang-driven Human Subject.
Dynamic Theme Engine: A clean, dark-mode messaging interface optimized for visual clarity.
Evaluation Window: An integrated 5-minute real-time timer for high-pressure identification.
Multi-Language UI: Seamless instant toggle between English and Russian interfaces.
Algorithmic Typing Simulation: Randomized delay engine to simulate human typing speeds.
How to run
Clone the repository:
Generate the Database: Run python build_data.py to compile the massive dialogue tree.
Run the project: Simply open index.html in any modern web browser.
Note: For the best visual experience, a screen resolution of 1920x1080 is recommended.
Tech stack
HTML5 — semantic structure and layout.
CSS3 — custom messenger-style components with smooth animations.
Vanilla JavaScript — core engine logic and real-time data processing.
Python 3 — algorithmic database generation and JSON stringification.
Zero-Dependency — no external libraries required for maximum speed.
Project structure
code
Text
📁 PROJECT_VOID
├── 📄 index.html
├── 📄 style.css
├── 📄 app.js
├── 📄 build_data.py
└── 📄 data.js (generated)
