fetch('https://api.github.com/repos/charliefox84/iryna-watch/releases/latest')
  .then(response => response.json())
  .then(data => {
    const tag = data.tag_name;
    const date = new Date(data.published_at).toLocaleDateString(undefined, {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
    document.getElementById('release-tag').textContent = `Last updated: ${date} · ${tag}`;
  })
  .catch(() => {
    document.getElementById('release-tag').textContent = 'Last updated: unavailable';
  });