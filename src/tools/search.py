from langchain.tools import tool


# TODO- implement
@tool("web_search")
def web_search(query: str, limit: int = 10) -> str:
  """Search the web for the query listed

  Args:
      query (str): Query to search the 
      limit (int, optional): Maximum number of results. Defaults to 10.
  """
    return "Web Result"
