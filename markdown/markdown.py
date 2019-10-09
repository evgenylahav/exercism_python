import re
from typing import Tuple, Callable, Match

UNORDERED_LIST = r'\* (.*)'
BOLD = r'(.*)__(.*)__(.*)'
ITALIC = r'(.*)_(.*)_(.*)'
HEADERS_AND_LISTS = r'<h|<ul|<li'


class ParseMarkdown:
    def __init__(self, markdown: str):
        self.lines = markdown.splitlines()

    @staticmethod
    def _add_tags(text: str, tag: str) -> str:
        return "<{}>{}</{}>".format(tag, text, tag)

    @staticmethod
    def _mark_with(analyzed_text: str, markdown: str, mark_func: Callable[[str], str]) -> str:
        found = re.match(markdown, analyzed_text)
        if found:
            analyzed_text = found.group(1) + mark_func(found.group(2)) + found.group(3)

        return analyzed_text

    @staticmethod
    def _hash_replacement(match_obj: Match) -> str:
        hash_char = '#'
        if match_obj.group(0) == hash_char * len(match_obj.group(0)):
            return ''
        else:
            return hash_char

    def _add_paragraph(self, text: str) -> str:
        return self._add_tags(text, 'p')

    def _add_bold(self, text: str) -> str:
        return self._add_tags(text, 'strong')

    def _add_italic(self, text: str) -> str:
        return self._add_tags(text, 'em')

    def _mark_unordered_list(self, line: str, is_in_list: bool) -> Tuple[str, bool]:
        found = re.match(UNORDERED_LIST, line)
        if found:
            list_item = found.group(1)
            list_item = self._mark_with(list_item, BOLD, self._add_bold)
            list_item = self._mark_with(list_item, ITALIC, self._add_italic)
            if not is_in_list:
                is_in_list = True
                line = '<ul>' + self._add_tags(list_item, 'li')
            else:
                line = self._add_tags(list_item, 'li')

        return line, is_in_list

    def _mark_headers(self, line: str) -> str:
        subbed_line = re.sub('^#{1,6}', self._hash_replacement, line)
        if subbed_line != line:
            num_of_replaced_hashes = len(line) - len(subbed_line)
            line = self._add_tags(subbed_line[1:], 'h' + str(num_of_replaced_hashes))

        return line

    def _mark_paragraph(self, line: str) -> str:
        if not re.match(HEADERS_AND_LISTS, line):
            line = self._add_paragraph(line)
        return line

    def _check_line(self, line: str, is_in_list: bool) -> Tuple[str, bool]:
        line = self._mark_with(line, BOLD, self._add_bold)
        line = self._mark_with(line, ITALIC, self._add_italic)
        line = self._mark_headers(line)
        line, is_in_list = self._mark_unordered_list(line, is_in_list)
        line = self._mark_paragraph(line)
        return line, is_in_list

    def parse_markdown(self) -> str:
        markdown_output = list()
        is_in_list = False
        for line in self.lines:
            line, is_in_list = self._check_line(line, is_in_list)
            markdown_output.append(line)

        if is_in_list:
            markdown_output.append('</ul>')

        return "".join(markdown_output)


def parse_markdown(markdown: str) -> str:
    return ParseMarkdown(markdown).parse_markdown()
