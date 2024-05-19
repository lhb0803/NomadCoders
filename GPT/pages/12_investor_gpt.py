from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool, BaseTool, DuckDuckGoSearchResults
from langchain.schema import SystemMessage, HumanMessage
from pydantic import BaseModel, Field
from typing import Type
import yfinance as yf
import streamlit as st
import os

st.set_page_config(
    page_title="InvestorGPT",
    page_icon="🤑"
)
st.title("InvestorGPT")

llm = ChatOpenAI(temperature=0.1, model_name="gpt-4o")

class StockMarketSymbolSearchToolArgsSchema(BaseModel):
    query: str = Field(description="The query you will search for")

class StockMarketSymbolSearchTool(BaseTool):
    name = "StockMarketSymbolSearchTool"
    description = """
    Use this tool to find the stock market symbol for a compnay.
    It takes a query as an argument.
    Example query: Stock Market Symbol for Apple Company
    """
    args_schema: Type[StockMarketSymbolSearchToolArgsSchema] = StockMarketSymbolSearchToolArgsSchema

    def _run(self, query):
        ddg = DuckDuckGoSearchResults()
        return ddg.run(query)

class CompanyOverviewArgsSchema(BaseModel):
    symbol: str = Field(description="Stock symbol of the company. Example: AAPL, TSLA")

class CompanyOverviewTool(BaseTool):
    name = "CompanyOverview"
    description = """
    Use this to get an overview of the financials of the company.
    Overview includes news, income statement, balance sheet and cashflow of the company.
    You should enter a stock symbol.
    """
    args_schema: Type[CompanyOverviewArgsSchema] = CompanyOverviewArgsSchema

    def _run(self, symbol):
        ticker = yf.Ticker(symbol)

        report = {
            "news": ticker.news,
            "income_statement": ticker.income_stmt,
            "balance_sheet": ticker.balance_sheet,
            "cashflow": ticker.cashflow,
        }
        return report

prompt = "Give me information on {company}'s stock and help me analyze if it's a potential good investment. You should refer to information which includes news, income statement, balance sheet and cashflow of the company. Also tell me what symbol does the stock have."

agent = initialize_agent(
    llm=llm,
    verbose=True,
    agent=AgentType.OPENAI_FUNCTIONS,
    handle_parsing_errors=True,
    tools=[
        StockMarketSymbolSearchTool(),
        CompanyOverviewTool(),
    ],
    agent_kwargs={
        "system_message": SystemMessage(content="""
            You are a hedge fund manager.
            
            You evaluate a company and provide your opinion and reasons why the stock is a buy or not.
            
            Consider the performance of a stock, the company overview and the income statement.
            
            Be assertive in your judgement and recommend the stock or advise the user against it.
        """),
        "human_message": HumanMessage(content=prompt)
    }
)

company = st.text_input("Write the name of the company you")

if company:
    result = agent.invoke(company)
    st.write(result["output"].replace("$", "\$"))
