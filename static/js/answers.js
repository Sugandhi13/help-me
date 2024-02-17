const editButtons = document.getElementsByClassName("btn-edit");
const answerText = document.getElementById("id_content");
const answerForm = document.getElementById("answerForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated answer's ID upon click.
* - Fetches the content of the corresponding answer.
* - Populates the `answerText` input/textarea with the answer's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_answer/{answerId}` endpoint.
*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let answerId = e.target.getAttribute("answer_id");
        let answerContent = document.getElementById(`answer${answerId}`).innerText;
        answerText.value = answerContent;
        submitButton.innerText = "Update";
        answerForm.setAttribute("action", `edit_answer/${answerId}`);
    });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
      let answerId = e.target.getAttribute("answer_id");
      deleteConfirm.href = `delete_answer/${answerId}`;
      deleteModal.show();
  });
}

// suppose the `id` attribute of element is `message_container`.
var message_ele = document.getElementById("msg");

setTimeout(function(){ 
   message_ele.style.display = "none"; 
}, 3000);
// Timeout is 3 sec, you can change it
