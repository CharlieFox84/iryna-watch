fetch('https://api.github.com/repos/charliefox84/iryna-watch/releases/latest')
  .then(response => response.json())
  .then(data => {
    const tag = data.tag_name;
    document.getElementById('release-tag').textContent = `Release: ${tag}`;
  })
  .catch(() => {
    document.getElementById('release-tag').textContent = 'Release: unavailable';
  });