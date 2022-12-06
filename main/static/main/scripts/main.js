// Function to handle new user signup
function newUserSignup(e) {
    e.preventDefault();
    let userFirstName = e.currentTarget.userFirstName.value;
    let userLastName = e.currentTarget.userLastName.value;
    let userEmail = e.currentTarget.userEmail.value;
    let userPassword = e.currentTarget.userPassword.value;

    //Utilize ajax to check backend
    $.ajax(
        {
            url: "/new_user_signup/",
            type: "POST",
            async: false,
            data: {
                "csrfmiddlewaretoken": e.currentTarget.csrfmiddlewaretoken.value,
                "user_first_name": userFirstName,
                "user_last_name": userLastName,
                "user_email": userEmail,
                "user_password": userPassword,
            },
            dataType: "json",
            success: function(response) {
                window.location.href="/login"
                },
            error: function(response) {
                alert(response.responseJSON.error)
            }
        }
    )

}

function userLogin(e) {
    e.preventDefault();
    let userEmail = e.currentTarget.userEmail.value;
    let userPassword = e.currentTarget.userPassword.value;

        $.ajax(
        {
            url: "/user_login/",
            type: "GET",
            data: {
                "csrfmiddlewaretoken": e.currentTarget.csrfmiddlewaretoken.value,
                "user_email": userEmail,
                "user_password": userPassword,
            },
            dataType: "json",
            success: function(response) {
                window.location.href="/myjobs"
                },
            error: function(response) {
                alert(response.responseJSON.error);
            }
        }
    )
}

function addNewJob() {
    document.querySelector(".add-job-btn").classList.toggle("hidden");
    document.querySelector(".page-text").classList.toggle("hidden");
    document.querySelector(".add-new-job-view").classList.toggle("hidden");
    document.querySelector(".jobs-list-view").classList.toggle("hidden");
}

function returnToJobList() {
    document.querySelector(".add-job-btn").classList.toggle("hidden");
    document.querySelector(".page-text").classList.toggle("hidden");
    document.querySelector(".add-new-job-view").classList.toggle("hidden");
    document.querySelector(".jobs-list-view").classList.toggle("hidden");
}

function saveJob(e) {
    e.preventDefault();
    let jobName = e.currentTarget.jobPosition.value;
    let companyName = e.currentTarget.companyName.value;
    let positionURL = e.currentTarget.positionURL.value;
    let eventSelect = e.currentTarget.eventSelect.value;
    let eventDate = e.currentTarget.eventDate.value;
    let personalPositionNotes = e.currentTarget.personalPositionNotes.value;
    let publicPositionNotes = e.currentTarget.publicPositionNotes.value;

        $.ajax(
        {
            url: "/save_job/",
            type: "POST",
            data: {
                "csrfmiddlewaretoken": e.currentTarget.csrfmiddlewaretoken.value,
                "job_name": jobName,
                "company_name": companyName,
                "position_url": positionURL,
                "event_select": eventSelect,
                "event_date": eventDate,
                "personal_position_notes": personalPositionNotes,
                "public_position_notes": publicPositionNotes,
            },
            dataType: "json",
            success: function(response) {
                    refresh_jobs_list();
                    returnToJobList();
                },
            error: function(response) {
                alert(response.responseJSON.error);
            }
        }
    )
}

function refresh_jobs_list() {
    $.ajax(
        {
            url: "/refresh_jobs/",
            success: function(response) {
                    $('#user-jobs-list').html(response);
                },
        }
    )
}

function delete_job(id) {
    $.ajax(
        {
            url: "/delete_job/",
            type: "GET",
            data: {
                "job_app_id": id,
            },
            dataType: "json",
            success: function(response) {
                    refresh_jobs_list();
                },
            error: function(response) {
                alert(response.responseJSON.error);
            }
        }
    )
}

