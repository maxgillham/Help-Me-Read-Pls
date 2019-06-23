// Open flags
let isBookmarksOpen = false;
let isSettingsOpen = false;
let isRecording = false;

// Bookmark tab toggle function
function toggleBookmarks(){

    // Get bookmarks tab
    const tab = document.getElementById("BookmarksTab");
    const button = document.getElementById("BookmarksButton");
    const mainScreen = document.getElementById("RecordingScreen");

    // Open if closed
    if(!isBookmarksOpen){
        isBookmarksOpen = true;
        tab.style.left = "0%";
        button.style.backgroundColor = "#ecf0f1";
        mainScreen.style.width = "72%"
    }
    // Close if open
    else{
        isBookmarksOpen = false;
        tab.style.left = "-28%";
        button.style.backgroundColor = "#2c3e50";
        mainScreen.style.width = "100%"
    }

}

// Settings tab toggle function
function toggleSettings(){

    // Get bookmarks tab
    const tab = document.getElementById("SettingsTab");
    const button = document.getElementById("SettingsButton");

    // Open if closed
    if(!isSettingsOpen){
        isSettingsOpen = true;
        tab.style.visibility = "visible";
        tab.style.opacity = "1.0";
    }
    // Close if open
    else{
        isSettingsOpen = false;
        tab.style.visibility = "hidden";
        tab.style.opacity = "0.0";
    }

}

// Record button toggle function
function toggleRecord(){

    // Get bookmarks tab
    const button = document.getElementById("RecordButton");
    const text = document.getElementById("RecordText");

    // Open if closed
    if(!isRecording){
        isRecording = true;
        button.style.backgroundColor = "#c0392b";
        button.style.top = "456px";
        button.style.boxShadow = "0px 0px 0px #2980B9";
        text.textContent = "Recording...";
    }
    // Close if open
    else{
        isRecording = false;
        button.style.backgroundColor = "#3498DB";
        button.style.top = "450px";
        button.style.boxShadow = "0px 6px 0px #2980B9";
        text.textContent = "Start Recording";
    }

}

// Clear text
function startClear(){

    // Get clear button
    const button = document.getElementById("ClearButton");
    const text = document.getElementById("ClearButtonText");

    // Start Clearing
    isClearing = true;
    button.style.boxShadow = "0px 0px 0px #95a5a6";
    button.style.backgroundColor = "#95a5a6";
    text.style.color = "#7f8c8d";
    button.style.top = "471px";

}

// Clear text
function finishClear(){

    // Get clear button
    const button = document.getElementById("ClearButton");
    const text = document.getElementById("ClearButtonText");

    // Unclear
    isClearing = false;
    button.style.boxShadow = "0px 6px 0px #95a5a6";
    button.style.backgroundColor = "#bdc3c7";
    text.style.color = "#95a5a6";
    button.style.top = "465px";

}
