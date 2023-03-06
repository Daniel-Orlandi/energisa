import httpx

class AsyncRequest:
  def __init__(self) -> None:
    self.client = None


  def StartClient(self)->None:    
      if(self.client == None):
        self.client = httpx.AsyncClient()

      else:
        raise Exception("client already initialized.")


  async def get(self, url:str, **Kwargs):
    try:
      self.StartClient()
      response = await self.client.get(url, **Kwargs)
    
    except httpx.TimeoutException as timeout_error:
      print(f'HTTP Exception for {timeout_error.request.url} - {timeout_error}')
    
    except httpx.NetworkError as network_error:
      print(f'HTTP Exception for {network_error.request.url} - {network_error}')
    
    except httpx.InvalidURL as url_error:
      print(f'HTTP Exception for {url_error.request.url} - {url_error}')
    
    except httpx.StreamError as stream_error:
      print(f'HTTP Exception for {stream_error.request.url} - {stream_error}')
    
    except Exception as general_error:
      print(f'Exception for {general_error}')    

    else:
      return response


  async def post(self, url:str, **Kwargs):
    try:
      self.StartClient()
      response = await self.client.post(url, **Kwargs)
    
    except httpx.TimeoutException as timeout_error:
      print(f'HTTP Exception for {timeout_error.request.url} - {timeout_error}')
    
    except httpx.NetworkError as network_error:
      print(f'HTTP Exception for {network_error.request.url} - {network_error}')
    
    except httpx.InvalidURL as url_error:
      print(f'HTTP Exception for {url_error.request.url} - {url_error}')
    
    except httpx.StreamError as stream_error:
      print(f'HTTP Exception for {stream_error.request.url} - {stream_error}')
    
    except httpx.Exception as general_error:
      print(f'HTTP Exception for {general_error.request.url} - {general_error}')    

    else:
      return response.json()

