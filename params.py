settings = {"site_title":"Demo blog", 
			"author":"Valentin Brosseau",
			"url":"http://demo.url",
			"input":"./source/",
			"output":"./output/",
			"plugins":['sitemap','blog','pyscss',"theme","static"],
			"title_as_name": False,
			"static_settings":"",
			"theme":"./theme/demo/",
			"blog_settings":{"index_page":"index_blog","nbchar_resume":100,"nb_per_page":7},
			"scss_settings":{"files":[('main.scss','main.css'),('pygments.scss','pygments.css')],"path":"./theme/demo/static/styles/"},

			"links":(
					    ('Accueil', '/'),
					    ('Blog', '/index_blog.html'),
					    ('Archives', '/archives.html'),
					    ('RSS Feed', 'feeds/all.atom.xml')
			        )
			}