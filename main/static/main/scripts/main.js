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
}
