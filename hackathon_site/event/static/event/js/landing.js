// Variables for navbar moving up on scroll
let didScroll;
let lastScrollTop = 0;
let delta = 5;
let navbarHeight = $(".navbar").outerHeight();

// Change navbar color on scroll
// Change height of navbar icon on scroll
$(document).scroll(function () {
    const $nav = $(".navbar");
    const $logo = $(".logoNav");

    $nav.toggleClass("navbarScrolled", $(this).scrollTop() > $nav.height());
    $logo.toggleClass("logoNavScrolled", $(this).scrollTop() > $nav.height());

    didScroll = true;
});

$(document).ready(function () {
    // Materialize stuff
    $(".sidenav").sidenav();
    $(".carousel").carousel({ dist: 0, padding: 600 });
    setInterval(function () {
        $(".carousel").carousel("next");
    }, 3000);

    $(".scrollspy").scrollSpy();
    $(".collapsible").collapsible();

    // Countdown stuff

    const now = new Date();
    let countDownDate;

    // Set the title based off what it's counting down to
    if (registrationOpenDate >= now) {
        countDownDate = registrationOpenDate;
        $("#countdownTitle").html("Registration Opens In");
    } else if (registrationCloseDate >= now) {
        countDownDate = registrationCloseDate;
        $("#countdownTitle").html("Registration Closes In");
    } else if (eventStartDate >= now) {
        countDownDate = eventStartDate;
        $("#countdownTitle").html("Event Starts In");
    }

    // Delete the entire countdown if event start date has passed
    if (eventStartDate < now) {
        $("#countdown").remove();
        $("#aboutText").removeClass("l7");
    } else {
        // Update the countdown every ten minute
        setInterval(setCounter(countDownDate), 600000);
    }

    setInterval(function () {
        if (didScroll) {
            hasScrolled();
            didScroll = false;
        }
    }, 250);
});

function setCounter(countDownDate) {
    const now = new Date();
    const distance = countDownDate - now;
    const days = Math.ceil(distance / (1000 * 60 * 60 * 24));

    // Check if we need a third digit or not
    if (days > 99) {
        $("#day1").html(Math.floor(days / 100));
    } else {
        $("#day1").parent().remove();
    }

    $("#day2").html(Math.floor(days / 10) % 10);
    $("#day3").html(days % 10);
}

function hasScrolled() {
    let st = $(this).scrollTop();

    // Make sure they scroll more than delta
    if (Math.abs(lastScrollTop - st) <= delta) return;

    // The class only applies to mobile view
    if (st > lastScrollTop && st > navbarHeight) {
        // Scroll down
        $(".navbar").addClass("navbarUp");
    } else {
        // Scroll Up
        if (st + $(window).height() < $(document).height()) {
            $(".navbar").removeClass("navbarUp");
        }
    }

    lastScrollTop = st;
}
