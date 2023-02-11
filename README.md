# crafting-list
A test web app that finds crafting recipes for Minecraft.

This python flask app uses HTTP requests to find crafting recipes from a database of all crafting recipes taken straight from the game.

At the moment, the user can browse based on:
* every item on a single page
* by official item ID
* by item group

At the moment, there is a main page and the rest is printed in JSON format on a separate page (will be updated with a proper graphical interface).

The site usage is self-explanatory.

### Technical details
For now, there are 3 pages in total:
* / (main page, takes no arguments)
* /recipes/all (takes no arguments)
* /recipes/specify (takes two arguments: `?id=item_id&group=item_group`)

Every sub-page can be accessed from the main page, and for now, there are only GET requests, since it's a strictly informative api.
