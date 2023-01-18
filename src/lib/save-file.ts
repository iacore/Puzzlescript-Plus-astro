export function savePlainTextFile(content: string, filename: string) {
    var textFileAsBlob = new Blob([content], {type:'text/plain'}); 
    var downloadLink = document.createElement("a");
    downloadLink.download = filename;
    downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
    downloadLink.click();
}
