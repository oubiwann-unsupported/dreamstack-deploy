setup:
	git init
	touch README.rst
	git add README.rst
	-git commit -m "Added README placeholder."
	git remote add origin git@github.com:dreamhost/dreamstack-deploy.git
	git push -u origin master

