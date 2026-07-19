/* ProductSiteCMS V0.5 revised - admin data loader */
(function () {
    'use strict';

    window.games = [];
    window.products = [];
    window.faqData = [];
    window.siteInfo = {};
    window.DEFAULT_GAME_ICON = "data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2240%22%20height%3D%2240%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22%238899A6%22%3E%3Cpath%20d%3D%22M12%202C6.48%202%202%206.48%202%2012s4.48%2010%2010%2010%2010-4.48%2010-10S17.52%202%2012%202zm0%203c1.66%200%203%201.34%203%203s-1.34%203-3%203-3-1.34-3-3%201.34-3%203-3zm0%2014.2c-2.5%200-4.71-1.28-6-3.22.03-1.99%204-3.08%206-3.08%201.99%200%205.97%201.09%206%203.08-1.29%201.94-3.5%203.22-6%203.22z%22%2F%3E%3C%2Fsvg%3E";

    async function readJson(filename) {
        const response = await fetch(`../data/${filename}`, { cache: 'no-store' });
        if (!response.ok) {
            throw new Error(`${filename} の読み込みに失敗しました: HTTP ${response.status}`);
        }
        return response.json();
    }

    window.loadGames = async function () {
        const data = await readJson('games.json');
        if (!Array.isArray(data)) throw new Error('games.json は配列形式である必要があります。');
        window.games = data
            .filter(game => game && game.status !== 'hide')
            .sort((a, b) => Number(a.sort || 999999) - Number(b.sort || 999999));
        return window.games;
    };

    window.loadProducts = async function () {
        const data = await readJson('products.json');
        if (!Array.isArray(data)) throw new Error('products.json は配列形式である必要があります。');
        window.products = data
            .filter(Boolean)
            .sort((a, b) =>
                Number(a.sort || 999999) - Number(b.sort || 999999) ||
                Number(a.id || 0) - Number(b.id || 0)
            );
        return window.products;
    };

    window.loadFAQ = async function () {
        const data = await readJson('faq.json');
        if (!Array.isArray(data)) throw new Error('faq.json は配列形式である必要があります。');
        window.faqData = data.filter(item => item && item.visible !== false);
        return window.faqData;
    };

    window.loadSiteInfo = async function () {
        const data = await readJson('siteinfo.json');
        if (!data || typeof data !== 'object' || Array.isArray(data)) {
            throw new Error('siteinfo.json はオブジェクト形式である必要があります。');
        }
        window.siteInfo = data;
        if (data.contact) {
            if (data.contact.xUrl) window.xContactUrl = data.contact.xUrl;
            if (data.contact.lineUrl) window.lineContactUrl = data.contact.lineUrl;
        }
        return window.siteInfo;
    };
})();
