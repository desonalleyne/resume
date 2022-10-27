AUTHOR = 'Deson Alleyne'
SITENAME = 'My Resume'
#SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output/'

TIMEZONE = 'America/Guyana'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS_IN_NEW_TAB = 'False'
# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
THEME = '/home/deson/pelican-themes/resume'
CSS_FILE = 'main-2.css'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Profile information
NAME = 'Deson Alleyne'
TAGLINE = 'System Administrator'
PIC = 'avatar.jpg'

#sidebar links
EMAIL = 'desonalleyne@gmail.com'
PHONE = '+592-617-1959'
WEBSITE = 'desonalleyne.github.io'
LINKEDIN = 'desonalleyne'
GITHUB = 'desonalleyne'
#TWITTER = '@desonalleyne'

CAREER_SUMMARY = 'A detail-oriented System Administrator with 7+ years of experience in designing, developing and maintaining large-scale customer-facing applications and financial systems. I am passionate about using technology to improve life and systems around me.'

SKILLS = [
	{
		'type': 'LANGUAGES',
		'list': [
			'Python, Bash Shell, Java, Ruby'
		]
	},
	{
		'type': 'FRAMEWORKS',
		'list': [
			'Aws/Chalice (Allow to quickly create and deploy applications that use AWS Lambda.)',
			'AWS Cloud Development Kit (AWS CDK)',
			'Boto3, psycopg2, slackbot, redis, kubernetes, pyinotify, lxml, kafka, flask, smtplib, threading, requests, etc.'
		]
	},
	{
		'type': 'TOOL',
		'list': [
			'Postgresql, Redis, Cassandra, pgAdmin, pgbarman, MongoDB',
			'Gitlab, Github, Gerrit, Jenkins, Ansible, Portainer, Traefic',
			'ElasticSearch, Kibana, Fluentd, Datadog, Grafana, Zabbix, Glowroot',
			'Kafka, SorlCloud, SystemD',
			'Jira, '
		]
	}
]


SKILLS = [
	{
		'type': 'LANGUAGES',
		'list':'Python, Bash'
	},
	{
		'type': 'TOOLS',
   		'list': [
				'OracleSQL, MySQL',
				'Postman, Github',
				'InfluxDB, Telegraf, Fluentd, Grafana',
				'Jira, UMLet, vim'
		],
  	}
]

xPROJECT_INTRO = 'Here are some projects I\'ve been working on lately.'

xPROJECTS = [
	{
		'title': 'Open Source Contributions',
		'tagline': 'Active contributor in FOSSASIA, worked on the Open Event project (both server and android app).Active contributor in CLTK, worked on the CLTK Web app and API.Made valuable contributions in phpBB, implemented a live search feature.Also made a few contributions to Processing.org and phpMyAdmin.'
	},
	{
		'title': 'Music Hub',
		'tagline': 'Android app that connects multiple devices via wifi and plays music in all connected devices simultaneously to create a loud stereo-like sound effect.'
	},
	{
		'title': 'Music Timer',
		'tagline': 'Android app that monitors phone’s movement to detect whether the user’s asleep and pause music playback accordingly.'
	}
]

LANGUAGES = [
	{
		'name': 'English',
		'description': 'Native'
	}
]

INTERESTS = [
	'Robotics',
	'Home automation',
	'Musical instruments'
]

EXPERIENCES = [
	{
		'job_title': 'System Administrator',
		'time': 'Aug 2020 - Present',
		'company': 'Mobile Money Guyana (Georgetown, Guyana)',
		'details': 'Manage technical operations of mmg+, the only mobile financial services (MFS) platform in Guyana. The platform facilitates bill & merchant payments, money transfers, airtime purchases etc via a mobile wallet.'
	},
	{
		'job_title': 'Assistant Analyst/Programmer',
		'time': 'Aug 2015 - Aug 2020',
		'company': 'Guyana Telephone & Telegraph (Georgetown, Guyana)',
		'details': 'Developed APIs and middleware applications to support prepaid mobile product line for self-service features.'
	},
	{
		'job_title': 'Teacher',
		'time': 'Oct 2014 - Aug 2015',
		'company': 'St. Stanislaus College (Georgetown, Guyana)',
		'details': 'Conducted class sessions and taught IT and CS to Grades 10-13 (90 students)'
	},
	{
		'job_title': 'Teaching Assistant (TA)',
		'time': 'Sep 2013 - May 2014',
		'company': 'University of Guyana (Georgetown, Guyana)',
		'details': 'Conducted tutorials and lab sessions covering topics in HTML, JavaScript, CSS, C Programming and Microsoft Office Suite (~40 students/session)'
	}
]

EDUCATIONS = [
	{
		'degree': 'Master of Science, Data Science',
		'meta': 'IU International University of Applied Science (Germany)',
		'time': '2021 - present'
	},
	{
		'degree': 'Bachelor of Science, Computer Science',
		'meta': 'University of Guyana (Guyana)',
		'time': '2010 - 2014'
	}
]

