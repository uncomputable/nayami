# Generate static website
deploy:
    hugo

# Open local blog in firefox
open:
    firefox localhost:1313

# Run local blog, include drafts, do live updates
serve:
    hugo server --buildDrafts --baseURL localhost

# Add a new post with the given title
add title:
    hugo new content posts/{{title}}.md
