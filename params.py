settings = {"site_title":"Demo blog", # Title of the website
			"author":"Valentin Brosseau", # Author of the website
			"url":"http://demo.url", # Url of the website
			"input":"./source/", # RST source file, Location of RST file
			"output":"./output/", # Output folder for the build
			"plugins":['sitemap','blog','pyscss',"theme","static"], # Enable plugin for this demo project
			"title_as_name": False, # Use the title in the RST as the filename for the output
			"static_settings":"", # Folder of the static files
			"theme":"./theme/demo/", # Folder of the theme
			"blog_settings":{"index_page":"index_blog","nbchar_resume":100,"nb_per_page":7}, # Specific settings for the blog plutin
			"scss_settings":{"files":[('main.scss','main.css'),('pygments.scss','pygments.css')],"path":"./theme/demo/static/styles/"}, # Specific settings for the pyScss plugin
			"build_diff":False, # Enable the differencial build, if True the Yasb script will build only New or Modified file since the last build. Be carrefull this settings may be incompatible with some plugins

			# Specific value (Can be used in template)
			"links":(
					    ('Accueil', '/'),
					    ('Blog', '/index_blog.html'),
					    ('Archives', '/archives.html'),
					    ('RSS Feed', 'feeds/all.atom.xml')
			        )
			}