const products = [
  { name: '吉伊卡哇抱枕', category: '生活雜貨', price: 680, visual: 'visual-white', icon: '☁️', type: 'plush' },
  { name: '小八貓隨行杯', category: '生活雜貨', price: 520, visual: 'visual-mint', icon: '🥤', type: 'bottle' },
  { name: '烏薩奇帆布袋', category: '生活雜貨', price: 450, visual: 'visual-yellow', icon: '🛍️', type: 'bag' },
  { name: '吉伊卡哇毛巾', category: '生活雜貨', price: 380, visual: 'visual-blue', icon: '🧺', type: 'towel' },
  { name: '三人組吊飾', category: '穿戴配件', price: 290, visual: 'visual-pink', icon: '🎀', type: 'charm' }
];
const grid = document.querySelector('#productGrid');
const cartCount = document.querySelector('#cartCount');
const toast = document.querySelector('#toast');
let cart = 0;

function renderProducts(filter = 'all') {
  const visible = filter === 'all' ? products : products.filter(product => product.category === filter);
  grid.innerHTML = visible.map((product, index) => `
    <article class="product-card" style="animation-delay:${index * 80}ms">
      <div class="product-visual ${product.visual}"><span class="heart">♡</span><span class="item-icon ${product.type}">${product.icon}</span></div>
      <div class="product-info"><div><p class="product-name">${product.name}</p><p class="category">${product.category}</p></div><span class="price">NT$ ${product.price}</span></div>
      <button class="add-btn" data-name="${product.name}">加入購物車 ＋</button>
    </article>`).join('');
}

renderProducts();
document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => {
  document.querySelector('.filter.active').classList.remove('active');
  button.classList.add('active');
  renderProducts(button.dataset.filter);
}));
grid.addEventListener('click', event => {
  if (!event.target.matches('.add-btn')) return;
  cart += 1;
  cartCount.textContent = cart;
  toast.textContent = `${event.target.dataset.name} 已加入購物車 ♡`;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2200);
});
const searchPanel = document.querySelector('#searchPanel');
document.querySelector('#searchButton').addEventListener('click', () => { searchPanel.classList.add('open'); document.querySelector('#searchInput').focus(); });
document.querySelector('#closeSearch').addEventListener('click', () => searchPanel.classList.remove('open'));
document.querySelector('#cartButton').addEventListener('click', () => {
  toast.textContent = cart ? `購物車裡有 ${cart} 件商品` : '購物車目前是空的';
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2200);
});
