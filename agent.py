from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from config import API_KEY, BASE_URL, MODEL

def get_agent(df):
    """
    Initializes and returns the LangChain Pandas agent.
    """
    llm = ChatOpenAI(
        openai_api_key=API_KEY,
        openai_api_base=BASE_URL,
        model_name=MODEL,
        temperature=0,
        default_headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"} 
    )
    
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        allow_dangerous_code=True,
        agent_type="tool-calling" 
    )
    
    return agent