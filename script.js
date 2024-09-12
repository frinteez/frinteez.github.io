document.addEventListener('DOMContentLoaded', function() {
    const tg = window.Telegram.WebApp;
    
    // Инициализация и отображение мини-приложения
    tg.expand();
    
    // Настройка кнопки
    const button = document.getElementById('mainButton');
    button.addEventListener('click', function() {
        tg.sendData("Button clicked!");
    });
});
