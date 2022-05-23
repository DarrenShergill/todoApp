/* Function will take a noteId that we pass and send a POST request to the delete-note end point.
After it gets a response from the delete-note endpoint, it is going to reload the window.
window.location.href = "/" means redirect us to the homepage which is what refreshes the page. */

function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
    window.location.href = "/";
    });
}