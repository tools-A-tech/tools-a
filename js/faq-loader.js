/* ProductSiteCMS V0.3 - FAQ JSON loader */
(function () {
    'use strict';

    window.faqData = [];

    window.loadFAQ = async function loadFAQ() {
        const response = await fetch('data/faq.json', { cache: 'no-store' });

        if (!response.ok) {
            throw new Error(`faq.json の読み込みに失敗しました: HTTP ${response.status}`);
        }

        const data = await response.json();

        if (!Array.isArray(data)) {
            throw new Error('faq.json の形式が正しくありません。配列形式にしてください。');
        }

        window.faqData = data
            .filter((item) => item && item.visible !== false)
            .sort((a, b) => {
                const sortA = Number.isFinite(Number(a.sort)) ? Number(a.sort) : 999999;
                const sortB = Number.isFinite(Number(b.sort)) ? Number(b.sort) : 999999;
                return sortA - sortB || Number(a.id || 0) - Number(b.id || 0);
            });

        return window.faqData;
    };
})();
