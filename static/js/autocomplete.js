/*
 * Project : KSRTC Seat Availability Notification System
 * Filename : autocomplete.js
 * Author : thameem
 * Current modification time : Sun, 7 Aug 2022 at 2:06 am India Standard Time
 * Last modified time : Sun, 7 Aug 2022 at 2:06 am India Standard Time
 */

// firebase configuration

const firebaseConfig = {
    apiKey: "AIzaSyAZTy6_ju9ivkIZGzezM_Z1rEVT7VBNPdI",
    authDomain: "ksrtc-notification-system.firebaseapp.com",
    databaseURL: "https://ksrtc-notification-system-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "ksrtc-notification-system",
    storageBucket: "ksrtc-notification-system.appspot.com",
    messagingSenderId: "349088019332",
    appId: "1:349088019332:web:e8cbaa5568c2e871a6a3d1"
};
//initialise firebase
firebase.initializeApp(firebaseConfig);

const db = firebase.firestore();
db.settings({timestampsInSnapshots: true});

var searchTimeout = null;
var resultsElm = document.getElementById('results');

function autoComplete(query){
    //todo - autocomplete
}