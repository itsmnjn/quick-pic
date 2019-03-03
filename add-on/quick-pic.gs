/**
 * @OnlyCurrentDoc
 *
 * The above comment directs Apps Script to limit the scope of file
 * access for this add-on. It specifies that this add-on will only
 * attempt to read or modify the files in which the add-on is used,
 * and not all of the user's files. The authorization request message
 * presented to users will reflect this limited scope.
 */

function onOpen(e) {
    DocumentApp.getUi()
        .createAddonMenu()
        .addItem("Start", "showSidebar")
        .addToUi();
}

function onInstall(e) {
    onOpen(e);
}

function showSidebar() {
    var ui = HtmlService.createHtmlOutputFromFile("sidebar").setTitle(
        "Quick Pic"
    );
    DocumentApp.getUi().showSidebar(ui);
}

function insertImage() {
    var cursor = DocumentApp.getActiveDocument().getCursor();
    var response = UrlFetchApp.fetch("https://cataas.com/cat");
    var pic = response.getAs("image/png");

    cursor.insertInlineImage(pic);
}

// function everyMinute(functionName) {
//     ScriptApp.newTrigger(functionName)
//         .timeBased()
//         .everyMinutes(1)
//         .create();
// }
