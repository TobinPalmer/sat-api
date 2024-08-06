(() => {
    const arr = [...document.querySelectorAll(".view-question-button")]
    const obj = {}

    let i = 0;
    setInterval(() => {
        arr[i].click()
        setTimeout(() => {
            const question = document.querySelector(".question")
            const answerChoices = document.querySelector(".answer-choices")
            const answer = document.querySelector(".answer-content")
            obj[arr[i].textContent] = {
                question: question.innerHTML,
                answerChoices: answerChoices.innerHTML,
                answer: answer.textContent,
                difficulty: document.querySelector(".tqdifficulty").getAttribute('aria-label').toLowerCase(),
                skill: document.querySelector("div.col-sm:nth-child(4) > div:nth-child(2)").textContent,
                domain: document.querySelector('div.col-sm:nth-child(3) > div:nth-child(2)').textContent,
            }
        }, 1000)
        console.log(obj)
        i++
    }, 3000)
})()