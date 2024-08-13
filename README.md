# 🚀 CrewAI Food and Beverage Delivery Analyzer

Welcome to the CrewAI Food and Beverage Delivery Analyzer! This project leverages the power of AI agents to analyze trends, markets, and develop innovative product ideas in the food and beverage delivery industry.

## 🌟 Overview

This CrewAI project is designed to provide comprehensive insights into the food and beverage delivery sector. It utilizes a team of AI agents to analyze trends, study market dynamics, and propose new product ideas.

## ✨ Features

- 🔍 Trend analysis in the food and beverage delivery industry
- 📊 Comprehensive market analysis
- 💡 Innovative product development proposals
- 🤖 AI-powered agents with specific roles and goals
- 🔗 Integration with external tools for data gathering

## 🛠️ Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/crewai-food-delivery-analyzer.git
   cd crewai-food-delivery-analyzer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key
     SERPER_API_KEY=your_serper_api_key
     ```

## 🚀 Usage

To run the analysis, simply execute the `run.py` script:

```
python run.py
```

The results will be printed to the console, and a product proposal will be saved in `Proposal.md`.

## 📁 Project Structure

- `agents.py`: Defines the AI agents (Trend Analyzer, Market Analyst, Product Manager)
- `crew.py`: Sets up the CrewAI configuration
- `tasks.py`: Defines the tasks for each agent
- `tools.py`: Configures external tools (SerperDev for web searches)
- `run.py`: Main script to execute the analysis
- `CHATGPT.py`: Configures the ChatGPT model

## 🤖 Agents

1. **Trend Analyzer**: Identifies and analyzes the latest trends in food and beverage delivery.
2. **Market Analyst**: Studies market dynamics, competitors, and growth opportunities.
3. **Product Manager**: Develops innovative product ideas based on trends and market analysis.

## 📝 Tasks

1. **Analyze Trends**: Identify key patterns and potential opportunities in the industry.
2. **Analyze Market**: Provide actionable insights on market segments and competitors.
3. **Develop Product**: Create a proposal for a new product that addresses market gaps.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


Created with ❤️ using CrewAI
