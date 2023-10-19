const submitIcons = document.querySelectorAll(".svg-cont");

submitIcons.forEach(submitIcon => {
    submitIcon.addEventListener("click", handleSubmit);
})

function handleSubmit(event) {
    console.log("handleSubmit triggered")

    const target = event.target
    //console.log(target)
    const parentTarget = target.parentElement
    // console.log(parentTarget)
    const grandparentTarget = parentTarget.parentElement
    // console.log(grandparentTarget)
    const greatparentTarget = grandparentTarget.parentElement
    //console.log(greatparentTarget)
    const profileFormDiv = greatparentTarget.parentElement
    //console.log(profileFormDiv)

    profileFormDiv.classList.remove("active")
    profileFormDiv.classList.add("inactive")

    profileFormDiv.nextElementSibling.classList.remove("inactive")
    profileFormDiv.nextElementSibling.classList.add("active")

}



