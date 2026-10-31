// INTERACTIVE CATALOGUE CONTROLLER FOR ADEEL ENGINEERING WORKS
import { CORE_MACHINES, PROCESSING_EQUIPMENT, IMPORTED_PRODUCTS } from './products-data.js';

document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('catalogue-grid');
  const countDisplay = document.getElementById('results-count');
  const searchInput = document.getElementById('search-input');
  const sortSelect = document.getElementById('sort-select');
  const filterTabs = document.querySelectorAll('[data-category]');

  if (!container) return;

  // Combine products
  const allItems = [
    ...CORE_MACHINES.map(m => ({ ...m, type: 'core', link: `/products/${m.slug}.html` })),
    ...PROCESSING_EQUIPMENT.map(p => ({ ...p, type: 'processing', link: `/imported-products.html#${p.id}`, overview: p.desc })),
    ...IMPORTED_PRODUCTS.map(i => ({ ...i, type: 'imported', link: `/imported-products.html#${i.id}`, overview: i.desc }))
  ];

  let currentCategory = 'all';
  let currentSearch = '';
  let currentSort = 'default';

  function render() {
    let filtered = allItems.filter(item => {
      // Category filter
      const matchesCategory = currentCategory === 'all' || 
        item.category.toLowerCase().replace(/[^a-z0-9]/g, '-') === currentCategory ||
        (currentCategory === 'core' && item.type === 'core') ||
        (currentCategory === 'pouch' && item.category.includes('Pouch')) ||
        (currentCategory === 'liquid' && item.category.includes('Liquid')) ||
        (currentCategory === 'powder' && item.category.includes('Powder')) ||
        (currentCategory === 'processing' && item.type === 'processing') ||
        (currentCategory === 'imported' && item.type === 'imported');

      // Search filter
      const q = currentSearch.toLowerCase().trim();
      const matchesSearch = !q || 
        item.name.toLowerCase().includes(q) || 
        (item.overview && item.overview.toLowerCase().includes(q)) ||
        (item.applications && item.applications.some(a => a.toLowerCase().includes(q)));

      return matchesCategory && matchesSearch;
    });

    // Sorting
    if (currentSort === 'alpha-asc') {
      filtered.sort((a, b) => a.name.localeCompare(b.name));
    } else if (currentSort === 'alpha-desc') {
      filtered.sort((a, b) => b.name.localeCompare(a.name));
    }

    // Render count
    if (countDisplay) {
      countDisplay.textContent = `Showing ${filtered.length} machine${filtered.length === 1 ? '' : 's'}`;
    }

    // Empty state
    if (filtered.length === 0) {
      container.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px; background: #ffffff; border: 1px dashed var(--color-border); border-radius: 12px;">
          <h3 style="font-size: 1.25rem; margin-bottom: 8px; color: var(--color-primary-dark);">No machines found</h3>
          <p style="color: var(--color-text-muted); margin-bottom: 20px;">Try adjusting your keywords or clearing the category filters.</p>
          <button id="reset-filters" class="btn btn-secondary btn-sm">Reset All Filters</button>
        </div>
      `;
      document.getElementById('reset-filters')?.addEventListener('click', () => {
        if (searchInput) searchInput.value = '';
        currentSearch = '';
        currentCategory = 'all';
        filterTabs.forEach(t => t.classList.toggle('active', t.getAttribute('data-category') === 'all'));
        render();
      });
      return;
    }

    // Render cards
    container.innerHTML = filtered.map(item => `
      <article class="machine-card" data-category="${item.category}">
        <div class="machine-card-media">
          <span class="machine-category-tag">${item.category}</span>
          <img src="${item.image}" alt="${item.name}" loading="lazy" />
        </div>
        <div class="machine-card-body">
          <h3 class="machine-card-title">${item.name}</h3>
          <p class="machine-card-desc">${item.overview || item.desc || ''}</p>
          ${item.speed ? `
            <div class="machine-card-meta">
              <div class="machine-meta-item">
                <span class="meta-label">Speed</span>
                <span class="meta-val">${item.speed}</span>
              </div>
              <div class="machine-meta-item">
                <span class="meta-label">Power</span>
                <span class="meta-val">${item.powerSupply || '220V'}</span>
              </div>
            </div>
          ` : `
            <div class="machine-card-meta">
              <div class="machine-meta-item">
                <span class="meta-label">Origin</span>
                <span class="meta-val">${item.type === 'core' ? 'Adeel Works' : 'Imported'}</span>
              </div>
              <div class="machine-meta-item">
                <span class="meta-label">Catalogue</span>
                <span class="meta-val">Page ${item.page || 1}</span>
              </div>
            </div>
          `}
          <div class="machine-card-footer">
            <a href="${item.link}" class="btn btn-secondary btn-sm">View Details</a>
            <a href="/request-quote.html?machine=${encodeURIComponent(item.name)}" class="btn btn-primary btn-sm">Inquire</a>
          </div>
        </div>
      </article>
    `).join('');
  }

  // Event listeners
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      currentSearch = e.target.value;
      render();
    });
  }

  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      currentSort = e.target.value;
      render();
    });
  }

  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      currentCategory = tab.getAttribute('data-category');
      render();
    });
  });

  // Initial render
  render();
});
