/*
 * Project : KSRTC Seat Availability Notification System
 * Filename : firebase.js
 * Author : thameem
 * Current modification time : Tue, 26 Jul 2022 at 9:11 AM India Standard Time
 * Last modified time : Tue, 26 Jul 2022 at 9:10 AM India Standard Time
 */


// firebase configuration

const firebaseConfig = {
    apiKey: "AIzaSyC4xUTtkqY_PzmJq9uwJ4Cg6FqExVe9ALs",
    authDomain: "development-375416.firebaseapp.com",
    projectId: "development-375416",
    storageBucket: "development-375416.appspot.com",
    messagingSenderId: "1048197151318",
    appId: "1:1048197151318:web:8eecbe8a0c9c9a03e899f7"

};
//initialise firebase
firebase.initializeApp(firebaseConfig);


//login with phone number

function submitPhoneNumberAuth() {
    const phoneNumber = document.getElementById("phone_number");
    if (phoneNumber.value.length !== 10) {
        alert("Enter 10 digit phone number")
    } else {
        const appVerifier = window.recaptchaVerifier;
        firebase
            .auth()
            .signInWithPhoneNumber("+91" + phoneNumber.value, appVerifier)
            .then(function (confirmationResult) {
                window.confirmationResult = confirmationResult;
                activateOTPField()
            })
            .catch(function (error) {
                console.log(error);
            });
    }
}


// to activate otp field on sending otp from firebase

function activateOTPField() {
    const elems = document.querySelectorAll(".otp_container");
    [].forEach.call(elems, function (el) {
        el.classList.remove("otp_container");
    });
    document.getElementById("phone_number").disabled = true;
    document.getElementById('sign_in_button').remove();
}

// on submitting the otp

function submitPhoneNumberAuthCode() {
    const code = document.getElementById("one_time_password").value;
    confirmationResult
        .confirm(code)
        .then(async function (result) {
            const user = result.user;
            const token = await user.getIdToken(false);
            if (token !== null && token !== undefined && token !== "") {
                sendAuthDataToServer(token);
            }
        })

        .catch(function (error) {
            alert(error)
        });
}

function sendAuthDataToServer(token) {
    const xhr = new XMLHttpRequest();
    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            if (this.responseText === "login_success") {
                location = "/user/home/";
            } else {
                alert("Error in Login");
            }
        }
    });
    const csrftoken = getCookie('csrftoken');
    xhr.open("POST", "/auth/callback/", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.setRequestHeader("BEARER", token);
    xhr.send();
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function firebaseSignOut() {
    // firebase configuration
    firebase.auth().signOut().then(function () {
        const xhr = new XMLHttpRequest();
        xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
                if (this.responseText === "logout_success") {
                    location = "/login";
                } else {
                    alert("Error in Logout");
                }
            }
        });
        xhr.open("POST", "/auth/logout/", true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.send();
    }, function (error) {
        console.error('Sign Out Error', error);
    });
}
