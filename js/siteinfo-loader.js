/* ProductSiteCMS V0.4 - Site information JSON loader */
(function () {
    'use strict';

    window.siteInfo = {};

    window.loadSiteInfo = async function loadSiteInfo() {
        const response = await fetch('data/siteinfo.json', { cache: 'no-store' });

        if (!response.ok) {
            throw new Error(`siteinfo.json の読み込みに失敗しました: HTTP ${response.status}`);
        }

        const data = await response.json();

        if (!data || typeof data !== 'object' || Array.isArray(data)) {
            throw new Error('siteinfo.json の形式が正しくありません。オブジェクト形式にしてください。');
        }

        window.siteInfo = data;

        if (data.contact) {
            if (data.contact.xUrl) window.xContactUrl = data.contact.xUrl;
            if (data.contact.lineUrl) window.lineContactUrl = data.contact.lineUrl;
        }

        return window.siteInfo;
    };
})();
