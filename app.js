let timeLeft = 300;
let currentLang = 'ru';
let humanPersona = Math.random() > 0.5 ? 'botA' : 'botB';
let currentNode = 'start';

const UI_TEXT = {
    ru: { ansBtn: "ВЕРДИКТ", modalTitle: "КТО БЫЛ ЧЕЛОВЕКОМ?", retryBtn: "ЗАНОВО", success: "ВЕРНО!", error: "ОШИБКА!", successDesc: "Вы распознали человека.", errorDesc: "Это была имитация." },
    en: { ansBtn: "VERDICT", modalTitle: "WHO WAS HUMAN?", retryBtn: "RETRY", success: "CORRECT!", error: "WRONG!", successDesc: "You recognized the human.", errorDesc: "That was an imitation." }
};

const timerEl = document.getElementById('timer');
const chatWin = document.getElementById('chat-container');
const grid = document.getElementById('options-grid');

const countdown = setInterval(() => {
    timeLeft--;
    let m = Math.floor(timeLeft / 60);
    let s = timeLeft % 60;
    timerEl.innerText = `${m}:${s < 10 ? '0'+s : s}`;
    if (timeLeft <= 0) { clearInterval(countdown); openModal(); }
}, 1000);

function changeLanguage() {
    currentLang = document.getElementById('lang-select').value;
    document.getElementById('ans-btn').innerText = UI_TEXT[currentLang].ansBtn;
    document.getElementById('modal-title').innerText = UI_TEXT[currentLang].modalTitle;
    document.getElementById('retry-btn').innerText = UI_TEXT[currentLang].retryBtn;
    if (DIALOGUE_DB[currentNode]) renderOptions(DIALOGUE_DB[currentNode]);
}

function addMsg(text, side) {
    const d = document.createElement('div');
    d.className = `msg ${side}`;
    d.innerText = text;
    chatWin.appendChild(d);
    chatWin.scrollTop = chatWin.scrollHeight;
}

function openModal() { document.getElementById('overlay').style.display = 'flex'; }

function checkResult(choice) {
    document.getElementById('overlay').style.display = 'none';
    const screen = document.getElementById('result-screen');
    const title = document.getElementById('result-title');
    const desc = document.getElementById('result-desc');
    screen.style.display = 'flex';
    if (choice === humanPersona) {
        title.innerText = UI_TEXT[currentLang].success;
        title.className = "success";
        desc.innerText = UI_TEXT[currentLang].successDesc;
    } else {
        title.innerText = UI_TEXT[currentLang].error;
        title.className = "error";
        desc.innerText = UI_TEXT[currentLang].errorDesc;
    }
}

async function loadNode(key) {
    currentNode = key;
    const node = DIALOGUE_DB[key];
    grid.innerHTML = '';
    await new Promise(r => setTimeout(r, 800));
    addMsg(node[humanPersona][currentLang], 'bot');
    renderOptions(node);
}

function renderOptions(node) {
    grid.innerHTML = '';
    node.options.forEach(o => {
        const b = document.createElement('button');
        b.className = 'opt-btn';
        b.innerText = o.text[currentLang];
        b.onclick = () => {
            addMsg(o.text[currentLang], 'user');
            loadNode(o.next);
        };
        grid.appendChild(b);
    });
}

window.onload = () => {
    changeLanguage();
    loadNode('start');
};