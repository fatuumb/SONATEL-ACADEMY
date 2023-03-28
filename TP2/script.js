const leftDiv = document.querySelector('.left');
const rightDiv = document.querySelector('.right');
const leftBtn = document.querySelector('#leftBtn');
const rightBtn = document.querySelector('#rightBtn');

const gaucheVersDroite = () => {
    const selectedElements = document.querySelectorAll('.left p:hover');
    selectedElements.forEach(element => {
        rightDiv.appendChild(element);
    });
}

const moveRightToLeft = () => {
    const selectedElements = document.querySelectorAll('.right p:hover');
    selectedElements.forEach(element => {
        leftDiv.appendChild(element);
    });
}

leftBtn.addEventListener('click', gaucheVersDroite);
rightBtn.addEventListener('click', moveRightToLeft);
