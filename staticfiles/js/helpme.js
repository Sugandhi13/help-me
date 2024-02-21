/* Declarion of constant variables */
const editButtons = document.getElementsByClassName("btn-edit");
const answerText = document.getElementById("id_content");
const answerForm = document.getElementById("answerForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteAnswerButtons = document.getElementsByClassName("btn-answer-delete");
const deleteQueryButtons = document.getElementsByClassName("btn-query-delete");
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

/* Answer edit button */
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

/* Answer delete button */
for (let button of deleteAnswerButtons) {
  button.addEventListener("click", (e) => {
      let answerId = e.target.getAttribute("answer_id");
      deleteConfirm.href = `delete_answer/${answerId}`;
      deleteModal.show();
  });
}

/* Query delete button */
for (let button of deleteQueryButtons) {
    button.addEventListener("click", (e) => {
        let queryId = e.target.getAttribute("query_id");
        deleteConfirm.href = `delete_query/${queryId}`;
        deleteModal.show();
    });
  }