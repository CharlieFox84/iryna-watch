// Toggle visibility of motion-related timeline cards
document.getElementById('show-motions').addEventListener('change', function () {
const showProcedural = this.checked;
document.querySelectorAll('section.timeline-card[data-tag="procedural-motion"]').forEach(card => {
    card.style.display = showProcedural ? 'block' : 'none';
});
});