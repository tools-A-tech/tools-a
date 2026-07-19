/* ProductSiteCMS V0.1 - 商品JSONローダー */
(function () {
    'use strict';

    window.products = [];

    window.loadProducts = async function loadProducts() {
        const response = await fetch('data/products.json', { cache: 'no-store' });
        if (!response.ok) {
            throw new Error(`products.jsonの読み込みに失敗しました: HTTP ${response.status}`);
        }

        const data = await response.json();
        if (!Array.isArray(data)) {
            throw new Error('products.jsonの形式が不正です。配列である必要があります。');
        }

        window.products = data
            .filter(product => product && product.status !== 'hide')
            .sort((a, b) => {
                const sortA = Number.isFinite(Number(a.sort)) ? Number(a.sort) : 999999;
                const sortB = Number.isFinite(Number(b.sort)) ? Number(b.sort) : 999999;
                return sortA - sortB || Number(a.id || 0) - Number(b.id || 0);
            });

        return window.products;
    };
})();
