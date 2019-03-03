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

function insertImage(id) {
    var doc = DocumentApp.getActiveDocument();
    var cursor = doc.getCursor();

    if (cursor) {
        var base = "https://quick-pic-233403.appspot.com/";
        var id = id;
        var link = base + "retrieve/" + id;

        var response = UrlFetchApp.fetch(link);
        var pic = response.getBlob();
        var inlineImage = cursor.insertInlineImage(pic);

        if (!inlineImage) throw "Cannot insert text here.";

        var newCursor = doc.newPosition(
            cursor.getElement(),
            cursor.getOffset() + 1
        );
        doc.setCursor(newCursor);
    } else {
        throw "Cannot find a cursor.";
    }
}
