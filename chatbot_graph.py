'''问答类'''

from typing import Union
from question_classifier import *
from question_parser import *
from answer_search import *

from pkg.api import E

class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent) -> Union[str, E.T]:
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return '', E.ERROR_CANOT_CLASSIFY
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_graphDB(res_sql)
        if not final_answers:
            return '', E.ERROR_GET_CONTENT
        else:
            return '\n'.join(final_answers), E.SUCCESS

chat_bot = ChatBotGraph()