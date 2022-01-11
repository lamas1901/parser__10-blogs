from .requests_session import RequestsSession
from typing import Sequence, AnyStr, Tuple


class HyperVisor:
  ''' a Class for hypervisoring all parser modules '''

  def __init__(self, keywords: Sequence[AnyStr], *parser_classes: Tuple[object]) -> None:
    self.parser_classes, self.parsers = parser_classes, None
    self.requests_session_class = RequestsSession()
    self.keywords = keywords

  async def initialize(self) -> None:
    requests_session = await self.requests_session_class.get_requests_session()

    self.parsers = [
      parser_class(requests_session, self.keywords)
    for parser_class in self.parser_classes]
