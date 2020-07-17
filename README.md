![The Paw Society](https://github.com/kervo/fullstack-milestone/blob/master/redme_files/homepage-proto.png "Homepage")

Welcome to the Paw society,

This is the Code Institute student template for Gitpod to present my final project about full stack frameworks with Django.

## The Paw Society - Django fullstack project
![The Paw Society](https://github.com/kervo/fullstack-milestone/blob/master/redme_files/wireframe.png "Wireframe")

# UX-Desing

Offers banner gives the opportunity to catch the user's attention with an attractive service deal

# Testing

* remote: error: File core.Microsoft.Pytho.3919.1594814483 is 225.15 MB; this exceeds GitHub's file size limit of 100.00 MB
I'm leaving a note here in case I get the same error. type this on the CLI `git filter-branch --tree-filter 'rm -f core.Microsoft*' HEAD` and add this file toi your .gitignore file `core.Microsoft* `

* Products not showing on Shop page: When I set up my JSON files, I did it with one entry only and after I added the rest of files but it wasn't showing on my Shop page. The solution was to load the data again with `python3 manage.py loaddata products.json`.

* TemplateSyntaxError("Could not parse the remainder: '%s' " django.template.exceptions.TemplateSyntaxError: Could not parse the remainder
Solution: I was using `{{ url 'product_detail' product.id }}` instead of `{% url 'product_detail' product.id %}` to link pages.


# References
* Photos: Pexel, Homepage: Photo by Helena Lopes from Pexels

