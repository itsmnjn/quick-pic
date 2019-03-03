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
    var body = doc.getBody();
    
    var bodyWidth = (96 * body.getPageWidth()) / 72;
    var idealWidth = bodyWidth / 2;
    
    var bodyHeight = (96 * body.getPageHeight()) / 72;
    var idealHeight = bodyHeight / 2;
    
    var cursor = doc.getCursor();

    if (cursor) {
        var base = "https://quick-pic.net/";
        var id = id;
        var link = base + "retrieve/" + id;

        var response = UrlFetchApp.fetch(link);
        
        if (response == "") {
            return;
        }
        
        var blob = response.getBlob();
        
        if (blob.getContentType() == "text/html") throw "Not an image";

        var inlineImage = cursor.insertInlineImage(blob);

        if (!inlineImage) throw "Cannot insert text here.";
        
        var imageWidth = inlineImage.getWidth();
        var imageHeight = inlineImage.getHeight();
        var aspectRatio = imageWidth / imageHeight;
        
        if (imageWidth > idealWidth) {
            
            inlineImage.setWidth(idealWidth);
            inlineImage.setHeight(idealWidth / aspectRatio);
        }
        
        if (imageHeight > idealHeight) {
            
            inlineImage.setHeight(idealHeight);
            inlineImage.setWidth(idealHeight * aspectRatio);
        }

        var newCursor = doc.newPosition(
            cursor.getElement(),
            cursor.getOffset() + 1
        );
        doc.setCursor(newCursor);
    } else {
        throw "Cannot find a cursor.";
    }
}