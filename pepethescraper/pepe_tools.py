from cleantext import clean

def clean_text(text):
	text = clean(text,
				fix_unicode=True,				# fix various unicode errors
				to_ascii=True,					# transliterate to closest ASCII representation
				lower=True,						# lowercase text
				no_line_breaks=False,			# fully strip line breaks as opposed to only normalizing them
				no_urls=False,					# replace all URLs with a special token
				no_emails=False,				# replace all email addresses with a special token
				no_phone_numbers=False,			# replace all phone numbers with a special token
				no_numbers=False,				# replace all numbers with a special token
				no_digits=False,				# replace all digits with a special token
				no_currency_symbols=False,		# replace all currency symbols with a special token
				no_punct=False,					# remove punctuations
				replace_with_punct="",			# instead of removing punctuations you may replace them
				replace_with_url="<URL>",
				replace_with_email="<EMAIL>",
				replace_with_phone_number="<PHONE>",
				replace_with_number="<NUMBER>",
				replace_with_digit="0",
				replace_with_currency_symbol="<CUR>",
				lang="en"						# set to 'de' for German special handling
			)

	return text