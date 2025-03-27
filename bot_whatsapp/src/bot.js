const wppconnect = require('@wppconnect-team/wppconnect');
const { exec } = require('child_process');

wppconnect.create({
    session: 'bot-session',
    catchQR: (base64Qr, asciiQR) => {
        console.log('QR Code gerado! Escaneie no seu celular.');
    },
    statusFind: (statusSession, session) => {
        console.log('Status da sessão: ', statusSession);
    }
}).then(client => start(client))
  .catch(error => console.log(error));

function start(client) {
    client.onMessage(async message => {
        if (message.body.toLowerCase() === '!solenidade') {
            exec('python3 solenidades_liturgicas/src/web_scraping.py', (error, stdout, stderr) => {
                if (error) {
                    client.sendText(message.from, 'Erro ao buscar solenidades.');
                    return;
                }
                client.sendText(message.from, `📆 Solenidade de hoje:\n${stdout}`);
            });
        }
    });
}