(async () => {
  function waitForElm(selector) {
    return new Promise(resolve => {
      if (document.querySelector(selector)) {
        return resolve(document.querySelector(selector));
      }

      const observer = new MutationObserver(mutations => {
        if (document.querySelector(selector)) {
          observer.disconnect();
          resolve(document.querySelector(selector));
        }
      });

      observer.observe(document.body, {
        childList: true,
        subtree: true
      });
    });
  }

  const arr = [...document.querySelectorAll(".view-question-button")]
  const obj = {}

  async function next(idx) {
    arr[idx].click()
    // const question = document.querySelector(".question")
    // const answerChoices = document.querySelector(".answer-choices")
    // const answer = document.querySelector(".answer-content")
    const question = await waitForElm(".question")
    const answerChoices = await waitForElm(".answer-choices")
    const answer = await waitForElm(".answer-content")

    const difficulty = (await waitForElm(".tqdifficulty")).getAttribute('aria-label').toLowerCase()
    const skill = (await waitForElm("div.col-sm:nth-child(4) > div:nth-child(2)")).textContent
    const domain = (await waitForElm('div.col-sm:nth-child(3) > div:nth-child(2)')).textContent

    obj[arr[idx].textContent] = {
      question: question.innerHTML,
      answerChoices: answerChoices.innerHTML,
      answer: answer.textContent,
      difficulty,
      skill,
      domain,
    }
    waitForElm(".cb-btn-close").then(e => {
      const base = 500
      setTimeout(() => {
        e.click()
      }, base)

      setTimeout(() => {
        console.log(obj)
        next(idx + 1)
      }, base + 300)
    })
  }
  next(0)
})()
