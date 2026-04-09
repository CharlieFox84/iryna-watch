# Write header (no echo -e needed)
printf "# Change Log (Last 30 Days)\n\nUpdated: %s\n\n" "$(date)" > commit.md

# Append git log entries
git log dev --since="30 days ago" --pretty=format:"- %s (%h, %ad)" --date=short \
  | sed 's|https://github.com/\([^/]\+\/[^ )]\+\)|**\1**|g' >> commit.md

# Ensure trailing newline
printf "\n" >> commit.md