import re

MARKDOWNS = {
    'unordered list': r'\* (.*)',
    'bold item': '(.*)__(.*)__(.*)',
    'italic item': '(.*)_(.*)_(.*)',
    'h6': '###### (.*)',
    'h2': '## (.*)',
    'h1': '# (.*)',
    'headers and lists': '<h|<ul|<li'
}


class ParseMarkdown:
    def __init__(self, markdown):
        self.lines = markdown.split('\n')
        self.current_line = ''
        self.is_in_list = False

    @staticmethod
    def _add_markdown(text: str, markdown: str) -> str:
        return "<{}>{}</{}>".format(markdown, text, markdown)

    @staticmethod
    def _match(line, markdown):
        return re.match(markdown, line)

    def _add_paragraph(self, text: str) -> str:
        return self._add_markdown(text, 'p')

    def _add_bold(self, text: str) -> str:
        return self._add_markdown(text, 'strong')

    def _add_italic(self, text: str) -> str:
        return self._add_markdown(text, 'em')

    def _mark_with(self, markdown, mark_func, text=None):
        found = self._match(text or self.current_line, markdown)
        if found:
            if text:
                text = found.group(1) + mark_func(found.group(2)) + found.group(3)
            else:
                self.current_line = found.group(1) + mark_func(found.group(2)) + found.group(3)
        if text:
            return text

    def _mark_unordered_list(self):
        found = self._match(self.current_line, MARKDOWNS['unordered list'])
        if found:
            list_item = found.group(1)
            list_item = self._mark_with(MARKDOWNS['bold item'], self._add_bold, list_item)
            list_item = self._mark_with(MARKDOWNS['italic item'], self._add_italic, list_item)
            if not self.is_in_list:
                self.is_in_list = True
                self.current_line = '<ul><li>' + list_item + '</li>'
            else:
                self.current_line = '<li>' + list_item + '</li>'

    def _mark_headers(self):
        if self._match(self.current_line, MARKDOWNS['h6']) is not None:
            self.current_line = self._add_markdown(self.current_line[7:], 'h6')
        elif self._match(self.current_line, MARKDOWNS['h2']) is not None:
            self.current_line = self._add_markdown(self.current_line[3:], 'h2')
        elif self._match(self.current_line, MARKDOWNS['h1']) is not None:
            self.current_line = self._add_markdown(self.current_line[2:], 'h1')

    def _mark_paragraph(self):
        if not self._match(self.current_line, MARKDOWNS['headers and lists']):
            self.current_line = self._add_paragraph(self.current_line)

    def _check_line(self):
        self._mark_with(MARKDOWNS['bold item'], self._add_bold)
        self._mark_with(MARKDOWNS['italic item'], self._add_italic)
        self._mark_headers()
        self._mark_unordered_list()
        self._mark_paragraph()

    def parse_markdown(self):
        markdown_output = ''
        self.is_in_list = False
        for self.current_line in self.lines:
            self._check_line()
            markdown_output += self.current_line

        if self.is_in_list:
            markdown_output += '</ul>'

        return markdown_output


def parse_markdown(markdown):
    parser = ParseMarkdown(markdown)
    return parser.parse_markdown()
