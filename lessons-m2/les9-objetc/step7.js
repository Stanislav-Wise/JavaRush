const timerId = setTimeout(() => console.log('3 seconds passed'), 3000);

setTimeout(() => {
    clearTimeout(timerId);
    console.log('Таймер отменен');
}, 1000)

