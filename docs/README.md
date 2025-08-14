# Home

Welcome to the H&H Local AI documentation. This site is built with [Docsify](https://docsify.js.org/#/), a static site generator that uses Markdown files to create a website.

---
## Dependencies
The site is built using the following dependencies:

**npm (node package manager)**
[Link to install instructions npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). But if you want the TLDR:

- You can install npm directly, or get the nvm (node version manager) tool to install npm.

For linux:
- Install nvim. See their [github page](https://github.com/nvm-sh/nvm) for more info.
- Or you can just install npm directly. `sudo apt install npm`

For Windows
- Install nvim. see their [github page](https://github.com/coreybutler/nvm-windows) for more info.
- Or you can just install npm directly. You will have to look up how to install npm on windows (I don't know how and I don't use Windows)

Whatever method you end up using, make sure you have the latest version of npm installed. After that, you will need to run the command `npm install docsify -g`

--- 

## How to use this site
The site is organized into pages and folders:

- The `docs/` folder is the "root" folder and it contains the following subfolders and key files:
  - The `index.html` file is the Docsify front page layout file
  - The `_sidebar.md` file provides a Docsify-compatible sidebar used by the site
  - The `guides/` folder contains guides and tutorials
  - The `components/` folder contains all the components used in the site
  - The `lib/` folder contains CSS and JavaScript files used by Docsify
  - The `about.md` file provides an overview of the project


The site is built using the `docsify serve` command, which starts a local server that serves the site at [localhost:3000](http://localhost:3000). To deploy the website
to GitHub Pages, run `docsify gh-deploy` from the root directory of the repository. This will build the site and deploy it to the `gh-pages` branch.

---

## How to build or edit this site
To edit the site, you can use any text editor or IDE that supports Markdown. The site is built using Docsify, which uses Markdown files to create the pages.

If you want to build and preview the site locally, you can use the `docsify serve docs` command to start a local server that serves the site at [localhost:3000](http://localhost:3000). It will live update as you make changes to the code/md files.

---

## How to navigate the site

You can navigate the site using the sidebar on the left side of the page. The sidebar is generated from the `_sidebar.md` file, which contains a list of pages and their corresponding links.

You can also use the search bar at the top of the page to search for specific pages or keywords.

- Start here: `index.html` (Docsify front page/home page). 
- Navigation: `_sidebar.md` provides a Docsify-compatible sidebar used by the site.
- Quick links:
  - `about.md` — project overview
  - `llm-arch.md` — architecture and agents
  - `llm-usage.md` — user-facing usage instructions

---

## How to add pages
To add a new page, you can create a new Markdown file in the `docs/` folder and add it to the sidebar in `_sidebar.md`. You can also create a new folder and add pages to it. Try and keep things tidy 
if you add a lot of pages.

---

## How to edit pages
To edit a page, you can open the Markdown file in a text editor or IDE that supports Markdown. You can also use a Markdown editor like [Obsidian](https://obsidian.md/), [Typora](https://typora.io/), [VS Code](https://code.visualstudio.com/), or [Neovim](https://github.com/neovim/neovim) with the *Markdown Preview Enhanced*.    


If you run the repository locally and open `docs/index.html` in a browser, Docsify will render the sidebar and pages.

