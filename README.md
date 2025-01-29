AI-Driven Supply Chain Optimization System

Overview :
The AI-Driven Supply Chain Optimization System leverages Large Language Models (LLMs) and machine learning techniques to enhance inventory management and predict potential supply chain disruptions. By integrating real-time data from external sources, it helps businesses proactively manage inventory levels and respond to global events such as trade restrictions and natural disasters.

Features :
Predictive Inventory Management: Uses AI to forecast supply chain bottlenecks.
Real-Time Alerts: Notifies users of potential disruptions via Slack.
Automated Inventory Optimization: Adjusts stock levels based on predictive insights.
ERP Integration: Connects with enterprise resource planning (ERP) systems for seamless stock adjustments.
External API Integration: Fetches news, supplier, and logistics data to assess risks.
Prerequisites
To use this system effectively, the following knowledge and tools are required:

Large Language Models (LLMs): Understanding how models like Meta LLaMA 3.2 function, including tokenization and text generation.
Programming Skills: Proficiency in Python and SQL.
API Handling: Familiarity with API requests and responses.

Installation and Setup
1. Install Dependencies
Ensure the required Python libraries are installed:
pip install textblob requests ollama
TextBlob: Used for sentiment analysis.
Requests: Handles API calls for real-time data.
Ollama: Manages the local LLM.

3. Set Up LLM
Install Ollama for local model execution.
Download and run the LLaMA 3.2 model:
ollama run llama3.2:1b
Verify system requirements: 8GB VRAM and 2GB free disk space recommended.

Models Used:
1. LLaMA 3.2 (1B Parameters)
Optimized for text-based NLP tasks such as summarization and retrieval.
Supports 128K tokens for long-context processing.
Outperforms many open-source and proprietary models in industry benchmarks.

Inventory Management System:
A user-friendly inventory management interface built with Python and Tkinter, focusing on pepper imports and exports.

Core Modules:
Dashboard: Displays inventory statistics and alerts.
Imports Module: Logs import transactions with supplier details and prevents overstocking.
Exports Module: Tracks exports, ensuring accurate record-keeping.
Inventory Viewer: Provides a real-time breakdown of stock levels.
Warning System: Sends alerts when inventory exceeds 80% capacity to prevent over-importing.
Real-Time Notifications
Integrates with Slack API to send alerts when disruptions are detected.
The AI analyzes news articles for events that may impact supply chains.
If a risk is identified, the system notifies users via a designated Slack channel.

Project Components:
1. Global Data Monitoring Engine
Collects data from news sources, supplier databases, and logistics reports.
Uses NLP techniques to analyze trends and identify risks.
2. Predictive Disruption Modeling
Applies machine learning algorithms to assess disruption probabilities.
Generates risk scores for potential supply chain events.
3. ERP System Integration
Connects with ERP platforms like SAP to automate inventory adjustments.
Suggests reorder points based on predictive analysis.
4. Alert & Reporting Dashboard
Provides real-time notifications through Slack or email.
Displays interactive visualizations of supply chain risks.

Usage:
The system continuously fetches and analyzes real-time data.
If a disruption is detected, it calculates risk scores and suggests inventory adjustments.
Users receive instant alerts on Slack or email.
ERP integration ensures automated stock replenishment based on risk analysis.
