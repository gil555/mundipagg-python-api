class Buyer:
	"""Class that represents a Buyer"""

	#: Buyer custom identification [String]
	buyerReference = None

	#: Email address [String]
	email = None

	#: Facebook ID [String]
	facebookId = None

	#: Gender [String]
	genderEnum = None

	#: Home phone [String]
	#: Pattern +##(###)########
	homePhone = None

	#: IP address [String]
	ipAddress = None

	#: Mobile Phone [String]
	#: Pattern +##(###)########
	mobilePhone = None

	#: Work Phone [String]
	workPhone = None

	#:  Buyer full name [String]
	name = None

	#: Document number [String]
	taxDocumentNumber = None		

	#: Twitter ID [String]
	twitterId = None		

	#: List of addresses [List] 
	addressCollection = []

	#: Buyer unique identification. Generated by Mundipagg [GUID]
	buyerKey = None

	#: Person for indivual people information or Company for enterprise information [String]
	personTypeEnum	= None

	#: CPF for person document number or CNPJ for company document number.
	taxDocumentTypeEnum = None

	class GenderEnum:
		Male = 'M'
		Female = 'F'

	class PersonTypeEnum:
		Person = 'Person'
		Company = 'Company'

	class DocumentType:
		CPF = 'CPF'
		CNPJ = 'CNPJ'		
	
	def __init__(self):				
		self.buyerKey = '00000000-0000-0000-0000-000000000000'		
		self.personTypeEnum	= self.PersonTypeEnum.Person		
		self.taxDocumentTypeEnum = self.DocumentType.CPF