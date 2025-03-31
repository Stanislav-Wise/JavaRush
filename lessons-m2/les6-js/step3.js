let playerLevel = 'veteran'; // Уровень доступа игрока
switch (playerLevel) {
    case 'newbie':
        console.log('Скидка 5% на все товары')
        break;
    case 'veteran':
        console.log('Скидка 10% на все оружие и броню.');
        break;
    case 'legend':
        console.log('Бесплатная бутылка Nuka-Cola Quantum!');
        break;
    default:
        console.log('У вас нет скидки.');
}

//   ===