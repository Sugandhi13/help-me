# Help Me !

Help Me is website, where you can ask any query and get responses from other users who have knowledge or experience in that domain. Whether you want to learn something new, get advice, share your opinions or just have fun, this is the place for you.

## AmIResponsive

![responsive_test](static/images/readme_images/amiresponsive.png)

Help Me ! is live, to access it <a href="https://help-me-038cd18040fa.herokuapp.com/" target="_blank">click here.</a>

## Table of contents

+ [UX](#ux)
+ [Design](#design)
+ [Features](#features)
+ [Testing](#testing)
+ [Technologies used](#technologies-used)
+ [Deployment](#deployment)
+ [Credits](#credits)

## UX

### Site Purpose

Our mission is to create a community of curious and helpful people who can learn from each other and exchange information on various topics. We believe that everyone has something valuable to offer and that by asking and answering questions, we can enrich our knowledge and understanding of the world.

### Audience

Help me is for everyone who have any query or would like to help other users, those have asked queries in different categories like,

- Education
- Entertainment
- Finance
- Food
- Health
- Politics
- Sports 
- Travel  

### Current User Goals

- Ask query
- Respond on a query
- Delete query
- Delete or edit responses
- Add user profile
- Contact admin for suggestion, thoughts

### Future User Goals

- Like, disklike or upvote different queries or response given by other users
- See all users profile
- See all queries asked or response given in a page
- Option to add new categories
- Filter queries or responses
- Upload image in add profile page

## Design

### Color scheme

![color_palette](static/images/readme_images/colorpalette.png)

### Typography

Lato font is the major font used in this website for all kind of text with fallback option to sans-serif if the browser don't support the preffered color Lato.

### Agile methodology

Agile project management principles guided the development of this project, leveraging GitHub Projects as the primary software for tracking user stories. Utilizing the Kanban board task view, I crafted a comprehensive user story template that served as the foundation for all project-related narratives. Beyond capturing the core user stories, GitHub Projects played a pivotal role in efficiently monitoring and addressing bugs identified throughout the project's lifecycle. 

### Wireframes

The separate documetns for the wireframes can be found here:

<details>
    <summary>Desktop Wireframes</summary>
    <details>
        <summary>Home Page (without login)</summary>
            <IMG src="static/images/readme_images/wireframe/homewithoutlogin_wf.png" alt="home_page_without_login"/>
    </details>
    <details>
        <summary>Home Page (with login)</summary>
        <IMG src="static/images/readme_images/wireframe/homewithlogin_wf.png" alt="home_page_with_login"/>
    </details>
    <details>
        <summary>Ask A Query Page</summary>
        <IMG src="static/images/readme_images/wireframe/askaquery_wf.png" alt="ask_query_page"/>
    </details>
    <details>
        <summary>Query Page</summary>
        <IMG src="static/images/readme_images/wireframe/query_wf.png" alt="query_page"/>
    </details>
    <details>
        <summary>Answer Page</summary>
        <IMG src="static/images/readme_images/wireframe/answer_wf.png" alt="answer_page"/>
    </details>
    <details>
        <summary>Add Profile Page</summary>
        <IMG src="static/images/readme_images/wireframe/addaprofile_wf.png" alt="add_profile_page"/>
    </details>
    <details>
        <summary>Profile Page</summary>
        <IMG src="static/images/readme_images/wireframe/profile_wf.png" alt="profile_page"/>
    </details>
    <details>
        <summary>About Us Page</summary>
        <IMG src="static/images/readme_images/wireframe/aboutus_wf.png" alt="about_us_page"/>
    </details>
    <details>
        <summary>Contact Us Page</summary>
        <IMG src="static/images/readme_images/wireframe/contactus_wf.png" alt="contact_us_page"/>
    </details>
    <details>
        <summary>Signup Page</summary>
        <IMG src="static/images/readme_images/wireframe/signup_wf.png" alt="sign_up_page"/>
    </details>
    <details>
        <summary>Login Page</summary>
        <IMG src="static/images/readme_images/wireframe/login_wf.png" alt="login_page"/>
    </details>
    <details>
        <summary>Logout Page</summary>
        <IMG src="static/images/readme_images/wireframe/logout_wf.png" alt="logout_page"/>
    </details>
    <details>
        <summary>Error Page</summary>
        <IMG src="static/images/readme_images/wireframe/error_wf.png" alt="error_page"/>
    </details>
</details>

<details>
    <summary>Mobile Wireframes</summary>
    <details>
        <summary>Home Page</summary>
        <IMG src="static/images/readme_images/wireframe/homemobile_wf.png" alt="home_page_mobile"/>
    </details>
</details>

### Database schema

The database schema is composed by 6 models: Category, Query, Answer, About, User Profile and Contact information. 

![database_schema](static/images/readme_images/erdiagram.png)

#### Category

This model consist of different categories available on website for which a user can ask or respond to queries. Only admin have access to this model and access to create a new categories. This model have following fields:

- Id: Unique id for each category and it works as primary key for the model.
- Title: A character field that handles category name.
- Slug: A character field and autogenerated with the help of summernotes. This helps in creating the urls and route user to a page where all queries for respective category can be seen.
- Fontawesome_Icon: A character field that handle the fontawesome icons text taken from w3c bootstrap website and fits for visualisation purpose of each category.
- Author: A character field that handle the username, who is adding the category. In current case, its only admin. But, in future goals, I would like to give oppurtunities to site user to add the categories if not exists already. Its a Forigen key to the django User model.
- Created_On: A Datetime field used to store the category creation datetime.

#### Query

This model consist of all queries that any user asks with Foriegn key link to Category model to handle display only queries for respective categories at front end. Site user have access to ask new queries in this model and admin have access to approve the queries to display asked queries to all users. This model have following fields:

- Id: Unique id for each query and it works as primary key for the model.
- Title: A character field that handles query title.
- Slug: A character field and autogenerated with the help of summernotes. This helps in creating the urls and route user to a page where all answer for respective query can be seen.
- Author: A character field that handle the username, who is asking the question based upon the session logged in. Its a Forigen key to the django User model.
- Category: A character field that handle the category for which the query has been asked and aligned to. Its a Forigen key to the Category model.
- Content: A Text field that handle the details view of the query. It has no words limit.
- Created_On: A Datetime field used to store the query creation datetime.
- Status: Its an integer field that is used to set status of the query. The default value is 0 that means Draft and admin can set this value to 1 that means Published and only after the status is set to 1 (Published) by the admin the query asked will be visible to all.

#### Answer

This model consist of all answer that any user writes with Foriegn key link to Query model to handle display only answer for respective query at front end. Site user have access to write answers in this model and admin have access to approve the answer to display answer written to all users. This model have following fields:

- Id: Unique id for each query and it works as primary key for the model.
- Query: A character field that handle the query for which the answer has been given. Its a Forigen key to the Query model.
- Author: A character field that handle the username, who is writing the answer based upon the session logged in. Its a Forigen key to the django User model.
- Content: A Text field that handle the details view of the answer. It has no words limit.
- Approved: Its an boolean field that is used to approve the answer. The default is not approved and admin mark it as approved by clicking the checkbox option on answer from on admin site. Once the answer is approved only after that it will be visible to all.
- Created_On: A Datetime field used to store the answer creation datetime.

#### UserProfile

This model consist of all user profiles that any logged in user create for itself. The user has been identify with the help of django user model to display the correct profile at front end. Site user have access to write information about its profile in this model and admin have access to upload the image for user profile. This model have following fields:

- Id: Unique id for each query and it works as primary key for the model.
- First_Name: A character field that handle the first name of the user.
- Last_Name: A character field that handle the last name of the user.
- Email: An email field that handle the email address of the user.
- Profile_Image: A Cloudinary field that handles the image uploaded by the admin for the user.
- Username: A character field that handle the username, who is writing its profile based upon the session logged in. Its a Forigen key to the django User model.
- Describe_Yourself: A Text field that handle the details view of the description the user write about itself. It has no words limit.
- Updated_On: A Datetime field used to store the last updated datetime.

#### About

This model consist of all about us information of this website. Only admin can update this model. This model have following fields:

- Id: Unique id for each query and it works as primary key for the model.
- Title: A character field that handle the Title for the about us page.
- Profile_Image: A Cloudinary field that handles the image uploaded by the admin for about us page.
- Content: A Text field that handle the details view of the description the admin writes about the website. It has no words limit and summernotes are used to store the data in rich text format.
- Updated_On: A Datetime field used to store the last updated datetime.

#### Contact

This model consist of all contact us information of when a site user writes to the admin. Any site user can update this model regardless of the user is logged in or not. This model have following fields:

- Id: Unique id for each query and it works as primary key for the model.
- Name: A character field that handle the name of the user who is trying to contact the admin.
- Email: An email field that handle the email address of the user.
- Message: A Text field that handle the details view of the message the user writes about the website admin. It has no words limit.
- Read: Its an boolean field that is used to mark the message as read by the admin. The default is not read and admin mark it as read by clicking the checkbox option on contact from on admin site.
- Created_On: A Datetime field used to store the contact message creation datetime.

## Features

### Common Features

#### Language Used

- Django
- Python
- HTML5
- CSS3
- Javascript

#### Navbar

- On large screens, the navbar displays brand icon and name along with links to Home, About, Contact Us, Ask a query. If user is not logged in it displays the Sign Up and Login links too. Also, on right corner a message dispalys that user is not logged in. 
- When the user is logged in apart from showing the navbar displays brand icon and name along with links to Home, About, Contact Us, Ask a query the Profile and logout links are dispalyed too. Also, on right corner a Hi username message display with some stylized view.
- In small screens, all links are placed within a burger menu. The brand name and icon display outside the collapseable burger menu.

<details>
    <summary>Desktop View (Without user login) </summary>
    <IMG src="static/images/readme_images/navbar/navbarwithoutuserlogin.png" alt="desktop_navbar_without_user_login"/>
</details>

<details>
    <summary>Mobile View  (Without user login) </summary>
        <IMG src="static/images/readme_images/navbar/navbarmobilewithoutuserlogin.png" alt="mobile_navbar_without_user_login"/>
</details>

<details>
    <summary>Desktop View  (With user login) </summary>
    <IMG src="static/images/readme_images/navbar/navbarwithuserlogin.png" alt="desktop_navbar_with_user_login"/>
</details>

<details>
    <summary>Mobile View  (With user login) </summary>
        <IMG src="static/images/readme_images/navbar/navbarmobilewithuserlogin.png" alt="mobile_navbar_with_user_login"/>
</details>

#### Footer

- Users have functional links to Facebook, Twitter, Instagram and YouTube. These links will open in a new tab as they are outside the web application. 

<details>
    <summary>Desktop View</summary>
    <IMG src="static/images/readme_images/navbar/footer.png" alt="desktop_footer"/>
</details>

<details>
    <summary>Mobile View</summary>
        <IMG src="static/images/readme_images/navbar/footermobile.png" alt="mobile_footer"/>
</details>

#### Index

- The landing page of the website display different categories a user can access or choose to ask queries or write answer for queries asked by other users.
- If user is not logged in then a message displays in the top right corner on navbar that the user is not logged in. Also, Signup and Login links show in navbar menu. Whereas the add or view profile buttons doesn't appear in navbar menu.

<details>
    <summary>Home Page - Desktop View (Without user login)</summary>
    <IMG src="static/images/readme_images/webpagewithoutuserlogin/homepagewithoutlogin.png" alt="homepage_without_user_login"/>
</details>

- If user is logged in then a greetings to the user as 'Hi! USERNAME' displays in the top right corner on navbar. Also, Signup and Login links disappear, whereas the profile and logout buttons become visible in navbar menu.

<details>
    <summary>Home Page - Desktop View (With user login)</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/homepageafteruserloginwithloginmessage.png" alt="homepage_with_user_login"/>
</details>

- On mobile, the navbar displays with collapseble burger menu icon. By default its collapsed. On first click over burger menu it expands and show all navbar menu links as per same criteria that applied in desktop view.

<details>
    <summary>Home Page - Mobile View</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/mobilehomepage.png" alt="mobile_homepage"/>
</details>

- Apart from the user, admin of the website additionally have the admin dashboard. From this the admin can access the different models that are used to store the data in them. Admin can take any kind of add, update, delete actions. At some places the access to admin is also restricted and that will be explained in upcoming steps. For e.g., Query or Answers content are un-editable by the admin. Though, admin still have the access to not approving them, hence not visible to all users or can delete them.

<details>
    <summary>Admin Dashboard</summary>
    <IMG src="static/images/readme_images/adminpage/adminhomepage.png" alt="admin_dashboard"/>
</details>

#### About us 

- This is an informational page that includes a brief description of the website, the mission with this website the owner would like to achieve, the services the website provides and explains what a user can do on the website and different categories available to ask queries and provide responses to already asked queries. Lastly it give short details about the team and encourage the user to reachout to development team with any feedback or suggestions.

<details>
    <summary>About Us Page (Without user login)</summary>
    <IMG src="static/images/readme_images/webpagewithoutuserlogin/aboutuspagewithoutlogin.png" alt="aboutus_page_without_user_login"/>
</details>

<details>
    <summary>About Us Page (With user login)</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/aboutuspagewithuserloggedin.png" alt="aboutus_page_with_user_login"/>
</details>

- Only the admin of the website has authorization to update the about us page content. 

<details>
    <summary>About Us Page - Admin</summary>
    <IMG src="static/images/readme_images/adminpage/aboutusadminview.png" alt="aboutus_page_admin"/>
</details>

<details>
    <summary>About Us Model - Admin</summary>
    <IMG src="static/images/readme_images/adminpage/aboutusmodeladminview.png" alt="aboutus_model_admin"/>
</details>

#### Contact

- This page contains a form for a user to directly contact the admin. The fields include name, email and message. 

<details>
    <summary>Contact Us Page (Without user login)</summary>
    <IMG src="static/images/readme_images/webpagewithoutuserlogin/contactuspagewithoutlogin.png" alt="contactus_page_without_user_login"/>
</details>

<details>
    <summary>Contact Us Page (With user login)</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/contactuspagewithuserloggedin.png" alt="contactus_page_with_user_login"/>
</details>

- If the form is invalid, error messages will be displayed. 

<details>
    <summary>Contact Us Page - Error</summary>
    <IMG src="static/images/readme_images/testing/contactus_error.png" alt="contactus_page_error"/>
</details>

- If the form is successfully submitted. A success message will display below the navbar.

<details>
    <summary>Contact Us Page - Success</summary>
    <IMG src="static/images/readme_images/testing/contactus_success.png" alt="contactus_page_success"/>
</details>

- The admin of the website can see the different message posted by the users using the contact us form. The admin also has the option to mark the message and read using the check-box option in the contact model. This will help the admin to track how many message he has already read and/or responded. 

<details>
    <summary>Contact Us Page - Admin</summary>
    <IMG src="static/images/readme_images/adminpage/contactusadminview.png" alt="contactus_page_admin"/>
</details>

<details>
    <summary>Contact Us Model - Admin</summary>
    <IMG src="static/images/readme_images/adminpage/contactusmodeladminview.png" alt="contactus_model_admin"/>
</details>

#### Ask a Query 

- A user should be logged in to ask a query on the webstie. If user is not yet logged in then a message with login button link will displays to the user. 

<details>
    <summary>Ask a Query Page (Without user login)</summary>
    <IMG src="static/images/readme_images/webpagewithoutuserlogin/askaquerypagewithoutlogin.png" alt="askaquery_page_without_user_login"/>
</details>

- If the user is logged in then a query form will appear that the user can fill to ask a query. If any required input is not give then the error will displays. 

<details>
    <summary>Ask a Query Error</summary>
    <IMG src="static/images/readme_images/testing/query_error.png" alt="askaquery_page_error"/>
</details>

- If all requried data is filled and user select a valid category as well then upon submission the a success message will appear just below the top navbar.

<details>
    <summary>Ask a Query Success</summary>
    <IMG src="static/images/readme_images/testing/queryaskedsuccessfullmessage.png" alt="askaquery_page_success"/>
</details>

- After successfully submitting the query. The user can go and see the query showing in respective category. Though, until the query is approved by the admin the query will only be visible to the authorized user only along with option of delete button to delete the query. Once the query is approved then the query is visible for all other users to see and write response against it.

<details>
    <summary>Queries Asked View</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/querypagewithunapprovedquerydisplay.png" alt="queries_asked_view"/>
</details>

- If the user press the delete button then a popup will appear to re-confirm the users choice to delete the query asked. An authonticated user can delete any old queries asked by them as well. But, the user can not delete any query asked by the other users.

<details>
    <summary>Query Delete Popup</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/deletequerypopupwhenclickeddeletebuttonbyloggedinuser.png" alt="queries_delete_reconfirm"/>
</details>

- If the users clicks on close button then nothing happen. But, if the users clicks on delete button again and confirms that he wants to delete the query asked. The delete success message will appear and the query will be delete from the database.

<details>
    <summary>Query Delete Success</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/querydeletedsuccessmessage.png" alt="queries_delete_success"/>
</details>

- Once the users posts a query and it goes to admin for approval. Admin gets a view of all the queries asked by different users. I have used summernotes admin functionality to display the customized details to admin and he has option to filter or sort the queries based upon time, users, category.

<details>
    <summary>Queries View - Admin</summary>
    <IMG src="static/images/readme_images/adminpage/queriesadminview.png" alt="queries_view_admin"/>
</details>

- Admin can click on any query, specifically the un-approved ones that has status of 'Draft' and go into the query model view to approve it. After selecting the 'Published' option from the dropdown menu the query will be start displaying for all the users. Henceforth other users on the website can write in response to that query.

<details>
    <summary>Queries Model - Admin</summary>
    <IMG src="static/images/readme_images/adminpage/querymodeladminview.png" alt="queries_model_view_admin"/>
</details>

#### Write an Answer 

- A user should be logged in to write an answer on the webstie. If user is not yet logged in then a message with login button link will displays to the user. 

<details>
    <summary>Write an Answer Page (Without user login)</summary>
    <IMG src="static/images/readme_images/webpagewithoutuserlogin/answerspagewithoutlogin.png" alt="answer_page_without_user_login"/>
</details>

- If the user is logged in then answer form will appear that the user can fill about the asked query. If required input is not give then the error will displays. 

<details>
    <summary>Write an Answer Error</summary>
    <IMG src="static/images/readme_images/testing/answer_error.png" alt="answer_page_error"/>
</details>

- If all requried data is filled then upon submission the a success message will appear just below the top navbar.

<details>
    <summary>Write an Answer Success</summary>
    <IMG src="static/images/readme_images/testing/answersubmittedsuccessmessage.png" alt="answer_page_success"/>
</details>

- After successfully submitting the answer. The user can see the answer at top of other queries and below the write an answer box. Though, until the answer is approved by the admin the answer will only be visible to the authorized user only along with option of edit and delete button to edit or delete the answer. Once the answer is approved then the answer is visible for all other users to see.

<details>
    <summary>Answer Written View</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/answersubmittedandwaitingforapproval.png" alt="answer_written_view"/>
</details>

- If the user press the edit button then the existing answer written by the user will re-appear in the write an answer box. An authonticated user further edit/update the old answer written by them as well.

<details>
    <summary>Answer Edit</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/answereditedbyuser.png" alt="answer_delete"/>
</details>

- Once the answer is update by the user then the user can click on submit button again and the answer will be re-submitted and will show to authunticated user only with message of waiting for approval.

<details>
    <summary>Answer Edit Success</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/answerupdatedsuccessmessage.png" alt="answer_edit_success"/>
</details>

- If the user press the delete button then a popup will appear to re-confirm the users choice to delete the answer wrote. An authonticated user can delete any old answer written by them as well. But, the user can not delete any answer written by the other users.

<details>
    <summary>Answer Delete Popup</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/deleteanswerpopoup.png" alt="answer_delete_reconfirm"/>
</details>

- If the users clicks on close button then nothing happen. But, if the users clicks on delete button again and confirms that he wants to delete the answer written. The delete success message will appear and the answer will be delete from the database.

<details>
    <summary>Answer Delete Success</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/answerdeletedsuccessmessage.png" alt="answer_delete_success"/>
</details>

- Once the users posts an answer and it goes to admin for approval. Admin gets a view of all the answers written by different users. I have used summernotes admin functionality to display the customized details to admin and he has option to filter or sort the answer based upon time, users etc.,

<details>
    <summary>Answer View - Admin</summary>
    <IMG src="static/images/readme_images/adminpage/answersadminview.png" alt="answer_view_admin"/>
</details>

- Admin can click on any answer, specifically the un-approved ones and go into the answer model view to approve it. After ticking the checkbox 'Approved' the answer will be start displaying for all the users.

<details>
    <summary>Answer Model - Admin</summary>
    <IMG src="static/images/readme_images/adminpage/answermodeladminview.png" alt="answer_model_view_admin"/>
</details>

#### Sign Up

- When not authenticated, users can create an account using a unique username and password.

<details>
    <summary>Signup Page</summary>
    <IMG src="static/images/readme_images/webpagewithoutuserlogin/signuppage.png" alt="signup_page"/>
</details>

- When the user attempts to create an account with an existing username, a password that does not fulfill the requirements, or if the passwords do not match, an error is displayed in the form.

<details>
    <summary>Signup Error</summary>
    <IMG src="static/images/readme_images/testing/signup_error.png" alt="signup_error"/>
</details>

- When users fill all details as per required criteria and submit the form. Signup successfull message will appear and user will logged into the website and redirected to Home page.

<details>
    <summary>Signup Form Example</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/testusersignup.png" alt="signup_form"/>
</details>

<details>
    <summary>Signup Success</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/signupsuccessmessage.png" alt="signup_success"/>
</details>

- The admin can see all the user who has created their account on website from the User model on django admin page.

<details>
    <summary>User Model View</summary>
    <IMG src="static/images/readme_images/adminpage/useradminview.png" alt="user_model_view"/>
</details>

#### Log In

- Login Page: A user can log in to the application by inputting their username and correct password.

<details>
    <summary>Login Page</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/loginpageuserlogin.png" alt="login_page"/>
</details>

- If, when logging in, the user inputs an incorrect username or password, the form will display the error.

<details>
    <summary>Login Error</summary>
    <IMG src="static/images/readme_images/testing/login_error.png" alt="login_error"/>
</details>

#### Log Out


- Logout Page: Here, the application asks the user for confirmation before logging out. 

<details>
    <summary>Logout Page</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/logoutpage.png" alt="logout_page"/>
</details>

#### Profile 

- After a user signs in the user has option to add its profile page. This page open up first with error with a button that is linked to add a profile, when the user clicks on Profile link from the navbar menu and if the user doesn't have an existing profile.

<details>
    <summary>Profile Not Found</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/errorwhennewuserclickonprofilepage.png" alt="profile_not_found"/>
</details>

- Then the user can create its profile by filling the information like the firstname, lastname, email id, profile image and writing few lines about itself under describe yourself text box.

<details>
    <summary>Profile Form</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/createprofilepage.png" alt="profile_form"/>
</details>

- If any incorrect information is filled then the user wil face error.

<details>
    <summary>Profile Form Error</summary>
    <IMG src="static/images/readme_images/testing/addprofile_error.png" alt="profile_form_error"/>
</details>

- If the form is valid, a success message stating that their profile has been created populate just below the navbar with a link to view the profile. The user can click on that link or from top navbar Profile menu can route to user profile page view. 

<details>
    <summary>Profile Form Success</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/profilecreatesuccessmessagewithlinkofprofileviewpage.png" alt="profile_form_success"/>
</details>

<details>
    <summary>Profile View</summary>
    <IMG src="static/images/readme_images/webpagewithuserlogin/profilepageofloggedinuserifusercreateditsprofile.png" alt="profile_form_success"/>
</details>

- The admin can view all the profiles created from the UserProfile view on the django admin dashboard. The user of summernotes helps here to customize the look of admin page as per admin need and also has various filter and sorting options.

<details>
    <summary>User Profile View - Admin</summary>
    <IMG src="static/images/readme_images/adminpage/usersprofileadminview.png" alt="user_profile_view_admin"/>
</details>

- The admin can edit a little like upload the profile photo on behalf of the user if the user writes to admin. As the upload photo functionality is not yet working on the website and it an open bug.

<details>
    <summary>User Profile Model - Admin</summary>
    <IMG src="static/images/readme_images/adminpage/userprofilemodeladminview.png" alt="user_profile_model_admin"/>
</details>

### Future Features

- Asynchronous behaviour
    - When a query or answer submitted once but if the page is refreshed the same query or answer gets re-submitted. A future feature is planned to avoid resubmitting it and clear out the page when these actions are taken by the user.

- Profile image upload by the user
    - When a user try to create its profile. Currently the profile image upload option is given but its not working and the site user is not able to load the profile image by itself. Only the admin can do it on the users behalf. Hence, in future release this bug is planned to fix.

- Further relevant feedback
    - Implement autohide notifications.
    - Implement like, upvote feature on queries and answers.
    - Implement edit query feature.
    - Implement a user can see all its queries and answer from a single profile page too.
    - Implement all profile page where a user can see breif profile info about other users too like how many query they have asked or answer they have given. What feilds they are expert of etc.,

## Testing

### Methodology 

Testing was an integral part of the project development, encompassing the use of Django debug pages and strategically placed print statements to verify the functionality of the code at various stages. Furthermore, a comprehensive testing approach was adopted, outlined below. This involved meticulous manual testing to ensure alignment with all user stories and acceptance criteria as well as some automated testing using for different forms.

#### Index page

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Navigation bar functionality (user not authenticated) | Click all available links | User is directed respectively to the home, about us, contact us, ask a query or account signup links | PASS |
| Navigation bar functionality (user authenticated) | Click all available links | User is directed respectively to the navbar links and has the correct account links (profile and logout) | PASS |
| Footer links | Click all available social media links | User is directed respectively to all social media links with  | PASS |
| Cateogries | Click all categories links | User is directed to queries page respected to each category and all queries belogns to that category should display on next page  | PASS |

#### About us page

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| About us info | Goto about us page and see info, profile image and updated on datetime | The latest about us info displays and the correct updated on datetime is visible on the page. | PASS |

#### Contact Us

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| ContactUs form - Form Validation | Submit empty form | Browser promts that required fields need to be filled | PASS |
| ContactUs form - Form Validation | Submit with an invalid email address | Error message is successfully displayed | PASS |
| ContactUs form - Form Validation | Submit valid form | User is redirect to success page stating that the response has been recorded | PASS |

#### Ask a Query

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Log-in button display and functionality (user not authenticated) | Access as an unauthenticated user and try to login using the link given. | A message successfully displays along with a button that redirects to log-in page | PASS |
| Create query form (user authenticated) | Access the ask a query page as an authenticated user. | When user is authenticated, the ask a query form is successfully displayed with the correct sign-in user at the top | PASS |
| Create query form - Form validation | Submit an empty form | The browser promts validation that all fields need to be filled. | PASS |
| Create query form - Form validation | Submit an incomplete form. | The browser promts validation that all fields need to be filled. | PASS |
| Create query form - Form validation | Submit a complete query. | The query is successfully submited and a success message is displayed, stating that the query is awaiting review. | PASS |

#### Queries

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Queries view page | Click on a category on index page | The new page open all queries belongs to that category asked by different users. The query count should display the number of all approved queries and a link to go back to Home page along with move to other category should display on this page. | PASS |
| Under review query | View a query that is yet to be approved by the admin and posted by the logged in user | The query title should display in faded text with a message underneath that the query is still under review with an option of delete button. The username and query asked datetime stamp should be visible too. | PASS |
| Approved query - asked by the logged in user | View a query that is approved and posted by the logged in user | The query title should display with normal text and delete query option button. The username and query asked datetime stamp should be visible too. | PASS |
| Under review query - Other user | Query asked by another user that is still under reivew with admin | The query posted by a user that is still under review should not be visible to other users. | PASS |
| Approved query - asked by any user | Query should be visible without delete query button | When an admin publishes a query the query should be visible to all users. But delete query button should be visible to authunticated user only who post that query initially and no other user. | PASS |
| Delete Query | As a query author click the delete query button under query options. | When the authenticated user is the author, it successfully displays the delete query modal when clicking the delete query option. On reconfirmation to delete, the query should delete permanently from the model. | PASS |

#### Answers

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Answer view page | Click on a query on queries page | The new page open all answers belongs to that query asked by a users. The answer count should display the number of all approved answers and a link to go back to queries page for the category that query belongs to should display on this page. | PASS |
| Log-in button display and functionality (user not authenticated) | Access as an unauthenticated user and try to login using the link given. | A message successfully displays along with a button that redirects to log-in page | PASS |
| Create answer form (user authenticated) | Displays write an answer text box as an authenticated user. | When user is authenticated, a write an answer text box should displayed. | PASS |
| Under review answer | View an answer that is yet to be approved by the admin and posted by the logged in user | The answer should display in faded text with a message underneath that the answer that it is still under review with options of edit and delete button. The username and answer written datetime stamp should be visible too. | PASS |
| Approved answer - asked by the logged in user | View an answer that is approved by admin and posted by the logged in user | The answer should display with normal text and edit / delete answer option button. The username and answer written datetime stamp should be visible too. | PASS |
| Under review answer - Other user | Answer written by another user that is still under reivew with admin | The answer posted by a user that is still under review should not be visible to other users. | PASS |
| Approved answer - asked by any user | Answer should be visible without edit and delete button | When an admin approves an answer the answer should be visible to all users. But edit and delete answer button should be visible to authunticated user only who wrote that answer initially and no other user. | PASS |
| Delete answer | As an answer author click the delete answer button under answer options. | When the authenticated user is the author, it successfully displays the delete answer modal when clicking the delete answer option. On reconfirmation to delete, the answer should delete permanently from the model. | PASS |
| Edit answer - Form validation | Submit an empty answer form. | An error message is displayed, stating that fields are are required. | PASS |
| Edit answer - Form validation | Submit an valid answer form. | A success message is displayed, stating that the answer was successfully updated and is awating for approval. | PASS |

#### Sign Up 

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| User sign-up page  | Page should display the sign up form. | User is successfully directed to the signup page and sees the signup form. | PASS |
| User sign-up - Form validation  | Submit an empty form. | Browser promts that required fields need to be filled. | PASS |
| User sign-up - Form validation  | Submit an incomplete form. | Browser promts that required fields need to be filled. | PASS |
| User sign-up - Form validation  | Submit an invalid password. | Form promts the errors in the password. | PASS |
| User sign-up - Form validation  | Submit non-matching invalid password. | Form promts the error. | PASS |
| User sign-up - Form validation  | Submit an exisiting user name. | Form promts that the username is already taken error. | PASS |

#### Log In 

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| User login page  | Page should display the login form. | User is successfully directed to the login page and sees the login form. | PASS |
| User login page - Form validation | Submit an incorrect username password. | Form promts that the username and/or password is not correct. | PASS |

#### Log Out 

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| User logout page  | Page should display the logout reconfirm message. | User is successfully directed to the logout page and sees the logout reconfim message with logout button. | PASS |
| User logout page - Form validation | Click in logout. | User is successfully logged out and a display message is displayed at the top. | PASS |

#### Profile

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Add profile page | As a new user click on Profile link on navbar menu | An error message should display that no profile found and gives a redirect button to goto add a user profile page. | PASS |
| Add profile - Form validation | Submit an empty form. | Browser promts that required fields need to be filled. | PASS |
| Add profile - Form validation | Submit an incomplete form. | Browser promts that required fields need to be filled. | PASS |
| Add profile - Form validation | Submit a valid form. | A success message is displayed with the link to redirect user to their profile. | PASS |
| View profile - Existing profile user | Click on Profile link on navbar menu. | If you already have a profile created previously. When click on navbar menu profile link the logged in user profile should be visible | PASS |

### Automatec Form Testing 
| Form  | Test Case | Expected Outcome | Results |  
| - | - | - | - |
| Contact Form | Testing when all valid inputs were given then form works as expected | Form is valid. | PASS |
| Contact Form | Testing when name field is missing then form should fail  | Name field is not valid, but the Form is valid | PASS |
| Contact Form | Testing when email field is entered incorrect then form should fail | Email field is not valid, but the Form is valid | PASS |
| Contact Form | Testing when message field is missing then form should fail | Message field is not valid, but the Form is valid | PASS |
| User Profile Form | Testing when all valid inputs were given then form works as expected | Form is valid | PASS |
| User Profile Form | Testing when firstname field is missing then form should fail | First name field is not valid, but the Form is valid | PASS |
| User Profile Form | Testing when lastname field is missing then form should fail | Last name field is not valid, but the Form is valid | PASS |
| User Profile Form | Testing when email field is missing then form should fail | Email field is not valid, but the Form is valid | PASS |
| User Profile Form | Testing when describe yourself field is missing then form should fail | Describe yourself field is not valid, but the Form is valid | PASS |
| Answer Form | Testing when all valid inputs were given then form works as expected | Form is valid | PASS |
| Answer Form | Testing when content field is missing then form should fail | Answer content can not be empty but Answer form is not valid | PASS |
| Query Form | Testing when title field is missing then form should fail | Query title can not be empty, but Query form is valid | PASS |
| Query Form | Testing when category field is missing then form should fail | Query category can not be empty, but Query form is valid | PASS |
| Query Form | Testing when category incorrect field is provided then form should fail | Random category is invalid, but Query form is valid | PASS |
| Query Form | Testing when content field is missing then form should fail | Query Content can not be empty, but Query form is valid | PASS |

- Automated testing results:

![automated_forms_testing](static/images/readme_images/testing/formsautomatedtestingresult.png)


### Validator testing 

#### W3C validator

- Error's found:

![W3C_validator_error](static/images/readme_images/testing/w3cvalidation_errors.png)

- Error's Fixed:

![W3C_validator_results](static/images/readme_images/testing/w3cvalidation.png)

#### CSS validator

- No error found.

![W3C_CSS_validator_results](static/images/readme_images/testing/w3ccssvalidation.png)

#### JavaScript (JSHint) validator

- No error found.

![JavaScript_validator_results](static/images/readme_images/testing/jshintjavascriptvalidation.png)

#### Python (PP8) validator

![PP8 validator](https://pep8ci.herokuapp.com/#) 

- Page has an excellent Accessibility rating in Lighthouse. 

INPUT 

- The python file passes through the PP8 validator with no issues except by the more than 79 characters per line recomended by PEP 8.
- Tested the site opens in Chrome, Safari and Mozilla. 
- No broken links

## Technologies used

### Programming languages

- HTML5
- CSS3
- JavaScript (jQuery)
- Python (Django)

### Frameworks, Libraries and programs used

- [Google Fonts](https://fonts.google.com/) 
- [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Github](https://github.com/juanovt10)
- [CodeAnywhere](https://id.codeanywhere.com/realms/default/protocol/openid-connect/auth?client_id=dashboard&redirect_uri=https%3A%2F%2Fapp.codeanywhere.com%2F&state=0ed650a0-13c7-4f57-8415-5704cc42250e&response_mode=fragment&response_type=code&scope=openid&nonce=2b3f7872-fc80-4c91-bc06-4850e0415d4b)
- [Gitpod](https://gitpod.io/workspaces)
- [Heroku](https://id.heroku.com/login)
- [Realtime Colors](https://www.realtimecolors.com/?colors=e6eef8-03060a-92b3de-262376-694cc9&fonts=Poppins-Poppins)
- [Django](https://www.djangoproject.com/)
- [Django databases](https://docs.djangoproject.com/en/5.0/ref/databases/)
- [Django cloudinary storage](https://djangopackages.org/packages/p/django-cloudinary-storage/)
- [Django-allauth](https://docs.allauth.org/en/latest/)
- [Guinicorn](https://gunicorn.org/)
- [Psycopg](https://www.psycopg.org/docs/)
- [Balsamiq](https://balsamiq.com/) - For wireframes 
- [Lucidchart](https://lucid.app/users/login#/login) - For database diagram 

## Deployment

### Forking the Github repository 

1. Go to [Track Tales Repository](https://github.com/juanovt10/tracktales-blog)
2. In the top right, click the "Fork" button.
3. There will now be a copy of the repository in your own Github account.

### Running the project locally

1. Go to [Track Tales Repository](https://github.com/juanovt10/tracktales-blog)
2. Click on the "Code" button.
3. Choose one of the following three options and click copy.
    - HTTPS
    - SSH
    - Github CLI
4. Open termina in your preferable IDE (cloud or local).
5. Type `git clone` and paste the URL that was copied in step 3. 
6. Press enter and the local close will be created.

### Deploying with Heroku

The following steps were taken from the Django "I think before I blog" walkthrough project provided by [Code Institute](https://codeinstitute.net/global/).

1. Login or create an account in [Heroku](https://id.heroku.com/login). 
2. Go to your dashboard on the top right and click the `New` dropdown button and select `Create New App`.
3. Enter a name of the project (must be unique).
4. Select the region your are working in. 

#### External database set up

I used [ElephantSQL](https://www.elephantsql.com/) as my database. 

1. Login or create an account. 
2. In dashboard on the right top corner click `Create New Instance`
3. You will be forward to a `Select a plan and name`:
    - `Name` should be the name of the project
    - `Plan` should be the type of subscription you have with ElephantSQL, in my case I used the `Tiny Turtle (Free)` plan.
    - `Tags` can be left in blank

    Then click on `Select Region`.

4. Here selecte your `Data center`. This is hosted with AWS. In my case due to my location I used `EU-West-1 (Ireland)`. Please note that you should select an AWS Availability Zone (AZ) closest where your main users will be located to reduce downtime.

    Then click `Review`.
5. Here you will check the name, cloud provider and region where the application will be hosted. If, everything is correct, click `Create instance`.
6. Go to dashboard and your instance will be there. Click in the name and under `Details` copy the `URL`, this will be values that will be needed for the [Heroku variables setup](#heroku-settings) and the [env.py](#envpy-file-set-up) file.

#### External storage set up

I used [Cloudinary](https://cloudinary.com/ip/gr-sea-gg-brand-home-base?utm_source=google&utm_medium=search&utm_campaign=goog_selfserve_brand_wk22_replicate_core_branded_keyword&utm_term=1329&campaignid=17601148700&adgroupid=141182782954&keyword=cloudinary&device=c&matchtype=e&adposition=&gad_source=1&gclid=Cj0KCQiAm4WsBhCiARIsAEJIEzUYoKHM06ldJtPMxUmtjFK3HxOkfQI3_8G9vOXPuRsPWuCVCSFEPzsaAjiJEALw_wcB) as cloud storage for this project. 

1. Create and account or login. 
2. Go to `Dashboard` and copy the `API Environment variable`.
3. This URL will be required when setting up the [env.py](#envpy-file-set-up) and the [Heroku variables](#heroku-settings). 

#### env.py file set up

1. In the root directory of your project create a new file called `env.py`.
2. Add this `env.py` file to your `.gitignore` file so the confidential information in the file is not push to Github.
3. In the `env.py` file import the `os` module and add the [database URL](#external-database-set-up).

```
os.environ["DATABASE_URL"]="<copiedURL>"
```

4. Then, using the same process create a `SECRET_KEY`. This can be anything, I used [RandomKeygen](https://randomkeygen.com/) to create a complicated key. 

```
os.environ["SECRET_KEY"]="<copiedGeneratedKEY>"
```

5. Then, using the same process, in the `env.py` file import the `os` module and add the [storageURL](#external-storage-set-up).

```
os.environ["CLOUDINARY_URL"]="<copiedCloudinaryURL>"
```

6. Save the file.

#### Heroku settings 

After the application is created in Heroku. Got to your dashboard and you will see the application name, click on it and then follow the following: 

1. Go to the settings tab and go to `ConfigVars` and click on `Reveal Config Vars` and set the following variables: 
    - Key: `PORT`, Value: `8000`
    - Key: `DATABASE_URL`, Value: [databaseURL](#external-database-set-up)
    - Key: `CLOUDINARY_URL`, Value [storageURL](#external-storage-set-up)
    - Key: `SECRET_KEY`, Value: [randomKey](#envpy-file-set-up)

2. After setting up the variables, go to `Buildpacks` and select `Python`.

#### Heroku deployment 

1. Go to `Deploy` tab and under `Deployment method` connect to the Github repository.
2. Then there can be two options: manual or automatic deployment. 
    - Manual deployment means that it will be necessary to go to Heroku and deploy the application each time that changes are made. 
    - Automatic deployment will re-deploy the application each time new code is pushed to Github. 
3. After selecting the deployment method, under `Manual Deployment` click `Deploy branch`. 

## Credits

### Design

The site type was a mixed between a social media and blog web application. The following sites were used for instpiration: 

- [LinkedIn](https://www.linkedin.com/)
- [Instagram](https://www.instagram.com)
- [Reddit](https://www.reddit.com/) 

Additionally, the [Bootstrap 5](https://getbootstrap.com/docs/5.2/getting-started/introduction/) framework was heavily used for the front-end development.

### Code

In Django, the typical workflow for creating a view involves writing the view code first and subsequently creating the template to render the view. However, I took a slightly different approach by starting with the template to visualize the application before refining the code. During this process, I faced an issue that wasn't addressed in the [Code Institute](https://codeinstitute.net/global/) Django walkthrough projects, particularly regarding the customization of form styling.

Initially, I applied Bootstrap classes to style the forms, but I encountered challenges to display the form fields with the desired styling. Thanks to the insights gained from [CodingEntrepreneurs Tutorial](/https://www.youtube.com/watch?v=quJzUzCs6Q0&t=623s), I was able to achieve the desired styling by implementing html attributes in the [forms.py](/postBoard/forms.py) file.

Given the project's data models, a crucial requirement was to generate a new user profile data instance upon a user's signup, followed by redirecting them to a "create profile" page for further profile completion

To address the first challenge, I devised two methods within [models.py](/postBoard/models.py) adorned with a receiver decorator. The initial method creates the user profile, while the subsequent method utilizes the newly generated username to populate the user profile created in the first method. This solution was inspired by insights gleaned from a relevant [Stack Overflow discussion](https://stackoverflow.com/questions/65876529/how-to-create-instance-of-model-during-user-registration-process-django). 

For the second issue, my inclination was to avoid altering predetermined properties in django-allauth. However, consulting another insightful [Stack Overflow discussion](https://stackoverflow.com/questions/20138049/redirect-user-to-another-url-with-django-allauth-log-in-signal?newreg=b829fa7359404ec7b3765563ae9f145b) guided me towards a solution. I introduced a new redirect method in [views.py](/postBoard/views.py) to seamlessly direct the user to the "create profile" page immediately after completing the signup process.

Another challenging feature I grappled with was prepopulating fields when users desired to edit a post or their profile. Initially, I attempted to utilize the get methods to extract data from the backend and populate the fields, but this approach proved ineffective. Seeking assistance, I came across a helpful [Stack Overflow discussion](https://stackoverflow.com/questions/12439180/prefill-form-with-jquery) that guided me to leverage JavaScript, specifically jQuery. This solution enabled me to retrieve the current existing data and seamlessly prefill the forms with this information.

During troubleshooting, I encountered challenges in understanding how to effectively debug activities occurring in the backend. To address this, I incorporated the [Django messages feature](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/#using-messages-in-views-and-templates). This implementation allowed me to display errors occurring in the templates, providing valuable insights during the debugging process.

In the final stages, while working on the presentation of dynamic content like post likes, post comments, and dates, I encountered limitations with certain syntax within the template. To overcome this issue, I discovered [Django custom template tags](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/). This feature proved invaluable as it enabled me to present likes, showcase comments alongside their respective posts, and exhibit dates for both posts and comments in a more user-friendly manner

### Media

All the hero images were taken from [Pexels](https://www.pexels.com/), a free image stick image provider. Then they were optimized to reduced their size. 

- [Hero Image Slide 1 (desktop)](https://www.pexels.com/photo/lake-and-mountain-417074/)
- [Hero Image Slide 1 (desktop)](https://www.pexels.com/photo/city-of-istanbul-turkey-with-view-of-sultan-ahmed-mosque-during-night-time-14356751/)
- [Hero Image Slide 3 (desktop)](https://www.pexels.com/photo/man-and-woman-near-waterfall-450441/)
- [Hero Image Slide 1 (mobile)](https://www.pexels.com/photo/people-on-road-2104044/)
- [Hero Image Slide 2 (mobile)](https://www.pexels.com/photo/photo-of-person-standing-on-a-famous-temple-2659475/)
- [Hero Image Slide 3 (mobile)](https://www.pexels.com/photo/people-sitting-in-front-of-bonfire-in-desert-during-nighttime-1703314/)
