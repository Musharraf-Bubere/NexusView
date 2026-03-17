from IPython import display
import urllib.request
from nexusview.custom_exception import InvalidURLException
from nexusview.logger import logger



def is_valid(URL: str) -> bool:
    try:
        response_status = urllib.request.urlopen(URL).getcode()
        assert response_status == 200
        logger.debug(f"response_status: {response_status}")
        return True
    except Exception as e:
        logger.exception(e)
        return False
    

def render_site(URL: str, width: str = "100%", height: str = "600") -> str:
    try:
        logger.info(f"Rendering site: {URL}")

        if is_valid(URL):
            response = display.IFrame(src=URL, width=width, height=height)
            display.display(response)
            return "success"
        else:
            raise InvalidURLException(f"Invalid URL: {URL}")

    except Exception as e:
        logger.error(e)
        raise
