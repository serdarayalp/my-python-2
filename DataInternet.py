import urllib

originalString = 'The sales tax of "New Jersey" is > 1%'

encodedString = urllib.quote_plus(originalString)


print encodedString
