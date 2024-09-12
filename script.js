document.addEventListener("DOMContentLoaded", function() {
    const tg = window.Telegram.WebApp;  // Получаем объект Telegram WebApp

    // Инициализация интерфейса
    tg.MainButton.text = "Send Message";
    tg.MainButton.show();

    // Обработка нажатия кнопки
    document.getElementById('send-message').addEventListener('click', function() {
        tg.sendData("Hello from my Mini App!"); // Отправляем сообщение в Telegram
    });

    tg.onEvent('mainButtonClicked', function() {
        tg.sendData("Main Button Clicked!"); // Обработка нажатия основной кнопки
    });
});
