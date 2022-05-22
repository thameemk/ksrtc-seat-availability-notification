/*
 * Project : KSRTC Seat Availability Notification System
 * Filename : firebase_auth.js
 * Author : thameem
 * Current modification time : Sun, 22 May 2022 at 11:45 PM India Standard Time
 * Last modified time : Sun, 22 May 2022 at 11:45 PM India Standard Time
 */

const firebaseConfig = {
    apiKey: "AIzaSyAZTy6_ju9ivkIZGzezM_Z1rEVT7VBNPdI",
    authDomain: "ksrtc-notification-system.firebaseapp.com",
    databaseURL: "https://ksrtc-notification-system-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "ksrtc-notification-system",
    storageBucket: "ksrtc-notification-system.appspot.com",
    messagingSenderId: "349088019332",
    appId: "1:349088019332:web:e8cbaa5568c2e871a6a3d1"
};
firebase.initializeApp(firebaseConfig);

window.onload = function () {
    // Listening for auth state changes.
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            // User is signed in.
            const uid = user.uid;
            const phoneNumber = user.phoneNumber;
            const accessToken = user.getIdToken()
            console.log(accessToken)

            // window.location = '/user/home';
        }
    });

    window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier(
        "recaptcha-container",
        {
            size: "invisible",
            callback: function (response) {
                submitPhoneNumberAuth();
            }
        }
    );

    recaptchaVerifier.render().then(function (widgetId) {
        window.recaptchaWidgetId = widgetId;
    });
}


function submitPhoneNumberAuth() {
    const phoneNumber = "+91" + document.getElementById("phone_number").value;
    console.log(phoneNumber)
    const appVerifier = window.recaptchaVerifier;
    firebase
        .auth()
        .signInWithPhoneNumber(phoneNumber, appVerifier)
        .then(function (confirmationResult) {
            window.confirmationResult = confirmationResult;
            activateOTPField()
        })
        .catch(function (error) {
            console.log(error);
        });
}

function activateOTPField() {
    console.log("true")
    const elems = document.querySelectorAll(".otp_container");
    [].forEach.call(elems, function (el) {
        el.classList.remove("otp_container");
    });
    document.getElementById("phone_number").disabled = true;
    document.getElementById('sign-in-button').remove();
}

function submitPhoneNumberAuthCode() {
    const code = document.getElementById("one_time_password").value;
    confirmationResult
        .confirm(code)
        .then(function (result) {
            const user = result.user;
            console.log(user);
        })
        .catch(function (error) {
            console.log(error);
        });
}

firebase.auth().onAuthStateChanged(function (user) {
    if (user) {
        console.log("USER LOGGED IN");
    } else {
        // No user is signed in.
        console.log("USER NOT LOGGED IN");
    }
});