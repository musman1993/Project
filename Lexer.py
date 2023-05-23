#Types of tokens
PRINT_TOKEN = 'printf'
R_PARENT    = '('
L_PARENT    = ')'
EOL         = ';'
STRING      = '"'
STRING_ALT  = "'"
LETTERS     = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm' #used for letter "detection"

class Token():
	def __init__(self, TokenType, value=[-1]):
		self._type = TokenType
		self._value = value
	def __repr__(self):
		return f'{self._type}:{self._value}'

class Lexer():
	def __init__(self, text):
		self.text   = text
		self.pos    = -1
		self.word   = ''
		self.letter = ''
	def step(self):
		self.pos += 1
		if len(self.text) > self.pos: 
			self.letter = self.text[self.pos]
			self.word += self.letter
	def print_word(self):
		print(self.word)


lexer = Lexer('test')
lexer.step()
lexer.step()
lexer.step()
lexer.step()
lexer.step()
lexer.print_word()