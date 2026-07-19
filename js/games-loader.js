/* ProductSiteCMS V0.2 - ゲーム一覧JSON読込 */
(function () {
    'use strict';

    window.games = [];
    window.DEFAULT_GAME_ICON = "data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2240%22%20height%3D%2240%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22%238899A6%22%3E%3Cpath%20d%3D%22M12%202C6.48%202%202%206.48%202%2012s4.48%2010%2010%2010%2010-4.48%2010-10S17.52%202%2012%202zm0%203c1.66%200%203%201.34%203%203s-1.34%203-3%203-3-1.34-3-3%201.34-3%203-3zm0%2014.2c-2.5%200-4.71-1.28-6-3.22.03-1.99%204-3.08%206-3.08%201.99%200%205.97%201.09%206%203.08-1.29%201.94-3.5%203.22-6%203.22z%22%2F%3E%3C%2Fsvg%3E";

    window.loadGames = async function loadGames() {
        const response = await fetch('data/games.json', { cache: 'no-store' });
        if (!response.ok) {
            throw new Error(`games.jsonの読み込みに失敗しました: HTTP ${response.status}`);
        }

        const data = await response.json();
        if (!Array.isArray(data)) {
            throw new Error('games.jsonの形式が不正です。配列形式で保存してください。');
        }

        window.games = data
            .filter(game => game && game.status !== 'hide')
            .sort((a, b) => {
                const sortA = Number.isFinite(Number(a.sort)) ? Number(a.sort) : 999999;
                const sortB = Number.isFinite(Number(b.sort)) ? Number(b.sort) : 999999;
                return sortA - sortB || Number(a.id || 0) - Number(b.id || 0);
            });

        return window.games;
    };
})();
