#!/bin/bash

# Generate a markdown changelog of commits from the last 30 days
echo -e "## Change Log (Last 30 Days)\n\nUpdated: $(date)\n" > commit.md
git log dev --since="30 days ago" --pretty=format:"- %s (%h)" >> commit.md